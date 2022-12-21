import random

def kamaneshka():
    count = 0
    while True:
        kmn = ['k', 'n','b']
        person = int(input('Выберите:\n1 - камень;\n2 - ножницы;\n3 - бумага;\n'))
        if person == 1:
            person_ch = kmn[0]
        if person == 2:
            person_ch = kmn[1]
        if person == 3:
            person_ch = kmn[2]

        comp_choice = random.choice(kmn)
        if person_ch == comp_choice:
            print('ничья')
        elif person_ch == 'k':
            if comp_choice == 'n':
                count+=1
                print('ты выиграл')
            else:
                count = 0
                print('ты проиграл')
        elif person_ch == 'n':
            if comp_choice == 'b':
                count += 1
                print('ты выиграл')
            else:
                count = 0
                print('ты проиграл')
        elif person_ch == 'b':
            if comp_choice == 'k':
                count += 1
                print('ты выиграл')
            else:
                count = 0
                print('ты проиграл')


        print(person_ch,comp_choice)
kamaneshka()