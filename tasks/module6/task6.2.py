lst = input().split()
p = []
while len(lst) !=1:
    if lst[1] > lst[0]:
        p.append(lst[1])
    lst = lst[1:]
print (' '.join(p))