a = int(input())
s = []
n = 0
while n**2 < a:
    n+=1
    s.append(n**2)
    if n**2 > a:
        s.pop()
print(s)