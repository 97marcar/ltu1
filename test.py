def firstDiff(lst1, lst2):
    if lst1 == lst2:
        return len(lst1)
    elif lst1[0] != lst2[0]:
        return 0
    else:
        return (1 + firstDiff(lst1[1:],lst2[1:]))


print(firstDiff([2,3,1,2],[8,3,1,2]))
print(firstDiff([8,3,1,2],[8,3,4,2]))
print(firstDiff([8,3,1,2],[8,3,1,2]))
print(firstDiff([],[]))
