import json
import globals as g
from random import *

def save():
    with open("Python - education/Seminar_8/hw/phonebook.json","w",encoding="utf-8") as fb:
        fb.write(json.dumps(g.phonebook, ensure_ascii=False))
    print("Телефонный справочник был успешно сохранен в файле phonebook.json")

def load():
    with open("Python - education/Seminar_8/hw/phonebook.json","r",encoding="utf-8") as fb:
        g.phonebook = json.load(fb)
    print("Телефонный справочник был успешно загружен.")   

def clear():
    g.phonebook.clear()
    print("Телефонный справочник был успешно очищен.\nНе забудьте сохранить изменения!\n")

def add():
    print('''
    Для того, чтобы добавить человека в телефонную книгу следуйте инструкциям ниже.
    Ecли какой-то параметр остутствует введите -\n''')
    f = input("Введите фамилию: ")
    name = input("Введите имя: ")
    secondName = input("Введите отчество: ")
    number = input("Введите мобильный телефон: ")
    g.phonebook.append({
    'Фамилия:': f'{f}',
    'Имя:': f'{name}',
    'Отчество:': f'{secondName}',
    'Телефон:': f'{number}'
    })
    print("Абонент успешно добавлен в телефонный справочник!\n")

def all():
    if g.phonebook == []:
        print('Книга пуста!')
    else:
        count = 0
        for i in g.phonebook:
            count += 1
            print(f'\nАбонент №{count}')
            for key, value in i.items():
                print(f'{key} {value}')

def red():
    n = int(input("Введите номер абонента, которого вы хотите отредактировать: "))
    try:
        f = input("Введите актуальную фамилию: ")
        g.phonebook[n-1].update({'Фамилия:' : f})
        name = input("Введите актуальное имя: ")
        g.phonebook[n-1].update({'Имя:' : name})
        secondName = input("Введите актуальное отчество: ")
        g.phonebook[n-1].update({'Отчество:' : secondName})
        number = input("Введите актуальный мобильный телефон: ")
        g.phonebook[n-1].update({'Телефон:' : number})
            
        print("Абонент успешно изменён!\n")
    except:
            print("Нет такого Абонента(")

def show():
    n = int(input("Введите номер абонента: "))
    print(f'\n{g.phonebook[n-1]}')

def random():
    try:
        print("Случайный абонент -" + choice(g.phonebook) )
    except:
        print("Походу ещё нет абонентов")

def delete():
    f = int(input("Введите номер абонента, которого нужно удалить: "))
    try:
        g.phonebook.pop(f-1)
        print(f"Абонент №{f} удалён!")
    except:
        print("Нет такого Абонента(")

def help():
    print('''Список комманд:\n
    /stop - закончить работу;
    /all - показать список всех абонентов;
    /add - добавить абонента;
    /delete - удалить абонента;
    /save - сохранить измения в файле;
    /load - загрузить данные из файла;
    /clear - очистить текущий справочник;
    /red - редактировать абонента;
    /show - показать абонента;\n''')