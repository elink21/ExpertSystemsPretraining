isEqual(La,Lb):-
    length(La,SizeA),
    length(Lb,SizeB),
    SizeA \== SizeB,
    false,!.

isEqual([],[]):-true,!.

isEqual([X|La],[X|Lb]):-isEqual(La,Lb).

isEqual([X|_],[Y|_]):-X\==Y,false,!.


isAJoint(La,Lb,Lc):-
    append(La,Lb,Joined),
    isEqual(Joined,Lc),true.



eq(L,L):-true,!.

junta(La,Lb,Lc):-
    append(La,Lb,Res),
    eq(Lc,Res).

