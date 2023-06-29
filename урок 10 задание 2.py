s=[int(i) for i in input('Введите исходные данные для словаря: ').split()]
sl={}
for x in s:
    sl[x]=x**x
for key,val in sl.items():
    print(key,val)