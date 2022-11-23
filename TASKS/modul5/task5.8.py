f = input().split()
count = 1
mcount = 1
p = []
while len(f) != 1:
    if f[1] == f[0]:
        count +=1
        mcount = count
    if f[1] != f[0]:
        p.append(mcount)
        count = 1
    f = f[1:]

print (max(p))
