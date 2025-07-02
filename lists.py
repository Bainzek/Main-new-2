#  lists is  a module for managing lists of items.
# this module provides functions to create, add, remove, and display items in a list.
# lists are used to store multiple items in a single variable
# lists can store different data types, including strings, integers, and other lists
# lists are mutable, meaning you can change their content after creation
# lists can be created using square brackets []
# or the list() constructor
# lists can be empty or contain items
# lists can be indexed, meaning you can access items by their position in the list
# example:
my_list = [1, 2, 3, 4, 5]
print(my_list)
# you can access items in a list using their index
print(my_list[0])  # prints the first item in the list
print(my_list[1])  # prints the second item in the list

# you can also use negative indexing to access items from the end of the list
print(my_list[-1])  # prints the last item in the list

# you can add items to a list using the append() method
my_list.append(6)
print(my_list)  # prints the list after adding an itemS

# you can remove items from a list using the remove() method
my_list.remove(3)
print(my_list)  # prints the list after removing an item

# you can also remove items by their index using the pop() method
my_list.pop(1)  # removes the item at index 1
print(my_list)  # prints the list after removing an item by index
# index 1 is the second item in the list

fruits = ["apple", "banana", "cherry", "strawberry"]
print(fruits[:3])
# slicing a list to get the first three items
print(fruits[1:])  # slicing a list to get all items from index 1 to the end
print(fruits[-2:])  # slicing a list to get the last two items