#задача 1
def division(*args):
    try:
        a = int(input("введите число a :"))
        b = int(input("введите число b :"))
        s = a / b
        return s
    except ValueError:
        print('Только цыфры')
    except ZeroDivisionError as  err:
        print("Делить на ноль нельзя!!!")

print(f'result{division()}')