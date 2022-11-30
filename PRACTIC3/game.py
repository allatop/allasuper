from base import *

kw = "\u25A0"
word = words(name)
lives = 1

def game(word,lives):
    word1 = word.copy()
    word = "".join(word)
    print(word)
    lenw = len(word)
    for i in range(lenw):
        word1[i] = kw
    kwstr = " ".join(word1)

    while lives > 0:
        print(f"{kwstr} | Кол-во жизней: {lives}")
        letter = input('Введи слово или букву: ')
        if letter == word:
            print('Вы выиграли! Ура')
            break
        if len(letter) > 1:
            print('Неверный ответ(')
        elif letter in word:
            for let in range(lenw):
                if word[let] == letter:
                    kwstr = kwstr.split(" ")
                    kwstr[let] = letter
                    kwstr = " ".join(kwstr)
        else:
            print('Такой буквы нет!')
            lives -= 1
        if kw not in kwstr:
            print('Вы выиграли! Ура')
            break
    if lives == 0:
        print(f"Вы проиграли!\nСлово: {word}")

print(game(word,lives))
