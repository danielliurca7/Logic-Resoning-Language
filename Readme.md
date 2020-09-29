# Logic Reasoning Language
An engine that parser a language similar to Prolog, processes logical statements and answer queries.
The reasoning in based on the backward chaining algorithm: starting from the conclusion and finding rules that can be demonstrated. 

## The language
The language is parsed with ANTLR4 and looks like:

Line ::= (Statement | Query) Comment | Comment

Statement ::= Atom | Atom ":" Condition

Condition ::= Atom | Atom "," Condition

Atom ::= Name "(" Terms ")" | Name "()"

Terms ::= Term | Term "," Terms

Term ::= Constant | Variable | Function

Function ::= Name "(" Terms ")" | Name "()"

Variable ::= "?" Name

Name ::= [A-Za-z_]+

Constant ::= Number | [A-Za-z][A-Za-z0-9]*

Number ::= "0" | [1-9][0-9]*

Query ::= "?" Atom

Comment ::= "#" [A-Za-z0-9 -_]

## Support for functions
There is support for functions and a few are implemented. In order to have a legitimate language there needs to be more basic functions implemented.
