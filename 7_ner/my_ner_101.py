import spacy
import gradio as gr


nlp = spacy.load("en_core_web_sm") # You need to execute python -m spacy download en_core_web_sm, to be able to use this module

# Code adapted from https://journal.code4lib.org/articles/15405
def ner(sentence):
    doc = nlp(sentence)
    places = [ent for ent in doc.ents if ent.label_ in ['GPE', 'LOC']]

    return places

demo = gr.Interface(fn=ner, inputs="text", outputs="text")
demo.launch()

 
 
