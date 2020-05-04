goods = []
i=1
while input("Что у вас?"):
    number = int(input("Сколько у вас продуктов: "))
    list = {}
    while i =< number :
        i +=1
        list_name = input("Название: ")
        list_prise = input("Цена: ")
        list[list_name] = list_prise
    goods.append(tuple([number, list]))
print(goods)
analitics = {}
for good in goods:
    for list_name, list_prise in good[1].items():
        if list_name in analitics:
            analitics[list_name].append(list_prise)
        else:
         analitics[list_name] = [list_prise]
print(analitics)