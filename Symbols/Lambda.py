from Symbols.symbol import Symbol
from Symbols.delta import Delta
from Symbols.id import Id

class Lambda(Symbol):
    def __init__(self, i):
        super().__init__("lambda")
        self.index = i
        self.environment = None
        self.identifiers = []
        self.delta = None
    
    def set_environment(self, n):
        self.environment = n
    
    def get_environment(self):
        return self.environment
    
    def set_delta(self, delta):
        self.delta = delta
    
    def get_delta(self):
        return self.delta
    
    def get_index(self):
        return self.index
