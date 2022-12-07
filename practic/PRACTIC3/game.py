from base import *

kw = "\u25A0"
word_list = words()


def game(word, lives, rec):
    while True:
        strlives = input('Выберите уровень сложности:\n1 - Лекгий (7 жизней)\n2 - Средний (5 жизней)\n3 - Сложный (3 жизни)')
        if strlives == '1':
            lives = 7
        if strlives == '2':
            lives = 5
        if strlives == '3':
            lives = 3
        break
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
            rec += 1
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
            rec += 1
            break
    if lives == 0:
        print(f"Вы проиграли!\nСлово: {word}")


print(game("молоко",lives,rec))
