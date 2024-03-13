sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog."
print(sentence.replace("!"," "))
sentence = sentence.upper()
print(sentence.replace("!"," "))
sentence = sentence.replace("!"," ").lower().replace("t","T",1)
# sentence = sentence.replace("!", " ")
# sentence = sentence.lower()
# sentence = sentence.replace("t","T",1)
print(sentence[::-1])
