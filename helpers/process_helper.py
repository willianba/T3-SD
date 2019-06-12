import sys


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


def get_process_parameters(process_line):
    process = process_line.split(" ")
    process_id = process[0]
    process_address = process[1], int(process[2])
    return process_id, process_address