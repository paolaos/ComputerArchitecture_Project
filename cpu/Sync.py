from threading import Lock


class Sync:
    def __init__(self):
        self.lock = Lock()

    def get_resource(self):
        return self.lock.acquire(False)
        # We use the Non-blocking acquire to prevent deadlocks
        # If the lock is locked, then it just returns false

    def free_resource(self):
        self.lock.release()
