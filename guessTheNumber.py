import random # imports a function that cna generate random numbers
# generate a correct to be guessed by our user
# correct_number = 12
correct_number = random.randint(0, 20)

print(f"the right num is {correct_number}")
# take input from the user that will be a number they will be guessing we will store it in a vairbale called usersGuess
users_guess = input("Guess any number between 0 and 20: ") # i give you a dirty coin
# compare that users guess to the correct_number
# if the usersGuess is equal to the correct_number
clean_the_coin = int(users_guess)
print(clean_the_coin == correct_number)
for number in range(5):
    print("attempt", number + 1)
   
    if (clean_the_coin == correct_number):
        print(f"yep i was thinking number {correct_number}, you get R{correct_number}")
    break
else:
    print(f"Haaaa you owe me R{correct_number}")
# ELSE print to tell the user pay the computer that guess in rands
