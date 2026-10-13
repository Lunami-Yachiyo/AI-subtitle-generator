from faster_whisper import WhisperModel


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

    for segment in segments:
        print(
            f"[{segment.start:.2f} -> {segment.end:.2f}] "
            f"{segment.text}"
        )
