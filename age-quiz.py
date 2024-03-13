age = int(input("Please enter your age: "))
if age >= 40 and age < 65:
    print("You're over the hill.")
elif age >= 65 and age < 100:
    print("Enjoy your retirement!")
elif age < 13 and age > 0:
    print("You qualify fot the kiddie discount.")
elif age == 21:
    print("Congrats on your 21st!")
elif age > 100:
    print("Sorry, tou're dead.")
elif age <= 0:
    print("Error!")
# extra bit: error in case if input is negative integer
else:
    print("Age is but a number.")