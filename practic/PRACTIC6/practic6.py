import re
name = 'text.txt'
a = []
def train(name):
    file = open(name,encoding="UTF-8")
    text = file.read()
    time =re.findall( r'(?:[А-Я][а-я]{0,5}\ [а-я]{0,1}\ )([^\n]+)',text)
    num = re.findall(r'\d{3,}',text)
    s =re.findall(r'[а-я]{1,2}\ ?[А-Я][а-я]+',text)
    while len(time)!=0:
        a.append(f'[{time[0]}] - Поезд № {num[0]} {s[0]}')
        time = time[1:]
        num = num[1:]
        s = s[1:]
    m = '\n'.join(a)
    return m

def new(name, m):
    file = open(name, encoding="UTF-8", mode='w')
    file.write(m)