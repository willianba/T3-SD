from threading import Thread
import socket
import random


class Sender(Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def send(self, time):
        selected_process = self.get_random_process().split(" ")
        process_host, process_port = selected_process[1], selected_process[2]
        send_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        send_socket.sendto(time, process_host, process_port)
        send_socket.close()

    def get_random_process(self):
        while True:
            processes = open("config").read().splitlines()
            selected_process = random.choice(processes)
            process_name = selected_process.split(" ")[0]
            if process_name != self.name:
                return selected_process
