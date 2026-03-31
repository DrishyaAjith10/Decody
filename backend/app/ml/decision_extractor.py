import re


def extract_decision(sentence: str):
    sentence_lower = sentence.lower()

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

    if not any(k in sentence_lower for k in keywords):
        return None

    # Try to extract core decision
    decision = sentence

    # Clean phrases
    decision = re.sub(r"(the team|we)\s+(have\s+)?(agreed|decided|concluded)\s+(to)?", "", decision, flags=re.IGNORECASE)

    decision = decision.strip().capitalize()

    return {
        "decision": decision
    }