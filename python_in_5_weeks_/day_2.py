## Gets the number of vowels, digits and others
# vowels = 0
# digits = 0
# others = 0

# user_input = input('Type something: ').strip()

# for index in user_input:
#     if index in 'aeiou':
#         vowels += 1
#     elif index.isdigit():
#         digits += 1
#     else:
#         others += 1

# print(f"Your input has vowels {vowels}, digits {digits} and others {others}")



## Pyramidal print - prints first letter and on.
# user_input = input('Type your name: ')
# x = 1
# for index in user_input:
#     name = []
#     name.append(index)
#     print(name[:x + 1])
#     x += 1
## ***Solution***
# for index in range(len(user_input)):
#     print(user_input[:index + 1])


## Print if 'index' is divisible by 'n'
# text = input("Type some text: ")
# n = int(input("Type a number: "))

# for index, char in enumerate(text):
#     if index % n == 0:
#         print(f"{index}: {char}")

## While sums user inputs until it hits 100
# total = 0
# is_not_max = True
# while is_not_max:
#     user = int(input("Type a number to add: "))
#     if user > 0:
#         print(f"{user} + {total}")
#         total += user
#         if total >= 100:
#             print(f"You've reached {total}")
#             is_not_max = False

## Odds and evens
# user = int(input("Type a number to add: "))
# if user % 2 == 0:
#     print("It's an even number!")
# else:
#     print("It's an odd number!")

## Split and Lists
# word = 'hello out there'
# word = word.split(' ') # Creates a list ['hello', 'out', 'there']
# my_list = list(word) # Creates a list ['h', 'e', 'l', 'l', 'o', ' ', 'o', 'u', 't', ' ', 't', 'h', 'e', 'r', 'e']
# print(my_list)

## Pig Latin sentence
# sentence = input('Enter a sentence: ').strip()

# for word in sentence.split():

#     if word[0] in 'aeiou':
#         print(word + 'way')
#     else:
#         print(word[1:] + word[0] + 'ay')

