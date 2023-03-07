# Ingest files from Microsoft Sharepoint

## 1. Using Office 365 & Microsoft Graph library for Python

- Using library [Office365-REST-Python-Client](https://github.com/vgrem/Office365-REST-Python-Client) by command below:
```
pip install Office365-REST-Python-Client
```

- Remember create `config.py` file to store secret, password,.. reference:

```
site_url = 'http://your-site/site/...'
password = ' '
target_folder_url = 'Shared Documents/Test_Sharepoint'
download_path = '/home/.../'
```

## 2. Using Azure Active Directory & Microsoft Graph API

### Setup 
- Setup [App Register](https://learn.microsoft.com/en-us/graph/auth-register-app-v2)
- Install [adal](https://pypi.org/project/adal/) library : `pip install adal`


### Testing
- Using [graph explorer](https://developer.microsoft.com/en-us/graph/graph-explorer) or Postman to test API.

### Learning more 
 - [Microsoft Graph API](https://learn.microsoft.com/en-us/graph/use-the-api)
 - [Azure Active Directory](https://learn.microsoft.com/en-us/azure/active-directory/)