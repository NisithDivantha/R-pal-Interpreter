# from NodeS import Node
# from NodeFactory import NodeFactory

# def standardize(self):
#     if not self.isStandardized:
#         for child in self.children:
#             child.standardize()
        
#         if self.data == "let":
#             # Standardizing let
#             temp1 = self.children[0].children[1]
#             temp1.setParent(self)
#             temp1.setDepth(self.depth + 1)
#             temp2 = self.children[1]                    
#             temp2.setParent(self.children[0])
#             temp2.setDepth(self.depth + 2)
#             self.children[1] = temp1
#             self.children[0].setData("lambda")
#             self.children[0].children[1] = temp2
#             self.setData("gamma")
        
#         elif self.data == "where":
#             # Standardizing where
#             temp = self.children[0]
#             self.children[0] = self.children[1]
#             self.children[1] = temp
#             self.setData("let")
#             self.standardize()
        
#         elif self.data == "function_form":
#             # Standardizing function_form
#             Ex = self.children[-1]
#             currentLambda = NodeFactory.getNode("lambda", self.depth + 1, self, [], True)
#             self.children.insert(1, currentLambda)
#             while self.children[2] != Ex:
#                 V = self.children[2]
#                 self.children.pop(2)
#                 V.setDepth(currentLambda.depth + 1)
#                 V.setParent(currentLambda)
#                 currentLambda.children.append(V)
#                 if len(self.children) > 3:
#                     currentLambda = NodeFactory.getNode("lambda", currentLambda.depth + 1, currentLambda, [], True)
#                     currentLambda.getParent().children.append(currentLambda)
#             currentLambda.children.append(Ex)
#             self.children.pop(2)
#             self.setData("=")
        
#         elif self.data == "lambda":
#             # Standardizing lambda (multi-parameter functions)
#             if len(self.children) > 2:
#                 Ey = self.children[-1]
#                 currentLambdax = NodeFactory.getNode("lambda", self.depth + 1, self, [], True)
#                 self.children.insert(1, currentLambdax)
#                 while self.children[2] != Ey:
#                     V = self.children[2]
#                     self.children.pop(2)
#                     V.setDepth(currentLambdax.depth + 1)
#                     V.setParent(currentLambdax)
#                     currentLambdax.children.append(V)
#                     if len(self.children) > 3:
#                         currentLambdax = NodeFactory.getNode("lambda", currentLambdax.depth + 1, currentLambdax, [], True)
#                         currentLambdax.getParent().children.append(currentLambdax)
#                 currentLambdax.children.append(Ey)
#                 self.children.pop(2)
 
#         elif self.data == "within":
#             # Standardizing within
#             X1 = self.children[0].children[0]
#             X2 = self.children[1].children[0]
#             E1 = self.children[0].children[1]
#             E2 = self.children[1].children[1]
#             gamma = NodeFactory.getNode("gamma", self.depth + 1, self, [], True)
#             lambda_ = NodeFactory.getNode("lambda", self.depth + 2, gamma, [], True)
#             # Existing code...
#             lambda_.children.append(E2)
#             gamma.children.append(lambda_)
#             gamma.children.append(E1)
#             self.children.clear()
#             self.children.append(self.children[X2])  
#             self.setData("=")
        
#         elif self.data == "@":
#             # Standardizing @
#             gamma1 = NodeFactory.getNode("gamma", self.depth + 1, self, [], True)
#             e1 = self.children[0]
#             e1.setDepth(e1.getDepth() + 1)
#             e1.setParent(gamma1)
#             n = self.children[1]
#             n.setDepth(n.getDepth() + 1)
#             n.setParent(gamma1)
#             gamma1.children.append(n)
#             gamma1.children.append(e1)
#             self.children.pop(0)
#             self.children.pop(0)
#             self.children.insert(0, gamma1)
#             self.setData("gamma")
        
