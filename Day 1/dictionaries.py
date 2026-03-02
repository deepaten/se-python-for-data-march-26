# Dictionaries -> Dicts organise data based on key/value pair

# Dicts are mutable and dynamic

# Make a dictionary
my_dictionary = {
    "first_name": "Deepa",
    "last_name": "Tendulkar",
    "address":"Reading"
}
# Get a value from dict
print(my_dictionary["first_name"])
print(my_dictionary["first_name"])
print(my_dictionary["last_name"])

# Change a value in a dict
my_dictionary["address"] = "123 street"
print(my_dictionary["address"])

print(my_dictionary)

# Add new key value pair
my_dictionary["job"] = "president"
print(my_dictionary.values())
print(my_dictionary.keys())

#Get key value pair values
for keys, values in my_dictionary.items():
    print(keys, values)

# Delete key value pair
del my_dictionary["first_name"]
print(my_dictionary)