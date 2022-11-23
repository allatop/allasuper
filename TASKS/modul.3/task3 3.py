s = input()
if s.count('f') == 0:
    print('-1')
elif s.count('f') == 1:
    print(s.index('f'))
else:
    print(s.index('f'), s.rindex('f'))
