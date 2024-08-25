from .rand import Rand

class Int(Rand):
    def __init__(self, data):
        super().__init__(data)
        self.symbols = []