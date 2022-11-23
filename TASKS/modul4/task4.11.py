a = int(input())
b = int(input())
f = int(input())
o = int(input())
if ((a + b)% 2 !=0) and ((f + o)% 2 !=0):
    print('yep')
elif ((a + b)% 2 ==0) and ((f + 0)% 2 ==0):
    print('yep')
else:
    print('nope')