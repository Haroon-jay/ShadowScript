from tokens import Integer, Float
class Interpreter:
    def __init__(self, tree) -> None:
        self.tree = tree


    def read_FLT(self, val):
        return float(val)
    def read_INT(self, val):
        return int(val)
    
    def compute_bin(self, left_node, operator, right_node):
        left_type = left_node.type
        right_type = right_node.type
        
        left = getattr(self, f"read_{left_type}")(left_node.value)
        right = getattr(self, f"read_{right_type}")(right_node.value)

        if operator.value == "+":
            output= left + right
        elif operator.value == "-":
            output = left - right
        elif operator.value == "*":
            output = left * right
        elif operator.value == "/":
            output = left / right
        
        return Integer(output) if (left_type == "INT" and right_node =="INT") else Float(output)

        
    def interpret(self, tree=None):
        if tree is None:
            tree = self.tree
        left_node = tree[0]    
        if isinstance(left_node, list):
            left_node = Interpreter(left_node).interpret()
        right_node = tree[2]
        if isinstance(right_node, list):
            right_node = Interpreter(right_node).interpret()
        operator = tree[1]

        return self.compute_bin(left_node, operator, right_node)