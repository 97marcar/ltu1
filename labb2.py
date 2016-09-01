# -*- coding: utf-8 -*-
def bounce(n,n2):
    if n >= 0:
        print(n),
        bounce(n-1,n2)
    elif n < 0 and n >= (n2*-1):
        print(n*-1),
        bounce(n-1,n2)
    else:
        pass

bounce(7,7)
