import cpu.Memory as Memory

class Processor:
    """Main function that calls all fundamental components from CPU"""
    def __init__(self):
        self._clock = 0
        self._data_memory = Memory
        self._instructions_memory = Memory

    @property
    def clock(self):
        return self._clock

    @clock.setter
    def clock(self, clock):
        self._clock = clock

    @property
    def data_memory(self):
        return self._data_memory

    @data_memory.setter
    def data_memory(self, data_memory):
        self._data_memory = data_memory

    @property
    def instructions_memory(self):
        return self._instructions_memory

    @instructions_memory.setter
    def instructions_memory(self, instructions_memory):
        self._instructions_memory = instructions_memory
