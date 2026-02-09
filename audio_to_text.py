# audio_to_text.py
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def transcribe_audio(audio_file):
    """
    Converts uploaded audio file to text using GPT-4o transcription
    """
    try:
        transcript = client.audio.transcriptions.create(
            file=audio_file,
            model="gpt-4o-transcribe"
        )
        return transcript.text
    except Exception as e:
        return f"Error: {e}"
