# Generated from .\LiurcaDaniel27BackwardReasoning\LiurcaDaniel27Grammer\LiurcaDaniel27Parser.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\16")
        buf.write("T\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\3\2\6\2\26\n\2\r\2\16\2\27\3\3\3")
        buf.write("\3\5\3\34\n\3\3\4\3\4\3\4\3\4\3\4\5\4#\n\4\3\4\3\4\5\4")
        buf.write("\'\n\4\3\5\3\5\3\5\3\5\3\5\5\5.\n\5\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\5\68\n\6\3\7\3\7\3\7\3\7\3\7\5\7?\n\7\3")
        buf.write("\b\3\b\3\b\3\b\5\bE\n\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\5\tO\n\t\3\n\3\n\3\n\3\n\2\2\13\2\4\6\b\n\f\16\20\22")
        buf.write("\2\2\2U\2\25\3\2\2\2\4\33\3\2\2\2\6\"\3\2\2\2\b-\3\2\2")
        buf.write("\2\n\67\3\2\2\2\f>\3\2\2\2\16D\3\2\2\2\20N\3\2\2\2\22")
        buf.write("P\3\2\2\2\24\26\5\4\3\2\25\24\3\2\2\2\26\27\3\2\2\2\27")
        buf.write("\25\3\2\2\2\27\30\3\2\2\2\30\3\3\2\2\2\31\34\5\6\4\2\32")
        buf.write("\34\5\22\n\2\33\31\3\2\2\2\33\32\3\2\2\2\34\5\3\2\2\2")
        buf.write("\35#\5\n\6\2\36\37\5\n\6\2\37 \7\b\2\2 !\5\b\5\2!#\3\2")
        buf.write("\2\2\"\35\3\2\2\2\"\36\3\2\2\2#&\3\2\2\2$%\7\6\2\2%\'")
        buf.write("\7\n\2\2&$\3\2\2\2&\'\3\2\2\2\'\7\3\2\2\2(.\5\n\6\2)*")
        buf.write("\5\n\6\2*+\7\7\2\2+,\5\b\5\2,.\3\2\2\2-(\3\2\2\2-)\3\2")
        buf.write("\2\2.\t\3\2\2\2/\60\7\13\2\2\60\61\7\3\2\2\61\62\5\f\7")
        buf.write("\2\62\63\7\4\2\2\638\3\2\2\2\64\65\7\13\2\2\65\66\7\3")
        buf.write("\2\2\668\7\4\2\2\67/\3\2\2\2\67\64\3\2\2\28\13\3\2\2\2")
        buf.write("9?\5\16\b\2:;\5\16\b\2;<\7\7\2\2<=\5\f\7\2=?\3\2\2\2>")
        buf.write("9\3\2\2\2>:\3\2\2\2?\r\3\2\2\2@E\7\t\2\2AE\7\13\2\2BE")
        buf.write("\7\f\2\2CE\5\20\t\2D@\3\2\2\2DA\3\2\2\2DB\3\2\2\2DC\3")
        buf.write("\2\2\2E\17\3\2\2\2FG\7\13\2\2GH\7\3\2\2HI\5\f\7\2IJ\7")
        buf.write("\4\2\2JO\3\2\2\2KL\7\13\2\2LM\7\3\2\2MO\7\4\2\2NF\3\2")
        buf.write("\2\2NK\3\2\2\2O\21\3\2\2\2PQ\7\5\2\2QR\5\n\6\2R\23\3\2")
        buf.write("\2\2\13\27\33\"&-\67>DN")
        return buf.getvalue()


