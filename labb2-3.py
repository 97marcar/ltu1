# -*- coding: utf-8 -*-

def summa(n):
    if n > 9:
        rest = n % 10
        div = n // 10
        return(summa(div)+rest)
        summa(div,total)
    else:
        return n

print(summa(123))

def summa2(n):
    total = 0
    while n > 0:
        rest = n % 10
        div = n // 10
        total += rest
        n = div
    return total

print(summa2(123))
