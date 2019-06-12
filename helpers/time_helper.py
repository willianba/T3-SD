from time import time


def get_milliseconds():
    return int(round(time()) * 1000)