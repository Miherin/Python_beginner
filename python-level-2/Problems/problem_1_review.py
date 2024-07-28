"""
Given a user's input of n, return a list of factorials from 0! to n!

Test cases:
0! = 1
1! = 1
2! = 1 x 2 = 2
4! = 1 x 2 x 3 x 4 = 24
"""


# Helper method to test equality
def assert_equals(actual, expected):
    assert actual == expected, f'Expected {expected}, got {actual}'


# Todo: Create a function that produces the factorial of a number
def factorial(n):
    product = 1
    for i in range(1, n + 1):
        product *= i
        print(product)
    return product

assert_equals(factorial(0), 1)
assert_equals(factorial(1), 1)
assert_equals(factorial(2), 2)
assert_equals(factorial(4), 24)

# Todo: Test factorial function


# Todo: Request a number from the user


# Todo: Print a list of factorials from 0 to the given number
number = int(input("Enter a number: "))

factorials = []

for i in range(number):
    factorials.append(factorial(i))

print(factorials)