import math
sideofT1 = int(input("Enter length of the first side of triangle: "))
sideofT2 = int(input("Enter length of the second side of triangle: "))
sideofT3 = int(input("Enter length of the third side of triangle: "))
# calculating half of the perimeter of the triangle
halfPerim = (sideofT1+sideofT2+sideofT3)/2
# using triangle area formula used when we know lengths of all sides and half perimeter
areaT = math.sqrt(halfPerim*(halfPerim-sideofT1)*(halfPerim-sideofT2)*(halfPerim-sideofT3))
# optional rounding up to 2 decimal places:
areaT = round(areaT,2)
print("Rounded area of triangle is:", areaT)
