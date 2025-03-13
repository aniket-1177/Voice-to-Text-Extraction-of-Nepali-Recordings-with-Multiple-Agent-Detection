import os
from flask import Flask, render_template, request, redirect, url_for
import whisper
from whisper_inference import transcribe_audio

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

# Load Whisper model
model = whisper.load_model("large")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        if file:
            file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(file_path)

            # Transcribe & detect speakers
            transcription, speaker_segments = transcribe_audio(file_path, model)

            return render_template("result.html", 
                                   transcription=transcription, 
                                   speaker_segments=speaker_segments)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
