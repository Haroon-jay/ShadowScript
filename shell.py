from lexer import Lexer
from tokenParser import TokenParser
from interpreter import Interpreter
while True:
    text = input("ShadowScript:")
    tokenizer = Lexer(text)
    tokens = tokenizer.tokenize()
    parser = TokenParser(tokens)
    parsed = parser.parse()
    print(parsed, 'parsed')
    interpreter = Interpreter(parsed)
    res  = interpreter.interpret()
    print(res, 'res')
