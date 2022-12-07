name = 'data.txt'


def readfile(name):
    file = open(name, encoding="UTF-8")
    text = file.read().split(' ')
    for i in range(len(text)):
        text[i] = text[i].lower()
    text = ' '.join(j for j in text if j.isalpha())
    text = text.split(' ')
    new = set(text)

    return list(new)


def savefile(name, new):
    file = open(name, encoding="UTF-8", mode='w')
    new = sorted(new)
    file.write("Количество уникальных слов: " + str(len(new)))
    file.write("\n-----------------------------\n")
    file.write('\n'.join(new))
