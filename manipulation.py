str_manip = input("Enter a sentence: ")
print(len(str_manip))
print(str_manip.replace(str_manip[-1],"@"))
print(str_manip[-1:-4:-1])
part1 = str_manip[0:3:1]
part2 = str_manip[-2::1]
fiveLetter = part1+part2
print(fiveLetter)
# for test: how are you