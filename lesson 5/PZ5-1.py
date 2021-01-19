# ------------------------------------1-----------------------------
'''
Создать программно файл в текстовом формате, записать
в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
'''

my_f = open('text_1.txt', 'w', encoding='utf-8')
line = ' '
while line:
    line = input('Пишите или не пишите!: ')
    my_f.write(f'{line}\n') if line != '' else my_f.close()

my_f = open('text_1.txt', 'r', encoding='utf-8')
content = my_f.readlines()
print(content)
my_f.close()
