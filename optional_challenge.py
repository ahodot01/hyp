# Compilation error:

# Not closed parenthesis, violation of syntax rules. 
# Error message: SyntaxError: '(' was never closed

print(("This is compilation error!")
      
# Runtime error:

# Element of list at index 4 doesn't exist. Existent ones are only 0, 1, 2, and 3.
# Error message: IndexError: list index out of range.

runtimeErrors = [1,2,3,6]
error = runtimeErrors[4]

# Logical error:

# Program will run without error messages, but it will give 
# incorrect answer. Average of both number is 15, but because 
# of logical error, which is ignorance of order of mathematical 
# calculations, we will get wrong result (20).

logical1 = 10
logical2 = 20

averageNumber = logical1 + logical2 / 2

print(averageNumber)