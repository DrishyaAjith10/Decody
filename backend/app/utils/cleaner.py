import re


def clean_transcript(text: str):
    """
    Basic transcript cleaning
    """

    # 🔹 remove timestamps [00:01], (00:01:23)
    text = re.sub(r"\[?\d{1,2}:\d{2}(:\d{2})?\]?", "", text)

    # 🔹 remove speaker labels (e.g., "John:", "Speaker 1:")
    text = re.sub(r"\b[A-Z][a-z]+:\s*", "", text)

    # 🔹 remove extra spaces/newlines
    text = re.sub(r"\s+", " ", text)

    # 🔹 remove filler noise words (optional, light touch)
    fillers = ["um", "uh", "okay", "yeah"]
    for f in fillers:
        text = re.sub(rf"\b{f}\b", "", text, flags=re.IGNORECASE)

    return text.strip()