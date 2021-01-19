def my_pow(x, y):
    i = 0
    c = 1
    if x > 0 and y < 0:
        while i > y:
            c = c / x
            y += 1
        print("Результат возведения в степень :", c)
    else:
        print("Не выполнены х или y ввода")

my_pow(x=int(input("введите положительное число x : ")), y=int(input("введите целое отрицательное число y : ")))