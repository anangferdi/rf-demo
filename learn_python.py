### You can find more detail on https://www.programiz.com/python-programming/tutorial

### Just print it
print("hai")


### Variables
#We do not need to define variable type in Python.
a = 5
print("a =", a)
a = "Test"
print("a =", a)


### Operators
x = 14
y = 4
# Add two operands
print('x + y =', x+y) # Output: x + y = 18

# Subtract right operand from the left
print('x - y =', x-y) # Output: x - y = 10

# Multiply two operands
print('x * y =', x*y) # Output: x * y = 56

# Divide left operand by the right one 
print('x / y =', x/y) # Output: x / y = 3.5

# Floor division (quotient)
print('x // y =', x//y) # Output: x // y = 3

# Remainder of the division of left operand by the right
print('x % y =', x%y) # Output: x % y = 2

# Left operand raised to the power of right (x^y)
print('x ** y =', x**y) # Output: x ** y = 38416


### Get input from user
# string_input = input("Enter your name : ")
# print("Welcome", string_input)


### Python data structure
##List
"""
A list is created by placing all the items (elements) inside a square bracket [] separated by commas.

It can have any number of items and they may be of different types (integer, float, string etc.)
"""
# empty list
my_list = []

# list of integers
my_list = [1, 2, 3]

# list with mixed data types
my_list = [1, "Hello", 3.4]

#Here's how you can access elements of a list.
language = ["French", "German", "English", "Polish"]

# Accessing first element
print(language[0])

# Accessing fourth element
print(language[3])


### Dictionaries
"""
Dictionary is an unordered collection of items. 
While other compound data types have only value as an element, a dictionary has a key: value pair. 
"""
# empty dictionary
my_dict = {}

# dictionary with integer keys
my_dict = {1: 'apple', 2: 'ball'}

# dictionary with mixed keys
my_dict = {'name': 'John', 1: [2, 4, 3]}

person = {'name':'Jack', 'age': 26, 'salary': 4534.2}
print(person['age']) # Output: 26

# Changing age to 36
person['age'] = 36 
print(person)

#adding item to dictionary
person['gender'] = "Male"
print(person)


### Python if else statement
num = -1

if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")


### while loop
n = 3

# initialize sum and counter
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i+1    # update counter

print("The sum is", sum)


### For loop
numbers = [6, 5, 3, 8, 4, 2]

sum = 0

# iterate over the list
for val in numbers:
    sum = sum+val

print("The sum is", sum)


### Function
def print_lines():
    print("I am line1.")
    print("I am line2.")

# function call
print_lines()

# add param on function
def add_numbers(a, b):
  sum = a + b
  return sum

result = add_numbers(4, 5)
print(result)