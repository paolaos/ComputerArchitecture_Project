from threading import Lock, Barrier


class Clock:

    def __init__(self, threads=2):
        self.clock_cycles = 0
        self.thread_count = threads
        self.barrier = Barrier(self.thread_count)
        self.clock_lock = Lock()

    def next_cycle(self):
        """
        Nuclearly increments the clock by half a second (representing one core).
        """
        self.clock_lock.acquire()
        self.clock_cycles += 0.5
        self.clock_lock.release()

    def get_clock(self):
        """
        :return: the amount of clock cycles that have passed
        """
        return int(self.clock_cycles)

    def wait_for_next_cycle(self):
        """
        Used in each of the cores, increments the clock by half a second and waits
        until the other core reached the barrier.
        """
        if self.thread_count > 0:
            try:
                self.next_cycle()
                self.barrier.wait()
            except:
                pass

    def remove_thread(self):
        """
        When one of the threads are done with the program executions, nuclearly
        decrements the current thread count and aborts from the barrier.
        """
        self.clock_lock.acquire()
        if self.thread_count > 0:
            self.thread_count -= 1
        else:
            self.barrier.abort()
        self.clock_lock.release()
