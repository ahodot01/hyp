import spacy

nlp = spacy.load('en_core_web_sm')

# EXAMPLES FROM WIKIPEDIA + FROM TASK
gardenpathSentences = ["The complex houses married and single soldiers and their families.",
                       "The horse raced past the barn fell.",
                       "The old man the boat.",
                       "Mary gave the child a Band-Aid.",
                       "That Jill is never here hurts.",
                       "The cotton clothing is made of grows in Mississippi."
                       ]

# ITERATION OVER EACH SENTENCE IN LIST
for sentence in gardenpathSentences:
    doc = nlp(sentence)

# ENTITIES (of any) AND DESCRIPTION (within upper for loop)  
    for ent in doc.ents:
        print(ent.text, ent.start_char, ent.end_char, ent.label_)
    print("\n")

# TOKENS AND TAGS (within upper for loop)
    for token in doc:
        print(token.text, token.pos_)

entity_explanation = spacy.explain("PERSON")
print(f"\nPERSON: {entity_explanation}")

# COMMENT
print("\nRecognizes named individual/s or fictional character/s")
print("Yes, it makes sense. Because it identifies a person or \nindividual mentioned in the text (name/s in this case).")

entity_explanation = spacy.explain("GPE")
print(f"\nGPE: {entity_explanation}")

# COMMENT
print("\nGeopolitical entity, i.e., countries, cities, states.")
print("Yes, it makes sense. Because it identifies a geopolitical \nentity, such as a country or city, mentioned in the \ntext (state in this case).")

print()