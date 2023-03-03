# Ingest data from Microsoft Sharepoint

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