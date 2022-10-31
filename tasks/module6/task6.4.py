l = input().split()
p = []
p.copy(l)
l[p.index(max(p))] =min(l)
l[p.index(min(p))] =max(l)
print (l)
