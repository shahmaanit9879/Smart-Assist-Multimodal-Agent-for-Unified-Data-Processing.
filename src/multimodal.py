from PIL import Image
import speech_recognition as sr

def process_image_input(image_path):
    """
    Basic image processing.
    Loads an image and returns a success message.
    (You can replace this later with AI image analysis.)
    """
    try:
        img = Image.open(image_path)
        img.verify()   # verifies that file is a valid image
        return "Image loaded successfully. (Add AI vision here)"
    except Exception as e:
        return f"Error processing image: {str(e)}"


def process_audio_input(audio_path):
    """
    Converts speech audio into text using Google's free recognizer.
    Supports WAV, MP3 (Streamlit saves everything as WAV).
    """
    recognizer = sr.Recognizer()

    try:
        with sr.AudioFile(audio_path) as source:
            audio_data = recognizer.record(source)

        text = recognizer.recognize_google(audio_data)
        return f"Transcribed Audio: {text}"

    except Exception as e:
        return f"Error processing audio: {str(e)}"
