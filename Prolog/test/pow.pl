pow(X,Y,Z):- Pow=X**Y, Z is Pow.

powF(X,0,Res):- Res is X,!.

powF(X,Y,Res):-
    N is Y-1,
    pow(X,N,Aux),
    Res is X*Aux.



otherPowTest(X,Y,Z):- powF(X,Y,Res),  Res is Z.
