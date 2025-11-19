# src/monitoring.py
import time
import json
import uuid
from datetime import datetime
from typing import Any, Callable

LOG_FILE = "agent_logs.jsonl"  # JSON-lines: each line is a JSON object

def _write_log(record: dict):
    """Append a JSON record to the log file (JSONL)."""
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")

def log_event(agent_name: str, event: str, data: Any = None, trace_id: str = None):
    """
    Write a simple event record.
    trace_id optional — include one to group events across a workflow.
    """
    if trace_id is None:
        trace_id = str(uuid.uuid4())
    rec = {
        "ts": datetime.utcnow().isoformat() + "Z",
        "trace_id": trace_id,
        "agent": agent_name,
        "event": event,
        "data_preview": str(data)[:500]
    }
    _write_log(rec)
    return trace_id

def log_and_time(agent_name: str, func: Callable, *args, **kwargs):
    """
    Run func(*args, **kwargs), measure duration, log a structured record,
    and return the function output.
    """
    trace_id = str(uuid.uuid4())
    start = time.time()
    try:
        out = func(*args, **kwargs)
        status = "ok"
    except Exception as e:
        out = {"error": str(e)}
        status = "error"
    duration_ms = round((time.time() - start) * 1000, 2)

    rec = {
        "ts": datetime.utcnow().isoformat() + "Z",
        "trace_id": trace_id,
        "agent": agent_name,
        "event": "call",
        "status": status,
        "duration_ms": duration_ms,
        "output_preview": str(out)[:1000]
    }
    _write_log(rec)
    return out
