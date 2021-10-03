import dropbox
import os

from dropbox.files import WriteMode
class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)
        for root,dirs,files in os.walk(file_from):
            for fileName in files:
                local_path = os.path.join(root,fileName)
                relative_path = os.path.relpath(local_path , file_from)
                dropbox_path = os.path.join(file_to , relative_path)
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(),dropbox_path , mode=WriteMode('overwrite'))

def main():
    access_token = 'sl.A5rwRRy4yXqitkrAq4_Y2VjgBCDhitYLQOBr3znOv0nDEXT8PQDmfGNdWKhiABbytF8hYAA_N22nymGOqpz_vAZFlX071N8Dtd5Ie-QFwRkunNPSs8f4S4pDO4VWdWeaEse0Ygo'
    transferData = TransferData(access_token)

    file_from = 'text.txt'
    file_to = '/Users/rachanajoshi/Dropbox/Mac/Desktop/CloudStorage/text.txt'  # The full path to upload the file to, including the file name
    
    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been moved")


main()