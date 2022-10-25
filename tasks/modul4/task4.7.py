s = input()
b = "  ".join(s).split()
o = b[::-1]
f = ''.join(b)
a = ''.join(o)
if a == f:
    print('да')
else:
    print('нет')
