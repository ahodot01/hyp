time1 = int(input("Swimming: Enter time in minutes: "))
time2 = int(input("Cycling: Enter time in minutes: "))
time3 = int(input("Running: Enter time in minutes: "))
totalT = int(time1+time2+time3)
print("Total Triathlon time is: " + str(totalT) + " minutes.")
if totalT <=100 and totalT > 0:
      print("You are qualified for an award: Provincial Colours!")
elif totalT > 100 and totalT <= 105:
      print("You are qualified for an award: Provincial Half Colours!")
elif totalT > 105 and totalT <= 110:
    print("You are qualified for an award: Provincial Scroll!")
else:
     print("No award")