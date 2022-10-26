import random
count = 0
lives = 3
while True:
    a = random.randint(0,10)
    b = random.randint(0,10)

    print(F'{a} + {b} = ')
    answ = int(input())
    if answ == (a + b) :
        count +=1
        print( 'Ответ верный!' )
    else:
        lives = lives - 1
        print ( f'Ответ неверный! Жизней осталось {lives}' )
    if lives == 0 :
        print (f"Игра закончилась! Ты набрал(а) {count}")
        break



