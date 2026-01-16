from pathlib import Path
import subprocess

FFMPEG_DIR = r"C:\Users\user\Downloads\ffmpeg-8.0.1-essentials_build\ffmpeg-8.0.1-essentials_build\bin"
FFMPEG_EXE = str(Path(FFMPEG_DIR) / "ffmpeg.exe")


def extract_audio_from_youtube(url, output_wav_path):
    """
    Downloads audio from YouTube and converts it to
    16kHz mono WAV for ML processing.
    """

    output_wav_path = Path(output_wav_path)
    output_wav_path.parent.mkdir(parents=True, exist_ok=True)

    # Step 1: Download + extract audio using yt-dlp
    subprocess.run([
        "yt-dlp",
        "-f", "bestaudio",
        "-x",
        "--audio-format", "wav",
        "--ffmpeg-location", FFMPEG_DIR,
        "-o", "temp_audio.%(ext)s",
        url
    ], check=True)

    # At this point, temp_audio.wav EXISTS (as you observed)

    # Step 2: Normalize audio for Whisper
    subprocess.run([
        FFMPEG_EXE,
        "-y",
        "-i", "temp_audio.wav",
        "-ar", "16000",
        "-ac", "1",
        str(output_wav_path)
    ], check=True)

    # Cleanup
    Path("temp_audio.wav").unlink()
    return str(output_wav_path)