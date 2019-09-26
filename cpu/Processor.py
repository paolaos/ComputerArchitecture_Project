import cpu.Memory as Memory

class Processor:
    """Main function that calls all fundamental components from CPU"""
    def __init__(self):
        self._clock = 0
        data_memory = Memory
        instructions_memory = Memory

    @property
    def clock(self):
        return self._clock

    @clock.setter
    def clock(self, clock):
        self._clock = clock
