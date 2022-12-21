list = []
c = 0

col = int(input())

for i in range(col):
    words = input().split()

    for k in words:
        list.append(k)

list = sorted(list)

for slovo in list:
    if list.count(slovo) > c:
        a = slovo
        c = list .count(slovo)

print(a)