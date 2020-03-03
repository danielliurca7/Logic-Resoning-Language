# Generated from .\LiurcaDaniel27BackwardReasoning\LiurcaDaniel27Grammer\LiurcaDaniel27Parser.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LiurcaDaniel27Parser import LiurcaDaniel27Parser
else:
    from LiurcaDaniel27Parser import LiurcaDaniel27Parser

# This class defines a complete generic visitor for a parse tree produced by LiurcaDaniel27Parser.

class LiurcaDaniel27ParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LiurcaDaniel27Parser#program.
    def visitProgram(self, ctx:LiurcaDaniel27Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LiurcaDaniel27Parser#linie.
    def visitLinie(self, ctx:LiurcaDaniel27Parser.LinieContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LiurcaDaniel27Parser#afirmatie.
    def visitAfirmatie(self, ctx:LiurcaDaniel27Parser.AfirmatieContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LiurcaDaniel27Parser#conditie.
    def visitConditie(self, ctx:LiurcaDaniel27Parser.ConditieContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LiurcaDaniel27Parser#atom.
    def visitAtom(self, ctx:LiurcaDaniel27Parser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LiurcaDaniel27Parser#termeni.
    def visitTermeni(self, ctx:LiurcaDaniel27Parser.TermeniContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LiurcaDaniel27Parser#termen.
    def visitTermen(self, ctx:LiurcaDaniel27Parser.TermenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LiurcaDaniel27Parser#functie.
    def visitFunctie(self, ctx:LiurcaDaniel27Parser.FunctieContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LiurcaDaniel27Parser#interogare.
    def visitInterogare(self, ctx:LiurcaDaniel27Parser.InterogareContext):
        return self.visitChildren(ctx)



del LiurcaDaniel27Parser