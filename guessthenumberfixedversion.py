import random # imports a function that cna generate random numbers
# generate a correct to be guessed by our user
# correct_number = 12
correct_number = random.randint(0, 20)

print(f"the right num is {correct_number}")
# take input from the user that will be a number they will be guessing we will store it in a vairbale called usersGuess
 # i give you a dirty coin
# compare that users guess to the correct_number
# if the usersGuess is equal to the correct_number
# line 13-
for number in range(5):
    has_lost = number == 4
    users_guess = input("Guess any number between 0 and 20: ")
    user_guess_int = int(users_guess)
    print("attempt", number + 1)

    if user_guess_int < 0 or user_guess_int > 20:
        print("The number you entered is over input value, please guess a number between 0 and 20.")
    elif user_guess_int == correct_number:
        if (user_guess_int == correct_number):
            print(f"yep i was thinking number {correct_number}, you get R{correct_number}")
        break
    else:
     if not has_lost:
            print(f"Wrong guess, try again! You have {4 - number} attempts left.")


        

if has_lost:
    print(f"Haaaa you owe me R{correct_number}")
# ELSE print to tell the user pay the computer that guess in rands
