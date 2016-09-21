import math

def derivate(f,x,h):
    answer = (f(x+h) - f(x-h))/(2*h)
    return(answer)



def twox(x):
    return(2*x)

def xsquared(x):
    return(x**2)

def halfx(x):
    return(x/2)

def xMeUMx(x):
    return(x-(math.e**(-x)))

print(derivate(twox,math.pi,0.0001))
print(derivate(xsquared,math.pi,0.0001))
print(derivate(halfx,math.pi,0.0001))
