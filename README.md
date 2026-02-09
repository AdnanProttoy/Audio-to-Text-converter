# Audio to Text Study Helper

A smart, student-focused chatbot built with Streamlit and OpenAI. This tool converts audio lectures into text and provides clear explanations in a mix of Simple English and Simple Bangla.


## Overview
This project is designed specifically for students who want to learn from recorded lectures. Whether the audio is in Hindi, Bangla, or English, the AI transcribes it and acts as a tutor to answer questions based on that content.

##  Live Demo

 -> https://audiototextconvertor.streamlit.app/


## Tech Stack
* Language: Python
* Web Framework: Streamlit
* AI Services: OpenAI API (GPT for logic, Whisper for audio)
* Config: python-dotenv


## Features
* Smart Transcription: Converts speech to text using OpenAI Whisper.
* Multi-lingual Support: Handles various spoken languages including Hindi and Bangla.
* Dual-Language AI: Explains complex topics in a student-friendly English + Bangla format.
* Web Interface: A clean, easy-to-use UI powered by Streamlit.
* Secure: API key handling using environment variables for safety.


## Project Structure
```text
Audio-to-Text-converter/
│
├── app.py              # Main Streamlit UI
├── helper_bot.py       # AI logic and tailored prompts
├── audio_to_text.py    # Transcription engine
├── requirements.txt    # List of dependencies
├── .gitignore          # Keeps secrets safe
└── README.md           # Project documentation
