dict = {}

for i in range(int(input())):
    for words in input().split(' '):
        dict[words] = dict.get(words, 0) + 1

for i in sorted(dict, key=dict.get, reverse=True):
    print(i, dict[i])