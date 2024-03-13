givenStars = int(input("Enter a number: "))

# givenStars = 5

# input "5" will output mentioned in task pattern:

# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

## previous attempts, etc.:
## if givenStars % 2 == 0:
##     for i in range(1,givenStars + 1):
##         print("*" * (i - 1))
## else:
##     for i in range(2,givenStars + 1):
##         print("*" * i)

# Below is iteration over sequence from "1" to "user input multiplied by 2, 
# but will not include last iteration (if input is "5", range will be from 1 
# to 9 and 5 x 2 = 10 is not included in range)

for k in range(1, 2 * givenStars):

# Below if, for example, input (givenStars) is "5", then variable numStars, 
# that will be used for printing stars ("*") later, will check if variable 
# "k" (in range from 1 to 9) is lower or equal user input ("5") and if so, 
# then it will store variable numStars equal to variable "k":
 
# 1 is lower or equal than 5 > numStars equals k and equals 1, 
# 2 is lower or equal than 5 > numStars equals k and equals 2,
# 3 is lower or equal than 5 > numStars equals k and equals 3, 
# 4 is lower or equal than 5 > numStars equals k and equals 4, 
# 5 is not lower but equal to 5 > numStars equals k and equals 5,
    
# loop "stops" as condition not met: 6 > 5 (and 6 < 10)
    
# Cause of this, later, it will print 1 star, then 2 stars and so on, ...
# until it reaches 5 stars.
    
    if k <= givenStars:
        numStars = k

# Below, in "opposite" case: variable "k" (in range from 1 to 9) is higher, 
# then user input (6 > 5). Then variable used to print stars ("*") later 
# (numStars) will be euqal to: user input (givenStars) multiplied by 2 and then 
# subtracted by variable "k".

# In case if user input is "5" (givenStars), then variable numStars becomes:
# 2 multiplied by 5 and subtracted by number from range of 1 to 9, which is
# higher, than 5. In our case "else" starts, when "k" is 6.
        
# Cause of this, later, it will print one less star as needed in task, until
# it reaches 1 star.

# 2 * 5 - 6 = 4, numStars becomes 4
# 2 * 5 - 7 = 3, numStars becomes 3
# 2 * 5 - 8 = 2, numStars becomes 2
# 2 * 5 - 9 = 1. numStars becomes 1
        
# loop "stops":
# last iteration in range is not included: 10, which is 5 x 2. 

    else:
        numStars = 2 * givenStars - k

# Below, printing stars "*" multiplied by variable numStars, that was determined
# each iteration of for loop during different value of variable "k" in range
# from 1 to 10, where 10 not included.

    print("*" * numStars)