from cpu.CacheLine import CacheLine
from cpu.Memory import Memory

BLOCK_SIZE = 16


class Cache:
    def __init__(self, memory):
        self._cache_line_0 = CacheLine()
        self._cache_line_1 = CacheLine()
        self._cache_line_2 = CacheLine()
        self._cache_line_3 = CacheLine()
        self._size = 4
        self.memory: Memory = memory


    @property
    def cache_line_0(self):
        return self._cache_line_0

    @cache_line_0.setter
    def cache_line_0(self, cache_line):
        self._cache_line_0 = cache_line

    @property
    def cache_line_1(self):
        return self._cache_line_1

    @cache_line_1.setter
    def cache_line_1(self, cache_line):
        self._cache_line_1 = cache_line

    @property
    def cache_line_2(self):
        return self._cache_line_2

    @cache_line_2.setter
    def cache_line_2(self, cache_line):
        self._cache_line_2 = cache_line

    @property
    def cache_line_3(self):
        return self._cache_line_3

    @cache_line_3.setter
    def cache_line_3(self, cache_line):
        self._cache_line_3 = cache_line

    def get_block_line(self, block_id):
        """
        Get the line where a bloc should be stored in the cache
        :param block_id: the id of the block
        :return: The line number
        """
        return int(block_id % self._size)

    def is_block_in_cache(self, block_id):
        """
        Check if a block is valid in the cache
        :param block_id:
        :return: True: hit, False: miss
        """
        line = self.get_block_line(block_id)
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

    def invalidate_block(self, block_id):
        """
        Invalidate a block in cache
        :param block_id:
        :return:
        """
        if self.is_block_in_cache(block_id):
            line = self.get_block_line(block_id)
            if line == 0:
                self.cache_line_0.status(False)
            if line == 1:
                self.cache_line_1.status(False)
            if line == 2:
                self.cache_line_2.status(False)
            if line == 3:
                self.cache_line_3.status(False)

    def store_block_to_cache(self, block):
        """
        Store a block in the cache
        :param block: the block that is going to be stored
        """
        line = self.get_block_line(block.block_id)
        if line == 0:
            self.cache_line_0.block(block)
            self.cache_line_0.status(True)
        if line == 1:
            self.cache_line_1.block(block)
            self.cache_line_1.status(True)
        if line == 2:
            self.cache_line_2.block(block)
            self.cache_line_2.status(True)
        if line == 3:
            self.cache_line_3.block(block)
            self.cache_line_3.status(True)

    def get_block(self, block_id):
        """
        Get the block
        :param block_id: the id of the block to be retrieved
        :return: the block
        """
        if self.is_block_in_cache(block_id):
            line = self.get_block_line(block_id)
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
            block = self.get_block(block_number)
            return block.get_word_from_number(self.get_word_number_from_address(address))
