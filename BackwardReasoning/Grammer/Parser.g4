parser grammar LiurcaDaniel27Parser;

options {
    tokenVocab = LiurcaDaniel27Lexer;
}

program : linie+;

linie : afirmatie | interogare;

afirmatie  : (atom | atom DECLARE conditie) (PERCENT DECIMAL)?;
conditie   : atom | atom COMMA conditie;
atom       : NUME LPAREN termeni RPAREN | NUME LPAREN RPAREN;
termeni    : termen | termen COMMA termeni;
termen     : NUMAR | NUME | VARIABILA | functie;
functie    : NUME LPAREN termeni RPAREN | NUME LPAREN RPAREN;
interogare : QMARK atom;