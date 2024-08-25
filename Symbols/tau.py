from .symbol import Symbol

class Tau(Symbol):
    def __init__(self, n):
        super().__init__("tau")
        self.n = n
        self.symbols = []

    def get_n(self):
        return self.n
