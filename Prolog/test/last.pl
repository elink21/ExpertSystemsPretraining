last(_,[]):-false,!.

last(X,[X]):-true,!.

last(X,[_|L]):-last(X,L).
