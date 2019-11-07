from threading import Thread, Event, Lock
from cpu.Memory import Memory
from cpu.Core import Core
from cpu.Block import Block
from cpu.Sync import Sync
from cpu.Cache import Cache
from cpu.ProgramsContext import ProgramsContext
import os


class Processor:
    """Main function that calls all fundamental components from CPU"""
    def __init__(self):
        self.clock = 0
        self.data_bus = Sync()
        self.instruction_bus = Sync()
        self.data_memory = Memory(0, 380)
        self.instructions_memory = Memory(0, 380)

        self.core_1_data_cache = Cache()
        self.core_1_instruction_cache = Cache()
        self.core_2_instruction_cache = Cache()
        self.core_2_data_cache = Cache()

        # self.core_1 = Core(self.core_1_data_cache, self.core_1_instruction_cache)
        # self.core_2 = Core(self.core_2_data_cache, self.core_2_instruction_cache)

        self.contexts = ProgramsContext()

    @property
    def clock(self):
        return self.clock

    @clock.setter
    def clock(self, clock):
        self.clock = clock

    @property
    def data_memory(self):
        return self.data_memory

    @data_memory.setter
    def data_memory(self, data_memory):
        self.data_memory = data_memory

    @property
    def instructions_memory(self):
        return self.instructions_memory

    @instructions_memory.setter
    def instructions_memory(self, instructions_memory):
        self.instructions_memory = instructions_memory

    @property
    def core_1(self):
        return self.core_1

    @core_1.setter
    def core_1(self, core_1):
        self.core_1 = core_1

    @property
    def core_2(self):
        return self.core_2

    @core_2.setter
    def core_2(self, core_2):
        self.core_2 = core_2

    @property
    def contexts(self):
        return self.contexts

    @contexts.setter
    def contexts(self, contexts):
        self.contexts = contexts

    @property
    def data_bus(self):
        return self.data_bus

    @data_bus.setter
    def data_bus(self, data_bus):
        self.data_bus = data_bus

    @property
    def instructions_bus(self):
        return self.instructions_bus

    @instructions_bus.setter
    def instructions_bus(self, instructions_bus):
        self.instructions_bus = instructions_bus

    # Processor methods
    def kick_start_program(self):
        self.load_memory_instructions()
        self.instantiate_data_memory()
        # to be completed

    def load_memory_instructions(self):
        current_block_number = 24
        for file_name in os.listdir('../assets'):
            file_ = open('../assets/' + file_name, 'r')
            last_block_number = self.store_instructions_in_memory(file_, current_block_number)
            current_block_number = last_block_number + 1

    def store_instructions_in_memory(self, file_, current_block_number):
        line = file_.readline()
        while line:
            split_line = line.split()
            if current_block_number % 4 == 0:
                temporary_block = Block()
                temporary_block.block_id = current_block_number
                temporary_block.word_0 = split_line
            else:
                if current_block_number % 4 == 1:
                    temporary_block.word_1 = split_line
                else:
                    if current_block_number % 4 == 2:
                        temporary_block.word_2 = split_line
                    else:
                        temporary_block.word_3 = split_line
                        self.instructions_memory.memory.append(temporary_block)

            line = file_.readline()
            current_block_number = current_block_number + 1

        return current_block_number

    def instantiate_data_memory(self):
        for i in range(0, 24):
            block = Block()
            block.block_id(i)
            block.word_0([0, 0, 0, 0])
            block.word_1([0, 0, 0, 0])
            block.word_2([0, 0, 0, 0])
            block.word_3([0, 0, 0, 0])


    def assign_program_to_core_1(self, program_context):
        self.core_1.run_program(program_context)

    def assign_program_to_core_2(self, program_context):
        self.core_2.run_program(program_context)

    def get_next_program(self):
        print('todo')
    # return the next program in program_context that has taken = False

    def init_threads(self):
        self.core_1 = Thread(None, None, "core1")
        self.core_2 = Thread(None, None, "core2")
