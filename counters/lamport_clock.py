from counters.counter import Counter


class LamportClock(Counter):
    def __init__(self):
        super().__init__()

    def update_value(self, value):
        self.lock.acquire()
        self.value = max(self.value, value)
        self.lock.release()
