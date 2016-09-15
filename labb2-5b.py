# -*- coding: utf-8 -*-

import math

def derivate(f,x,h):
    answer = (f(x+h) - f(x-h))/(2*h)
    return(answer)

def solve(f,x0,h,str):
    xn = x0
    while True:
        if (xn - (xn -((f(xn))/derivate(f,xn,h)))) > 0:
            if (xn - (xn -((f(xn))/derivate(f,xn,h)))) < h:
                break
            else:
                xn = xn -((f(xn))/derivate(f,xn,h))
        elif (xn - (xn -((f(xn))/derivate(f,xn,h)))) < 0:
            if (xn - (xn -((f(xn))/derivate(f,xn,h)))) > (h*-1):
                break
            else:
                xn = xn -((f(xn))/derivate(f,xn,h))
        else:
            xn = xn -((f(xn))/derivate(f,xn,h))
    print(xn,str)


def xsquareM1(x):
    return((x**2)-1)

def twoupxM1(x):
    return((2**x)-1)

def xMeUMx(x):
    return(x-(math.e**(-x)))

solve(xsquareM1,-4,0.0001,"ETT")
solve(twoupxM1,-9,0.00001,"NOLL")
solve(xMeUMx,1123,0.000000001,"e")
