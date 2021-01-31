seq(_,[],_,_):-false,!.

seq(X,[Y|_],X,Y):-true,!.

seq(X,[Y],X,Y):-true,!.

seq(_,[Y|L],A,B):- seq(Y,L,A,B).

isSequence([X|L],A,B):-seq(X,L,A,B).
