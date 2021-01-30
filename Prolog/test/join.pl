isAlone([_],Res):-Res is 0,!.
isAlone([_|_],Res):-Res is 1.


equation(X,Y,Z):-Z is X+Y.
