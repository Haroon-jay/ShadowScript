from tokens import Integer, Float, Operator

class Lexer:
    digits = "0123456789"
    operators="+-/*()"
    stop_words = [" "]
    def __init__(self, text):
        self.text = text
        self.idx = 0
        self.tokens = []
        self.char = self.text[self.idx]
        self.token=None
   
    def tokenize(self):
        while self.in_text():
            if self.char in Lexer.digits:
                self.token = self.extract_number()
            elif self.char in Lexer.operators:
                self.token = Operator(self.char) 
                self.move()
            elif self.char in Lexer.stop_words:
                self.move()
                continue
            self.tokens.append(self.token)    
        return self.tokens    
    def extract_number(self):
        token=""
        isFloat=False
        while (self.char in Lexer.digits or self.char == ".") and (self.in_text()):
            if self.char == ".":
                isFloat = True
            token+=self.char
            self.move()
            
        return Integer(token) if not isFloat else Float(token)
    
    def in_text(self):
        if self.idx< len(self.text):
            return True
        return False   
    def move(self):
        self.idx+=1
        if self.in_text():
            self.char = self.text[self.idx]

   



lexer = Lexer("4 + 1")


