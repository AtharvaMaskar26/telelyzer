from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import os
import shutil
from pydantic import BaseModel

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

UPLOAD_FOLDER = './tempdir'
ALLOWED_EXTENSIONS = {'wav', 'mp3', 'ogg'}

# Create upload folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename: str) -> bool:
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def transcribe_audio(file_path: str) -> str:
    # Placeholder function for audio transcription
    # Replace this with your actual transcription logic
    return f"Transcription for {file_path}"

def analyze_call(transcript: str, script: str) -> str:
    # Placeholder function for call analysis
    # Replace this with your actual analysis logic
    return f"Analysis of transcript: {transcript} compared to script: {script}"

class FileAnalysisResult(BaseModel):
    fileName: str
    transcript: str
    analysis: str

@app.get("/")
def hello():
    return "hello"

@app.post("/upload", response_model=List[FileAnalysisResult])
async def upload_files(files: List[UploadFile] = File(...)):
    if not files:
        raise HTTPException(status_code=400, detail="No files uploaded")

    results = []

    for file in files:
        if file and allowed_file(file.filename):
            file_path = os.path.join(UPLOAD_FOLDER, file.filename)
            
            # Save the file
            with open(file_path, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)

            # Process the file
            transcript = transcribe_audio(file_path)
            analysis = analyze_call(transcript, "Hello I hope you are doing great.")

            results.append(FileAnalysisResult(
                fileName=file.filename,
                transcript=transcript,
                analysis=analysis
            ))

            # Clean up: remove the temporary file
            os.remove(file_path)
        else:
            raise HTTPException(status_code=400, detail=f"File {file.filename} has an invalid extension")

    return results

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)