from random import *
import json
import commands as cmds
import globals as g

g.phonebook = []

try:
    cmds.load()
    print('Добро пожаловать в телефонный справочник!\nСписок всех команд: /help')
except:
    print('Добро пожаловать в телефонный справочник!\nСписок всех команд: /help')
    with open("phonebook.json","w",encoding="utf-8") as fb:
        fb.write(json.dumps(g.phonebook, ensure_ascii=False))

while True:
    command=input("Введите комманду: ")
    if command=="/stop":
        cmds.save()
        print("До следующей встречи!")
        break
    elif command=="/all":
        cmds.all()      
    elif command =="/add":
        cmds.add()
    elif command=="/delete":
        cmds.delete()
    elif command=="/random":
        cmds.random()
    elif command =="/save":
        cmds.save()
    elif command=="/load":
        cmds.load()
    elif command=="/clear":
        cmds.clear()
    elif command=="/red":
        cmds.red()
    elif command=="/show":
        cmds.show()
    elif command=="/help":
        cmds.help()
    else:
        print("Неверная комманда. Список актуальных комманд: /help")