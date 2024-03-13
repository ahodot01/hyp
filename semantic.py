import spacy
nlp = spacy.load('en_core_web_sm') # en_core_web_SM

print("")
print("Currently en_core_web_sm is used:")
print("")

tokens = nlp('cat apple monkey banana')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# I noticed: 

# 1. Annoying message in output/terminal, saying:
# UserWarning: [W007] The model you're using has no word vectors loaded, 
# so the result of the Token.similarity method will be based on the tagger, 
# parser and NER, which may not give useful similarity judgements. This may 
# happen if you're using one of the small models, e.g. `en_core_web_sm`, 
# which don't ship with word vectors and only use context-sensitive tensors. 
# You can always add your own word vectors, or use one of the larger models 
# instead if available.
        
# 2. Cat has higher similarity with apple(fruit), than with monkey(animal).
# Banana has higher similarity with monkey(animal), than with apple(fruit).
# ... and so on and on. Very weird output.
        
tokens = nlp('plane car human dolphin')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# Same weird similarities: human("animal") has higher similarity with car, 
# than with dolphin(animal).
        
# -----------------------------------------------------------------------
        
nlpp = spacy.load('en_core_web_md') # en_core_web_MD

print("")
print("Currently en_core_web_md is used:")
print("")

tokens = nlpp('cat apple monkey banana')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

tokens = nlpp('plane car human dolphin')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# "en_core_web_md" option has seems to give legit(closer to reality) outputs of similarity.        
# Noticed, that human and car similarity has NEGATIVE number.
# Noticed, that human has higher similarity with plane, than with dolphin.
        
print("")
print("Currently en_core_web_md (same) is used for Practical Task 2 regarding Movies:")

print("\nRecently you watched Planet Hulk. \n\nIf you liked it, than below is name and \ndescription of movies you may consider \nto watch as well:")

movies = [ "Movie A: \nWhen Hiccup discovers Toothless isn't the only Night Fury, he must \nseek 'The Hidden World', a secret Dragon Utopia before a hired tyrant named Grimmel \nfinds it first.",
           "Movie B: \nAfter the death of Superman, several new people present themselves \nas possible successors.",
           "Movie C: \nA darkness swirls at the center of a world-renowned dance company, \none that will engulf the artistic director, an ambitious young dancer, and a grieving \npsychotherapist. Some will succumb to the nightmare. Others will finally wake up.",
           "Movie D: \nA humorous take on Sir Arthur Conan Doyle's classic mysteries featuring \nSherlock Holmes and Doctor Watson.",
           "Movie E: \n16-year-old girl and her extended family are left reeling after her \ncalculating grandmother unveils an array of secrets on her deathbed.",
           "Movie F: \nIn the last moments of World War II, a young German soldier fighting \nfor survival finds a Nazi captain's uniform. Impersonating an officer, the man quickly \ntakes on the monstrous identity of the perpetrators he is trying to escape from.",
           "Movie G: \nThe world at an end, a dying mother sends her young son on a quest to \nfind the place that grants wishes.",
           "Movie H: \nA musician helps a young singer and actress find fame, even as age and \nalcoholism send his own career into a downward spiral.",
           "Movie I: \nCorporate analyst and single mom, Jen, tackles Christmas with a \nbusiness-like approach until her uncle arrives with a handsome stranger in tow.",
           "Movie J: \nAdapted from the bestselling novel by Madeleine St John, Ladies in \nBlack is an alluring and tender-hearted comedy drama about the lives of a group of department \nstore employees in 1959 Sydney.",
         ]

watched_movie = [ "Will he save their world or destroy it? When the Hulk becomes too dangerous \nfor the Earth, the Illuminati trick Hulk into a shuttle and launch him \ninto space to a planet where the Hulk can live in peace. Unfortunately, \nHulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."
                ]

for token in movies:
    token = nlpp(token)
    for token_ in watched_movie:
        token_ = nlpp(token_)
        if token.similarity(token_) > 0.85: # above 0.85 similarity is advised to watch
            print(f"{token}")

# Couldn't do TITLE ONLY as output. Tried lists and dictionaries. 
# All that didn't work. Waiting for feedback.