from threading import Lock


class Clock:
    def __init__(self):
        self.clock = 0
        self.lock = Lock()

    def next_cycle(self):
        self.lock.acquire()
        self.clock += 1
        self.lock.release()

    def get_clock(self):
        self.lock.acquire()
        actual_clock = self.clock
        self.lock.release()
        return actual_clock
