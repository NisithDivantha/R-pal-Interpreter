from Standardizer.standardizer_node import Node

class AST:
    def __init__(self, root):
        self.root = root
    
    def set_root(self, root):
        self.root = root
    
    def get_root(self):
        return self.root
    
    def standardize(self):
        if not self.root.isStandardized:
            self.root.standardize()
    
    def pre_order_traverse(self, node, i):
        print("." * i + node.getData())
        for child in node.children:
            self.pre_order_traverse(child, i + 1)
    
    def print_ast(self):
        self.pre_order_traverse(self.get_root(), 0)

    def print_tree(self,node, depth=0):
        if node is None:
            return
        print("  " * depth + node.data)
        for child in node.children:
            self.print_tree(child, depth + 1)