from LexicalAnalyzer.lexical_analyzer import tokenize
from Parser.my_parser import Parser
from Standardizer.ast_factory import ASTFactory
from CSEmachine.cse_machine_factory import CSEMachineFactory

class Evaluvator:
    @staticmethod
    def evaluate(filename):

        with open(filename, 'r') as file:
            input_text = file.read()
    
        tokens = tokenize(input_text)
        if not tokens:
            print("Empty PROGRAM!!!!!!!!")
            return ""

        parser = Parser(tokens)
        ast = parser.parse()
        string_ast = parser.convert_ast_to_string_ast()

        ast_factory = ASTFactory()
        ast = ast_factory.get_abstract_syntax_tree(string_ast)
        ast.standardize()


        csem_factory = CSEMachineFactory()
        csem = csem_factory.get_cse_machine(ast)
        return csem.get_answer()
