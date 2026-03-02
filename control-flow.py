# Control flow -> How does a program decide what to do next?
from operator import truediv

# Conditional statements
age = 13

if age >= 18:
    print("You are an official adult")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a child.")


# Comparison and logical operators
age = 25
has_id = True

if age >=18 and has_id:
    print("Entry allowed enjoy the movie")
else:
    print("Entry denied, age restricted below 18")

    # Using 'or'

day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("It's the weekend!")

# Using 'not'

light_on = False

if not light_on:
    print("Turn on the light!")

# Loops - used to iterate over sequence
# for loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("I like "+fruit)

# while loop
num = 1

while num <= 5:
    print(num)
    num += 1

# loops with a range
for i in range(5):
    print(i)



