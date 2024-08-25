from LexicalAnalyzer.tokens import MyToken
from LexicalAnalyzer.tokentype import TokenType
from LexicalAnalyzer.lexical_analyzer import tokenize
import sys
import os
# Example usage
project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
input_file_name = os.path.join(project_dir, "test program.txt")

# Read the contents of the input file
with open(input_file_name, 'r') as file:
    input_text = file.read()

tokens = tokenize(input_text)

for token in tokens:
    print(token)
