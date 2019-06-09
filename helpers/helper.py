import sys
from time import time


def get_milliseconds():
    return int(round(time()) * 1000)


def get_process_id(ip):
    processes = open(sys.argv[1])
    for line in processes:
        if ip in line:
            process = line.split(" ")
            return process[0]
