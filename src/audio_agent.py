# src/audio_agent.py
from src.guardrails import check_file_size_bytes

def handle_audio(file_obj):
    try:
        size = getattr(file_obj, "size", 0)
    except Exception:
        size = 0
    ok, err = check_file_size_bytes(size)
    if not ok:
        return {"ok": False, "error": err}
    # Placeholder result
    return {"ok": True, "result": "Audio transcribed successfully"}
