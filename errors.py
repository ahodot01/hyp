# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

# print "Welcome to the error program"
#     print "\n"

# ERRORS: 
# Compilation: No parenthesis in both print statements.
# Compilation: Wrong/unexpected indentation.

# Correct one below:

print("Welcome to the error program")
print("\n")

# Variables declaring the user's age, casting the str to an int, and printing the result
#    age_Str == "24 years old" 
#    age = int(age_Str) 
#    print("I'm" + age + "years old.")

# ERRORS:
# Compilation: Unexpected/wrong indentation.
# Compilation: Value age_Str defined, but not correctly for programm to run.
# Compilation: Usage of "==" to perhaps define variable, while it has different purpose.
# Runtime: Textual symbols(and special characters) as a string cannot be converted to integer.
# Runtime: Wrong syntax with wrong type of variable: cannot concatenate integer, only string.

# correct one below:

age_Str = "24" 
age = int(age_Str) 
print("I'm", age,"years old.")

    # Variables declaring additional years and printing the total years of age
#    years_from_now = "3"
#    total_years = age + years_from_now
#
# print "The total number of years:" + "answer_years"

# ERRORS:
# Compilation: Unexpected/wrong indentation.
# Runtime: Cannot "mathematically" add string and integer, conversion needed.
# Compilation: No parenthesis in print statement
# Runtime: Undefined or/and wrong variable "answer_years"
# Compilation: Wrong syntax to print integer.

## There are options to convert type of variable OR use correct syntax for type of variable.

# Correct one below:

years_from_now = int("3")
total_years = age + years_from_now
print("The total number of years:", total_years)

# Variable to calculate the total amount of months from the total amount of years and printing the result
#total_months = total * 12
#print "In 3 years and 6 months, I'll be " + total_months + " months old"

# ERRORS:
# Compilation: No parenthesis in print statement.
# Runtime: Value "total" is not defined. Wrong variable used.
# Compilation: Wrong syntax to concatenate integer in print statement.
# Logical: Perhaps "total_years" (instead of "total") meant to be used from previous task.
# Logical: Extra calculation (inside print statement) added to get... 
# ... 330 months as needed from #HINT and as it says in print statement.

# Correct one below:

total_months = total_years * 12
print("In 3 years and 6 months, I'll be ", total_months + 6," months old")

#HINT, 330 months is the correct answer