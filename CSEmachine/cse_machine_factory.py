from CSEmachine.cse_machine import CSEMachine
from Symbols.e import E
from Symbols.delta import Delta 
from Symbols.b import B
from Symbols.beta import Beta
from Symbols.bool import Bool
from Symbols.bop import Bop
from Symbols.delta import Delta
from Symbols.dummy import Dummy
from Symbols.gamma import Gamma
from Symbols.id import Id
from Symbols.int import Int
from Symbols.tau import Tau
from Symbols.tup import Tup
from Symbols.uop import Uop
from Symbols.e import E
from Symbols.err import Err
from Symbols.rator import Rator
from Symbols.str import Str
from Symbols.Lambda import Lambda
from Symbols.ystar import Ystar
from Standardizer.ast import AST


class CSEMachineFactory:
    def __init__(self):
        self.e0 = E(0)
        self.i = 1
        self.j = 0

    def get_symbol(self, node):
        # print("in here")
        data = node.data
        children = node.children
        
        # Unary operators
        if data == "not" or data == "neg":
            return Uop(data)
        # Binary operators
        elif data in ["+", "-", "*", "/", "**", "&", "or", "eq", "ne", "ls", "le", "gr", "ge", "aug"]:
            return Bop(data)
        # Gamma
        elif data == "gamma":
            return Gamma()
        # Tau
        elif data == "tau":
            return Tau(len(children))
        # Ystar
        elif data == "<Y*>":
            return Ystar()
        # Operands
        # elif data == "lambda":
        #     return Lambda(self.i)
        else:
            if data.startswith("<IDENTIFIER:"):
                return Id(data[4:-1])
            elif data.startswith("<INTEGER:"):
                return Int(data[9:-1]) 
            elif data.startswith("<STRING:"):
                return Str(data[9:-2])
            elif data.startswith("<NIL"):
                return Tup()
            elif data.startswith("<true>"):
                return Bool("true")
            elif data.startswith("<false>"):
                return Bool("false")
            elif data.startswith("<dummy>"):
                return Dummy()
            else:
                print("Err node:", data)
                return Err()
    def get_control(self, ast):
        # print(ast.root)
        control = [self.e0, self.get_delta(ast.get_root())]
        return control

    def get_stack(self):
        stack = [self.e0]
        return stack

    def get_environment(self):
        environment = [self.e0]
        return environment

    def get_cse_machine(self, ast):
        return CSEMachine(self.get_control(ast), self.get_stack(), self.get_environment())

    def get_delta(self, node):
        delta = Delta(self.j)
        self.j += 1
        # print("node data", node.data)
        delta.symbols = self.get_pre_order_traverse(node)
        # for i in delta.symbols:
        #     print(i.data)
        # print("delta symbols", delta.symbols.data)
        return delta
    
    def get_pre_order_traverse(self, node):
        symbols = []
        if node.data == "lambda":
            symbols.append(self.get_lambda(node))
        elif node.data == "->":
            symbols.append(self.get_delta(node.children[1]))
            symbols.append(self.get_delta(node.children[2]))
            symbols.append(Beta())
            symbols.append(self.get_b(node.children[0]))
        else:
            symbols.append(self.get_symbol(node))
            for child in node.children:
                symbols.extend(self.get_pre_order_traverse(child))
        return symbols


    
    def get_lambda(self, node):
        lambda_obj = Lambda(self.i)
        self.i += 1
        lambda_obj.set_delta(self.get_delta(node.children[1]))
        if "," == node.children[0].data:
            for identifier in node.children[0].children:
                lambda_obj.identifiers.append(Id(identifier.data[4:-1]))
        else:
            lambda_obj.identifiers.append(Id(node.children[0].data[4:-1]))
        return lambda_obj

    def get_b(self, node):
        b = B()
        b.symbols = self.get_pre_order_traverse(node)
        return b
# Path: CSEmachine/cse_machine.py