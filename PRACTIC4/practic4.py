mama = 'data.txt'


def readfile(mama):
    file = open(mama, encoding="UTF-8")
    text = file.read().lower()
    alfa = "йцукенгшщзхъфывапролджэячсмитьбюё"
    for i in range(len(text)):
        if not (text[i] in alfa):
            text = text.replace(text[i], '')
    return text


print(readfile(mama))
