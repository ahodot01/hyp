import math
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan")
print("")
userChoice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()
# userChoice = userChoice.lower()
print("Your choice is", userChoice)
while True:
    if userChoice == "investment":
        depAmount = int(input("Enter the amount of money to deposit: "))
        intRate = float(input("Enter the interest rate (without %): "))
        years = int(input("Enter the number of years: "))
        interest = str(input("Enter 'Simple' or 'Compund': ")).lower()
#       interest = interest.lower()
        if interest == "simple":
            sInt = depAmount * (1 + (intRate/100) * years)
            print("Simple interest amount will be: £",round(sInt,2))
            break
        else:
            cInt = depAmount * math.pow((1 + (intRate/100)),years)
            print("Compund interest will be: £",round(cInt,2))
            break
    elif userChoice == "bond":
        houseV = int(input("Enter the value of the house: "))
        intRate = float(input("Enter the interest rate (without %): "))
        months = int(input("Enter the number of months you plan to repay the bond: "))
        repayment = int((((intRate/100)/12) * houseV) / 1 - (1 + ((intRate/100)/12)) ** - months)
        print("Monthly repayment amount will be: £",repayment)
        break
    else:
        userChoice = input("Error! Please enter either 'investment' or 'bond': ").lower()
        print("Your choice is", userChoice)
#       userChoice = userChoice.lower() 

# as a bonus it is possible to check each input 
# for mistakes and if they are within certain range
# using more while loops, operators (<, >, !=, and, etc.)
# and also .isintance and .lower method/s. 

# Took a while to create proper error checking loop :)
        