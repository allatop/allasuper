count = 0
f = input().split()

while len(f) != 1:
    if f[1] > f[0]:
        count +=1
    f= f[1:]
print (count)