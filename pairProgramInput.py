# Mbuzu
    # the main steps in an application
    # 1. take input from a user - comment, photo, vidoe
    # 2. we process that input - // assign it to the user that created it
    # 3. Store the input // store that input for later use
    # 4. Read it to use it later - viewing the video or the comment the image

    # CRUD
    # C - Create
    # R - Read
    # U - Update
    # D - Delete

# print(f"1 + 1 = {1 + 1}")
# take input from the user/keyboard
num = input('Enter a value you want to double here: ')

# process the information ( we will double the number)
# doubled_num = num * 2 - we wrapped num in a function called int to stop it form concatenate 1+2+3 = 123

doubled_num = int(num) * 2
num_add3 = float(num) + 3

print("My num" + num) # this is called string concatenation
# Read the processed info
print(f"the number you entered is {num}" ) # string interpolation
print(f"after doubling it, the number is {doubled_num}")
print(f"after adding 3 to it as a float, the number is {num_add3}")


my_first_name = input("My first name is: ")
my_last_name = input("My last name is: ")
my_age = input("my age is: ")

print("Hi my " + my_first_name + " my lastname is " + my_last_name + " I am " + my_age + " years old") # the sad thing about concat
print(f"Hi my first name is {my_first_name}, and my last name is {my_last_name}. This year I will be {my_age} years old") # string interpolation