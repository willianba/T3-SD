import sys
from time import time


def get_milliseconds():
    return int(round(time()) * 1000)


def get_process_id(ip):
    process = get_process(ip).split(" ")
    return process[0]


def get_process_address(ip):
    process = get_process(ip).split(" ")
    return process[1], process[2]


def get_process(ip):
    processes = open(sys.argv[1])
    for process in processes:
        if ip in process:
            return process
