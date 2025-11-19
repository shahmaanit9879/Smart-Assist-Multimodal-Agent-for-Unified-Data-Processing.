import time, json, uuid

LOG_FILE = "agent_logs.jsonl"

def log_and_time(agent_name, func, *args):
    trace_id = str(uuid.uuid4())
    start = time.time()

    try:
        result = func(*args)
        status = "success"
    except Exception as e:
        result = {"error": str(e)}
        status = "failed"

    entry = {
        "trace_id": trace_id,
        "agent": agent_name,
        "status": status,
        "duration_ms": round((time.time() - start) * 1000, 2),
    }

    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(entry) + "\n")

    return result
