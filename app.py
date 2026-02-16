import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import tempfile
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="Audio Language Transcriber", layout="wide")
st.title("🎧 Audio Language Transcriber")
st.write("Upload an audio file and get all the words in the same language as the audio!")

audio_file = st.file_uploader(
    "Upload an audio file (mp3, wav, m4a):",
    type=["mp3", "wav", "m4a"]
)

def transcribe_audio(audio_file):
    # save uploaded file
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(audio_file.read())
        tmp_path = tmp.name

    # Whisper transcription (STABLE)
    with open(tmp_path, "rb") as f:
        transcript = client.audio.transcriptions.create(
            file=f,
            model="whisper-1"
        )

    os.remove(tmp_path)
    return transcript.text

if st.button("Transcribe Audio"):
    if audio_file:
        with st.spinner("Transcribing audio..."):
            text = transcribe_audio(audio_file)

        st.subheader("Full Transcription")
        st.write(text)

        st.download_button(
            "Download as TXT",
            text,
            file_name="transcription.txt"
        )
    else:
        st.warning("Please upload an audio file!")

