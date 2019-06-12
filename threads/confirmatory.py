import socket
from threading import Thread


class Confirmatory(Thread):
    def __init__(self, address):
        super().__init__()
        self.address = address
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.buffer = 4096
        self.daemon = True

    def run(self):
        self.socket.bind(self.address)
        self.socket.settimeout(0.5)

    def confirm(self):
        tries = 0
        while True:
            if tries < 3:
                try:
                    self.socket.recvfrom(self.buffer)
                    return True
                except socket.timeout:
                    tries += 1
            else:
                return False
