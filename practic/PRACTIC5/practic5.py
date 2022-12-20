name = input('Введите имя файла: ')


def readfile(name):
    try:
        file = open(name, encoding="UTF-8")
        txt = file.read().splitlines()
        txt = [int(i) for i in txt]

        if txt[0] != len(txt[1:]):
            raise KeyError

    except KeyError:
        return 'Количество чисел не соответствует первому числу!'
    except ValueError:
        return 'Файл заполнен неверно!'
    except FileNotFoundError:
        return 'Неверное имя файла!'
    return txt[1:]


print(readfile(name))
