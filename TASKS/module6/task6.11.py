f = input()
i = f.index('h')
g = f.rindex('h')
o = f[i+1:g]
o = o[::-1]
print(f[:i+1]+o+f[g:])
