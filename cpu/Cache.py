class Cache:
    def __init__(self):
        self._storage = []
        self._status_blocks = []
        self._address_blocks = []
        self._size = 0

    @property
    def storage(self):
        return self._storage

    @storage.setter
    def storage(self, storage):
        self._storage = storage

    @property
    def status_blocks(self):
        return self._status_blocks

    @status_blocks.setter
    def status_blocks(self, status_blocks):
        self._status_blocks = status_blocks

    @property
    def address_blocks(self):
        return self._address_blocks

    @address_blocks.setter
    def address_blocks(self, address_blocks):
        self._address_blocks = address_blocks

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size
