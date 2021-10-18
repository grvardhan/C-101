import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token

        def upload_file(self,file_from,file_to):
            dbx=dropbox.Dropbox(self.access_token)

            f=open(file_from,"rb")
            dbx.files_upload(f.raed(),file_to)

            def main():
                access_token = 'sl.AbKQY7cwlr949HZB7JxLOMrnYKuY39PSkiEnMjmzkLJ8mukldzSQjT8oLVfn_A-kB4yn6O0erRD07aV-9JeaGvvRPoLFEVvwg3_p2AufnKjhGlCgTVtpR4YV0SKhk6nbU2-ztZAB'
                transferData = TransferData(access_token)
                transferData.upload_file(file_from, file_to)
                print("file has been moved !!!")
                main()