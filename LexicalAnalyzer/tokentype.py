from enum import Enum

class TokenType(Enum):
    KEYWORD = 1
    IDENTIFIER = 2
    INTEGER = 3
    STRING = 4
    END_OF_TOKENS = 5
    PUNCTUATION = 6
    OPERATOR = 7