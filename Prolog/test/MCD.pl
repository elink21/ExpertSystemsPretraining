mcd(A,0,Res):-Res is A,!.
mcd(A,B,Res):-
    R is A mod B,
    mcd(B,R,Res).


