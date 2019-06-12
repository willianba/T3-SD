import sys
import time
import random

from node import Node
from counters.counter import Counter
from threads.synchronizer import Synchronizer
from helpers.process_helper import get_process_parameters
from helpers.threads_helper import create_synchronizer_thread

current_node = None
config_file = sys.argv[1]
processes = open(config_file)
nodes = {}
last_node_id = None
events = Counter()


def main():
    create_nodes()
    synchronize()
    current_node.start_receiver()
    run_events()


def create_nodes():
    global current_node
    global last_node_id
    for line in processes:
        process_id, process_address = get_process_parameters(line)
        if process_id == sys.argv[2]:
            current_node = Node(process_id, process_address, events)
        else:
            nodes[process_id] = Node(process_id, process_address, events)
        last_node_id = process_id


def synchronize():
    synchronizer = create_synchronizer_thread(current_node.pid, current_node.address, get_process_list())
    if (sys.argv[2] == last_node_id):
        print("Sending signal to all processes.")
        synchronizer.send_signal()
    else:
        print("Waiting signal from last process.")
        synchronizer.receive_signal()


def get_process_list():
    return processes.readlines()


def run_events():
    while events.read() < 100:
        time.sleep(random.randint(1, 2))
        if is_local():
            current_node.increment_local()
            increment_event()
        else:
            send_clock_value()   
            confirm_value_receipt()
            increment_event()


def is_local():
    return random.choice([True, False])


def increment_event():
    events.increment()


def send_clock_value():
    target = get_target_node()
    current_node.send_clock_value(target.pid, target.address)


def get_target_node():
    return nodes[random.choice(list(nodes.keys()))]


def confirm_value_receipt():
    if not current_node.receive_confirmation():
        print("Cannot send clock value. Exiting.")
        sys.exit(-2)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python app.py <config_file> <process_id>")
        sys.exit(-1)
    main()
