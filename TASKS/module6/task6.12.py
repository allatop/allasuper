f = input()
i = f.index('h')
g = f.rindex('h')
o = list(f.replace('h','H'))
o[i] = 'h'
o[g] = 'h'
print(''.join(o))


