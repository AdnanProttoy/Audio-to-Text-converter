# app.py
import streamlit as st
from audio_to_text import transcribe_audio

st.set_page_config(page_title="Audio Transcriber", layout="wide")
st.title("🎧 Audio Language Transcriber")
st.write("Upload an audio file and get all the words in the audio language!")

st.markdown("---")

audio_file = st.file_uploader(
    "Upload an audio file (mp3, wav, m4a):", 
    type=["mp3", "wav", "m4a"]
)

if st.button("Transcribe Audio"):
    if audio_file:
        with st.spinner("Transcribing audio..."):
            full_text = transcribe_audio(audio_file)
        st.subheader("Full Transcription:")
        st.write(full_text)
    else:
        st.warning("Please upload an audio file!")

