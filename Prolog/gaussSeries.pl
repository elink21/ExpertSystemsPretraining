gaussSeries(X,Sum):- 0 is X,Sum is 0.
gaussSeries(X,Sum):-
    A is X-1 ,
    gaussSeries(A,Ra),
    Sum is X+Ra.



