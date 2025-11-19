# src/guardrails.py
import re
from typing import Tuple

# Simple PII patterns (expand as needed)
PII_PATTERNS = {
    "EMAIL": r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",
    "PHONE": r"\b(?:\+?\d{1,3}[-.\s]?)?(?:\d{2,4}[-.\s]?){1,4}\d{2,4}\b",
    "SSN": r"\b\d{3}-\d{2}-\d{4}\b"
}

def redact_pii(text: str) -> str:
    """
    Replace detected PII with placeholder tokens, e.g. {EMAIL} or {PHONE}.
    Safe default: masking (keeps structure but removes real values).
    """
    if not text:
        return text

    out = text
    for label, pattern in PII_PATTERNS.items():
        out = re.sub(pattern, "{" + label + "}", out)
    return out

def contains_pii(text: str) -> Tuple[bool, dict]:
    """
    Quick check: returns (has_pii, summary_dict)
    summary_dict maps label -> count detected
    """
    found = {}
    for label, pattern in PII_PATTERNS.items():
        matches = re.findall(pattern, text)
        if matches:
            found[label] = len(matches)
    return (len(found) > 0, found)
