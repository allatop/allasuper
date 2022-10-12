dict = {}

def get_name():
    name = input("Введите имя контакта: ")
    name = name.title().strip()
    return name

def get_number():
    number = input("Введите номер телефона: ")
    number = number.replace(' ', '')
    number = number.replace('-', '')
    if number[0] == '9' and len(number) == 10:
        number = '+7' + number
    if number[0] == '8' and len(number) == 11:
        number = '+7' + number[1:]
    if number[0] == '7' and len(number) == 11:
        number = '+' + number
    if number[:2] == '+7' and len(number) == 12:
        return number
    else:
        print('Неправильно набран номер!')
        return get_number()


def contact(dict, name, number):
    dict[name] = number
    print('Контакт добавлен')
    return dict

def sh_contact(dict):
    print("Список контактов:")
    for i in dict:
        print(i, dict[i])

def delete_contact(dict, name):
    if True:
        dict.pop(name)
        print("Контакт успешно удален!")
    else:
        print('Такого контакта нет!')

def ch_contact(dict, name, number):
    if name in dict:
        dict[name] = number
    else:
        print('Такого контакта нет')


def menu(dict):
    while True:
        print(f'Выберите действие: \n1. Добавить контанкт \n2. Просмотреть список контактов \n3. Удалить контакт \n4. Изменить номер телефона \n5. Выход')
        p = int(input())
        if p == 1:
            contact(dict, get_name(), get_number())
        if p == 2:
            sh_contact(dict)
        if p == 3:
            delete_contact(dict, get_name())
        if p == 4:
            ch_contact(dict, get_name(), get_number())
        if p == 5:
            print("Спасибо за использование")
            break
dict = {}
menu(dict)
