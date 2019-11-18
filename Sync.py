from threading import Lock


class Sync:
    """
    All functionality related to the lock/mutex synchronisation mechanism
    used in this programme.
    """
    def __init__(self):
        self.lock = Lock()
        self.busy_cycles = 0
        self.core_id = -1

    def get_resource(self, cycles, core_id):
        """
        Attempts to get a resource that uses locks to avoid non-nuclear access.
        The non-blocking approach is used to prevent deadlocks.
        :param cycles:
        :param core_id:
        :return: false if the lock is locked, true if it isn't (and changes
        access and information parameters
        """
        status = self.lock.acquire(False)
        if status:
            self.busy_cycles = cycles
            self.core_id = core_id
        return status
        # We use the Non-blocking acquire to prevent deadlocks
        # If the lock is locked, then it just returns false

    def free_resource(self):
        """
        Releases lock for a specific resource and changes access and information
        parameters.
        """
        self.core_id = -1
        self.lock.release()

    def decrease_cycles(self):
        """
        Decreases access cycles from the resource in case it has not finished. Frees
        resource if there are no remaining busy cycles.
        """
        if self.busy_cycles > 0:
            self.busy_cycles -= 1
        if self.busy_cycles == 0:
            self.free_resource()
