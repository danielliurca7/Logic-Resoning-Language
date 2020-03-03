# Generated from .\LiurcaDaniel27BackwardReasoning\LiurcaDaniel27Grammer\LiurcaDaniel27Lexer.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\16")
        buf.write("N\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2")
        buf.write("\6\2\35\n\2\r\2\16\2\36\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3")
        buf.write("\5\3\6\3\6\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\7\t\63\n\t")
        buf.write("\f\t\16\t\66\13\t\5\t8\n\t\3\n\3\n\3\n\3\n\3\13\6\13?")
        buf.write("\n\13\r\13\16\13@\3\f\3\f\3\f\3\r\3\r\7\rH\n\r\f\r\16")
        buf.write("\rK\13\r\3\r\3\r\2\2\16\3\r\5\3\7\4\t\5\13\6\r\7\17\b")
        buf.write("\21\t\23\n\25\13\27\f\31\16\3\2\7\5\2\13\f\16\17\"\"\3")
        buf.write("\2\62;\3\2\63;\6\2\62;C\\aac|\3\2\f\f\2R\2\3\3\2\2\2\2")
        buf.write("\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3")
        buf.write("\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2")
        buf.write("\2\2\2\27\3\2\2\2\2\31\3\2\2\2\3\34\3\2\2\2\5\"\3\2\2")
        buf.write("\2\7$\3\2\2\2\t&\3\2\2\2\13(\3\2\2\2\r*\3\2\2\2\17,\3")
        buf.write("\2\2\2\21\67\3\2\2\2\239\3\2\2\2\25>\3\2\2\2\27B\3\2\2")
        buf.write("\2\31E\3\2\2\2\33\35\t\2\2\2\34\33\3\2\2\2\35\36\3\2\2")
        buf.write("\2\36\34\3\2\2\2\36\37\3\2\2\2\37 \3\2\2\2 !\b\2\2\2!")
        buf.write("\4\3\2\2\2\"#\7*\2\2#\6\3\2\2\2$%\7+\2\2%\b\3\2\2\2&\'")
        buf.write("\7A\2\2\'\n\3\2\2\2()\7\'\2\2)\f\3\2\2\2*+\7.\2\2+\16")
        buf.write("\3\2\2\2,-\7<\2\2-.\7/\2\2.\20\3\2\2\2/8\t\3\2\2\60\64")
        buf.write("\t\4\2\2\61\63\t\3\2\2\62\61\3\2\2\2\63\66\3\2\2\2\64")
        buf.write("\62\3\2\2\2\64\65\3\2\2\2\658\3\2\2\2\66\64\3\2\2\2\67")
        buf.write("/\3\2\2\2\67\60\3\2\2\28\22\3\2\2\29:\5\21\t\2:;\7\60")
        buf.write("\2\2;<\5\21\t\2<\24\3\2\2\2=?\t\5\2\2>=\3\2\2\2?@\3\2")
        buf.write("\2\2@>\3\2\2\2@A\3\2\2\2A\26\3\2\2\2BC\5\t\5\2CD\5\25")
        buf.write("\13\2D\30\3\2\2\2EI\7%\2\2FH\n\6\2\2GF\3\2\2\2HK\3\2\2")
        buf.write("\2IG\3\2\2\2IJ\3\2\2\2JL\3\2\2\2KI\3\2\2\2LM\b\r\2\2M")
        buf.write("\32\3\2\2\2\b\2\36\64\67@I\3\b\2\2")
        return buf.getvalue()


class LiurcaDaniel27Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    LPAREN = 1
    RPAREN = 2
    QMARK = 3
    PERCENT = 4
    COMMA = 5
    DECLARE = 6
    NUMAR = 7
    DECIMAL = 8
    NUME = 9
    VARIABILA = 10
    WS = 11
    COMENTARIU = 12

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'?'", "'%'", "','", "':-'" ]

    symbolicNames = [ "<INVALID>",
            "LPAREN", "RPAREN", "QMARK", "PERCENT", "COMMA", "DECLARE", 
            "NUMAR", "DECIMAL", "NUME", "VARIABILA", "WS", "COMENTARIU" ]

    ruleNames = [ "WS", "LPAREN", "RPAREN", "QMARK", "PERCENT", "COMMA", 
                  "DECLARE", "NUMAR", "DECIMAL", "NUME", "VARIABILA", "COMENTARIU" ]

    grammarFileName = "LiurcaDaniel27Lexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


