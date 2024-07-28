## How we would generally do it.
# numbers = [1, 2, 3, 4, 5]
# new_list = []
# for n in numbers:
#     multiplies = n * n
#     new_list.append(multiplies)
# print(new_list)

## How to loop through a list using List of Comprehension
numbers = [1, 2, 3, 4, 5]
new_list = [n*n for n in numbers]
print(new_list)