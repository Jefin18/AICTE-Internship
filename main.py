import json
from ingest.youtube_audio import extract_audio_from_youtube
from asr.transcribe import transcribe_audio
from pipeline.event_pipeline import run_event_pipeline

# ===== USER INPUT =====
youtube_url = input("Enter YouTube video URL: ")

audio_path = "data/audio/sample.wav"
transcript_path = "data/transcripts/sample.json"
output_path = "data/outputs/events.json"

# ===== STEP 1: DATA INGESTION =====
print("Extracting audio from YouTube...")
extract_audio_from_youtube(youtube_url, audio_path)

# ===== STEP 2: ASR =====
print("Running speech-to-text...")
segments = transcribe_audio(audio_path, transcript_path)

# ===== STEP 3: ML EVENT DETECTION =====
print("Detecting events...")
events = run_event_pipeline(segments)

# ===== SAVE OUTPUT =====
with open(output_path, "w") as f:
    json.dump(events, f, indent=2)

print("Pipeline completed.")
print("Results saved to:", output_path)
