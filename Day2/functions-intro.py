# Functions
# function is a block of reusable code that performs a specific task !

# why functions are good:
# 1 makes code cleaner
# 2 stops you repeatedly to write same code (DRY)
# 3 makes code more modular -> reusability, maintainability

# syntax
#def function_name():
#    return something

# simple print
def hello(name):
    print("Hello "+name)

#calling the function
hello("Deepa")

#addition
def add(a,b):
    return a+b

print(add(3,4))

#4. Even or Odd?

#Write a function is_even() that takes a number as input.
#Return "Even" if the number is even, "Odd" if it’s odd.
def is_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(is_even(62))


#5. Word Multiplier function
#Write a function repeat_word(word, times)
#It should return the word repeated times number of times.
def word_multiplier(word,times):
    return word*times

new_word = word_multiplier("Good Afternoon! ", 3)

print(new_word)

#6. Factorial function
#Write a function factorial(n) that calculates the factorial of n.
#Example: factorial(5) → 5 * 4 * 3 * 2 * 1 = 120.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(9))

#7. Default parameters

#Write a function power(base, exponent=2)
#By default, it should square the base.
#If an exponent is provided, use it instead.
def power(base, exponent=2):
    return base ** exponent

num_power = power(8,3)
print("Power of 8 is: ",num_power)