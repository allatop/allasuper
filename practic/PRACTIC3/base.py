def words(name='words.txt'):
    file = open(name, encoding="UTF-8")
    text = file.read().split(' ')

    return text

# def repeat():
#     while True:
#         regame = input('Хотите сыграть еще раз?')
#         if regame == 'да':
#             game.game(word, lives,rec)
#         else:
#             print(f'Ваш рекорд:{rec} ')
#         break