class LiurcaDaniel27Parser ( Parser ):

    grammarFileName = "LiurcaDaniel27Parser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'?'", "'%'", "','", "':-'" ]

    symbolicNames = [ "<INVALID>", "LPAREN", "RPAREN", "QMARK", "PERCENT", 
                      "COMMA", "DECLARE", "NUMAR", "DECIMAL", "NUME", "VARIABILA", 
                      "WS", "COMENTARIU" ]

    RULE_program = 0
    RULE_linie = 1
    RULE_afirmatie = 2
    RULE_conditie = 3
    RULE_atom = 4
    RULE_termeni = 5
    RULE_termen = 6
    RULE_functie = 7
    RULE_interogare = 8

    ruleNames =  [ "program", "linie", "afirmatie", "conditie", "atom", 
                   "termeni", "termen", "functie", "interogare" ]

    EOF = Token.EOF
    LPAREN=1
    RPAREN=2
    QMARK=3
    PERCENT=4
    COMMA=5
    DECLARE=6
    NUMAR=7
    DECIMAL=8
    NUME=9
    VARIABILA=10
    WS=11
    COMENTARIU=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def linie(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LiurcaDaniel27Parser.LinieContext)
            else:
                return self.getTypedRuleContext(LiurcaDaniel27Parser.LinieContext,i)


        def getRuleIndex(self):
            return LiurcaDaniel27Parser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = LiurcaDaniel27Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 18
                self.linie()
                self.state = 21 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==LiurcaDaniel27Parser.QMARK or _la==LiurcaDaniel27Parser.NUME):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LinieContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def afirmatie(self):
            return self.getTypedRuleContext(LiurcaDaniel27Parser.AfirmatieContext,0)


        def interogare(self):
            return self.getTypedRuleContext(LiurcaDaniel27Parser.InterogareContext,0)


        def getRuleIndex(self):
            return LiurcaDaniel27Parser.RULE_linie

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLinie" ):
                return visitor.visitLinie(self)
            else:
                return visitor.visitChildren(self)




    def linie(self):

        localctx = LiurcaDaniel27Parser.LinieContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_linie)
        try:
            self.state = 25
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LiurcaDaniel27Parser.NUME]:
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.afirmatie()
                pass
            elif token in [LiurcaDaniel27Parser.QMARK]:
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self.interogare()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AfirmatieContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self):
            return self.getTypedRuleContext(LiurcaDaniel27Parser.AtomContext,0)


        def DECLARE(self):
            return self.getToken(LiurcaDaniel27Parser.DECLARE, 0)

        def conditie(self):
            return self.getTypedRuleContext(LiurcaDaniel27Parser.ConditieContext,0)


        def PERCENT(self):
            return self.getToken(LiurcaDaniel27Parser.PERCENT, 0)

        def DECIMAL(self):
            return self.getToken(LiurcaDaniel27Parser.DECIMAL, 0)

        def getRuleIndex(self):
            return LiurcaDaniel27Parser.RULE_afirmatie

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAfirmatie" ):
                return visitor.visitAfirmatie(self)
            else:
                return visitor.visitChildren(self)




    def afirmatie(self):

        localctx = LiurcaDaniel27Parser.AfirmatieContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_afirmatie)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 27
                self.atom()
                pass

            elif la_ == 2:
                self.state = 28
                self.atom()
                self.state = 29
                self.match(LiurcaDaniel27Parser.DECLARE)
                self.state = 30
                self.conditie()
                pass


            self.state = 36
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==LiurcaDaniel27Parser.PERCENT:
                self.state = 34
                self.match(LiurcaDaniel27Parser.PERCENT)
                self.state = 35
                self.match(LiurcaDaniel27Parser.DECIMAL)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditieContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self):
            return self.getTypedRuleContext(LiurcaDaniel27Parser.AtomContext,0)


        def COMMA(self):
            return self.getToken(LiurcaDaniel27Parser.COMMA, 0)

        def conditie(self):
            return self.getTypedRuleContext(LiurcaDaniel27Parser.ConditieContext,0)


        def getRuleIndex(self):
            return LiurcaDaniel27Parser.RULE_conditie

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditie" ):
                return visitor.visitConditie(self)
            else:
                return visitor.visitChildren(self)




    def conditie(self):

        localctx = LiurcaDaniel27Parser.ConditieContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_conditie)
        try:
            self.state = 43
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 38
                self.atom()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 39
                self.atom()
                self.state = 40
                self.match(LiurcaDaniel27Parser.COMMA)
                self.state = 41
                self.conditie()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUME(self):
            return self.getToken(LiurcaDaniel27Parser.NUME, 0)

        def LPAREN(self):
            return self.getToken(LiurcaDaniel27Parser.LPAREN, 0)

        def termeni(self):
            return self.getTypedRuleContext(LiurcaDaniel27Parser.TermeniContext,0)


        def RPAREN(self):
            return self.getToken(LiurcaDaniel27Parser.RPAREN, 0)

        def getRuleIndex(self):
            return LiurcaDaniel27Parser.RULE_atom

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = LiurcaDaniel27Parser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_atom)
        try:
            self.state = 53
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 45
                self.match(LiurcaDaniel27Parser.NUME)
                self.state = 46
                self.match(LiurcaDaniel27Parser.LPAREN)
                self.state = 47
                self.termeni()
                self.state = 48
                self.match(LiurcaDaniel27Parser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 50
                self.match(LiurcaDaniel27Parser.NUME)
                self.state = 51
                self.match(LiurcaDaniel27Parser.LPAREN)
                self.state = 52
                self.match(LiurcaDaniel27Parser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermeniContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def termen(self):
            return self.getTypedRuleContext(LiurcaDaniel27Parser.TermenContext,0)


        def COMMA(self):
            return self.getToken(LiurcaDaniel27Parser.COMMA, 0)

        def termeni(self):
            return self.getTypedRuleContext(LiurcaDaniel27Parser.TermeniContext,0)


        def getRuleIndex(self):
            return LiurcaDaniel27Parser.RULE_termeni

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermeni" ):
                return visitor.visitTermeni(self)
            else:
                return visitor.visitChildren(self)




    def termeni(self):

        localctx = LiurcaDaniel27Parser.TermeniContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_termeni)
        try:
            self.state = 60
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 55
                self.termen()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 56
                self.termen()
                self.state = 57
                self.match(LiurcaDaniel27Parser.COMMA)
                self.state = 58
                self.termeni()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermenContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMAR(self):
            return self.getToken(LiurcaDaniel27Parser.NUMAR, 0)

        def NUME(self):
            return self.getToken(LiurcaDaniel27Parser.NUME, 0)

        def VARIABILA(self):
            return self.getToken(LiurcaDaniel27Parser.VARIABILA, 0)

        def functie(self):
            return self.getTypedRuleContext(LiurcaDaniel27Parser.FunctieContext,0)


        def getRuleIndex(self):
            return LiurcaDaniel27Parser.RULE_termen

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermen" ):
                return visitor.visitTermen(self)
            else:
                return visitor.visitChildren(self)




    def termen(self):

        localctx = LiurcaDaniel27Parser.TermenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_termen)
        try:
            self.state = 66
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 62
                self.match(LiurcaDaniel27Parser.NUMAR)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 63
                self.match(LiurcaDaniel27Parser.NUME)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 64
                self.match(LiurcaDaniel27Parser.VARIABILA)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 65
                self.functie()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctieContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUME(self):
            return self.getToken(LiurcaDaniel27Parser.NUME, 0)

        def LPAREN(self):
            return self.getToken(LiurcaDaniel27Parser.LPAREN, 0)

        def termeni(self):
            return self.getTypedRuleContext(LiurcaDaniel27Parser.TermeniContext,0)


        def RPAREN(self):
            return self.getToken(LiurcaDaniel27Parser.RPAREN, 0)

        def getRuleIndex(self):
            return LiurcaDaniel27Parser.RULE_functie

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctie" ):
                return visitor.visitFunctie(self)
            else:
                return visitor.visitChildren(self)




    def functie(self):

        localctx = LiurcaDaniel27Parser.FunctieContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_functie)
        try:
            self.state = 76
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 68
                self.match(LiurcaDaniel27Parser.NUME)
                self.state = 69
                self.match(LiurcaDaniel27Parser.LPAREN)
                self.state = 70
                self.termeni()
                self.state = 71
                self.match(LiurcaDaniel27Parser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 73
                self.match(LiurcaDaniel27Parser.NUME)
                self.state = 74
                self.match(LiurcaDaniel27Parser.LPAREN)
                self.state = 75
                self.match(LiurcaDaniel27Parser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterogareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def QMARK(self):
            return self.getToken(LiurcaDaniel27Parser.QMARK, 0)

        def atom(self):
            return self.getTypedRuleContext(LiurcaDaniel27Parser.AtomContext,0)


        def getRuleIndex(self):
            return LiurcaDaniel27Parser.RULE_interogare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterogare" ):
                return visitor.visitInterogare(self)
            else:
                return visitor.visitChildren(self)




    def interogare(self):

        localctx = LiurcaDaniel27Parser.InterogareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_interogare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(LiurcaDaniel27Parser.QMARK)
            self.state = 79
            self.atom()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





