from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.user_credential import UserCredential
from office365.sharepoint.files.file import File
from office365.sharepoint.folders.folder import Folder
from config import site_url, username, password, target_folder_url

ctx = ClientContext(site_url).with_credentials(UserCredential(username, password))

def enum_folder(parent_folder, fn):
    """
    :type parent_folder: Folder
    :type fn: (File)-> None
    """
    parent_folder.expand(["Files", "Folders"]).get().execute_query()
    for file in parent_folder.files:  # type: File
        fn(file)
    for folder in parent_folder.folders:  # type: Folder
        enum_folder(folder, fn)


def print_file(f):
    """
    :type f: File
    """
    print(f.properties['ServerRelativeUrl'])


root_folder = ctx.web.get_folder_by_server_relative_path(target_folder_url)
# enum_folder(root_folder, print_file)

files = root_folder.get_files(True).execute_query()
[print_file(f) for f in files]