userInput1 = int(input("Enter first integer: "))
userInput2 = int(input("Enter second integer: "))
userInput3 = int(input("Enter third integer: "))
inputs_list = [userInput1, userInput2, userInput3]
# list needed as "sum" accepts only 2 arguments (variables) maximum.
print(sum(inputs_list))
print(userInput1 - userInput2)
print(userInput3 * userInput1)
# "int" to round up as an option:
# print(int(sum(inputs_list)/userInput3))
print(sum(inputs_list)/userInput3)