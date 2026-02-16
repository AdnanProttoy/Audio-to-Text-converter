import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os
import tempfile

# Load API key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="Audio Transcriber", layout="wide")
st.title("🎧 Audio Language Transcriber")
st.write("Upload an audio file and get all the words in the same language as the audio!")

st.markdown("---")

audio_file = st.file_uploader(
    "Upload an audio file (mp3, wav, m4a):", 
    type=["mp3", "wav", "m4a"]
)

def transcribe_audio_simple(audio_file):
    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(audio_file.read())
        tmp_path = tmp.name

    # Use OpenAI transcription
    with open(tmp_path, "rb") as f:
        transcript = client.audio.transcriptions.create(
            file=f,
            model="gpt-4o-transcribe"
        )
    os.remove(tmp_path)
    return transcript.text

if st.button("Transcribe Audio"):
    if audio_file:
        with st.spinner("Transcribing audio..."):
            text = transcribe_audio_simple(audio_file)
        st.subheader("Full Transcription:")
        st.write(text)

        st.download_button(
            label="Download as TXT",
            data=text,
            file_name="transcription.txt",
            mime="text/plain"
        )
    else:
        st.warning("Please upload an audio file!")
