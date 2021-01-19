my_list = [15, 2, 3, 1, 7, 5, 4, 10]
my_new_list = [my_list[num] for num in range(1,len(my_list)) if my_list[num] > my_list[num -1]]
print(f'Исходный список {my_list}')
print(f'Новый список {my_new_list}')

