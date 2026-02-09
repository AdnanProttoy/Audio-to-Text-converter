# app.py
import streamlit as st
from helper_bot import get_answer
from audio_to_text import transcribe_audio

# Page config
st.set_page_config(page_title="Audio Study Helper", layout="wide")
st.title("🎧 Audio Study Helper Chatbot")
st.write("Upload an audio file, type your question, and get answers in English & Bangla!")

st.markdown("---")

# Audio Question (Any Language → English+Bangla)
st.subheader("Ask a Question from Audio")
audio_file = st.file_uploader(
    "Upload an audio file (mp3, wav, m4a):", 
    type=["mp3", "wav", "m4a"]
)
audio_question = st.text_input("Type your question about the audio:")

if st.button("Answer Audio Question"):
    if audio_file and audio_question:
        with st.spinner("Transcribing audio..."):
            audio_text = transcribe_audio(audio_file)

        prompt = f"""
        Here is the transcribed text from audio (any language): 
        {audio_text}

        Question: {audio_question}

        Explain the answer in simple English and Bangla.
        """
        answer = get_answer(prompt)
        st.subheader("Answer (English + Bangla):")
        st.write(answer)
    else:
        st.warning("Please upload an audio file and type your question!")
