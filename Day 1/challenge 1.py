#Use input() to grab a number value from the user and cast it to a float.
#Divide the new float by any number and cast the result to an int.
#Use input() to grab the name of a user and print "Hello [name]!".

float_val = float(input("Please enter float number: "))
int_val = int(float_val / 5)
print(int_val)

user_name =input("Please enter your name: ")
print( "Hello "+user_name)
