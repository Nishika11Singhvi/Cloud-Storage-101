import os
import dropbox;
from dropbox.files import WriteMode

class TransferData:
    def __init__(self,access_token):
        self.access_token =  access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):

            for filename in files:
                local_path = os.path.join(root, filename)

                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)
                
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_token = 'sl.BE0DM62pC--pV8X-pZMjU8lCduFdtNuqaG1U_T7m-pI3FlUSN_kuc5EUXQeJHm1013X4AG3PoKh-csuqESz3t9qH4r7jAGq7vxMwCCPbX9r4IY2fuGcqBxZe0zxPL_mTsfyPBbJWfLlm'
    transferData = TransferData(access_token)

    file_from = str(input("Enter the folder path to transfer"))
    file_to = input("Enter the full path to upload to dropbox")  

    transferData.upload_file(file_from,file_to)
    print("Your file has been moved")

main()