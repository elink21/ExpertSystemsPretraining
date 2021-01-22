c(a,b,7).
c(i,f,11).
c(d,h,4).
c(f,a,8).
c(f,g,10).
c(h,f,9).
c(d,i,2).


path(X,Y):-c(X,Y,_).

path(X,Y):- c(X,Z,_) , path(Z,Y).



