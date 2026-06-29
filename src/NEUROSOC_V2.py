# SECOND CODE WITH GEMINI AND GROQ AS FALLBACK

import os
import time
import requests
from groq import Groq
from dotenv import load_dotenv

# -------------------------
# Load Environment Variables
# -------------------------

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# -------------------------
# Initialize Groq Client
# -------------------------

groq_client = Groq(api_key=GROQ_API_KEY)

# -------------------------
# Gemini
# -------------------------

def gemini_model(prompt):

    url = (
        "https://generativelanguage.googleapis.com/v1beta/models/"
        f"gemini-2.5-flash:generateContent?key={GEMINI_API_KEY}"
    )

    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": prompt
                    }
                ]
            }
        ]
    }

    print("GENERATING RESPONSE USING GEMINI...\n")

    retries = 2

    for attempt in range(retries):

        try:

            response = requests.post(
                url,
                json=data,
                timeout=15
            )

            if response.status_code == 200:

                result = response.json()

                return result["candidates"][0]["content"]["parts"][0]["text"]

            print(f"Gemini returned {response.status_code}")

            if response.status_code == 429:
                time.sleep(5)
            else:
                time.sleep(2)

        except requests.exceptions.RequestException as e:

            print("Gemini Error:", e)
            time.sleep(2)

    return None


# -------------------------
# Groq
# -------------------------

def groq_model(prompt):

    print("GENERATING RESPONSE USING GROQ...\n")

    try:

        completion = groq_client.chat.completions.create(

            model="llama-3.3-70b-versatile",

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0.2,
            max_completion_tokens=1024,
            top_p=1,
            stream=False
        )

        return completion.choices[0].message.content

    except Exception as e:

        print("Groq Error:", e)

        return None


# -------------------------
# Main Logic
# -------------------------

def main():

    prompt = input("Ask Anything: ")

    response = gemini_model(prompt)

    if response is None:

        print("\nGemini unavailable.")
        print("Switching to Groq...\n")

        response = groq_model(prompt)

    if response is None:

        print("Both AI providers failed.")

    else:

        print("\n========== RESPONSE ==========\n")
        print(response)


if __name__ == "__main__":
    main()

