from functools import reduce


def my_func(el_p, el):
    return el_p * el

print(f'Список {[el for el in range(100, 1000) if el % 2 == 0]}')
print(f'Произведение всех значений {reduce(my_func, [el for el in range(100, 1000) if el % 2 == 0])}')