from src.assistant import SmartAssistAI

app = SmartAssistAI()

# Example API-like usage
def run_demo():
    print("=== API Demo ===")
    data = {
        "text": "AI agents are improving automation.",
        "image_path": "sample.jpg"
    }

    result = app.safe_execute("Analyze the text and image", data)
    print(result)

if __name__ == "__main__":
    run_demo()
