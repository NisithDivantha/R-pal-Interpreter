from Symbols.b import B
from Symbols.id import Id
from Symbols.tau import Tau
from Symbols.eta import Eta
from Symbols.gamma import Gamma
from Symbols.e import E
from Symbols.tup import Tup
from Symbols.ystar import Ystar
from Symbols.rator import Rator
from Symbols.bop import Bop
from Symbols.uop import Uop
from Symbols.delta import Delta
from Symbols.err import Err
from Symbols.int import Int
from Symbols.bool import Bool
from Symbols.b import B
from Symbols.eta import Eta
from Symbols.beta import Beta
from Symbols.Lambda import Lambda
from Symbols.str import Str
from Symbols.dummy import Dummy

class CSEMachine:
    def __init__(self, control, stack, environment):
        self.control = control
        self.stack = stack
        self.environment = environment

    # def set_control(self, control):
    #     self.control = control

    # def set_stack(self, stack):
    #     self.stack = stack

    # def set_environment(self, environment):
    #     self.environment = environment

    def print_stack(self):
        print("Stack: ", end="")
        for symbol in self.stack:
            print(symbol.get_data(), end="")
            if isinstance(symbol, Lambda):
                print(symbol.get_index(), end="")
            elif isinstance(symbol, Delta):
                print(symbol.get_index(), end="")
            elif isinstance(symbol, E):
                print(symbol.get_index(), end="")
            elif isinstance(symbol, Eta):
                print(symbol.get_index(), end="")
            print(",", end="")
        print()
    
    def print_control(self):
        # print('here')
        print("Control: ", end="")
        for symbol in self.control:
            print(symbol.get_data(), end="")
            if isinstance(symbol, Lambda):
                print(symbol.get_index(), end="")
            elif isinstance(symbol, Delta):
                print(symbol.get_index(), end="")
            elif isinstance(symbol, E):
                print(symbol.get_index(), end="")
            elif isinstance(symbol, Eta):
                print(symbol.get_index(), end="")
            print(",", end="")
        print()

    def execute(self):
        current_environment = self.environment[0]
        j = 1
        while self.control:
            # self.print_control()
            # self.print_stack()
            # print('\n')
            current_symbol = self.control.pop()


            # Check if the extracted part is in the list of allowed values
            
            if isinstance(current_symbol, Id):
                data_part = current_symbol.get_data().split(":")[1].strip()
                # print("data_part: ", data_part)
                # Define the list of allowed values
                # print(data_part)
                allowed_values = ["Print", "Stem", "Stern", "Conc", "Order", "Null", 
                            "Itos", "Isstring", "Istuple", "Isdummy", "Istruthvalue", "Isfunction"]
                if data_part not in allowed_values:
                    # print('allowed')
                    self.stack.insert(0, current_environment.lookup(current_symbol))
                else:
                    # print('mot allowed')
                    self.control.pop()
                    self.handle_builtin_functions(data_part)
            elif isinstance(current_symbol, Lambda):
                current_symbol.set_environment(current_environment.get_index())
                self.stack.insert(0, current_symbol)
            elif isinstance(current_symbol, Gamma):
                next_symbol = self.stack.pop(0)
               

                if isinstance(next_symbol, Lambda):
                    lambda_func = next_symbol
                    e = E(j)
                    j += 1
                    
                    if len(lambda_func.identifiers) == 1:
                        e.values[lambda_func.identifiers[0]] = self.stack[0]
                        del self.stack[0]
                    else:
                        tup = self.stack[0]
                        del self.stack[0]
                        i = 0
                        for identifier in lambda_func.identifiers:
                            e.values[identifier] = tup.symbols[i]
                            i += 1
                    
                    for environment in self.environment:
                        if environment.get_index() == lambda_func.get_environment():
                            e.set_parent(environment)
                    
                    current_environment = e
                    self.control.append(e)
                    self.control.append(lambda_func.get_delta())
                    self.stack.insert(0, e)
                    self.environment.append(e)

                # elif isinstance(next_symbol, Tup):
                #     tup = next_symbol
                #     print(self.stack[0].get_data())
                #     i = int(self.stack[0].get_data())
                #     del self.stack[0]
                #     self.stack.insert(0, tup.symbols[i-1])

                # elif isinstance(next_symbol, Tup):
                #     # Handle Tup expression
                #     # tup = next_symbol
                #     i = int(self.stack.pop(0).get_data())
                #     print(i)
                #     self.stack.insert(0, tup.symbols[i - 1])

                elif isinstance(next_symbol, Tup):
                    # print("next_symbol: ", next_symbol.get_data())
                    # for i in next_symbol.symbols:
                    #     print("i: ", i.get_data())
                    tup = self.stack.pop(0)
                    # print("tup: ", tup.get_data())
                    i = tup.get_data()
                    self.stack.insert(0, next_symbol.symbols[int(i) - 1])

                # if isinstance(next_symbol, Tup):
                #     tup = next_symbol
                    
                #     i = float(self.stack[0].get_data())
                #     print(i)
                #     self.stack.pop(0)
                #     self.stack.insert(0, tup.symbols[int(i) - 1])

                elif isinstance(next_symbol, Ystar):
                    lambda_func = self.stack.pop(0)
                    eta = Eta()
                    eta.set_index(lambda_func.get_index())
                    eta.set_environment(lambda_func.get_environment())
                    eta.set_identifier(lambda_func.identifiers[0])
                    eta.set_lambda(lambda_func)
                    self.stack.insert(0, eta)
                elif isinstance(next_symbol, Eta):
                    eta = next_symbol
                    lambda_func = eta.get_lambda()
                    self.control.append(Gamma())
                    self.control.append(Gamma())
                    self.stack.insert(0, eta)
                    self.stack.insert(0, lambda_func)
                
                elif isinstance(next_symbol, Int):                    
                    self.stack.insert(0, next_symbol)

                elif isinstance(next_symbol, Str):
                    self.stack.insert(0, next_symbol)
                else:
                    self.handle_builtin_functions(next_symbol)

            elif isinstance(current_symbol, E):
                # Remove the element at index 1 from the stack
                del self.stack[1]
                # Set the corresponding environment's 'isRemoved' attribute to True
                self.environment[current_symbol.get_index()].set_is_removed(True)
                
                y = len(self.environment)
                # print(y)
                while y > 0:
                    if not self.environment[y - 1].get_is_removed():
                        current_environment = self.environment[y - 1]
                        break
                    else:
                        y -= 1

            elif isinstance(current_symbol, Rator):
                if isinstance(current_symbol, Uop):
                    rator = current_symbol
                    rand = self.stack.pop(0)
                    print(rand.get_data())
                    self.stack.insert(0, self.apply_unary_operation(rator, rand))
                elif isinstance(current_symbol, Bop):
                    rator = current_symbol
                    rand1 = self.stack.pop(0)
                    # print(rand1.get_data())
                    rand2 = self.stack.pop(0)
                    self.stack.insert(0, self.apply_binary_operation(rator, rand1, rand2))

            elif isinstance(current_symbol, Beta):
                if self.stack[0].get_data() == True:
                    
                    self.control.pop()
                else:
                    self.control.pop(-2)
                self.stack.pop(0)
            elif isinstance(current_symbol, Tau):
                tau = current_symbol
                tup = Tup()
                for _ in range(tau.get_n()):
                    tup.symbols.append(self.stack.pop(0))
                self.stack.insert(0, tup)
            elif isinstance(current_symbol, Delta):
                self.control.extend(current_symbol.symbols)
            elif isinstance(current_symbol, B):
                self.control.extend(current_symbol.symbols)
            else:
                self.stack.insert(0, current_symbol)
    def handle_builtin_functions(self, next_symbol):
        if "Print" == next_symbol:
            if self.stack[0].get_data() == "tup":
                # print(self.stack[0].get_data())
                self.control.clear()

            pass  # do nothing
        elif "Stem" == next_symbol:
            # implement Stem function
            # print('stem')         
            s = self.stack.pop(0)
            s.set_data(s.get_data()[0])
            self.stack.insert(0, s)
            
        elif "Stern" == next_symbol:
            # print('here')
            
            s = self.stack[0]
            self.stack.pop(0)
            s.set_data(s.get_data()[1:])
            self.stack.insert(0, s)

        elif "Conc" == next_symbol:
            s1 = self.stack[0]
            s2 = self.stack[1]
            self.stack.pop(0)
            self.stack.pop(0)
            s1.set_data(s1.get_data() + s2.get_data())
            self.stack.insert(0, s1)
        elif "Order" == next_symbol:
            tup = self.stack[0]
            self.stack.pop(0)
            n = Int(str(len(tup.symbols)))
            self.stack.insert(0, n)
        elif "Null" == next_symbol:
            pass  # implement
        elif "Itos" == next_symbol:
            pass  # implement
        elif "Isinteger" == next_symbol:
            if isinstance(self.stack[0], Int):
                self.stack.insert(0, Bool(True))
            else:
                self.stack.insert(0, Bool(False))
            self.stack.pop(1)
        elif "Isstring" == next_symbol:
            if isinstance(self.stack[0], Str):
                self.stack.insert(0, Bool(True))
            else:
                self.stack.insert(0, Bool(False))
            self.stack.pop(1)
        elif "Istuple" == next_symbol.get_data():
            if isinstance(self.stack[0], Tup):
                self.stack.insert(0, Bool(True))
            else:
                self.stack.insert(0, Bool(False))
            self.stack.pop(1)
        elif "Isdummy" == next_symbol.get_data():
            if isinstance(self.stack[0], Dummy):
                self.stack.insert(0, Bool(True))
            else:
                self.stack.insert(0, Bool(False))
            self.stack.pop(1)
        elif "Istruthvalue" == next_symbol.get_data():
            if isinstance(self.stack[0], Bool):
                self.stack.insert(0, Bool(True))
            else:
                self.stack.insert(0, Bool(False))
            self.stack.pop(1)
        elif "Isfunction" == next_symbol.get_data():
            if isinstance(self.stack[0], Lambda):
                self.stack.insert(0, Bool(True))
            else:
                self.stack.insert(0, Bool(False))
            self.stack.pop(1)

    def apply_unary_operation(self, rator, rand):
        if "neg" == rator.get_data():
            val = int(rand.get_data())
            return Int((-1 * val))
        elif "not" == rator.get_data():
            return Bool(not val)
        else:
            return Err()

    def apply_binary_operation(self, rator, rand1, rand2):
        if rator.get_data() == "+":
            # print("rand1: ", rand1.get_data())
            val1 = int(rand1.get_data())
            val2 = int(rand2.get_data())
            return Int((val1 + val2))
        elif rator.get_data() == "-":
            val1 = int(rand1.get_data())
            val2 = int(rand2.get_data())
            return Int((val1 - val2))
        elif rator.get_data() == "*":
            val1 = int(rand1.get_data())
            val2 = int(rand2.get_data())
            return Int((val1 * val2))
        elif rator.get_data() == "/":
            val1 = int(rand1.get_data())
            val2 = int(rand2.get_data())
            return Int((val1 / val2))
        elif rator.get_data() == "**":
            val1 = float(rand1.get_data())
            val2 = float(rand2.get_data())
            return Int(str(val1 ** val2))
        elif rator.get_data() == "&":
            val1 = (rand1.get_data())
            val2 = (rand2.get_data())
            return Bool((val1 and val2))
        elif rator.get_data() == "or":
            val1 = (rand1.get_data())
            val2 = (rand2.get_data())
            # print(val1)
            return Bool((val1 or val2))
        elif rator.get_data() == "eq":
            val1 = int(rand1.get_data())
            val2 = int(rand2.get_data())
            return Bool((val1 == val2))
        elif rator.get_data() == "ne":
            val1 = int(rand1.get_data())
            val2 = int(rand2.get_data())
            return Bool((val1 != val2))
        elif rator.get_data() == "ls":
            val1 = int(rand1.get_data())
            val2 = int(rand2.get_data())
            return Bool((val1 < val2))
        elif rator.get_data() == "le":
            val1 = int(rand1.get_data())
            val2 = int(rand2.get_data())
            return Bool((val1 <= val2))
        elif rator.get_data() == "gr":
            val1 = int(rand1.get_data())
            val2 = int(rand2.get_data())
            return Bool((val1 > val2))
        elif rator.get_data() == "ge":
            val1 = int(rand1.get_data())
            val2 = int(rand2.get_data())
            return Bool((val1 >= val2))
        elif rator.get_data() == "aug":
            if isinstance(rand2, Tup):
                rand1.symbols.extend(rand2.symbols)
            else:
                rand1.symbols.append(rand2)
            return rand1
        else:
            return Err()


    def get_tuple_value(self, tup):
        # print('gonna')
        temp = "("
        # print(temp)
        for symbol in tup.symbols:
            # print(symbol)
            if isinstance(symbol, Tup):
                temp += str(self.get_tuple_value(symbol)) + ", "
                # print(temp)
            else:
                temp += str(symbol.get_data()) + ", "
        # print(tup.symbols)       
        temp = temp[:-2] + ")"
        # print(temp)
        return temp

    def get_answer(self):
        self.execute()
        # for i in range(len(self.stack)):
        #     print(i, self.stack[i].get_data())
        # print(self.stack)
        if isinstance(self.stack[0], Tup):
            return self.get_tuple_value(self.stack[0])
        if isinstance(self.stack[0], Int):
            return int(self.stack[0].get_data())
        return self.stack[0].get_data()

    # def print_control(self):
    #     print("Control: ", end="")
    #     for symbol in self.control:
    #         print(symbol.get_data(), end="")
    #         if isinstance(symbol, Lambda):
    #             print(symbol.get_index(), end="")
    #         elif isinstance(symbol, Delta):
    #             print(symbol.get_index(), end="")
    #         elif isinstance(symbol, E):
    #             print(symbol.get_index(), end="")
    #         elif isinstance(symbol, Eta):
    #             print(symbol.get_index(), end="")
    #         print(",", end="")
    #     print()


    def print_environment(self):
        for symbol in self.environment:
            print("e" + str(symbol.get_index()) + " --> ", end="")
            if symbol.get_index() != 0:
                print("e" + str(symbol.get_parent().get_index()))
            else:
                print()
