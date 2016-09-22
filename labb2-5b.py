# -*- coding: utf-8 -*-

import math

def derivate(f,x,h):
    answer = (f(x+h) - f(x-h))/(2*h)
    return(answer)

def solve(f,x0,h):
    xn = x0
    x_nMx_n1 = (xn - (xn -((f(xn))/derivate(f,xn,h))))
    while (x_nMx_n1 > 0 and x_nMx_n1 > h) or (x_nMx_n1 < 0 and x_nMx_n1 < (h*-1)):
        xn = xn -((f(xn))/derivate(f,xn,h))
        x_nMx_n1 = (xn - (xn -((f(xn))/derivate(f,xn,h))))
    return(xn)


def xsquareM1(x):
    return((x**2)-1)

def twoupxM1(x):
    return((2**x)-1)

def xMeUMx(x):
    return(x-(math.e**(-x)))

print(solve(xsquareM1,-4,0.0001))
print(solve(twoupxM1,-9,0.00001))
print(solve(xMeUMx,1123,0.000000001))

"""if  (xn - (xn -((f(xn))/derivate(f,xn,h)))) > 0:
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
    xn = xn -((f(xn))/derivate(f,xn,h))"""
