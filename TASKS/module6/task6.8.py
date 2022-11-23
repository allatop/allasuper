h = input()

print(h[2])
print(h[-1])
print(h[:5])
print(h[:-2])
print(h[::2])
f = list(h)
f = f[1::]
f = f[::2]
print(''.join(f))
print(h[::-1])
k = h[::2]
print(k[::-1])
