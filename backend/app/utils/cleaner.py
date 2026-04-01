import re

def clean_transcript(text: str):

    # remove timestamps like [00:01] or 00:01:23
    text = re.sub(r"\[?\d{1,2}:\d{2}(:\d{2})?\]?", "", text)

    # normalize spaces BUT KEEP NEWLINES
    text = re.sub(r"[ \t]+", " ", text)

    # remove filler words
    fillers = ["um", "uh", "okay", "yeah"]
    for f in fillers:
        text = re.sub(rf"\b{f}\b", "", text, flags=re.IGNORECASE)

    return text.strip()