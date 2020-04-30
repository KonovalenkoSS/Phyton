vir = int(input("Введите вашу выручку "))
izd = int(input("Введите ваши издержки "))
if vir > izd:
    rent = vir - izd
    sotr = int(input("Ваша компания работает с прибылью в %i ! Подскажите сколько у вас сотрудников " %(rent)))
    prem = rent / sotr
    print("Прибыль на каждого сотрудника составила %i" %(prem))
else:
    print("У вас не рентабильная фирма")