a = input()
b = input()
c = input()
d = input()
e = '0'
f = a + b + c + d + e
f = ' '.join(f).split()
count = 0
while len(f) != 1:
    if f[1] > f[0]:
        count +=1
    f= f[1:]
print (count)