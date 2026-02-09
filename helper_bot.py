# helper_bot.py
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# System prompt
SYSTEM_PROMPT = """
You are a Study Helper AI.

Rules:
1. Always understand the user's input text, no matter the original language (Hindi, Bangla, etc.).
2. Respond in both:
   - Simple English
   - Simple Bangla
3. If the input is not in English or Bangla, translate it first before explaining.
4. Be clear, beginner-friendly, and provide examples if possible.
5. Focus on educational explanations suitable for students.
"""

def get_answer(user_prompt: str) -> str:
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.6,
            max_tokens=400
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {e}"

