from typing import Dict
from .symbol import Symbol
from .id import Id

class E(Symbol):
    def __init__(self, i):
        super().__init__("e")
        self.index = i
        self.parent = None
        self.is_removed = False
        self.values = {}

    def set_index(self, i):
        self.index = i

    def get_index(self):
        return self.index

    def set_parent(self, e):
        self.parent = e

    def get_parent(self):
        return self.parent

    def set_is_removed(self, is_removed):
        self.is_removed = is_removed

    def get_is_removed(self):
        return self.is_removed

    # def lookup(self, id):
    #     if id in self.values:
    #         return self.values[id]
    #     elif self.parent is not None:
    #         return self.parent.lookup(id)
    #     else:
    #         return Symbol(id.get_data())


    def lookup(self, id):
        for key in self.values:
            if key.get_data() == id.get_data():
                return self.values[key]
        if self.parent is not None:
            return self.parent.lookup(id)
        else:
            return Symbol(id.get_data())
