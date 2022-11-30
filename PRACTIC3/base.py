import random

name = 'words.txt'


def words(name):
    file = open(name, encoding="UTF-8")
    text = file.read().split(' ')
    word = random.choice(text)
    word = " ".join(word).split()

    return word



