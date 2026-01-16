import yt_dlp
import os
import subprocess
import uuid

RAW_AUDIO_DIR = "data/raw_audio"

os.makedirs(RAW_AUDIO_DIR, exist_ok=True)

def download_youtube_audio(youtube_url: str) -> str:
    """
    Downloads audio from YouTube and converts it to:
    WAV | mono | 16kHz
    Returns absolute path of saved audio file
    """

    audio_id = str(uuid.uuid4())
    temp_file = f"{audio_id}.webm"
    output_wav = os.path.join(RAW_AUDIO_DIR, f"{audio_id}.wav")

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": temp_file,
        "quiet": True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])

    # Convert to WAV (mono, 16kHz)
    subprocess.run([
        "ffmpeg", "-y",
        "-i", temp_file,
        "-ac", "1",
        "-ar", "16000",
        output_wav
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    os.remove(temp_file)
    return output_wav
