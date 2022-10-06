s = input()
a = " ".join(s).split()
c = a.index("f")
o = a[::-1]
b = o.index("f")
print(c,len(o) - 1 - b)