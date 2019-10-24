from cpu.CacheLine import CacheLine


class Cache:
    def __init__(self):
        self._cache_line_0 = CacheLine
        self._cache_line_1 = CacheLine
        self._cache_line_2 = CacheLine
        self._cache_line_3 = CacheLine
        self._size = 4

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

    def get_block_line(self, block_address):
        return block_address % self._size

    def is_block_in_cache(self, block_address):
        """Return a boolean that indicates if the block is valid in the cache

            Is the block valid in the cache
            """
        line = self.get_block_line(block_address)
        in_cache = False
        if line == 0:
            in_cache = block_address == self.cache_line_0.block_id and self.cache_line_0.status
        if line == 1:
            in_cache = block_address == self.cache_line_1.block_id and self.cache_line_1.status
        if line == 2:
            in_cache = block_address == self.cache_line_2.block_id and self.cache_line_2.status
        if line == 3:
            in_cache = block_address == self.cache_line_3.block_id and self.cache_line_3.status
        return in_cache

    def invalidate_block(self, block_address):
        if self.is_block_in_cache(block_address):
            line = self.get_block_line(block_address)
            if line == 0:
                self.cache_line_0.status = False
            if line == 1:
                self.cache_line_1.status = False
            if line == 2:
                self.cache_line_2.status = False
            if line == 3:
                self.cache_line_3.status = False

    def set_block(self, block_address, block_content):
        print('hello')
