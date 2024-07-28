'''real_reais'''
# x = int(input("Type a number: "))
# y = int(input("Type other number: "))
# total = x + y
# real_reais = lambda value: str(value) + " real" if value == 1 else str(value) + " reais"
# print(f"The sum of {real_reais(x)} plus {real_reais(y)} is {real_reais(total)}")

'''Drawing importing Turtle'''
# from turtle import Turtle, Screen
# import turtle
# import random

# mike = Turtle()
# mike.hideturtle()
# mike.teleport(-200, 100)
# mike.speed(0)
# turtle.colormode(255)

# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return (r, g, b)

# while True:
#     mike.pencolor(random_color())
#     mike.forward(400)
#     mike.right(179)

# screen = Screen()
# screen.exitonclick()

'''Print in inverted order'''
# name = 'My name is Mike'.split()
# inverted_name = ''
'''First try'''
# for i in range(len(name)):
#     name_i = name[i]
#     name_i_len = len(name_i)
#     while name_i_len > 0:
#         for j in range(name_i_len -1, - 1, -1):
#             inverted_name += ' '.join(name_i[j])
#             name_i_len -= 1        
# print(inverted_name)
'''Second try with [::-1]'''
# name = 'My name is Mike'.split()
# inverted_name = []
# for index in name:
#     inverted_name.append(index[::-1])
# name = ' '.join(inverted_name)
# print(name)

'''## Remove items from a list while iterating ##'''
'''Solution 1'''
# number_list = [100, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# i = 0
# list_len = len(number_list)
# while i < list_len:
#     if number_list[i] > 50:        
#         number_list.pop(i)
#         list_len -= 1
#     else:
#         i += 1
# print(number_list)

''' Solution 2'''
# for i in range(len(number_list) -1, -1, -1):
#     if number_list[i] > 50:        
#         number_list.pop(i)
# print(number_list)

'''Reverse Dictionary mapping'''
# ascii_dict = {'A': 65, 'B': 66, 'C': 67, 'D': 68}
# new_dict = {}
# for key in ascii_dict:
#     new_dict[ascii_dict[key]] = key
# print(new_dict)

'''Factorial Calculator'''
# number = 5
# factorial = 1
# factorial_list = []
# for num in range(1, number + 1):
#     factorial = factorial * num
#     factorial_list.append(factorial)
# print(factorial_list)

'''Pyramid print pattern'''
# x = 1
# for i in range(5, 0, -1):
#     for j in range(i, 0, -1):
#         print(x, end='')
#     print('')
#     x += 1

'''Inner function'''
# x = 'Bobby'
# y = 'Fofao'
# def join_names(first_name, second_name):
#     return first_name + second_name
# def join_dev(name):
#     return name + 'Dogs'
# print(join_dev(join_names(x,y)))

'''Modify one element inside a list'''
# list1 = [5, [10, 15, [20, 25, [30, 35], 40], 45], 50]
# list1[1][2][2][1] = 3500
# print(list1)
'''using for loop'''
# def modify_list(lst):
#     for i in range(len(lst)):
#         if isinstance(lst[i], list):
#             modify_list(lst[i])  # Recursively call modify_list for sublists
#         elif lst[i] == 35:
#             lst[i] = 3500  # Modify the value to 3500
# # Call the function to modify list1
# modify_list(list1)

'''Access the nested key'''
# emp_dict = {
#     "company": {
#         "employee": {
#             "name": "Jess",
#             "payable": {
#                 "salary": 9000,
#                 "increment": 12
#             }
#         }
#     }
# }
# print(emp_dict['company']['employee']['payable']['increment'])

# st = 'print only words that start with s in this sentence'.split()
# for word in st:
#     if st[word][0] == 's':
#         print(word)

# num_list = [x for x in range(0,50) if x % 3 == 0]
# print(num_list)

# st = 'Print every word in this sentence that has an even number of letters'.split()
# for i in st:
#     if len(i) % 2 == 0:
#         print(i, end=' ')

# for i in range(4, 0, -1):
#     print('mike'[:i])