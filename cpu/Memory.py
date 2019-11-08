from cpu.Block import Block
from cpu.Instruction import Instruction

BLOCK_SIZE = 16


class Memory:
    def __init__(self, starting_address, length):
        self._memory = [0] * length
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

    def get_block(self, block_index):
        address = block_index * BLOCK_SIZE
        if self.length > address >= 384:
            # its an instruction
            block = Block()
            block.block_id = block_index
            block.word_0 = Instruction(self._memory[address], self._memory[address+1], self._memory[address+2],
                                       self._memory[address+3])
            block.word_1 = Instruction(self._memory[address + 4], self._memory[address+5], self._memory[address+6],
                                       self._memory[address+7])
            block.word_2 = Instruction(self._memory[address + 8], self._memory[address+9], self._memory[address+10],
                                       self._memory[address+11])
            block.word_3 = Instruction(self._memory[address + 12], self._memory[address+13], self._memory[address+14],
                                       self._memory[address+15])
            return block

        if 0 <= address < 384:
            # Data
            block = Block()
            block.block_id = block_index
            block.word_0 = self._memory[address]
            block.word_1 = self._memory[address + 1]
            block.word_2 = self._memory[address + 2]
            block.word_3 = self._memory[address + 3]
            return block

        else:
            print("There was an error retrieving the block number ", block_index)

    def print_memory(self):
        # debugging purposes
        i = 0
        k = 0
        times = int(len(self.memory) / 16)
        if len(self.memory) % times > 0:
            times -= 1
        while k < times:
            print(self.memory[i], "\t", self.memory[i+1], "\t", self.memory[i+2], "\t", self.memory[i+3], "\t|\t",
                  self.memory[i+4], "\t", self.memory[i+5], "\t", self.memory[i+6], "\t", self.memory[i+7], "\t|\t",
                  self.memory[i+8], "\t", self.memory[i+9], "\t", self.memory[i+10], "\t", self.memory[i+11], "\t|\t",
                  self.memory[i+12], "\t", self.memory[i+13], "\t", self.memory[i+14], "\t", self.memory[i+15], "\t|\t")
            i += 16
