def is_decision(sentence: str):
    keywords = [
        "agreed",
        "decided",
        "concluded",
        "finalized",
        "approved",
        "will proceed",
        "we will",
        "plan is",
        "going with"
    ]

    sentence_lower = sentence.lower()

    return any(k in sentence_lower for k in keywords)