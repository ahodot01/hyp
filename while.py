# took a while to sort this out

number_Inputs = []
count = 0
average = 0

while True:
    input_by_User = input("Please enter a number: ")

    if input_by_User == '-1':    
        if count > 0:            
            average = sum(number_Inputs) / count
            print("You entered '-1' so loop will now stop!")

# limiting variable 'average' to 2 decimals
            print(f"Average number of inputs is: {average:.2f}")

# tried to add this below, but program works without it:
# after calculating average making list empty and counter 0
#           number_Inputs = []
#           count = 0

            break

# count is 0 (lines 33,35) so if "-1" entered, loop skips to "else"
        else:

# loop won't stop if "-1" is the very first input
            print("You entered '-1', but there are no entries to calculate average!")
    try:
        number = int(input_by_User)
        
# adding entries to list ONLY(!) of they are not equal to "-1"
        if number != -1:  
            number_Inputs.append(number) 
            count += 1 
    except ValueError:
        print("Invalid input!")
