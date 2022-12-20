dict = {}
count = int(input())

for i in range(count):
    s, s1 = input().split()
    dict[s] = s1

key = input()
print(dict[key])

