from cpu.CacheLine import CacheLine


class Cache:
    def __init__(self):
        self._cache_line_0 = CacheLine()
        self._cache_line_1 = CacheLine()
        self._cache_line_2 = CacheLine()
        self._cache_line_3 = CacheLine()
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

    def get_block_line(self, block_id):
        return block_id % self._size

    def is_block_in_cache(self, block_id):
        """Return a boolean that indicates if the block is valid in the cache

            True: hit
            False: miss """
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

    def load_block_to_cache(self, block):
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
