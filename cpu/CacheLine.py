from cpu.Block import Block


class CacheLine:
    def __init__(self):
        self.status = False
        self.block = Block()

    def get_block_id(self):
        return self.block.block_id
