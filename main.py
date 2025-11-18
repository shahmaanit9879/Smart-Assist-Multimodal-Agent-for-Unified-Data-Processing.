from src.assistant import SmartAssistAI

def main():
    ai = SmartAssistAI()

    print("\n🤖 SMARTASSIST — Multimodal AI (Console Mode)\n")
    print("Choose an option:")
    print("1. Text Input")
    print("2. Image Input")
    print("3. Audio Input")
    print("4. Exit")

    while True:
        choice = input("\nEnter your choice (1/2/3/4): ")

        if choice == "1":
            text = input("Enter your text: ")
            result = ai.process_text(text)
            print("👉 Output:", result)

        elif choice == "2":
            image_path = input("Enter image file path: ")
            result = ai.process_image(image_path)
            print("👉 Output:", result)

        elif choice == "3":
            audio_path = input("Enter audio file path: ")
            result = ai.process_audio(audio_path)
            print("👉 Output:", result)

        elif choice == "4":
            print("Exiting... Goodbye!")
            break

        else:
            print("❗ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
