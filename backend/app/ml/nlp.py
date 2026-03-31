
import spacy 

# Load model once
nlp = spacy.load("en_core_web_sm")


def process_text(text: str):
    return nlp(text)


def get_sentences(doc):
    return [sent.text.strip() for sent in doc.sents]


def get_entities(doc):
    return [(ent.text, ent.label_) for ent in doc.ents]