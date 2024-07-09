# Create a list
my_list = [1, 2, 3, 4, 5]
print("Initial list:", my_list)

# Add an element to the list
my_list.append(6)
print("List after adding an element:", my_list)

# Remove an element from the list
my_list.remove(3)
print("List after removing an element:", my_list)

# Modify an element in the list
my_list[2] = 10
print("List after modifying an element:", my_list)

# Create a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
print("\nInitial dictionary:", my_dict)

# Add a key-value pair to the dictionary
my_dict['d'] = 4
print("Dictionary after adding a key-value pair:", my_dict)

# Remove a key-value pair from the dictionary
del my_dict['b']
print("Dictionary after removing a key-value pair:", my_dict)

# Modify a value in the dictionary
my_dict['c'] = 10
print("Dictionary after modifying a value:", my_dict)


# Initial tuple
my_tuple = (1, 2, 3, 4, 5)
print("Original tuple:", my_tuple)

# Converting tuple to list to add an element
temp_list = list(my_tuple)
temp_list.append(6)
my_tuple = tuple(temp_list)
print("After adding an element:", my_tuple)

# Converting tuple to list to remove an element
temp_list = list(my_tuple)
temp_list.remove(3)
my_tuple = tuple(temp_list)
print("After removing an element:", my_tuple)

# Converting tuple to list to modify an element
temp_list = list(my_tuple)
temp_list[2] = 10  # Modify the third element
my_tuple = tuple(temp_list)
print("After modifying an element:", my_tuple)