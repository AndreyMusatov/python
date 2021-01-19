#Задача 2
def database(surname, name, year, city, email, telephone):
    return ' '.join([surname, name,  year, city, email, telephone])



print(database (surname = input("введите фамилию :"), name = input('введите имя :'), year = input("введите год рождения :"), city = input("введите ваш город проживания :"),
                email= input("введите эл.почту :"), telephone = input("Введите телефон :")))

