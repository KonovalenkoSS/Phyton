first_list = [55, 3, 35, 45, 2, 13, 66]
#first_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
second_list = [el for num, el in enumerate(first_list) if first_list[num - 1] < first_list[num]]
print(f'Исходный список {first_list}')
print(f'Новый список {second_list}')