# loops are to create repetitions in code
# for loops
for number in range (2):
    print("attempt")

# number is a variable of integer type
# range(5) is a function that generates a sequence of numbers from 0 to 9

for number in range (4):
    print("attempt", number + 1, "of 4 attempts")
# stating number + 1 is to start counting from 1 instead of 0
# range(1, 11) generates numbers from 1 to 10

for number in range (1, 11 , 3):
    print("attempt", number, number * ".")

# break statement helps to stop the loop
# for else statement is used to execute a block of codee when the loop is not broken

success = True
for number in range (3):
    print("attempt",number + 1)
    if (success):
        print("you have won")
        break
    else:
     print("attempt",number + 1, ", you have lost")

