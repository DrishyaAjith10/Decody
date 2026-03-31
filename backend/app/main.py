"""
Decody Entry Point

Runs basic NLP pipeline on sample transcript.
"""

from app.ml.nlp import process_text, get_sentences, get_entities


def run():
    text = """
    John will prepare the project report by Friday.
    Sarah needs to finalize the UI design next week.
    We discussed marketing strategies but no final decision was made.
    """

    doc = process_text(text)

    print("---- SENTENCES ----")
    for s in get_sentences(doc):
        print(s)

    print("\n---- ENTITIES ----")
    for e in get_entities(doc):
        print(e)


if __name__ == "__main__":
    run()