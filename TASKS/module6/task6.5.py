l = input().split()
p = input().split()
count = 0
while len(l) != 0:
    for i in range(len(p)):
        if l[0] == p[i]:
            count += 1
    l = l[1::]
print (count)