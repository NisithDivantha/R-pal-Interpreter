# import re
# from .tokens import MyToken

# def tokenize(input_str):
#     tokens = []
#     keywords = {
#         'COMMENT': r'//.*',
#         'KEYWORD': r'(let|in|fn|where|aug|or|not|gr|ge|ls|le|eq|ne|true|false|nil|dummy|within|and|rec)\b',
#         'IDENTIFIER': r'[a-zA-Z][a-zA-Z0-9_]*',
#         'INTEGER': r'\d+',
#         'OPERATOR': r'[+\-*<>&.@/:=~|$\#!%^_\[\]{}"\'?]+',
#         'STRING': r'\'\'\'(?:\\t|\\n|\\\'|\\\'\'|[\(\);,\'a-zA-Z0-9+\-*<>&.@/:=~|$\#!%^_\[\]{}"\'?\s])+\'\'\'',
#         'SPACES': r'[ \t\n]+',
#         'PUNCTUATION': r'[();,]'
#     }
    
#     while input_str:
#         matched = False
#         for key, pattern in keywords.items():
#             match = re.match(pattern, input_str)
#             if match:
#                 if key != 'SPACES':
#                     if key == 'COMMENT':
#                         comment = match.group(0)
#                         input_str = input_str[match.end():]
#                         matched = True
#                         break
#                     else:
#                         tokens.append(MyToken(key, match.group(0)))
#                         input_str = input_str[match.end():]
#                         matched = True
#                         break
#                 input_str = input_str[match.end():]
#                 matched = True
#                 break
#         if not matched:
#             print("Error: Unable to tokenize input")
#     return tokens




# def tokenize(input_str):
#     tokens = []
#     keywords = {
#         'Comment': r'//.*',
#         'Identifier': r'[a-zA-Z][a-zA-Z0-9_]*',
#         'Integer': r'\d+',
#         'Operator': r'[+\-*<>&.@/:=~|$\#!%^_\[\]{}"\'?]+',
#         'String': r'\'\'\'(?:\\t|\\n|\\\'|\\\'\'|[\(\);,\'a-zA-Z0-9+\-*<>&.@/:=~|$\#!%^_\[\]{}"\'?\s])+\'\'\'',
#         'Spaces': r'[ \t\n]+',
#         'Punctuation': r'[();,]'
#     }
    
#     while input_str:
#         matched = False
#         for key, pattern in keywords.items():
#             match = re.match(pattern, input_str)
#             if match:
#                 if key != 'Spaces':
#                     if key == 'Comment':
#                         comment = match.group(0)
#                         input_str = input_str[match.end():]
#                         matched = True
#                         break
#                     else:
#                         tokens.append(tokens(key, match.group(0)))
#                         input_str = input_str[match.end():]
#                         matched = True
#                         break
#                 input_str = input_str[match.end():]
#                 matched = True
#                 break
#         if not matched:
#             print("Error: Unable to tokenize input")
#     return tokens

import re
from .tokens import MyToken
from .tokentype import TokenType  # Import TokenType enum

def tokenize(input_str):
    tokens = []
    keywords = {
    'COMMENT': r'//.*',
    'KEYWORD': r'(let|in|fn|where|aug|or|not|gr|ge|ls|le|eq|ne|true|false|nil|dummy|within|and|rec)\b',
    # 'STRING': r"'(?:\\t|\\n|\\\'|\\\'\'|[\(\);,'a-zA-Z0-9+\-*<>&.@/:=~|$\#!%^_\[\]{}\"\'?\s])+?'",
    'STRING': r'\'(?:\\\'|[^\'])*\'',
    'IDENTIFIER': r'[a-zA-Z][a-zA-Z0-9_]*',
    'INTEGER': r'\d+',
    'OPERATOR': r'[+\-*<>&.@/:=~|$\#!%^_\[\]{}"\'?]+',
    'SPACES': r'[ \t\n]+',
    'PUNCTUATION': r'[();,]'
}

    
    while input_str:
        matched = False
        for key, pattern in keywords.items():
            match = re.match(pattern, input_str)
            if match:
                if key != 'SPACES':
                    if key == 'COMMENT':
                        comment = match.group(0)
                        input_str = input_str[match.end():]
                        matched = True
                        break
                    else:
                        token_type = getattr(TokenType, key)  # Get TokenType enum value
                        if not isinstance(token_type, TokenType):
                            raise ValueError(f"Token type '{key}' is not a valid TokenType")
                        tokens.append(MyToken(token_type, match.group(0)))
                        input_str = input_str[match.end():]
                        matched = True
                        break
                input_str = input_str[match.end():]
                matched = True
                break
        if not matched:
            print("Error: Unable to tokenize input")
    return tokens


