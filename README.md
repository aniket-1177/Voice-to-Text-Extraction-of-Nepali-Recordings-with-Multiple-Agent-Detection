# Voice-to-Text Extraction of Nepali Recordings with Multiple Agent Detection

## Project Overview
This project is an AI-powered speech-to-text system that transcribes Nepali customer service calls and identifies multiple speakers. It utilizes Whisper for Automatic Speech Recognition (ASR) and Pyannote for speaker diarization.

## Features
- **Speech-to-Text Transcription**: Converts Nepali speech into text.
- **Speaker Diarization**: Identifies and segments multiple speakers in an audio file.
- **Web Interface**: A simple Flask-based UI for uploading and transcribing audio files.

---

## Project Structure
```
ASR_NEPAL/
│── Dataset/
│   ├── Nepali Speech To Text Dataset/
│   │   ├── audio_chunks/       # Audio files in WAV format
│   │   ├── transcripts/        # Ground truth transcriptions
├── processed_audio/    # Processed audio files
│── static/
│   ├── styles.css             # CSS for styling the web UI
│── templates/
│   ├── index.html             # Upload page
│   ├── result.html            # Display results page
│── uploads/                   # Folder for uploaded files
│── .env                       # Environment variables
│── app.py                     # Flask backend
│── notebook.ipynb             # Jupyter notebook
│── requirements.txt           # Dependencies list
│── transcripts.csv            # Processed transcriptions (from notebook)
│── whisper_inference.py       # Whisper ASR inference script
│── whisper_transcriptions.csv # Output transcriptions (from notebook)
```

---

## Installation & Setup
### Prerequisites
- Python 3.8+
- Virtual environment (recommended)
- FFmpeg installed
- User Access tokens authenticate your identity to the Hugging Face Hub

### Setup Instructions
1. **Clone the repository**
   ```sh
   git clone https://github.com/aniket-1177/Voice-to-Text-Extraction-of-Nepali-Recordings-with-Multiple-Agent-Detection.git
   cd ASR_NEPAL
   ```
2. **Create a virtual environment**
   ```sh
   python -m venv venv
   ```
3. **Activate the virtual environment**   
   ```sh
   venv\Scripts\activate     # On Windows
   ```
4. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```
5. **Set up environment variables** (Create a `.env` file and add API keys)
6. **Run the Flask app**
   ```sh
   python app.py
   ```
7. **Access the Web UI**
   Open `http://127.0.0.1:5000/` in your browser.

---

## Usage
### 1. Upload an Audio File
- Go to the web UI (`index.html`), choose a Nepali audio file, and submit.

### 2. View Transcriptions
- After processing, the transcriptions and speaker labels will be displayed.

### 3. Check Output Files
- `whisper_transcriptions.csv` contains the extracted text.
- `transcripts.csv` stores ground truth transcriptions for evaluation.

---

## Model Details
- **Speech Recognition:** OpenAI's Whisper (large model)
- **Speaker Diarization:** Pyannote-audio

---

## Future Enhancements
- Improve diarization accuracy
- Integrate real-time transcription
- Add a database for storing transcriptions

---

