# Piece of code to play around with the functionalities of spacy
# Based on https://spacy.io/usage/spacy-101 

import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Apple is looking at buying U.K. startup for $1 billion")
for token in doc:
    print(token.text, token.pos_, token.dep_, token.shape_)

print(spacy.explain("nsubj"))