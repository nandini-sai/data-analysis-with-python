import os

def clear_terminal():
    # Check the operating system and clear the terminal accordingly
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Unix/Linux/Mac
        os.system('clear')

# Call the function to clear the terminal
clear_terminal()

# Creating a list
my_list = [1, 2, 3, 4, 5]
print("Original list:", my_list)

# Adding an element to the list
my_list.append(6)
print("List after adding an element:", my_list)

# Removing an element from the list
my_list.remove(3)
print("List after removing an element:", my_list)

# Modifying an element in the list
my_list[1] = 10
print("List after modifying an element:", my_list)


# Creating a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
print("\nOriginal dictionary:", my_dict)

# Adding an element to the dictionary
my_dict['d'] = 4
print("Dictionary after adding an element:", my_dict)

# Removing an element from the dictionary
del my_dict['b']
print("Dictionary after removing an element:", my_dict)

# Modifying an element in the dictionary
my_dict['a'] = 10
print("Dictionary after modifying an element:", my_dict)


# Creating a set
my_set = {1, 2, 3, 4, 5}
print("\nOriginal set:", my_set)

# Adding an element to the set
my_set.add(6)
print("Set after adding an element:", my_set)

# Removing an element from the set
my_set.remove(3)
print("Set after removing an element:", my_set)

# Modifying a set element
my_set.discard(4)  # Remove element if present
my_set.add(10)     # Add a new element
print("Set after modifying an element:", my_set)
