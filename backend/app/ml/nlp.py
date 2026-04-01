
import spacy 

# Load model once
nlp = spacy.load("en_core_web_sm")


def process_text(text: str):
    return nlp(text)

def split_by_speaker(text: str):
    lines = text.split("\n")
    return [line.strip() for line in lines if line.strip()]

def get_sentences(doc):
    return [sent.text.strip() for sent in doc.sents]


def get_entities(doc):
    return [(ent.text, ent.label_) for ent in doc.ents]