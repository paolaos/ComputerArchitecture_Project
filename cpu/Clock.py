from threading import Lock, Barrier


class Clock:
    def __init__(self, threads=2):
        self.clock_cycles = 0
        self.thread_count = threads
        self.barrier = Barrier(self.thread_count)
        self.clock_lock = Lock()

    def next_cycle(self):
        self.clock_lock.acquire()
        self.clock_cycles += 0.5
        self.clock_lock.release()

    def get_clock(self):
        return int(self.clock_cycles)

    def wait_for_next_cycle(self):
        if self.thread_count > 0:
            try:
                self.next_cycle()
                self.barrier.wait()
            except:
                pass

    def remove_thread(self):
        self.clock_lock.acquire()
        if self.thread_count > 0:
            self.thread_count -= 1
        else:
            self.barrier.abort()
        self.clock_lock.release()
