# PSEUDOCODE
# request input of Name
# store input in variable called "name"
# request input of Age
# store input in variable called "age"
# request input of house number
# store input in variable called "houseNumber"
# request input of street
# store input in variable called "streetName"
# output string which inlcudes variables "name", "age", "houseNumber", ...
# ... and "streetName" with additional words making it loook like an ...
# ... appropriate sentence.

name = input("Name: ")
age = input("Age: ")
houseNumber = input("House Number: ")
streetName = input("Street name (... street/road/way): ")
print("This is " + name + ". He is " + age + 
      " years old and lives at house number " + 
      houseNumber + " on " + streetName + ".")
