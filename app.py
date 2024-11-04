import streamlit as st
import os
import tempfile
from utils import *

# Title
st.title("Multi-File Upload and Processing App")

# File Uploader - Allow multiple audio files
uploaded_files = st.file_uploader("Choose audio files to upload", accept_multiple_files=True, type=["wav", "mp3", "ogg"])

# Check if files are uploaded
if uploaded_files:
    # List to store processed results
    processed_results = []
    
    for uploaded_file in uploaded_files:
        # Process each uploaded audio file as needed (for now, just storing the file name)
        file_name = uploaded_file.name
        file_path = os.path.join("./tempdir", uploaded_file.name)

        with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

        # 1. Transcribe Audio
        transcripts = transcribe_audio(file_path)

        st.write(transcripts)

        st.write(analyze_call(transcripts, script="Hello I hope you are doing great."))
        
        processed_results.append(file_name)
else:
    st.write("Please upload at least one audio file to proceed.")