#         elif self.data == "and":
#             # Standardizing and (simultaneous definitions)
#             comma = NodeFactory.getNode(",", self.depth + 1, self, [], True)
#             tau = NodeFactory.getNode("tau", self.depth + 1, self, [], True)
#             for equal in self.children:
#                 equal.children[0].setParent(comma)
#                 equal.children[1].setParent(tau)
#                 comma.children.append(equal.children[0])
#                 tau.children.append(equal.children[1])
#             self.children.clear()
#             self.children.append(comma)
#             self.children.append(tau)
#             self.setData("=")
        
#         elif self.data == "rec":
#             # Standardizing rec
#             X = self.children[0].children[0]
#             E = self.children[0].children[1]
#             F = NodeFactory.getNode(X.getData(), self.depth + 1, self, X.children, True)
#             G = NodeFactory.getNode("gamma", self.depth + 1, self, [], True)
#             Y = NodeFactory.getNode("<Y*>", self.depth + 2, G, [], True)
#             L = NodeFactory.getNode("lambda", self.depth + 2, G, [], True)
#             X.setDepth(L.depth + 1)
#             X.setParent(L)
#             E.setDepth(L.depth + 1)
#             E.setParent(L)
#             L.children.append(X)
#             L.children.append(E)
#             G.children.append(Y)
#             G.children.append(L)
#             self.children.clear()
#             self.children.append(F)
#             self.children.append(G)
#             self.setData("=")
        
#         # Unary & binary operators, tuples, conditionals, and commas are not standardized due to CSE rules 6-13
        
#         self.isStandardized = True


