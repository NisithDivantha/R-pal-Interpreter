from .rand import Rand

class Str(Rand):
    def __init__(self, data):
        super().__init__(data)
        self.symbols = []
