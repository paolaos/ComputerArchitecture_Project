from cpu.CacheLine import CacheLine
from cpu.Memory import Memory

BLOCK_SIZE = 16


class Cache:
    def __init__(self, memory, cycles_to_load):
        self.cache_line_0 = CacheLine()
        self.cache_line_1 = CacheLine()
        self.cache_line_2 = CacheLine()
        self.cache_line_3 = CacheLine()
        self.size = 4
        self.memory: Memory = memory
        self.cycles_to_load = cycles_to_load

    def _get_block_line(self, block_id):
        """
        Get the line where a block should be stored in the cache
        :param block_id: the id of the block
        :return: The line number
        """
        return int(block_id % self.size)

    def _set_word_in_block(self, block_id, word, address):
        line = self._get_block_line(block_id)
        word_number = self.get_word_number_from_address(address)
        if line == 0:
            block = self.cache_line_0.block
        if line == 1:
            block = self.cache_line_1.block
        if line == 2:
            block = self.cache_line_2.block
        if line == 3:
            block = self.cache_line_3.block

        block.block_id = block_id

        if word_number == 0:
            block.word_0 = word
        if word_number == 1:
            block.word_1 = word
        if word_number == 2:
            block.word_2 = word
        if word_number == 3:
            block.word_3 = word

    def is_block_in_cache(self, block_id):
        """
        Check if a block is valid in the cache
        :param block_id:
        :return: True: hit, False: miss
        """
        line = self._get_block_line(block_id)
        in_cache = False
        if line == 0:
            in_cache = block_id == self.cache_line_0.get_block_id() and self.cache_line_0.status
        if line == 1:
            in_cache = block_id == self.cache_line_1.get_block_id() and self.cache_line_1.status
        if line == 2:
            in_cache = block_id == self.cache_line_2.get_block_id() and self.cache_line_2.status
        if line == 3:
            in_cache = block_id == self.cache_line_3.get_block_id() and self.cache_line_3.status
        return in_cache

    def invalidate_block(self, address):
        """
        Invalidate a block in cache
        :param address: address of the memory that should be invalidated
        """
        block_id = self.get_block_number_from_address(address)
        if self.is_block_in_cache(block_id):
            line = self._get_block_line(block_id)
            if line == 0:
                self.cache_line_0.status = False
            if line == 1:
                self.cache_line_1.status = False
            if line == 2:
                self.cache_line_2.status = False
            if line == 3:
                self.cache_line_3.status = False

    def store_block_to_cache(self, block):
        """
        Store a block in the cache
        :param block: the block that is going to be stored
        """
        line = self._get_block_line(block.block_id)
        if line == 0:
            self.cache_line_0.block = block
            self.cache_line_0.status = True
        if line == 1:
            self.cache_line_1.block = block
            self.cache_line_1.status = True
        if line == 2:
            self.cache_line_2.block = block
            self.cache_line_2.status = True
        if line == 3:
            self.cache_line_3.block = block
            self.cache_line_3.status = True

    def _get_block(self, block_id):
        """
        Get the block
        :param block_id: the id of the block to be retrieved
        :return: the block
        """
        if self.is_block_in_cache(block_id):
            line = self._get_block_line(block_id)
            if line == 0:
                return self.cache_line_0.block
            if line == 1:
                return self.cache_line_1.block
            if line == 2:
                return self.cache_line_2.block
            if line == 3:
                return self.cache_line_3.block

    def get_block_number_from_address(self, address):
        """

        :param address:
        :return:
        """
        return int(address // BLOCK_SIZE)

    def get_word_number_from_address(self, address):
        """

        :param address:
        :return:
        """
        return int(address % BLOCK_SIZE)

    def load_block(self, address):
        """

        :param address:
        :return:
        """
        block_number = self.get_block_number_from_address(address)
        block = self.memory.get_block(block_number)
        self.store_block_to_cache(block)

    def get_word_from_address(self, address):
        """
        Returns the word corresponding to a given address, resolves cache misses
        :param address:
        :return:
        """
        block_number = self.get_block_number_from_address(address)
        is_block_in_cache = self.is_block_in_cache(block_number)
        if not is_block_in_cache:
            # miss
            self.load_block(address)

        is_block_in_cache = self.is_block_in_cache(block_number)
        if is_block_in_cache:
            # hit
            block = self._get_block(block_number)
            return block.get_word_from_number(self.get_word_number_from_address(address))

    def get_loading_cycles(self, address):
        """
        Returns the amount of cycles that will take to get
        :param address:
        :return: the amount of cycles used to load the block
        """
        block_number = self.get_block_number_from_address(address)
        is_block_in_cache = self.is_block_in_cache(block_number)
        if is_block_in_cache:
            # hit
            return 0
        else:
            # miss
            return self.cycles_to_load

    def store_word(self, word, address):
        block_number = self.get_block_number_from_address(address)
        is_block_in_cache = self.is_block_in_cache(block_number)
        # store the word in cache if it is loaded
        if not is_block_in_cache:
            self._set_word_in_block(block_number, word, address)

        # store in data memory
        if address < 384:
            self.memory.set_value(word, address)
        else:
            print("Invalid data memory address ", address)

    def print_cache(self):
        self.cache_line_0.print_cache_line()
        self.cache_line_1.print_cache_line()
        self.cache_line_2.print_cache_line()
        self.cache_line_3.print_cache_line()
        print()
