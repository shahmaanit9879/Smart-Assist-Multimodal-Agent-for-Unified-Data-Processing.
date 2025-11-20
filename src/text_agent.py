# src/text_agent.py
from src.guardrails import check_text_input

def handle_text(text):
    ok, err = check_text_input(text)
    if not ok:
        return {"ok": False, "error": err}
    # Simple processing (placeholder)
    return {"ok": True, "result": "Processed Text: " + text}
