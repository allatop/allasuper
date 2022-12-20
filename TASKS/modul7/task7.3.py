dict = {}
count = int(input())

for i in range(count):
    s, s1 = input().split()
    if s in dict:
        dict[s] = str(int(s1) + int(dict[s]))
    else:
        dict[s] = s1

for s, s1 in sorted(dict.items()):
    print(s + ' ' + s1)




