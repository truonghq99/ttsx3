from email.mime import audio
from fileinput import filename
from fastapi import FastAPI, File, UploadFile
import speech_recognition as sr


app = FastAPI()

@app.post("/voice/regconize")
async def create_upload_file(file: UploadFile):
    print(file.filename)
    r = sr.Recognizer()
    with sr.AudioFile(file.file) as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data)
        print(text)
    return {"response": text}