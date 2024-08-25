import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from LexicalAnalyzer.lexical_analyzer import tokenize
from Parser.my_parser import Parser
from Standardizer.ast import AST
from Standardizer.ast_factory import ASTFactory

def main() :

    project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    input_file_name = os.path.join(project_dir, "test program.txt")

    with open(input_file_name, 'r') as file:
        input_text = file.read()

    tokens = tokenize(input_text)
    # for token in tokens :
    #     print(token.get_value(), token.get_type())
        # print(token)

    parser = Parser(tokens)
    parser.parse()
    stringast = parser.convert_ast_to_string_ast()
    # for i in stringast :
    #     print(i)
    astfactory = ASTFactory()
    ast  = astfactory.get_abstract_syntax_tree(stringast)
    ast.standardize()

    ast.print_ast()


if __name__ == '__main__' :
    main()