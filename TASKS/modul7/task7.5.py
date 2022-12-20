list = []
files = []
for i in range(int(input())):
    answer = input()
    list.append(answer)
    files.append(answer.split(' ')[0])

for i in range(int(input())):
    o, filename = input().split()
    o = o.upper()
    if o == 'EXECUTE' or o == 'WRITE' or o == 'READ':
        o = o[0]
        flag = 0
        for data in list:
            if data.count(filename) and data.count(o):
                flag = 1
        if flag == 1:
            print('OK')
        else:
            print('Denied')
