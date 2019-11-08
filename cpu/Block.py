class Block:
    def __init__(self):
        self._block_id = -1
        self._word_0 = []
        self._word_1 = []
        self._word_2 = []
        self._word_3 = []

    @property
    def block_id(self):
        return self._block_id

    @block_id.setter
    def block_id(self, block_id):
        self._block_id = block_id

    @property
    def word_0(self):
        return self._word_0

    @word_0.setter
    def word_0(self, word):
        self._word_0 = word

    @property
    def word_1(self):
        return self._word_1

    @word_1.setter
    def word_1(self, word):
        self._word_1 = word

    @property
    def word_2(self):
        return self._word_2

    @word_2.setter
    def word_2(self, word):
        self._word_2 = word

    @property
    def word_3(self):
        return self._word_3

    @word_3.setter
    def word_3(self, word):
        self._word_3 = word

    def get_block_id_from_address(self, address):
        return address // 16

    def get_word_from_number(self, number):
        word = number // 4
        if word == 0:
            return self.word_0
        if word == 1:
            return self.word_1
        if word == 2:
            return self.word_2
        if word == 3:
            return self.word_3
