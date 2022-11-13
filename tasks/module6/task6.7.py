f = input().split()
k = f.copy()
k = k[1::]
for i in f:
    if i in k:
        print('yes')
    else:
        print('no')
    k = k[1::]
