import os
import requests
import json
from urllib.parse import urljoin
from adal import AuthenticationContext
from credentials import *

# Get an access token using the AuthenticationContext and the above parameters
authority_url = "https://login.microsoftonline.com/" + tenant_id
context = AuthenticationContext(authority_url)
token = context.acquire_token_with_client_credentials(resource, client_id, client_secret)

# Set the headers for the API requests
headers = {
    "Authorization": "Bearer " + token["accessToken"],
    "Content-Type": "application/json"
}

# Make a GET request to the Graph API to get the Site ID
site_api_url = "https://graph.microsoft.com/v1.0/sites?search=data_site"
response = requests.get(site_api_url, headers=headers)
site_data = json.loads(response.text)
site_id = site_data["value"][0]["id"]
print(site_id)

drive_api_url = f"https://graph.microsoft.com/v1.0/sites/{site_id}/drive/root:/books"
response = requests.get(drive_api_url, headers=headers)
drive_data = json.loads(response.text)
folder_id = drive_data["id"]
print(folder_id)

# Make a GET request to the Drive API to get a list of files for the specified folder
files_api_url = urljoin("https://graph.microsoft.com/v1.0/drives/", drive_data["parentReference"]["driveId"]) + "/items/" + folder_id + "/children"
response = requests.get(files_api_url, headers=headers)
files_data = json.loads(response.text)
# print(files_data)

for file in files_data["value"]:
    file_api_url = "https://graph.microsoft.com/v1.0/drives/" + drive_data["parentReference"]["driveId"] + "/items/" + file["id"] + "/content"
    response = requests.get(file_api_url, headers=headers)
    file_path = os.path.join(local_dir, file["name"])
    with open(file_path, "wb") as f:
        f.write(response.content)