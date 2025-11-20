# src/guardrails.py
def check_text_input(text):
    if text is None:
        return False, "No text provided"
    if not isinstance(text, str):
        return False, "Text must be a string"
    if len(text.strip()) == 0:
        return False, "Text is empty"
    return True, ""

def check_file_size_bytes(size_bytes, max_mb=10):
    max_bytes = max_mb * 1024 * 1024
    if size_bytes > max_bytes:
        return False, f"File too large. Max {max_mb} MB"
    return True, ""
