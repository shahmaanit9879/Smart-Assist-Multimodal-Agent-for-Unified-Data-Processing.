from src.assistant import SmartAssistAI
from src.logger import log_event
from src.a2a_protocol import A2AProtocol


def main():
    print("\n===== SMARTASSIST AI - MULTIMODAL AGENT =====\n")

    # Initialize AI system
    ai = SmartAssistAI()

    # Initialize A2A Protocol (for deployment-style communication)
    protocol = A2AProtocol()

    while True:
        print("\nChoose an option:")
        print("1. Process Text")
        print("2. Process Image")
        print("3. Process Audio")
        print("4. Send Result via A2A Protocol")
        print("5. Exit")

        choice = input("\nEnter choice (1-5): ")

        if choice == "1":
            text = input("\nEnter text: ")
            response = ai.process_text(text)
            print("\n📝 TEXT RESULT:", response)
            log_event("text_processed", response)

        elif choice == "2":
            path = input("\nEnter image path: ")
            response = ai.process_image(path)
            print("\n🖼 IMAGE RESULT:", response)
            log_event("image_processed", response)

        elif choice == "3":
            path = input("\nEnter audio path: ")
            response = ai.process_audio(path)
            print("\n🎧 AUDIO RESULT:", response)
            log_event("audio_processed", response)

        elif choice == "4":
            data = input("\nEnter message to send via A2A: ")
            response = protocol.send(data)
            print("\n📡 SENT VIA A2A:", response)

        elif choice == "5":
            print("\nExiting SmartAssist AI. Goodbye!")
            break

        else:
            print("\nInvalid choice. Try again.")


if __name__ == "__main__":
    main()
