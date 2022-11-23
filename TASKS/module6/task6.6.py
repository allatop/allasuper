l = input().split()
p = input().split()
f = []
while len(l) != 0:
    for i in range(len(p)):
        if l[0] == p[i]:
            f.append(l[0])
    l = l[1::]
print(' '.join(f))