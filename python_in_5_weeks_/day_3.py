## Dictionaries: 
# Exercise 1.
# menu = {
#     "sandwich": 15,
#     "tea": 8,
#     "apple": 3
# }
# user_order = []
# while True:
#     user_input = input("Menu: sandwich and tea, which would you like: ").strip().lower()
#     if user_input == '':
#         break
#     if user_input in menu:
#         for i in menu:
#             if i == user_input:
#                 user_order.append(menu[i])
#     if user_input == 'finish':
#         print(f"The total is {sum(user_order)}")


## Exercise 2.
# counts = {"vowels": 0, "digits": 0, "others": 0}

# while True:
#     user_input = input("Type a text: ").strip().lower()
#     if user_input == '':        
#         break
#     for i in user_input:
#         if i.isdigit():
#             counts["digits"] += 1
#         if i in "aeiou":
#             counts["vowels"] += 1
#         else:
#             counts["others"] +=1    
# print(counts)

