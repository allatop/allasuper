name = 'text'

def readfile(name):
    try:
        file = open(name, encoding="UTF-8")
        txt = file.read().splitlines()
        txt = [int(i) for i in txt]

        if txt[0] != len(txt[1:]):
            raise KeyError

    except KeyError:
        return 'no'
    return txt[1:]

print(readfile(name))