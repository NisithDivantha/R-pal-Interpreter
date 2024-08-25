from .symbol import Symbol

class Delta(Symbol):
    def __init__(self, i):
        super().__init__("delta")
        self.index = i

    def set_index(self, i):
        self.index = i

    def get_index(self):
        return self.index
