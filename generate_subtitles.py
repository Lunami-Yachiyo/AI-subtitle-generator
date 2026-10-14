from faster_whisper import WhisperModel
from pathlib import Path

def main(file_name : str):
    model = WhisperModel(
        "small",
        device="cpu",
        compute_type="int8"
    )

    segments, info = model.transcribe(
        f"input/{file_name}.mp3",
        language="ja"
    )

    print(f"Detected language: {info.language}")

    Path("output").mkdir(parents=True, exist_ok=True)
    with open(f'output/{file_name}.srt', 'w', encoding="utf-8") as f:

        for idx, segment in enumerate(segments, start=1):
            f.write(
                f"{idx}\n"
                f"{format_time(segment.start)} --> {format_time(segment.end)}\n"
                f"{segment.text}\n\n"
            )

def format_time(seconds):
    ms = round(seconds * 1000)

    hours = ms // 3600000
    ms -= hours * 3600000
    minutes = ms // 60000
    ms -= minutes * 60000
    seconds = ms // 1000
    ms -= seconds * 1000

    return f"{hours:02d}:{minutes:02d}:{seconds:02d},{ms:03d}"