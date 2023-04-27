# Piece of code to play around with the functionalities of spacy
# Based on https://spacy.io/usage/spacy-101 

import spacy

nlp = spacy.load("en_core_web_sm")
#doc = nlp("Apple is looking at buying U.K. startup for $1 billion")
doc = nlp("Dresden is the capital city of the German state of Saxony and its second most populous city after Leipzig.")

for token in doc:
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
            token.shape_, token.is_alpha, token.is_stop)

print(spacy.explain("nsubj"))