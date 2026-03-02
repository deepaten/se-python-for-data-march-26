import sys
#  Consolidating basics of Python

# Variables
x = 10 # int
name = "Deepa" # str
is_happy = True # boolean

# Using variables
print("Hello")
print(name)
print("Are you happy?",is_happy)
print(x)

# Re-assigning values
x = 20
print("Now",x)

# Memory concept
my_number = 25
print(my_number)

my_number = my_number + 4
print(my_number)

food = "pasta"
print("I was born in ", x," and my favourite food is "+food)

# Types - int, floats, string, bool
num1 = 1
print(num1)
print(type(num1))
# print(sys.getsizeof(num1))

# Casting
my_num = 5 #int
my_float = float(my_num)
print(my_float)

my_string = "456"
my_int = int(my_string)
print(my_int)

# User Input
user_number = int(input("Enter a number between 1 and 10: "))
print("Your number is ",user_number)
print(type(user_number))
