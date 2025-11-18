from assistant import SmartAssistAI

def main():
    ai = SmartAssistAI()

    print("\n====================================")
    print("   SMARTASSIST – CLI TEXT MODE")
    print("====================================\n")
    print("Type your message and press ENTER.")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        response = ai.process_text(user_input)
        print("AI:", response)

if __name__ == "__main__":
    main()
