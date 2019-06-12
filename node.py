from counters.lamport_clock import LamportClock
from helpers.time_helper import get_milliseconds
from helpers.threads_helper import start_receiver_thread, create_sender_thread, create_confirmatory_thread


class Node:
    def __init__(self, pid, address, events):
        self.pid = pid
        self.address = address
        self.events = events
        self.clock = LamportClock()

    def start_receiver(self):
        start_receiver_thread(self.pid, self.address, self.clock)

    def send_clock_value(self, pid, address):
        self.clock.increment()
        clock_value = self.clock.read()
        sender = create_sender_thread(self.pid)
        sender.send(address, clock_value)

    def receive_confirmation(self):
        address = (self.address[0], self.address[1] + 1)
        confirmatory = create_confirmatory_thread(address)
        result = confirmatory.receive_confirmation()
        return result

    def increment_local(self):
        self.clock.increment()
        print("{} {} {} l".format(
            get_milliseconds(),
            self.pid,
            self.clock.read()
        ))
