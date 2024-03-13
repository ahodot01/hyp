# Took 5 days to complete this task. 
# Lots and lots of mistakes fixed and lots and lots of tests made.
# Wish to get a LOT of feedback.

import pandas as pd
import spacy
from spacytextblob import spacytextblob

# loading spacy (sm or md) and adding spacytextblob pipe
nlp = spacy.load('en_core_web_sm')
# nlp = spacy.load('en_core_web_md')
nlp.add_pipe('spacytextblob')

# Loading dataset
def loading(file):
    # To make it look more serious :)
    print("Loading dataset.....")
    # low_memory=False, to prevent low memory warnings (file/dataset is quite big)
    data = pd.read_csv(file, low_memory=False)
    # To make it look more serious :)
    print(f"Number of reviews loaded: {len(data)}.")
    return data

# Preprocessing data (specifically reviews.text column)
def preprocess(data):
    # To make it look more serious :)
    print("Preprocessing data......")
    # Remove missing values: None, NaN, Nonetype
    data.dropna(subset=['reviews.text'], inplace=True)
    # Remove stopwords, punctuation and perform basic text cleaning
    clean_reviews = []
    for review in data['reviews.text']:
        doc = nlp(review)
        clean_review = ' '.join([token.text.lower().strip() for token in doc if not token.is_stop and not token.is_punct])
        clean_reviews.append(clean_review)    
    data['clean_reviews'] = clean_reviews
    # to make it look more serious :)
    print("Preprocessing accomplished!!!!")
    return data

# Analyzing data. "text" is a "single_review" in this context.
def analyze(text):
    doc = nlp(text)
    polarity = doc._.blob.polarity
    # splitting and rounding variables' scores of sentiment instruction
    sent = round(doc._.blob.sentiment[0], 2)
    subj = round(doc._.blob.sentiment[1], 2)
    # Limiting polarity score up to 2 decimals
    print(f"\nPolarity analysis score is: {polarity:.2f}.")
    # Printing out sentiment and subjectivity
    print(f"\nSentiment analysis results: \nSentiment score: {sent}; Subjectivity score: {subj}.")
    # Determining polarity only (can be adjusted: for example, Neutral may be between -0.1 and 0.1)
    if polarity is None:
        return 'Unknown'
    elif polarity > 0:
        return 'Positive'
    elif polarity < 0:
        return 'Negative'
    else:
        return 'Neutral'

#   elif polarity >= -0.1 and <= 0.1:
#       return 'Neutral'

# Other outputs (Positive/Negative) in this case (lines 61,62) must be adjusted as well.

# Main function
def main():
    # Defining source (MUST BE in same workspace folder)
    file = "amazon_product_reviews.csv"
    # Running all the functions (above): loading, preprocess, analyze.
    data = loading(file)
    preprocessed_data = preprocess(data)
    print(preprocessed_data['clean_reviews']) # optional (may limit with .head(), etc.)
    single_review = preprocessed_data.iloc[0]['clean_reviews']
    sentiment = analyze(single_review)
    print(f"\nSentiment of the sample review: {sentiment}.")
    print()

# Executing main function
main()