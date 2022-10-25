a = input()
b = input()
c = input()
d = input()
e = input()
t = input()
y = input()
w = input()
q = input()
z = '0'
f = a + b + c + d + e + t + y + w + q + z
f = ' '.join(f).split()
count = 1
while len(f) != 1:
    if f[1] == f[0]:
        count +=1
    f= f[1:]
print (count)
