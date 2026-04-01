from app.ml.nlp import process_text
import re

def extract_details(sentence: str):


    who = None
    when = None

    # 🔥 HANDLE "John: ..."
    if ":" in sentence:
        parts = sentence.split(":", 1)
        who = parts[0].strip()
        sentence = parts[1].strip()

    doc = process_text(sentence)

    # 🔥 Extract DATE
    for ent in doc.ents:
        if ent.label_ == "DATE":
            when = ent.text

    # 🔥 Clean WHAT
    what = sentence

    if when:
        what = what.replace(when, "")

    # remove helper words
    what = re.sub(r"\b(will|should|needs to|have to|by)\b", "", what, flags=re.IGNORECASE)

    # 🔥 remove trailing prepositions (VERY IMPORTANT)
    what = re.sub(r"\b(on|at|by|for|to)\s*$", "", what, flags=re.IGNORECASE)

    # normalize spacing
    what = " ".join(what.split()).strip()

    # remove trailing punctuation
    what = what.rstrip(".,!?")

    return {
        "who": who,
        "what": what,
        "when": when
    }