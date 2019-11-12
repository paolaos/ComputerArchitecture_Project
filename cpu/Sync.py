from threading import Lock


class Sync:
    def __init__(self):
        self.lock = Lock()
        self.busy_cycles = 0

    def get_resource(self, cycles):
        status = self.lock.acquire(False)
        if status:
            self.busy_cycles = cycles
        return status
        # We use the Non-blocking acquire to prevent deadlocks
        # If the lock is locked, then it just returns false

    def free_resource(self):
        self.lock.release()

    def decrease_cycles(self):
        if self.busy_cycles > 0:
            self.busy_cycles -= 1
        if self.busy_cycles == 0:
            self.free_resource()
