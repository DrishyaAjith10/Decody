def parse_vtt(text: str):
    import re

    lines = text.split("\n")
    cleaned_lines = []

    for line in lines:
        line = line.strip()

        # remove timestamps
        if re.match(r"\d{2}:\d{2}:\d{2}\.\d{3}", line):
            continue

        if "-->" in line:
            continue

        if not line:
            continue

        if "WEBVTT" in line:
            continue

        # KEEP speaker lines intact
        cleaned_lines.append(line)

    return "\n".join(cleaned_lines)