from sys import argv
from os import path 
from ply import lex
"""
This next import allows PLY lex to be aware of our lexical 
specification. Without it, everything breaks :)
"""
from ivy_lexer import *

def main():
    """
    Check to ensure that 1) an input file was provided and 2)
    the input file exists.
    """
    if len(argv) < 2:
        print("Error: No input file provided.")
        exit()
    elif len(argv) > 2:
        print("Error: Too many arguments provided. Only one input file is allowed.")
        exit()
    else:
        if not path.exists(argv[1]):
            print("Error: File `%s` not found. Compilation terminated." % (argv[1]))
            exit()
        
        with open(argv[1]) as f:
            contents = f.read()        

        """
        These are PLY lex specific functions. See the PLY documentation
        `https://www.dabeaz.com/ply/ply.html#ply_nn3` for details on these 
        functions
        """
        lexer = lex.lex()
        lexer.input(contents)

        """Creating a tokens list that we can pass around later on"""
        myTokens = []
        while True:
            tok = lexer.token()
            if not tok:
                break
            myTokens.append(tok)
        
        """
        Printing the tokens. Each token includes: 
        1) Token type
        2) Token value (the actual string matched)
        3) Line number
        4) Character number within the line
        """
        for token in myTokens:
            print(token)

        

if __name__ == "__main__":
    main()