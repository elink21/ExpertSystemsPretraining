gaussSeries(0,0):-!.

gaussSeries(X,Sum):-
    A is X-1 ,
    gaussSeries(A,Ra),
    Sum is X+Ra.




