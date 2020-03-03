from .LiurcaDaniel27Parser import *
from .LiurcaDaniel27ParserVisitor import *
from LiurcaDaniel27BackwardReasoning.LiurcaDaniel27Logic.LiurcaDaniel27Representation import *
from LiurcaDaniel27BackwardReasoning.LiurcaDaniel27Logic.LiurcaDaniel27BC import *

class LiurcaDaniel27Visitor(LiurcaDaniel27ParserVisitor):
    def __init__(self, verbose = False):
        self.kb = []
        self.verbose = verbose


    # Visit a parse tree produced by LogicParser#program.
    def visitProgram(self, ctx:LiurcaDaniel27Parser.ProgramContext):
        for linie in ctx.linie():
            linie.accept(self)

        return None


    # Visit a parse tree produced by LogicParser#linie.
    def visitLinie(self, ctx:LiurcaDaniel27Parser.LinieContext):
        if ctx.afirmatie():
            ctx.afirmatie().accept(self)
        else:
            ctx.interogare().accept(self)


    # Visit a parse tree produced by LogicParser#afirmatie.
    def visitAfirmatie(self, ctx:LiurcaDaniel27Parser.AfirmatieContext):
        if ctx.DECIMAL() is None:
            percent = 1.0
        else:
            percent = float(ctx.DECIMAL().getText())

        if ctx.conditie():
            add_statement(
                self.kb,
                ctx.atom().accept(self),
                percent,
                *ctx.conditie().accept(self)
            )
        else:
            add_statement(
                self.kb,
                ctx.atom().accept(self),
                percent
            )


    # Visit a parse tree produced by LogicParser#conditie.
    def visitConditie(self, ctx:LiurcaDaniel27Parser.ConditieContext):
        atom_list = [ctx.atom().accept(self)]

        if ctx.conditie():
            atom_list += ctx.conditie().accept(self)

        return atom_list


    # Visit a parse tree produced by LogicParser#atom.
    def visitAtom(self, ctx:LiurcaDaniel27Parser.AtomContext):
        if ctx.termeni():
            return make_atom(
                ctx.NUME().getText(),
                *ctx.termeni().accept(self)
            )
        else:
            return make_atom(
                ctx.NUME().getText()
            )

    # Visit a parse tree produced by LogicParser#termeni.
    def visitTermeni(self, ctx:LiurcaDaniel27Parser.TermeniContext):
        termeni_list = [ctx.termen().accept(self)]

        if ctx.termeni():
            termeni_list += ctx.termeni().accept(self)

        return termeni_list


    # Visit a parse tree produced by LogicParser#termen.
    def visitTermen(self, ctx:LiurcaDaniel27Parser.TermenContext):
        if ctx.NUMAR():
            return make_const(ctx.NUMAR().getText())

        if ctx.NUME():
            return make_const(ctx.NUME().getText())

        if ctx.VARIABILA():
            return make_var(ctx.VARIABILA().getText()[1:])

        if ctx.functie():
            return ctx.functie().accept(self)

    # Visit a parse tree produced by LogicParser#functie.
    def visitFunctie(self, ctx:LiurcaDaniel27Parser.FunctieContext):
        if ctx.termeni():
            return make_function_call(
                ctx.NUME().getText(),
                *ctx.termeni().accept(self)
            )
        else:
            return make_function_call(
                ctx.NUME().getText()
            )


    # Visit a parse tree produced by LogicParser#interogare.
    def visitInterogare(self, ctx:LiurcaDaniel27Parser.InterogareContext):
        theorem = ctx.atom().accept(self)

        subst = backward_chaining(self.kb, theorem, verbose = self.verbose)

        print('Query is:', print_formula(theorem, True))
        if isinstance(subst, list):
            for s in subst:
                if isinstance(s[0], dict):
                    print(' ; '.join(['{0} : {1}'.format(k, get_value(v)) for k, v in s[0].items()]), '' if s[1] == 1.0 else '% ' + str(s[1]))
                else:
                    print(s[0], '' if s[1] == 1.0 else '% ' + str(s[1]))
        else:
            print(subst[0])
        print()
