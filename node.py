from threads.sender import Sender
from threads.receiver import Receiver
from helpers.helper import get_milliseconds
from counters.lamport_clock import LamportClock


class Node:
    def __init__(self, pid, host, port, events):
        self.pid = pid
        self.address = (host, int(port))
        self.events = events
        self.clock = LamportClock()

    def start_receiver(self):
        receiver = Receiver(self.pid, self.address, self.clock)
        receiver.start()

    def send(self, pid, address):
        sender = Sender(self.pid, self.clock, self.events)
        sender.start()
        sender.send(pid, address)
        sender.join()

    def increment_local(self):
        self.clock.increment()
        print("{} {} {} l".format(
            get_milliseconds(),
            self.pid,
            self.clock.read()
        ))
