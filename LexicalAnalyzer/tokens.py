from .tokentype import TokenType

class MyToken:
    def __init__(self, token_type, value):
        if not isinstance(token_type, TokenType):
            raise ValueError("token_type must be an instance of TokenType enum")
        self.type = token_type
        self.value = value

    # Getters for type and value
    def get_type(self):
        return self.type

    def get_value(self):
        return self.value
    
    def __str__(self):
        return f"<{self.type.name}, {self.value}>"
