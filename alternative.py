# PREVIOUS SUBMISSION

# part 1

text = "Hello World"
text = text.replace("l","L",1).replace("o","O",1).replace("r","R",1).replace("d","D",1)
print(text)
altText = [text[2],text[4],text[8],text[10]]
uppText = "".join(char.upper() if char in altText 
                   else char for char in text)
print(uppText)

# RESUBMISSION

uteXt = ""

for c in range(len(text)):
    if c % 2 == 0:
        uteXt += text[c].upper()
    else:
        uteXt += text[c]
       
print(uteXt)

# PREVIOUS SUBMISSON

# part 2 

texxt = "I am learning to code"
texxtAlt = texxt.replace("am","AM").replace("to","TO")
print(texxtAlt)
texxt2 = texxt.split()
texxt3 = texxt2.pop(1)
texxt4 = texxt2.pop(2)
texxt5 = texxt2.insert(1,texxt3.upper())
texxt5 = texxt2.insert(3,texxt4.upper())
texxt5 = " ".join(texxt2)
print(texxt5)

# RESUBMISSION

ateXt = texxt.split()

for w in range(len(ateXt)):
    if w % 2 != 0:
        ateXt[w] = ateXt[w].upper()

aJoined = " ".join(ateXt) # with " " separator, otherwise "IAMl..."
print(aJoined)