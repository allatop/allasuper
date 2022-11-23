f = input().split()
l = []
h = 0
for i in f:
    h += 1
    if i in l:
        print('да')
    else:
        print('нет')
    l = f[:h]
