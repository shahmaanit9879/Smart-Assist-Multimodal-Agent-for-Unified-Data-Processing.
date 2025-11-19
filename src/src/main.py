from agents import CoordinatorAgent
from logger import log_event
from a2a_protocol import A2AProtocol

def run():
    log_event("System started")

    coordinator = CoordinatorAgent()
    a2a = A2AProtocol()

    # Example text processing
    result_text = coordinator.route("This is a sample text")
    print("TEXT RESULT:", result_text)
    log_event(f"TextAgent Output: {result_text}")

    # Example A2A message
    msg = a2a.send("Coordinator", "TextAgent", "Summarize this text")
    print("A2A MESSAGE:", msg)

    # Example image
    result_img = coordinator.route("example_image.png")
    print("IMAGE RESULT:", result_img)
    log_event(f"ImageAgent Output: {result_img}")

if __name__ == "__main__":
    run()
