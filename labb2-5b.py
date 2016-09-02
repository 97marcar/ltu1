def derivate(f,x,h):
    answer = (f(x+h) - f(x-h))/(2*h)
    return(answer)

def solve(f,x0,h):
    xn+1 = xn -((f(xn))/derivate(f,xn,h))

def xsquareM1(x):
    return(x**2-1)

def twoupxM1(x):
    return(2**x-1)
