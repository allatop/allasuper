s=input().split(' ')
a = '0 '
for i in range(len(s)):
    count = 0
    for j in range(i):
        if s[i] == s[j]:
            count = count+1
        if j == (i-1):
            a = a + f'{count} '
print(a)