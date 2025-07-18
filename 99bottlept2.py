i = 1
for i in range(99 , -1 , -1):
    if i == 1:
        print(f"{i} bottle of beer on the wall, {i} botttle of bear")
        print(f"Take one doen pass it around,no more bottles of bear on the wall.")
    elif i == 0:
        print("No more bottles of bear on the wall, no more bottles of bear.")
        print("Go to the store and buy some more, 99 bottles of bear on the wall.")
    else:
        print(f"{i} bottles of bear on the wall,{i} bottles of bear")
        print(f"Take one down, pass it around, {i} bottles of bear on the wall.")
