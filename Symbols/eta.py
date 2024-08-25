from .symbol import Symbol

class Eta(Symbol):
    def __init__(self):
        super().__init__("eta")
        self.index = 0
        self.environment = 0
        self.identifier = None
        self.lambda_expr = None

    def set_index(self, i):
        self.index = i

    def get_index(self):
        return self.index

    def set_environment(self, e):
        self.environment = e

    def get_environment(self):
        return self.environment

    def set_identifier(self, id):
        self.identifier = id

    def set_lambda(self, lambda_expr):
        self.lambda_expr = lambda_expr

    def get_lambda(self):
        return self.lambda_expr
