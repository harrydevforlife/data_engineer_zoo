from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.user_credential import UserCredential
from office365.sharepoint.files.file import File
from office365.sharepoint.folders.folder import Folder
from works.ingest.sharepoint.config import site_url, user_credentials

ctx = ClientContext(site_url).with_credentials(UserCredential("manhtct@inter-k.com", "Hcmute2021@"))
folder_name = 'Test_SharePoint'

def get_all_files_from_document_library(folder_name: str) -> list:
    try:
        # user_credentials = UserCredential(global_settings.SYSTEM_USER_SPO, secret.SYSTEM_USER_PWD)
        # ctx = ClientContext(f"{global_settings.SHAREPOINT_BASE_URL}/sites/{spo_site}").with_credentials(user_credentials)
        files = ctx.web.get_folder_by_server_relative_url(folder_name).files
        ctx.load(files).execute_query()
        file_list = []
        for file in files:
            file_list.append({"Name": file.name, "ServerRelativeUrl": file.serverRelativeUrl})

    except:
        print("Could not retrieve files from folder '%s/%s'", folder_name)
        return None
    return file_list