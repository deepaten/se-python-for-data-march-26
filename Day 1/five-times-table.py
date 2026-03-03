#Extended Multiplication Table Challenge (No Loops)
#Create a multiplication table for the 5X table using only lists and list methods (no loops)
#Find and print the following
#Print the full list
#Remove one value from the list
#insert a number back in the correct place
#Remove the last value
#Print the 5th element
#Find the position of 40 in the list
#Count how many times 5 appears in the list

five_tt = [5]
five_tt.append(10)
five_tt.append(15)
five_tt.extend([20, 25, 30, 35, 40, 45, 50])

print(five_tt)
five_tt.pop(1 ) # removed value from list
print(five_tt)
five_tt.insert(1,10) # inserted value back at correct place
print(five_tt)
five_tt.pop() # last value removed
print(five_tt[4])
pos = five_tt.index(40) # find index of 40
print(pos, " index of 40")
count = five_tt.count(5)  # count how many times 5 appears
print(count)







