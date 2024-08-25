from .rand import Rand

class Id(Rand):
    def __init__(self, data):
        super().__init__(data)
        self.symbols = []

    def get_data(self):
        return super().get_data()
