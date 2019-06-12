from threads.sender import Sender
from threads.receiver import Receiver
from threads.confirmatory import Confirmatory
from helpers.helper import get_milliseconds
from counters.lamport_clock import LamportClock


class Node:
    def __init__(self, pid, address, events):
        self.pid = pid
        self.address = address
        self.events = events
        self.clock = LamportClock()

    def start_receiver(self):
        receiver = Receiver(self.pid, self.address, self.clock)
        receiver.start()

    def send_clock_value(self, pid, address):
        self.clock.increment()
        clock_value = self.clock.read()
        sender = Sender(self.pid)
        sender.start()
        sender.join()
        sender.send(pid, address, clock_value)

    def receive_confirmation(self):
        address = (self.address[0], self.address[1] + 1)
        confirmatory = Confirmatory(address)
        confirmatory.start()
        confirmatory.join()
        result = confirmatory.receive_confirmation()
        return result

    def increment_local(self):
        self.clock.increment()
        print("{} {} {} l".format(
            get_milliseconds(),
            self.pid,
            self.clock.read()
        ))
