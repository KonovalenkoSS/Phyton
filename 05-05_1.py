def func (x, y):
    try:
        z = x / y
        return z
    except ZeroDivisionError:
        return "Делитель не должен быть равен 0"
    except ValueError:
        return "Необходимо ввести число"
print(func(int(input("Введите делимое = ")), int(input("Введите делитель = "))))