import sys
from os import path

from antlr4 import *
from LiurcaDaniel27BackwardReasoning.LiurcaDaniel27Grammer.LiurcaDaniel27Lexer import LiurcaDaniel27Lexer
from LiurcaDaniel27BackwardReasoning.LiurcaDaniel27Grammer.LiurcaDaniel27Parser import LiurcaDaniel27Parser
from LiurcaDaniel27BackwardReasoning.LiurcaDaniel27Grammer.LiurcaDaniel27Visitor import LiurcaDaniel27Visitor


def main():
    if len(sys.argv) != 2 and len(sys.argv) != 3:
        print('Invalid number of arguments')
        return
    else:
        verbose  = False
        filename = 'teste/test' + sys.argv[1] + '.txt'

        if not path.exists(filename):
            print('File ' + filename + ' does not exist')
            return

        if len(sys.argv) == 3:
            if sys.argv[2] == '--verbose':
                verbose  = True
            else:
                print('Invalid second argument')
                return

    lexer = LiurcaDaniel27Lexer(FileStream(filename))
    stream = CommonTokenStream(lexer)
    parser = LiurcaDaniel27Parser(stream)
    tree = parser.program()
    visitor = LiurcaDaniel27Visitor(verbose)
    tree.accept(visitor)

if __name__ == '__main__':
    main()