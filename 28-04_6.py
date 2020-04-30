day = 1
run = int(input("Сколько спортсмен пробежал в первый день - "))
run2 = int(input("Сколько должен пробегать в день - "))
while run2 >= run:

    run = (run * 110) / 100
    day = day + 1

else:
    print("спортмен пробежит на %i день" %(day))