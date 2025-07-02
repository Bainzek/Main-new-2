# modulo operator %
# its a percentage symbol that gives remainder of a division operation
# example:
10 % 2
# the is no remainder for 2 into 10 therefore answer would be 0
5 % 2
# answer would be 1 bcz 2 goes in twice remainder 1

# task

for i in range(1,30):
    if i % 3 == 0 and i % 5 == 0:
        print(i, "is fiz buz")
    elif i % 3 == 0:
        print(i, "is fiz")
    elif i % 5 == 0:
        print(i, "is buz")
        

    
