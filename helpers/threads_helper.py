from threads.sender import Sender
from threads.receiver import Receiver
from threads.synchronizer import Synchronizer


def start_receiver_thread(pid, address, clock):
    Receiver(pid, address, clock).start()


def create_sender_thread(pid):
    sender = Sender(pid)
    sender.start()
    sender.join()
    return sender


def create_synchronizer_thread(pid, address, processes):
    synchronizer = Synchronizer(pid, address, processes)
    synchronizer.start()
    synchronizer.join()
    return synchronizer
