from threading import Thread
import socket


buffer = 4096


class Receiver(Thread):
    def __init__(self, name, host, port):
        super().__init__(name=name)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.address = (host, port)

    def run(self):
        self.start_socket()
        self.listen_socket()

    def start_socket(self):
        self.sock.bind(self.address)

    def listen_socket(self):
        new_time = self.sock.recvfrom(buffer)