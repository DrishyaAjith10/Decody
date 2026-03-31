from app.ml.nlp import process_text, get_sentences
from app.ml.action_extractor import filter_action_items


def run():

    print("DECODY STARTED")

    text = """
    John will prepare the project report by Friday.
    Sarah needs to finalize the UI design next week.
    We discussed marketing strategies but no final decision was made.
    The team agreed to revisit the pricing model.
    """

    doc = process_text(text)
    sentences = get_sentences(doc)

    print("---- ALL SENTENCES ----")
    for s in sentences:
        print(s)

    print("---- ACTION ITEMS ----")
    actions = filter_action_items(sentences)

    for a in actions:
        print(a)

if __name__ == "__main__":
    run()