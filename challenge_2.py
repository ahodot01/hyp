string_fav=input("Enter your favourite restaurant: ")
int_fav=input("Enter your favourite number: ")
print(string_fav)
print(int_fav)
string_fav=int(string_fav)

# Code works, but...

# Getting error message:
# string_fav=int(string_fav)
#            ^^^^^^^^^^^^^^^
# ValueError: invalid literal for int() with base 10: `...`

# Why?
# I presume it happens because variable is in textual (non-digit) format.