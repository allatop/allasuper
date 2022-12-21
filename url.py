import urllib.request
import re

url = "https://quke.ru/shop/smartfony/apple?page-size=72"
site = urllib.request.urlopen(url).read().decode("utf8")
name = re.findall(r'(?:"name": )([^,]+)',site)
price =re.findall(r'(?:"price": )([^\n]+)',site)
# print(name,price)
# with open('book.txt', "w", encoding='UTF-8') as file:
#     while len(name) != 0:
#         file.write(f'{name[0]} | {price[0]}\n ')
#         name = name[1:]
#         price = price[1:]
dict = {}
while len(price) != 0:
    dict[name[0]] = price[0]
    name = name[1:]
    price = price[1:]
print(dict)
dictk = sorted([int(i) for i in dict.values()])
print(dictk)
sotrdict = {}
for j in dictk:
    for k in dict.keys():
        if dict[k] == str(j):
            sotrdict[k] = dict[k]
print(sotrdict)
# print (len(name),len(price))