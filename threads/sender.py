import json
import socket
from threading import Thread

from helpers.helper import get_milliseconds


class Sender(Thread):
    def __init__(self, pid, clock, events):
        super().__init__()
        self.pid = pid
        self.clock = clock
        self.events = events
        self.daemon = True

    def send(self, pid, address):
        self.clock.increment()
        send_time = self.clock.read()
        send_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        send_socket.sendto(json.dumps(send_time).encode(), address)
        send_socket.close()
        self.events.increment()
        print("{} {} {} s {}".format(
            get_milliseconds(),
            self.pid,
            send_time,
            pid
        ))
