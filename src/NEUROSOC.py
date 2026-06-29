import requests
import json
import time

use_gemini = True

def GEMINI_MODEL():
    API_KEY = "AIzaSyCv9gKEtOkfNtD4xkOctXMNYk9GgaOzZiM"
    global prompt
    global use_gemini
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"
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
    i = 0
    print("GENERATING RESPONSE USING GEMINI MODEL...")
    success = False

    while i < 2:
        try:
            response = requests.post(url, json=data, timeout = 15)

            status = response.status_code
            if status == 200:
                a = response.text
                read_text = json.loads(a)
                #print(read_text)
                print(read_text['candidates'][0]['content']['parts'][0]['text'])
                success = True
                break
            else:
                print('Gemini failed with status code' , status , 'trying once again')
                time.sleep(2)
        except requests.exceptions.ReadTimeout:
            print('Gemini failed due to timeout... Trying once more...')
        
        i += 1
        time.sleep(3)
    use_gemini = success

def OLLAMA_MODEL():
    global prompt
    response = requests.post(
        "http://localhost:11434/api/generate",
        json = {
            'model' : 'llama3',
            'prompt' : prompt,
            'stream' : False
        }
    )
    print(response.status_code)
    print(response.json()['response'])

prompt = input('Ask Anything!')

def USE_LOGIC():
    GEMINI_MODEL()
    if not use_gemini:
        print("Falling back to Ollama model...")
        print('GENERATING RESPONSE USING OLLAMA MODEL...')
        OLLAMA_MODEL()
    else:
        pass

USE_LOGIC()

