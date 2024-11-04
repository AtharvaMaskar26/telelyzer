import requests
import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
client = OpenAI()

def transcribe_audio(audio_path: str) -> str:
    """
    Description:
        - This function takes the audio_path and returns transcription
    """

    audio_file= open(audio_path, "rb")
    translation = client.audio.translations.create(
    model="whisper-1", 
    file=audio_file
    )
    
    return translation.text
    