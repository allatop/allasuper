import random
count = 0
ass = []
n = 0
count1= 0
while n != 10:
    ass.append(random.randint(1,365))
    n += 1
    print(ass)
for i in range (len(ass)):
    for j in range (i + 1, len(ass)):
        if ass[i ] == ass[j]:
            count+=1

        else:
            count1+=1
print(count,count1)
if count / 253 >= 0.5:
    print('правда')
else:
    print('ложь')