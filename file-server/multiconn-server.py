import socket
import threading
import os

class Server:
    def __init__(self):
        self.server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.accept_clients()
    
    def accept_clients(self):
        host = "0.0.0.0"
        port = 8080
        self.server.bind((host,port))
        self.server.listen(5)
        print("SERVER'S IP: "+host)
        print("SERVER'S PORT: "+str(port))

        while True:
            clientsock, addr = self.server.accept()
            threading.Thread(target=self.handle_client,args=(clientsock,addr,)).start()

    def handle_client(self,clientsock,addr):
        data = clientsock.recv(1024).decode()
    
        if not os.path.exists(data):
            clientsock.send("file-doesn't-exist".encode())

        else:
            clientsock.send("file-exists".encode())
            print('Sending',data)
            if data != '':
                file = open(data,'rb')
                data = file.read(1024)
                while data:
                    clientsock.send(data)
                    data = file.read(1024)

                clientsock.shutdown(socket.SHUT_RDWR)
                clientsock.close()
                

server = Server()

