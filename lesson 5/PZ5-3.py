# ------------------------------------3-----------------------------
'''
Создать текстовый файл (не программно), построчно записать
фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней
величины дохода сотрудников.
'''

with open('text_3.txt', 'r', encoding='utf-8') as my_file:
    names = []
    aver_income = 0
    num = 0
    for line in my_file:
        num += 1
        name, income = (i for i in line.split())
        income = float(income)
        if income < 20000:
            names.append(name)
        aver_income += income
    aver_income /= num
print(*names)
print(aver_income)