# audio_to_text.py
import os
import tempfile
from openai import OpenAI
from pydub import AudioSegment
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def transcribe_audio(audio_file):
    # Save uploaded audio to temp file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        audio = AudioSegment.from_file(audio_file)
        audio = audio.set_channels(1).set_frame_rate(16000)
        audio.export(tmp.name, format="wav")
        temp_audio_path = tmp.name

    # Split audio into 30-second chunks
    chunk_length_ms = 30 * 1000
    chunks = []

    audio = AudioSegment.from_wav(temp_audio_path)
    for i in range(0, len(audio), chunk_length_ms):
        chunk = audio[i:i + chunk_length_ms]
        chunk_file = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
        chunk.export(chunk_file.name, format="wav")
        chunks.append(chunk_file.name)

    # Transcribe each chunk
    full_text = ""
    for chunk_path in chunks:
        with open(chunk_path, "rb") as f:
            transcript = client.audio.transcriptions.create(
                file=f,
                model="gpt-4o-transcribe"  # audio → text
            )
            full_text += transcript.text + " "

        os.remove(chunk_path)

    os.remove(temp_audio_path)

    return full_text.strip()
