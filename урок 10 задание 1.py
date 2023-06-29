pets={}
pet={}
i=0
v=['год', 'года', 'лет']
r=''
while True:
    print('Введите команду: ')
    print('Записать в словарь(1): ')
    print('Прочитать из словаря(2): ')
    print('Выйти из программы(3): ')
    komanda=input()
    if komanda=='1':
        vid = input('Введите вид питомца: ')
        god = input('Введите возраст питомца: ')
        name = input(' Введите имя питомца: ')
        namev= input(('Введите имя владельца: '))
        if name in pets.keys():
            print(f'Уже есть {name}')
            continue
        else:
            if namev in pets.values():
                print(f'Уже есть {namev}')
                continue
            else:
                pet['Вид питомца'] = vid
                pet['Возраст питомца'] = int(god)
                pet['Имя владельца'] = namev
                pets[name] = pet
                i+=1
    if komanda=='2':
        x=input('Введите имя питомца или "всё": ')
        if x=='всё':
            print(pets)
        else:
            god = str(pets[x]["Возраст питомца"])
            n = len(god)
            if n == 1:
                temp = int(god)
            if n == 2:
                temp = int(god[1])
            if n == 3:
                temp = int(god[2])
            if temp == 1:
                r = v[0]
            if temp in [2, 3, 4]:
                r = v[1]
            if temp in range(5, 10):
                r = v[2]
            print(f'Это {pets[x]["Вид питомца"]} по кличке "{x}". Возраст питомца: {pets[x]["Возраст питомца"]} {r}. Имя владельца: {pets[x]["Имя владельца"]}')
    if komanda=='3':
        break