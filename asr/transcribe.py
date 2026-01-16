import os
import whisper
import json
from pathlib import Path

# 🔴 IMPORTANT: Tell Whisper exactly where ffmpeg is
FFMPEG_DIR = r"C:\Users\user\Downloads\ffmpeg-8.0.1-essentials_build\ffmpeg-8.0.1-essentials_build\bin"
os.environ["PATH"] = FFMPEG_DIR + os.pathsep + os.environ.get("PATH", "")

model = whisper.load_model("medium")

def transcribe_audio(audio_path, output_path):
    result = model.transcribe(audio_path)

    segments = []
    for seg in result["segments"]:
        segments.append({
            "text": seg["text"].strip(),
            "start": seg["start"],
            "end": seg["end"]
        })

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(segments, f, indent=2)

    return segments