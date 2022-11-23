a = int(input())
b = a+1
s = []
while b>2:
    b -= 1
    if a % b == 0:
        s.append(b)
print (min(s))

