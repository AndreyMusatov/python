# задача 1

name = str(input("Введите ваше имя :"))
age = int(input("Введите ваш возрост: "))
print("Привет,", name, "поздравляю тебе уже", age, "лет.")

# Задача 2

time = int(input("Введите время в секундах : "))
hh = time // 3600
min = (time - hh * 3600) // 60
sec = time - (hh * 3600 + min * 60)
print(f"Время в формате чч:мм:сс  {hh} : {min} : {sec}")
# Задача 3
n = input("Введите число :")
nn = str(n * 2)
nnn = str(n * 3)
print("Сумма чисел n:", int(n) + int(nn) + int(nnn))

# задача 4
n = int(input("Введите целое положительное число "))
max = n % 10
while n >= 1:
    n = n // 10
    if n % 10 > max:
        max = n % 10
    if n > 9:
        continue
    else:
        print("Максимальное цифра в числе ", max)
        break
# Задача 5

profit = int(input("Введите свою сумму выручки :"))
cost = int(input("Введите сумму издержки :"))
if profit > cost:
    print("Выручка больше издержек")
    staff = int(input("Введите количество сотрудников :"))
    profit_sraff = profit / staff
    print(f'Прибыль фирмы в расчете на одного сотрудника :{profit_sraff:.2f}')
elif profit == cost
    print("Доход равен 0")
else:
    print("Издержки больше выручки")
#Задача 6

sportsman = int(input("Сколько км пробегаешь сотрудник в первый день :"))
total = int(input("Введите общий желаемый результат в км :"))
day = 1
while sportsman < total:
    print(f'{day}-день:{sportsman:.3f}')
    sportsman = + sportsman * 1.1
    day +=1

print(f'Результат достигнут : {total} км')