fact(X,Res):- 1 is X, Res is X.
fact(X,Res) :-
    A is X-1,
    fact(A,Aux),
    Res is X*Aux.
