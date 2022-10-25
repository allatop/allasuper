import random
t=0
for i in range(1000):
    dic = {}
    for j in range(23):
        m = random.randint(1, 12)
        if m in [1, 3, 5, 7, 8, 10, 12]:
            d = random.randint(1, 31)
        elif m in [2]:
            d = random.randint(1, 28)
        else:
            d = random.randint(1, 30)
        dic[j] = m, d
    if len(set(list(dic.values()))) < 23:
        t+=1
print(t/1000)
if(t/1000>0.5):
    print("Правда")
else:
    print("Ложь")

