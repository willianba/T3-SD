import socket
from threading import Thread

from helpers.process_helper import get_process_parameters


class Synchronizer(Thread):
    def __init__(self, pid, address, processes):
        super().__init__()
        self.pid = pid
        self.address = address
        self.processes = processes
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.buffer = 4096
        self.daemon = True

    def run(self):
        self.socket.bind(self.address)

    def send_signal(self):
        for process in self.processes:
            process_id, process_address = get_process_parameters(process)
            if process_id != self.pid:
                self.socket.sendto(b"start", process_address)
        self.socket.close()
    
    def receive_signal(self):
        self.socket.setblocking(True)
        self.socket.recvfrom(self.buffer)