# -*- coding: utf-8 -*-


def bounce(n):
    if n > 0:
        print(n),
        bounce(n-1)
        print(n),
    elif n == 0:
        print(0),
    else:
        pass

bounce(7)
