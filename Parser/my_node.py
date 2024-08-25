from enum import Enum


class NodeType(Enum):
    let = 1
    fcn_form = 2
    identifier = 3
    integer = 4
    string = 5
    where = 6
    gamma = 7
    lambda_expr = 8
    tau = 9
    rec = 10
    aug = 11
    conditional = 12
    op_or = 13
    op_and = 14
    op_not = 15
    op_compare = 16
    op_plus = 17
    op_minus = 18
    op_neg = 19
    op_mul = 20
    op_div = 21
    op_pow = 22
    at = 23
    true_value = 24
    false_value = 25
    nil = 26
    dummy = 27
    within = 28
    and_op = 29
    equal = 30
    comma = 31
    empty_params = 32


class Node:
    def __init__(self, node_type, value, children):
        self.type = node_type
        self.value = value
        self.no_of_children = children
