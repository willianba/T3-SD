from threading import Lock


class Counter:
    def __init__(self):
        self.lock = Lock()
        self.value = 0

    def increment(self):
        self.lock.acquire()
        self.value += 1
        self.lock.release()

    def read(self):
        self.lock.acquire()
        value = self.value
        self.lock.release()
        return value
