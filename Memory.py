from Block import Block
from Instruction import Instruction

BLOCK_SIZE = 16


class Memory:

    def __init__(self, starting_address, length):
        self.memory = [0] * length
        self.length = length
        self.starting_address = starting_address


    def get_block(self, block_index):
        """
        Creates a copy of a block object from memory with its respective values,
        based on the solicited block's index. Generally used when core needs to
        read a value from memory.
        :param block_index: index of the solicited block
        :return: an instance of a block with its respective values
        """
        address = block_index * BLOCK_SIZE
        if self.length > address >= 384:
            # in case it's an instruction block
            block = Block()
            block.block_id = block_index
            block.word_0 = Instruction(self.memory[address], self.memory[address+1], self.memory[address+2],
                                       self.memory[address+3])
            block.word_1 = Instruction(self.memory[address + 4], self.memory[address+5], self.memory[address+6],
                                       self.memory[address+7])
            block.word_2 = Instruction(self.memory[address + 8], self.memory[address+9], self.memory[address+10],
                                       self.memory[address+11])
            block.word_3 = Instruction(self.memory[address + 12], self.memory[address+13], self.memory[address+14],
                                       self.memory[address+15])
            return block

        if 0 <= address < 384:
            # in case it's a data block
            block = Block()
            block.block_id = block_index
            block.word_0 = self.memory[address]
            block.word_1 = self.memory[address + 1]
            block.word_2 = self.memory[address + 2]
            block.word_3 = self.memory[address + 3]
            return block

        else:
            print("There was an error retrieving the block number ", block_index)

    def set_value(self, value, address):
        """
        Accesses a memory address to change its value. Generally used when core
        needs to write a value in memory.
        :param value: the new value that wants to be written in memory
        :param address: where in memory the value will be written
        """
        self.memory[address//4] = value

    def print_memory(self):
        """
        Used mainly for debugging purposes, prints a user friendly state of the
        memory in order to check the values.
        """
        print("\nState of the memory")
        i = 0
        while i < len(self.memory):
            print(self.memory[i], "\t", self.memory[i+1], "\t", self.memory[i+2], "\t", self.memory[i+3], "\t|\t",
                  self.memory[i+4], "\t", self.memory[i+5], "\t", self.memory[i+6], "\t", self.memory[i+7], "\t|\t",
                  self.memory[i+8], "\t", self.memory[i+9], "\t", self.memory[i+10], "\t", self.memory[i+11], "\t|\t",
                  self.memory[i+12], "\t", self.memory[i+13], "\t", self.memory[i+14], "\t", self.memory[i+15], "\t|\t")
            i += 16

    def print_part_of_memory(self, start, end):
        """
        Used mainly for debugging purposes, prints a user friendly section of the
        memory in order to check the values at a specific place.
        :param start: initial position in memory to print
        :param end: final position in memory to print
        """
        i = start
        while i < end / 4:
            print(self.memory[i], "\t", self.memory[i + 1], "\t", self.memory[i + 2], "\t", self.memory[i + 3], "\t|\t",
                  self.memory[i + 4], "\t", self.memory[i + 5], "\t", self.memory[i + 6], "\t", self.memory[i + 7],
                  "\t|\t",
                  self.memory[i + 8], "\t", self.memory[i + 9], "\t", self.memory[i + 10], "\t", self.memory[i + 11],
                  "\t|\t",
                  self.memory[i + 12], "\t", self.memory[i + 13], "\t", self.memory[i + 14], "\t", self.memory[i + 15],
                  "\t|\t")
            i += 16
