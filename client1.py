import socket
from threading import Thread
import sys
from User import User
from Chatroom import Chatroom

class Client(object):
    """docstring for Client."""

    def __init__(self):
        super(Client, self).__init__()
        self.client_sock = socket.socket()
        self.HOST = 'localhost'
        self.PORT = 8000
        self.client_sock.connect((self.HOST, self.PORT))

    def run(self):
        print 'Connected to Server...'
        self.uname = raw_input('Enter your name: ')
        self.client_sock.send(self.uname)
        Thread(target=self.send).start()
        Thread(target=self.receive).start()

    def send(self):
        while True:
            try:
                msg = raw_input(">>")
                if len(msg) < 1000 and len(msg) > 0:
                    self.client_sock.send(msg)
                else:
                    sys.stdout.write("\n Message length must be between 0 and 1000 characters\n")
            except Exception as e:
                print(e.message)
                self.client_sock.shutdown(1)
                self.client_sock.close()
                return False

    def receive(self):
        while True:
            try:
                data = self.client_sock.recv(1024)
                sys.stdout.write("\n" + str(data) + "\n>>")
                sys.stdout.flush()
            except Exception as e:
                print(e.message)
                self.client_sock.shutdown(1)
                self.client_sock.close()
                return False
