c(a,b,7).
c(i,f,11).
c(d,h,4).
c(f,a,8).
c(f,g,10).
c(h,f,9).
c(d,i,2).

hasEdge(X):- c(X,_,_).


reach(Start,End,Intermediate,Cost):-
    c(Start,Intermediate,C1),c(Intermediate,End,C2), Cost is C1+C2.



