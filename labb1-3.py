# -*- coding: utf-8 -*-

def kostnad(P,r,a):
    k = P+(a+1)*P*r/2
    return("Den totala kostnaden efter "+str(a)+" år är "+str(int(k))+" kr")

cost = kostnad(50000, 0.03, 10)

print(cost)
