from .symbol import Symbol

class Err(Symbol):
    def __init__(self):
        super().__init__("error")
        self.symbols = []