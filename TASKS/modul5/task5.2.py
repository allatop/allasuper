a = int(input())
n = 25
s = []
while n >= 1:
    n-=1
    if 2**n <= a:
        s.append(n)
print(max(s),2**max(s))