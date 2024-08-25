# import sys
# import os

# sys.path.append('/Users/nisith/Desktop/Programming Languages/Project')

# from parser import Parser
# from LexicalAnalyzer.lexical_analyzer import tokenize


# def main():
#     project_dir = '/Users/nisith/Desktop/Programming Languages/Project'
#     input_file_name = os.path.join(project_dir, "t1.txt")

#     # Read the contents of the input file
#     with open(input_file_name, 'r') as file:
#         input_text = file.read()

#     # Tokenize the input text
#     tokens = tokenize(input_text)

#     try:
#         parser = Parser(tokens)
#         ast = parser.parse()
#         if ast is None:
#             return

#         # Print the generated AST
#         for node in ast:
#             print(node)

#         string_ast = parser.convert_ast_to_string_ast()
#         for string in string_ast:
#             print(string)

#     except Exception as e:
#         print(str(e))

# if __name__ == "__main__":
#     main()
#############
import sys
import os

# Adding the parent directory of the script to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Parser.my_parser import Parser
from LexicalAnalyzer.lexical_analyzer import tokenize


def get_string_ast():
    project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    input_file_name = os.path.join(project_dir, "test program.txt")
    # print("Project directory:", project_dir)
    # print("Input file path:", input_file_name)

    # Read the contents of the input file
    with open(input_file_name, 'r') as file:
        input_text = file.read()

    # Tokenize the input text
    tokens = tokenize(input_text)
    try:
        parser = Parser(tokens)

        ast = parser.parse()
      
        if ast is None:
            return None

        string_ast = parser.convert_ast_to_string_ast()
        return string_ast

    except Exception as e:
        print(str(e))
        return None

if __name__ == "__main__":
    string_ast = get_string_ast()
    if string_ast:
        for string in string_ast:
            print(string)




# import sys
# import os

# # Adding the parent directory of the script to sys.path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# from Parser.my_parser import Parser
# from LexicalAnalyzer.lexical_analyzer import tokenize
# from Standardizer.AST import AST

# def main():
#     project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
#     input_file_name = os.path.join(project_dir, "t1.txt")

#     print("Project directory:", project_dir)
#     print("Input file path:", input_file_name)

#     # Read the contents of the input file
#     with open(input_file_name, 'r') as file:
#         input_text = file.read()

#     # Tokenize the input text
#     tokens = tokenize(input_text)

#     try:
#         parser = Parser(tokens)
#         ast = parser.parse()
#         if ast is None:
#             return

#         # Construct the AST using AST class
#         abstract_syntax_tree = AST(ast)

#         # Print the AST
#         print("Abstract Syntax Tree:")
#         abstract_syntax_tree.print_ast()

#     except Exception as e:
#         print(str(e))

# if __name__ == "__main__":
#     main()




# import sys
# import os

# # Adding the parent directory of the script to sys.path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# from Parser.my_parser import Parser
# from LexicalAnalyzer.lexical_analyzer import tokenize
# from Standardizer.ASTFactory import ASTFactory

# def main():
#     project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
#     input_file_name = os.path.join(project_dir, "t1.txt")

#     print("Project directory:", project_dir)
#     print("Input file path:", input_file_name)

#     # Read the contents of the input file
#     with open(input_file_name, 'r') as file:
#         input_text = file.read()

#     # Tokenize the input text
#     tokens = tokenize(input_text)

#     try:
#         parser = Parser(tokens)
#         ast = parser.parse()
#         if ast is None:
#             return

#         # Convert the AST to a list of data representing the tree structure
#         ast_data = parser.convert_ast_to_string_ast()
#         # Construct the AST using ASTFactory
#         ast_factory = ASTFactory()
#         abstract_syntax_tree = ast_factory.get_abstract_syntax_tree(ast_data)
#         print(abstract_syntax_tree
#         # Now you can work with the abstract_syntax_tree as needed
        
#     except Exception as e:
#         print(str(e))

# if __name__ == "__main__":
#     main()
