import socket
import os


target_ip = "0.0.0.0"
target_port = 8080

class Client:
    def __init__(self):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

        self.s.connect((target_ip,int(target_port)))
        self.main()

    def main(self):
        while True:
            file_name = input('Enter web.txt or app.txt or sys.txt to be downloaded! ')
            self.s.send(file_name.encode())

            confirmation = self.s.recv(1024)
            if confirmation.decode() == "file-exists":        
                downloaded_file = 'server_'+file_name
                if os.path.exists(downloaded_file): os.remove(downloaded_file)

                with open(downloaded_file,'wb') as file:
                    while True:
                        data = self.s.recv(1024)
                        if not data:
                            break
                        file.write(data)

                print(file_name,'successfully downloaded.')

        else:
            print("File doesn't exist on server.")
            self.s.shutdown(socket.SHUT_RDWR)
            self.s.close()
               
client = Client()
