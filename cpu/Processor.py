from cpu.Memory import Memory
from cpu.Core import Core
from cpu.Block import Block
from cpu.ProgramsContext import ProgramsContext
import os


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

    def kick_start_program(self):
        self.load_memory_instructions()
        self.instantiate_data_memory()
        return 0

    def load_memory_instructions(self):
        current_block_number = 24
        for file_name in os.listdir('assets'):
            file_ = open(file_name, 'r')
            last_block_number = self.store_instructions_in_memory(file_, current_block_number)
            current_block_number = last_block_number + 1

    def store_instructions_in_memory(self, file_, current_block_number):
        line = file_.readline()
        while line:
            split_line = line.split()
            block = self.create_instruction_block(split_line, current_block_number)
            self._instructions_memory.memory(self._instructions_memory.memory().extend(block))
            current_block_number = current_block_number + 1

        return current_block_number

    def create_instruction_block(self, line, number):
        temporary_block = Block()
        temporary_block.block_id = number
        temporary_block.word_0(line[0])
        temporary_block.word_1(line[1])
        temporary_block.word_2(line[2])
        temporary_block.word_3(line[3])
        return temporary_block

    def instantiate_data_memory(self):
        for i in range(0, 24):
            block = Block()
            block.block_id(i)
            block.word_0([0, 0, 0, 0])
            block.word_1([0, 0, 0, 0])
            block.word_2([0, 0, 0, 0])
            block.word_3([0, 0, 0, 0])

        return 0

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
