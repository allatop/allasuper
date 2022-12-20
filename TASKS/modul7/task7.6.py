g = {}
for i in range(int(input())):
    cities = input().split()
    for city in cities[1:]:
        g[city] = cities[0]

list = []
for i in range(int(input())):
    list.append(g.get(input()))

for i in list:
    print(i)
