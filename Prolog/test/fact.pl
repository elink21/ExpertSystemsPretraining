fact(1,Res):- Res is 1,!.
fact(0,Res):- Res is 1,!.
fact(X,Res):-
    N is X-1,
    fact(N,Aux),
    Res is X*Aux.



testFact(X,Y):-
    fact(Y,N),
    N is X.
