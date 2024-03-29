import json
import socket
from threading import Thread

from helpers.time_helper import get_milliseconds
from helpers.process_helper import get_process_id


class Receiver(Thread):
    def __init__(self, pid, address, clock):
        super().__init__()
        self.pid = pid
        self.address = address
        self.clock = clock
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.buffer = 4096
        self.daemon = True

    def run(self):
        self.socket.bind(self.address)
        self.listen()

    def listen(self):
        while True:
            received_time, address = self.socket.recvfrom(self.buffer)
            self.socket.sendto(b"confirmation", address)
            received_time = json.loads(received_time.decode())
            self.clock.update_value(received_time)
            self.clock.increment()
            print("{} {} {} r {} {}".format(
                get_milliseconds(),
                self.pid,
                self.clock.read(),
                get_process_id(address[0]),
                received_time
            ))
