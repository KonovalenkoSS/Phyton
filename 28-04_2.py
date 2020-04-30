time = int(input("Введите время "))
time_h = time // 3600
print("Вы ввели число состоящее из %i часов" %(time_h))
time_m = (time - (3600 * time_h))//60
print("Вы ввели число состоящее из %i минут" %(time_m))
time_s = time - (3600 * time_h) - (60 * time_m)
print("Вы ввели число состоящее из %i секунд" %(time_s))
time_h = str(time_h)
time_m = str(time_m)
time_s = str(time_s)
print("Ваш результат %s:%s:%s" % (time_h,time_m, time_s))