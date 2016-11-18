def fnk(m,n):
    if m == 0:
        return (n+1)
    elif n == 0:
        return(fnk(m-1,1))
    elif n > 0 and m > 0:
        return(fnk(m-1,fnk(m,n-1)))

def fnk2(m,n):
    if m > 0 and n > 0:
        return(fnk2(m-1,fnk2(m,n-1)))
    elif m > 0:
        return(fnk(m-1,1))
    else:
        return(n+1)

print(fnk(1,3))
print(fnk2(1,3))
