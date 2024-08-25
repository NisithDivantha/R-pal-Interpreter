from Standardizer.NodeFactory import NodeFactory
from Standardizer.ast import AST
from Standardizer.standardizer_node import Node

class ASTFactory:
    def __init__(self):
        pass
    
    def get_abstract_syntax_tree(self, data):
        node = Node()
        root = Node.getNode2(data[0], 0)
        previous_node = root
        current_depth = 0
        
        for s in data[1:]:
            i = 0  # index of word
            d = 0  # depth of node
            
            while s[i] == '.':
                d += 1
                i += 1
            
            current_node = Node.getNode2(s[i:], d)
            
            if current_depth < d:
                previous_node.children.append(current_node)
                current_node.setParent(previous_node)
            else:
                while previous_node.getDepth() != d:
                    previous_node = previous_node.getParent()
                previous_node.getParent().children.append(current_node)
                current_node.setParent(previous_node.getParent())
            
            previous_node = current_node
            current_depth = d
        
        return AST(root)
