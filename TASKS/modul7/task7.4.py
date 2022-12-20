words = []
c = int(input())
for i in range(c):
    s = input().split(' ')
    for j in s:
        words.append(j)
words = sorted(words)

max = 0
answer = ''
for word in words:
    if words.count(word) > max:
        answer = word
        max = words.count(word)
print(answer)