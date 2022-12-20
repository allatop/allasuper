def words(name):
    file = open(name, encoding="UTF-8")
    text = file.read().split(' ')
    file.close()

    return text


# print(words('words.txt'))

def record(rec):
    with open('record.txt') as file:
        text = file.read()

    if rec > int(text):
        with open('record.txt', "w") as file:
            file.write(str(rec))
            print(f"Молодец! Ты побил свой рекорд: {rec}")
    if rec <= int(text):
        print(f"Текущий рекорд: {rec}\nВаш рекорд: {text} ")
