import os
from config import site_url, username, password, download_path, target_folder_url
from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.user_credential import UserCredential
from office365.sharepoint.files.file import File
from office365.sharepoint.folders.folder import Folder

client_context = ClientContext(site_url).with_credentials(UserCredential(username, password))

root_folder = client_context.web.get_folder_by_server_relative_path(target_folder_url)
files = root_folder.get_files(True).execute_query()

for f in files:
    file_url = f.properties['ServerRelativeUrl']
    file_name = os.path.basename(file_url)
    save_path = os.path.join(download_path, file_name)
    with open(save_path, "wb") as local_file:
            file = client_context.web.get_file_by_server_relative_url(file_url).download(local_file).execute_query()

    print("[OK] file has been downloaded: {0}".format(file_name))

print("[DONE] All files has been downloaded into: {0}".format(download_path))