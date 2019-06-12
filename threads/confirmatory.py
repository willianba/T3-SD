import socket
from threading import Thread


def send_confirmation(address):
    confirmation_address = get_confirmation_address(address)
    send_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    send_socket.sendto(b"confirm", confirmation_address)
    send_socket.close()


def get_confirmation_address(address):
    host = address[0]
    port = int(get_process_address(host)[1]) + 1
    return (host, port)


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

    def receive_confirmation(self):
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
