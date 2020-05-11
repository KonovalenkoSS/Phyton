goods = int(input("Сколько будет товара "))
n = 1
my_dict = []
my_list = []
my_analys = {}
while n <= goods:
    my_dict = dict({'Название': input("Введите название "), 'Цена': input("Введите цену "),
                    'Количество': input('Введите количество '), 'Ед.': input("Введите единицу измерения ")})
    my_list.append((n, my_dict))
    n += 1
    my_analys = dict(
        {'Название': my_dict.get('Название'), 'Цена': my_dict.get('Цена'), 'Количество': my_dict.get('Количество'),
         'Ед.': my_dict.get('Ед.')})
print(my_list)
print(my_analys)