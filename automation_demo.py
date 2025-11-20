import time
from src.assistant import SmartAssistAI

agent = SmartAssistAI()

def scheduled_task():
    print("Running scheduled monitoring task...")
    response = agent.safe_execute("Monitor system health", {})
    print(response)

if __name__ == "__main__":
    for i in range(3):
        scheduled_task()
        time.sleep(2)  # simulate cron timing
