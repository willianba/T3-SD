import sys
import time
import random

from node import Node
from counters.counter import Counter

current_node = None
config_file = sys.argv[1]
processes = open(config_file)
nodes = {}
events = Counter()


def main():
    create_nodes()
    current_node.start_receiver()
    run_events()


def create_nodes():
    global current_node
    for line in processes:
        process = line.split(" ")
        if process[0] == sys.argv[2]:
            current_node = Node(process[0], process[1], int(process[2]), events)
        else:
            nodes[process[0]] = Node(process[0], process[1], process[2], events)


def run_events():
    while events.read() < 100:
        time.sleep(random.randint(1, 2))
        if random.choice([True, False]):
            current_node.increment_local()
            events.increment()
        elif events.read() > 5:
            target = nodes[random.choice(list(nodes.keys()))]
            current_node.send(target.pid, target.address)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python app.py <config_file> <process_id>")
        sys.exit(-1)
    main()
