i = int(input())
s = [1, 1]
n = 1
a = s.copy()
while len(s) !=15 :
    s.append(a[0]+a[1])
    a = s.copy()
    a = a[n:]
    n+=1

print(s[i-1])
