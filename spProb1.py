# Perform standard imports:
import spacy
nlp = spacy.load('./spacy-ner-annotator-master/puneethModel')
tokens = nlp("lets look into the price of polo? at amazon.")
print(tokens[0],tokens[1],tokens[2])

for en in tokens.ents:
    print(en.text, en.label_)