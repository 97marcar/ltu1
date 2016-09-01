# -*- coding: utf-8 -*-

def bounce2(n):
    for i in range(n, (-1*(n+1)), -1):
      if i < 0:
          i = (i*-1)
      print(i),

bounce2(7)
