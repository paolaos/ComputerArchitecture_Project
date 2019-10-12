class Memory:
    def __init__(self, starting_address, length):
        self._memory = []
        self._length = length
        self._starting_address = starting_address

    @property
    def memory(self):
        return self._memory

    @memory.setter
    def memory(self, memory):
        self._memory = memory

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, length):
        self._length = length

    @property
    def starting_address(self):
        return self._starting_address

    @starting_address.setter
    def starting_address(self, starting_address):
        self._starting_address = starting_address
