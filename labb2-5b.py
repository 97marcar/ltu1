

import math
def derivate(f,x,h):
    answer = (f(x+h) - f(x-h))/(2*h)
    return(answer)

def solve(f,x0,h):
    nextcheck = 0
    xn = x0
    while True:
        if (xn - (xn -((f(xn))/derivate(f,xn,h)))) > 0:
            if (xn - (xn -((f(xn))/derivate(f,xn,h)))) < h:
                print(h)
                print(xn - (xn -((f(xn))/derivate(f,xn,h))))
                break
            else:
                xn = xn -((f(xn))/derivate(f,xn,h))
        elif (xn - (xn -((f(xn))/derivate(f,xn,h)))) < 0:
            print("iii")
            if (xn - (xn -((f(xn))/derivate(f,xn,h)))) < (h*-1):
                print(h)
                print(xn - (xn -((f(xn))/derivate(f,xn,h))))
                break
            else:
                xn = xn -((f(xn))/derivate(f,xn,h))
        else:
            xn = xn -((f(xn))/derivate(f,xn,h))

        nextcheck += 1
        if nextcheck >= 1000:
             print(h)
             print(xn - (xn -((f(xn))/derivate(f,xn,h))))
             break
    print(xn)


def xsquareM1(x):
    return((x**2)-1)

def twoupxM1(x):
    return((2**x)-1)

def xMeUMx(x):
    return(x-(math.e**(-x)))

solve(xsquareM1,4,0.0001)
solve(twoupxM1,-13,0.000000001)
solve(xMeUMx,1,0.00001)
