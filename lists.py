# Lists - ordered, mutable collections of values. Allows duplicates

trainee_list = ["Abbas", "Deepa", "Lui", "Kojo"]
print(trainee_list[0])
print(trainee_list[-1])
print(trainee_list[:2])
print("here")
print(trainee_list[:3])

# Check if specific value in the list
print("Deepa" in trainee_list) # prints true

# Change elements of list
trainee_list[0] = "Deepa"
print(trainee_list)

# print length of the list
print(len(trainee_list))

# List methods
num_list = [1, 5, 6, 3, 75, 2 ]

# insert 450 at the second element of the list
num_list.insert(2,450)
print(num_list)
num_list.pop()
print(num_list)

num_list.pop(0)
print(num_list)

# sort a list->smallest to largest
num_list.sort()
print(num_list)

# Add element to the end of the list
num_list.append(45)
print(num_list)

# slicing - slice returns a portion of the list from Initial to end at a step size of IndexStep
# syntax of slice List[Initial : End: Indexstep]
my_list = [10, 20, 30, 40, 50, 60, 70]
print(my_list)

#show entire list
print(my_list[::])

print(my_list[0::2])