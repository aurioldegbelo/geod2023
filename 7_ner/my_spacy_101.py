# Piece of code to play around with the functionalities of spacy
# Based on https://spacy.io/usage/spacy-101 

import spacy
'''
nlp = spacy.load("en_core_web_sm")
#doc = nlp("Apple is looking at buying U.K. startup for $1 billion")
doc = nlp("Dresden is the capital city of the German state of Saxony and its second most populous city after Leipzig.")
for token in doc:
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
            token.shape_, token.is_alpha, token.is_stop)

print("---------------------------------")

for token in doc:
    print(token.text, token.lemma, token.pos, token.tag, token.dep,
            token.shape, token.is_alpha, token.is_stop)


for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)

print(spacy.explain("nsubj"))



nlp = spacy.load("en_core_web_sm")
# Merge noun phrases and entities for easier analysis
nlp.add_pipe("merge_entities")
nlp.add_pipe("merge_noun_chunks")

TEXTS = [
    "Net income was $9.4 million compared to the prior year of $2.7 million.",
    "Revenue exceeded twelve billion dollars, with a loss of $1b.",
]
for doc in nlp.pipe(TEXTS):
    for token in doc:
        if token.ent_type_ == "MONEY":
            # We have an attribute and direct object, so check for subject
            if token.dep_ in ("attr", "dobj"):
                subj = [w for w in token.head.lefts if w.dep_ == "nsubj"]
                if subj:
                    print(subj[0], "-->", token)
            # We have a prepositional object with a preposition
            elif token.dep_ == "pobj" and token.head.dep_ == "prep":
                print(token.head.head, "-->", token)

'''

nlp = spacy.load("en_core_web_md")
tokens = nlp("dog cat banana afskfsd")

print("----------------------------------")
# https://spacy.io/models/en
print("List of labels available for ner in English")
nlp_en = spacy.load("en_core_web_sm")
ner_en_labels = nlp_en.get_pipe('ner').labels
for label in ner_en_labels: 
    print(label, spacy.explain(label))

print("----------------------------------")
# https://spacy.io/models/de
print("List of labels available for ner in German")
nlp_de = spacy.load('de_core_news_sm')
ner_de_labels = nlp_de.get_pipe('ner').labels
for label in ner_de_labels: 
    print(label, spacy.explain(label))



'''
for token in tokens:
    print(token.text, token.has_vector, token.vector_norm, token.is_oov)


doc1 = nlp("I like salty fries and hamburgers.")
doc2 = nlp("Fast food tastes very good.")

# Similarity of two documents
print(doc1, "<->", doc2, doc1.similarity(doc2))
# Similarity of tokens and spans
french_fries = doc1[2:4]
burgers = doc1[5]
print(french_fries, "<->", burgers, french_fries.similarity(burgers))

#print(tokens[0].text, tokens[0].vector)


text = "It’s official: Apple is the first U.S. public company to reach a $1 trillion market value"

# Process the text
doc = nlp(text)

# Print the document text
print(doc.text)
'''