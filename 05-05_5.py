def sum ():
    sum_res = 0
    ex = False
    while ex == False:
        number = input('Введитес число или "-" для выхода - ').split()
        res = 0
        for el in range(len(number)):
            if number[el] == '-':
                ex = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f'Сумма чисел равна {sum_res}')
    print(f'Ваша последняя сумма {sum_res}')
sum()