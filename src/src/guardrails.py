import re

def remove_pii(text):
    text = re.sub(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", "[EMAIL]", text)
    text = re.sub(r"\b\d{10}\b", "[PHONE]", text)
    return text
