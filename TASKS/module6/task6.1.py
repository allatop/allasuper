lst = [int(s) for s in input().split()]
p = []
while len(lst) !=0:
    a = lst[0]
    if a % 2 != 0:
        p.append(a)
    lst = lst[1:]
print (p)