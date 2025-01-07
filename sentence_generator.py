from deep_translator import GoogleTranslator
from gtts import gTTS
import playsound
import os
import google.generativeai as genai

# get the api key from the .env variable GEMINI_API_KEY using python-dotenv

from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Set up Gemini API (replace with your API key)
genai.configure(api_key=GEMINI_API_KEY)

def generate_sentence():
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content("generate a useful sentence, simple, used in everyday life, that a beginner in english can use")
    return response.text.strip()

def translate_to_hindi(text):
    translator = GoogleTranslator(source='auto', target='hi')
    return translator.translate(text)

def text_to_speech(text, lang='en'):
    tts = gTTS(text=text, lang=lang)
    filename = f"audio_{lang}.mp3"
    tts.save(filename)
    return filename

def main():
    english_sentence = generate_sentence()
    print(f"Generated English sentence: {english_sentence}")
    
    hindi_sentence = translate_to_hindi(english_sentence)
    print(f"Hindi translation: {hindi_sentence}")
    
    english_audio_file = text_to_speech(english_sentence, 'en')
    hindi_audio_file = text_to_speech(hindi_sentence, 'hi')
    
    print("Playing English audio:")
    playsound.playsound(english_audio_file)
    
    print("Playing Hindi audio:")
    playsound.playsound(hindi_audio_file)

if __name__ == "__main__":
    main()
