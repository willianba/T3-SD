import json
import socket
from threading import Thread

from helpers.time_helper import get_milliseconds


class Sender(Thread):
    def __init__(self, pid):
        super().__init__()
        self.pid = pid

    def send(self, pid, address, clock_value):
        send_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        send_socket.sendto(json.dumps(clock_value).encode(), address)
        send_socket.close()
        print("{} {} {} s {}".format(
            get_milliseconds(),
            self.pid,
            clock_value,
            pid
        ))
