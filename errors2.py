# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

#animal = Lion
#animal_type = "cub"
#number_of_teeth = 16

#full_spec = "This is a {animal}. It is a {number_of_teeth} and it has {animal_type} teeth"

#print full_spec

# ERRORS:
# Compilation: No parenthesis in print statement
# Runtime: Name "Lion" is not defined. "" must be used to define variable as a string.
# Compilation: Wrong syntax using curly brackets(format) and variables.
# Logical: Wrong order of variables(words) in sentence. It makes no sense.

# Correct one below:

animal = "Lion"
animal_type = "cub"
number_of_teeth = 16

full_spec = "This is a {}. It is a {} and it has {} teeth".format(animal, animal_type, number_of_teeth)

print(full_spec)