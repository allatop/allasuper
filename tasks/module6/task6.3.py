l = input().split()
if len(l) % 2 == 0:
    l[::2], l[1::2] = l[1::2],l[::2]
    print(' '.join(l))
else:
    a = l.pop(-1)
    l[::2], l[1::2] = l[1::2], l[::2]
    l.append(a)
    print(' '.join(l))