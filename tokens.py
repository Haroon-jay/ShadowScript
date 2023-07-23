class Token:
    def __init__(self, value, typ):
        self.value = value
        self.type=typ
    def __repr__(self) -> str:
        return str(self.value)   

class Integer(Token):
    def __init__(self, value):
        super().__init__(value, "INT")

class String(Token):
    pass

class Float(Token):
    def __init__(self, value):
        super().__init__(value, "FLT")    


class Operator(Token):
    def __init__(self, value):
        super().__init__(value, "OP")    