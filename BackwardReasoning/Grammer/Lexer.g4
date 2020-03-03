lexer grammar LiurcaDaniel27Lexer;

tokens {
    LPAREN,
    RPAREN,
    QMARK,
    PERCENT,
    COMMA,
    DECLARE,

    NUMAR,
    DECIMAL,
    NUME,
    VARIABILA
}

WS : [ \n\f\r\t]+ -> skip;

LPAREN  : '(';
RPAREN  : ')';
QMARK   : '?';
PERCENT : '%';
COMMA   : ',';
DECLARE : ':-';

NUMAR     : [0-9] | [1-9][0-9]*;
DECIMAL   : NUMAR '.' NUMAR;
NUME      : [A-Za-z0-9_]+;
VARIABILA : QMARK NUME;

COMENTARIU : '#' ~'\n'* -> skip;