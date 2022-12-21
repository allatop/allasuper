import random
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")


def computer_choies():
    y = int(random.randint(1, 3))
    if y == 1:
        chooise = "камень"
    if y == 2:
        chooise = "ножницы"
    if y == 3:
        chooise = "бумага"

    file.write(f'[{now.strftime("%H:%M:%S")}] Компьютер выбрал {chooise} \n')

    return y


def player_choose(x, record):
    current_time = now.strftime("%H:%M:%S")

    x = int(input())

    if x == 1:
        chooise = "камень"
    if x == 2:
        chooise = "ножницы"
    if x == 3:
        chooise = "бумага"
    if x == 4:
        file.write(f'[{now.strftime("%H:%M:%S")}] Конец игры \n')
        file.write(f'[{now.strftime("%H:%M:%S")}] Рекордная серия {record}\n')

        file.close()
        return x

    if x != 4:
        file.write(f'[{now.strftime("%H:%M:%S")}] Игрок выбрал {chooise} \n')
        return x


def funk(x, y, schet, record):
    if (x == 1 and y == 1) or (x == 2 and y == 2) or (x == 3 and y == 3):
        file.write(f'[{now.strftime("%H:%M:%S")}] Количество очков {schet}) \n')

    if x == 1 and y == 2:
        schet += 1
        file.write(f'[{now.strftime("%H:%M:%S")}] Количество очков {schet}) \n')

    if x == 1 and y == 3:
        file.write(f'[{now.strftime("%H:%M:%S")}] Количество очков {schet})\n')

    if x == 2 and y == 1:
        file.write(f'[{now.strftime("%H:%M:%S")}] Количество очков {schet})\n')

    if x == 2 and y == 3:
        schet += 1
        file.write(f'[{now.strftime("%H:%M:%S")}] Количество очков {schet})\n')

    if x == 3 and y == 1:
        schet += 1
        file.write(f'[{now.strftime("%H:%M:%S")}] Количество очков {schet})\n')

    if x == 3 and y == 2:
        file.write(f'[{now.strftime("%H:%M:%S")}] Количество очков {schet})\n')

    if schet > record:
        return schet
    else:
        return record


record = 0
schet = 0
x = 0
file = open("play.txt", "w", encoding="utf-8")
print("Начало игры")
file.write(f'[{now.strftime("%H:%M:%S")}] Начало игры \n')
print("Выберите: \n 1 - Камень \n 2 - Ножницы \n 3 - Бумага \n 4 - Выход")
while x != 4:
    x = input()
    x = player_choose(x, record)
    if x == 4:
        break
    y = computer_choies()
    record = funk(x, y, schet, record)
file.write(123456)
