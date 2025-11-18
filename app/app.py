import streamlit as st
from src.assistant import SmartAssistAI
from src.utils import save_uploaded_file, format_response

st.set_page_config(
    page_title="SMARTASSIST — Multimodal AI",
    page_icon="🤖",
    layout="centered"
)

ai = SmartAssistAI()

st.title("🤖 SMARTASSIST — Multimodal AI Agent")
st.write("Your capstone project: Text, Image & Audio Understanding in one app.")

# ----------- TEXT INPUT -----------
st.subheader("📝 Text Input")

text_input = st.text_input("Enter your question:")
if st.button("Process Text"):
    output = ai.process_text(text_input)
    st.success(format_response(output))

# ----------- IMAGE INPUT -----------
st.subheader("🖼️ Image Input")

uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    save_path = f"temp/{uploaded_image.name}"
    save_uploaded_file(uploaded_image, save_path)
    st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)

    if st.button("Process Image"):
        result = ai.process_image(save_path)
        st.info(format_response(result))

# ----------- AUDIO INPUT -----------
st.subheader("🎤 Audio Input")

uploaded_audio = st.file_uploader("Upload audio", type=["wav", "mp3", "m4a"])

if uploaded_audio is not None:
    save_path = f"temp/{uploaded_audio.name}"
    save_uploaded_file(uploaded_audio, save_path)
    st.audio(uploaded_audio)

    if st.button("Process Audio"):
        result = ai.process_audio(save_path)
        st.warning(format_response(result))

# Footer
st.write("---")
st.write("Built for Capstone Project • SMARTASSIST Multimodal AI")
