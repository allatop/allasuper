import urllib.request
import re

url = "https://moskva1.jsprav.ru/avtorskaya-i-eksklyuzivnaya-mebel/"
site = urllib.request.urlopen(url).read().decode("utf8")
#print(site)
patern = r'(?:(?:company-info-name-org">)([^<]+)(?:[\w\W]+?data-rating=")([^"]+)(?:[\w\W]+?company-info-address-full company-info-text">\s+)([^\n]+)(?:[\w\W]+?company-info-time-full company-info-text">)([^<]+)(?:[\w\W]+?data-phone=")([^"]+)(?:[\w\W]+?title="Официальный сайт">)([^<]+))'
dict = re.findall(patern, site)
print(dict)