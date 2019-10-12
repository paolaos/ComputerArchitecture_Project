from cpu.Memory import Memory
from cpu.Core import Core
from cpu.ProgramsContext import ProgramsContext

class Processor:
    """Main function that calls all fundamental components from CPU"""
    def __init__(self):
        self._clock = 0
        self._data_memory = Memory(0, 380)
        self._instructions_memory = Memory(381, 636)
        self._core_1 = Core()
        self._core_2 = Core()
        self._contexts = ProgramsContext()
        self._data_bus = 0
        self._instructions_bus = 0

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

    @property
    def core_1(self):
        return self._core_1

    @core_1.setter
    def core_1(self, core_1):
        self._core_1 = core_1

    @property
    def core_2(self):
        return self._core_2

    @core_2.setter
    def core_2(self, core_2):
        self._core_2 = core_2

    @property
    def contexts(self):
        return self._contexts

    @contexts.setter
    def contexts(self, contexts):
        self._contexts = contexts

    @property
    def data_bus(self):
        return self._data_bus

    @data_bus.setter
    def data_bus(self, data_bus):
        self._data_bus = data_bus

    @property
    def instructions_bus(self):
        return self._instructions_bus

    @instructions_bus.setter
    def instructions_bus(self, instructions_bus):
        self._instructions_bus = instructions_bus
