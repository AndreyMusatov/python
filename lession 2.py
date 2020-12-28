# Задача 1
result_list = [2, 'text', 456, 45.3, None]

for i in result_list:
    print(type(i))
# Задача 2
el_count = int(input("Введите количество элементов списка "))
my_list = []
i = 0
el = 0
while i < el_count:
    my_list.append(input("Введите следующее значение списка "))
    i += 1
for elem in range(int(len(my_list) / 2)):
    my_list[el], my_list[el + 1] = my_list[el + 1], my_list[el]
    el += 2
print(my_list)

# задача 3
seasons_list = ['Зима', 'весна', 'лето', 'осень']
month = int(input("Введите месяц по номеру "))
if month == 1 or month == 12 or month == 2:
    print(seasons_list[0])
elif 2 < month < 6:
    print(seasons_list[1])
elif 5 < month < 9:
    print(seasons_list[2])
elif 10 < month < 12:
    print(seasons_list[3])
else:
    print("Такого месяца не существует")

month = int(input("Введите месяц по номеру "))
seasons_dict = {1: 'Зима', 2: 'весна', 3: 'лето', 4: 'осень'}
if month == 1 or month == 12 or month == 2:
    print(seasons_dict.get(1))
elif 2 < month < 6:
    print(seasons_dict.get(2))
elif 5 < month < 9:
    print(seasons_dict.get(3))
elif 10 < month < 12:
    print(seasons_dict.get(4))
else:
    print("Такого месяца не существует")

# задача 4
my_str = input("Введите слова разделеной проблемом : ")
my_word = []
num = 1
for i in range(my_str.count(' ') + 1):
    my_word = my_str.split()
    if len(str(my_word)) <= 10:
        print(f" {num} {my_word[i]}")
        num += 1
    else:
        print(f" {num} {my_word[i][0:10]}")
        num += 1

# Задача 5
my_list = [7, 5, 3, 3, 2]
print(f"Рейтинг - {my_list}")
digit = int(input("Введите число (111 - выход) "))
while digit != 111:
    if 0 < digit < 10:
        for el in range(len(my_list)):
            if my_list[el] == digit:
                my_list.insert(el + 1, digit)
                break
            elif my_list[el] > digit and my_list[el + 1] < digit:
                my_list.insert(el + 1, digit)
                break
            print(f"текущий список - {my_list}")
            digit = int(input("Введите число "))

# Задача 6

goods = []
s = int(input("Введите количество товара "))
features = {'название': '', 'цена': '', 'количество': '', 'eд': ''}
my_analys = {'название': [], 'цена': [], 'количество': [], 'eд': []}
i = 1
feature_ = None
while i <= s:
    for f in features.keys():
        feature_ = input(f'Введите "{f}"')
        features[f] = int(feature_) if (f == 'цена' or f == 'количество') else feature_
        my_analys[f].append(features[f])
        goods.append((i, features))
    i += 1
print(f'\n{"-" * 15} Анализ{"-" * 15}\n ')
for key, value in my_analys.items():
    print(f'{key}: {value}')
print("-" * 37)
