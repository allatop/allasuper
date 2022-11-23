f = input()
i = f.index('h')
g = f.rindex('h')
print(f[:i] + f[g+1:])

