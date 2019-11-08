from cpu.Memory import Memory
from cpu.Core import Core
from cpu.Block import Block
from cpu.Sync import Sync
from cpu.Cache import Cache
from cpu.ProgramsContextHelper import create_context
import os


class Processor:
    def __init__(self):
        self.clock = 0
        self.data_bus = Sync()
        self.instruction_bus = Sync()
        self.data_memory = Memory(0, 380)
        self.instructions_memory = Memory(24, 636)

        self.core_1_data_cache = Cache(self.data_memory)
        self.core_1_instruction_cache = Cache(self.instructions_memory)
        self.core_2_instruction_cache = Cache(self.instructions_memory)
        self.core_2_data_cache = Cache(self.data_memory)
        self.core_1 = Core(1, self.core_1_data_cache, self.core_1_instruction_cache, self, self.data_bus,
                           self.instruction_bus)
        self.core_2 = Core(2, self.core_1_data_cache, self.core_1_instruction_cache, self, self.data_bus,
                           self.instruction_bus)

        self.contexts = []

    # Processor methods
    def kick_start_program(self):
        self.load_memory_instructions()
        self.instantiate_data_memory()
        self.core_1.run()
        # self.core_2.run()
        # todo add ending of the program

    def store_instructions_in_memory(self, file_, current_block_number):
        line = file_.readline()
        temporary_block = Block()
        block_id = 24
        while line:
            split_line = line.split()
            if current_block_number % 4 == 0:
                temporary_block = Block()
                temporary_block.block_id = block_id
                temporary_block.word_0 = list(map(int, split_line))
                block_id += 1

            else:
                if current_block_number % 4 == 1:
                    temporary_block.word_1 = list(map(int, split_line))
                else:
                    if current_block_number % 4 == 2:
                        temporary_block.word_2 = list(map(int, split_line))
                    else:
                        temporary_block.word_3 = list(map(int, split_line))
                        self.instructions_memory.memory.append(temporary_block)

            line = file_.readline()
            current_block_number = current_block_number + 1

        return block_id

    def load_memory_instructions(self):
        current_block_number = 24
        current_file_number = 0
        for file_name in os.listdir('../assets'):
            file_ = open('../assets/' + file_name, 'r')
            create_context(current_file_number, current_block_number*16, self.contexts)
            last_block_number = self.store_instructions_in_memory(file_, current_block_number)
            current_block_number = last_block_number + 1
            current_file_number += 1
            # todo fix memory (fill the whole block)

    def instantiate_data_memory(self):
        for i in range(0, 24):
            block = Block()
            block.block_id = i
            block.word_0 = [0, 0, 0, 0]
            block.word_1 = [0, 0, 0, 0]
            block.word_2 = [0, 0, 0, 0]
            block.word_3 = [0, 0, 0, 0]

