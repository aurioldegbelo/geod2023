import spacy
import gradio as gr

nlp = spacy.load("en_core_web_sm")

# Code adapted from https://journal.code4lib.org/articles/15405
def ner(sentence):
    doc = nlp(sentence)
    places = [ent for ent in doc.ents if ent.label_ in ['GPE', 'LOC']]

    return places

demo = gr.interface(fn=ner, inputs="text", outputs="text")
demo.launch()

 
 
