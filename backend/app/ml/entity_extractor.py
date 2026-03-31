"""
entity_extractor.py

Extracts structured information (Who, What, When)
from action-item sentences.
"""

from app.ml.nlp import process_text


def extract_details(sentence: str):
    """
    Extract who, what, and when from a sentence.

    Args:
        sentence (str)

    Returns:
        dict
    """

    doc = process_text(sentence)

    who = None
    when = None

    # Extract entities
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            who = ent.text
        elif ent.label_ == "DATE":
            when = ent.text

    # Extract WHAT (basic logic)
    what = sentence

    # Remove who and when from sentence
    if who:
        what = what.replace(who, "").strip()

    if when:
        what = what.replace(when, "").strip()

    # Clean extra words
    what = what.replace("by", "").strip()
    what = what.replace("will", "").strip()
    what = what.replace("needs to", "").strip()

    return {
        "who": who,
        "what": what,
        "when": when
    }