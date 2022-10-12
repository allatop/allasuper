import random
s = 0
p = 0
while True:
    a = [0 , 1, 0]
    b = random.choice(a)
    a.pop(b)
    a.remove(0)
    c = a.pop()
    if c == 0:
        p+=1
    else:
        s+=1
    if p+s == 10000:
        break

print(f'Процент побед если участник остался при своем выборе: {p//100}%  \nПроцент побед если участник поменял выбор: {s//100}%')

