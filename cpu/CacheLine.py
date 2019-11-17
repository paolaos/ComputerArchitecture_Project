from cpu.Block import Block


class CacheLine:
    def __init__(self):
        self.status = False
        self.block = Block()

    def get_block_id(self):
        return self.block.block_id

    def print_cache_line(self):
        status = "I"
        if self.status:
            status = "C"
        print(status, " ", self.block.block_id, " ", self.block.word_0, " ", self.block.word_1, " ", self.block.word_2,
              " ", self.block.word_3)
