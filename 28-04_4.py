first = int(0)
zero = int(0)
num = int(input("Введите число "))
while first > zero:
    zero = num % 10
    if first < zero:
        zero = first
    num = num // 10
else:
    print("Максимальное число %i" %(zero))
