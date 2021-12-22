import dropbox 

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
    
    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f= open(file_from, "rb")
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = "sl.A-qyXzKdb2OsR_xY7gzMgTAsbToCTeUwPCr8YnMkkhEQI4l8mMnFN5JwwlfsXkHEtk-MOv4su65YPPZISe3bxT1TqhAwJJrwiT4fHE5vhNLUuPlJRTdIuPmEGjXB2wfRM1jTD7k"
    transferData = TransferData(access_token)

    file_from = 'test.txt'
    file_to = '/test_dropbox/test.txt'

    transferData.upload_file(file_from, file_to )
    print("File lhas been moved !!!!")        

main()