class Node:

    def __init__(self) :
        self.data = None
        self.depth = None
        self.parent = None
        self.children = []
        self.isStandardized = False

    def getNode(self, data, depth, parent, children, isStandardized) :
        node = Node()
        node.setData(data)
        node.setDepth(depth)
        node.setParent(parent)
        node.children = children
        node.isStandardized = isStandardized
        return node

    def getNode2(data, depth) :
        node = Node()
        node.setData(data)
        node.setDepth(depth)
        node.children = []
        return node

    def setData(self, data) :
        self.data = data
    
    def getData(self) :
        return self.data
    
    def getDegree(self) :
        return len(self.children)
    
    def setDepth(self, depth) :
        self.depth = depth

    def getDepth(self) :
        return self.depth
    
    def setParent(self, parent) :
        self.parent = parent

    def getParent(self) :
        return self.parent
    
    def standardize(self) :
        if not self.isStandardized :
            for child in self.children :
                child.standardize()

            node = Node()

            if self.getData() == 'let' :
                temp1 = self.children[0].children[1]
                temp1.setParent(self)
                temp1.setDepth(self.getDepth() + 1)
                temp2 = self.children[1]
                temp2.setParent(self.children[0])
                temp2.setDepth(self.getDepth() + 2)
                self.children[1] = temp1
                self.children[0].setData('lambda')
                self.children[0].children[1] = temp2
                self.setData('gamma')

            elif self.getData() == 'where' :
                temp = self.children[0]
                self.children[0] = self.children[1]
                self.children[1] = temp
                self.setData('let')
                self.standardize()

            elif self.getData() == 'function_form' :
                Ex = self.children[self.getDegree() - 1]
                currentLambda = node.getNode('lambda', self.getDepth() + 1, self, [], True)
                self.children.insert(1, currentLambda)
                while self.children[2] != Ex :
                    V = self.children[2]
                    self.children.pop(2)
                    V.setDepth(currentLambda.getDepth() + 1)
                    V.setParent(currentLambda)
                    currentLambda.children.append(V)
                    if self.getDegree() > 3 :
                        currentLambda = node.getNode('lambda', currentLambda.getDepth() + 1, currentLambda, [], True)
                        currentLambda.getParent().children.append(currentLambda)
                currentLambda.children.append(Ex)
                self.children.pop(2)
                self.setData('=')

            elif self.getData() == 'lambda' :
                if self.getDegree() > 2 :
                    Ey = self.children[self.getDegree() - 1]
                    currentLambdaX = node.getNode('lambda', self.getDepth() + 1, self, [], True)
                    self.children.append(currentLambdaX)
                    while self.children[2] != Ey :
                        V = self.children[2]
                        self.children.pop(2)
                        V.setDepth(currentLambdaX.getDepth() + 1)
                        V.setParent(currentLambdaX)
                        currentLambdaX.children.append(V)
                        if self.getDegree() > 3 :
                            currentLambdaX = node.getNode('lambda', currentLambdaX.getDepth() + 1, currentLambdaX, [], True)
                            currentLambdaX.getParent().children.append(currentLambdaX)
                    currentLambdaX.children.append(Ey)
                    self.children.pop(2)

            elif self.getData() == 'within' :
                X1 = self.children[0].children[0]
                X2 = self.children[1].children[0]
                E1 = self.children[0].children[1]
                E2 = self.children[1].children[1]
                gamma = node.getNode('gamma', self.getDepth() + 1, self.getParent(), [], True)
                Lambda = node.getNode('lambda', self.getDepth() + 2, gamma, [], True)
                X1.setDepth(X1.getDepth() + 1)
                X1.setParent(Lambda)
                X2.setDepth(X1.getDepth() - 1)
                X2.setParent(self)
                E1.setDepth(E1.getDepth())
                E1.setParent(gamma)
                E2.setDepth(E2.getDepth() + 1)
                E2.setParent(Lambda)
                Lambda.children.append(X1)
                Lambda.children.append(E2)
                gamma.children.append(Lambda)
                gamma.children.append(E1)
                self.children.clear()
                self.children.append(X2)
                self.children.append(gamma)
                self.setData('=')

            elif self.getData() == '@' :
                gamma1 = node.getNode('gamma', self.getDepth() + 1, self.getParent(), [], True)
                e1= self.children[0]
                e1.setDepth(e1.getDepth() + 1)
                e1.setParent(gamma1)
                n = self.children[1]
                n.setDepth(n.getDepth() + 1)
                n.setParent(gamma1)
                gamma1.children.append(n)
                gamma1.children.append(e1)
                self.children.pop(0)
                self.children.pop(0)
                self.children.insert(0, gamma1)
                self.setData('gamma')
            
            elif self.getData() == 'and' :
                comma = node.getNode(',', self.getDepth() + 1, self.getParent(), [], True)
                tau = node.getNode('tau', self.getDepth() + 1, self, [], True)
                for equal in self.children :
                    equal.children[0].setParent(comma)
                    equal.children[1].setParent(tau)
                    comma.children.append(equal.children[0])
                    tau.children.append(equal.children[1])
                self.children.clear()
                self.children.append(comma)
                self.children.append(tau)
                self.setData('=')

            elif self.getData() == 'rec' :
                X = self.children[0].children[0]
                E = self.children[0].children[1]
                F = node.getNode(X.getData(), self.getDepth() + 1, self, X.children, True)
                G = node.getNode('gamma', self.getDepth() + 1, self, [], True)
                Y = node.getNode('<Y*>', self.getDepth() + 2, G, [], True)
                L = node.getNode('lambda', self.getDepth() + 2, G, [], True)
                X.setDepth(L.getDepth() + 1)
                X.setParent(L)
                E.setDepth(L.getDepth() + 1)
                E.setParent(L)
                L.children.append(X)
                L.children.append(E)
                G.children.append(Y)
                G.children.append(L)
                self.children.clear()
                self.children.append(F)
                self.children.append(G)
                self.setData('=')

            else :
                pass
        
        self.is_standardized = True
        
    def print_tree(self,node, depth=0):
        if node is None:
            return
        print("  " * depth + node.data)
        for child in node.children:
            self.print_tree(child,depth + 1)