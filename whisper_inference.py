import os
import whisper
from pyannote.audio.pipelines.speaker_diarization import SpeakerDiarization
from pyannote.core import Segment

# Retrieve the Hugging Face authentication token from the environment variables
auth_token = os.getenv("HF_AUTH_TOKEN")

# Load models
diarization_pipeline = SpeakerDiarization.from_pretrained("pyannote/speaker-diarization", use_auth_token=auth_token)

def transcribe_audio(audio_path, model):
    """ Transcribe audio and detect speakers """
    # Transcribe
    result = model.transcribe(audio_path)
    transcription = result["text"]

    # Perform Speaker Diarization
    diarization_result = diarization_pipeline(audio_path)
    
    speaker_segments = []
    for turn, _, speaker in diarization_result.itertracks(yield_label=True):
        speaker_segments.append(f"{speaker}: {turn.start:.2f}s - {turn.end:.2f}s")

    return transcription, speaker_segments
