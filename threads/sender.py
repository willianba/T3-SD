import json
import socket
from threading import Thread

from helpers.time_helper import get_milliseconds


class Sender(Thread):
    def __init__(self, pid):
        super().__init__()
        self.pid = pid
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.settimeout(3)

    def send(self, pid, address, clock_value):
        try:
            self.socket.sendto(json.dumps(clock_value).encode(), address)
            self.socket.recvfrom(4096)
            self.socket.close()
            print("{} {} {} s {}".format(
                get_milliseconds(),
                self.pid,
                clock_value,
                pid
            ))
            return True
        except socket.timeout:
            return False