# def __init__(self, input_file_name):
#     self.input_file_name = input_file_name
#     self.tokens = []

# def scan(self):
#     try:
#         with open(self.input_file_name, 'r') as file:
#             line_count = 0
#             for line in file:
#                 line_count += 1
#                 self.tokenize(line)
#                 # try:
#                 #     self.tokenize_line(line)
#                 # except CustomException as e:
#                 #     raise CustomException(f"{e.message} in LINE: {line_count}\nERROR in lexical_analysis.")
#     except IOError as e:
#         print("Error reading file:", e)

#     return self.tokens

# def tokenize(self, line):
#     # Tokenization patterns
#     digit = r"\d"
#     letter = r"[a-zA-Z]"
#     operator_symbol = r"[+\-*/<>&.@/:=~|$!#%^_\[\]{}\"`\\?]"
#     escape = r"(\\\\'|\\\\t|\\\\n|\\\\\\\\)"

#     identifier_pattern = re.compile(letter + r"(" + letter + r"|" + digit + r"|" + r"_)*")
#     integer_pattern = re.compile(digit + r"+")
#     operator_pattern = re.compile(operator_symbol + r"+")

#     punctuation_pattern = re.compile(r"[(),;]")
#     spaces_pattern = re.compile(r"(\s|\t)+")

#     string_pattern = re.compile(r"'(" + letter + r"|" + digit + r"|" + operator_symbol + r"|" + escape + r"|" + r"|".join([r"\\\\" + p for p in ["(", ")", ";", ",", "'", "a-zA-Z0-9+\-*/<>&.@/:=~|$!#%^_\[\]{}\"`\\?"]]) + r")*'")
#     comment_pattern = re.compile(r"//.*")

#     current_index = 0
#     while current_index < len(line):
#         current_char = line[current_index]

#         # Skip spaces and comments
#         space_match = spaces_pattern.match(line[current_index:])
#         comment_match = comment_pattern.match(line[current_index:])
#         if comment_match:
#             comment = comment_match.group()
#             current_index += len(comment)
#             continue
#         if space_match:
#             space = space_match.group()
#             current_index += len(space)
#             continue

#         # Identifier
#         identifier_match = identifier_pattern.match(line[current_index:])
#         if identifier_match:
#             identifier = identifier_match.group()
#             keywords = [
#                 "let", "in", "fn", "where", "aug", "or", "not", "gr", "ge", "ls",
#                 "le", "eq", "ne", "true", "false", "nil", "dummy", "within", "and", "rec"
#             ]
#             token_type = TokenType.KEYWORD if identifier in keywords else TokenType.IDENTIFIER
#             self.tokens.append(MyToken(token_type, identifier))
#             current_index += len(identifier)
#             continue

#         # Integer
#         integer_match = integer_pattern.match(line[current_index:])
#         if integer_match:
#             integer = integer_match.group()
#             self.tokens.append(MyToken(TokenType.INTEGER, integer))
#             current_index += len(integer)
#             continue

#         # Operator
#         operator_match = operator_pattern.match(line[current_index:])
#         if operator_match:
#             operator = operator_match.group()
#             self.tokens.append(MyToken(TokenType.OPERATOR, operator))
#             current_index += len(operator)
#             continue

#         # String
#         string_match = string_pattern.match(line[current_index:])
#         if string_match:
#             string = string_match.group()
#             self.tokens.append(MyToken(TokenType.STRING, string))
#             current_index += len(string)
#             continue

#         # Punctuation
#         punctuation_match = punctuation_pattern.match(current_char)
#         if punctuation_match:
#             self.tokens.append(MyToken(TokenType.PUNCTUATION, current_char))
#             current_index += 1
#             continue

            # # Must throw an exception if the next token is not of any type
            # raise CustomException(f"Unable to tokenize the CHARACTER: {current_char} at INDEX: {current_index}")