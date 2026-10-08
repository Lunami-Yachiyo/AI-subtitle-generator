from faster_whisper import WhisperModel


def main():
    model = WhisperModel(
        "small",
        device="cpu",
        compute_type="int8"
    )

    segments, info = model.transcribe(
        "sample.mp3",
        language="ja"
    )

    print(f"Detected language: {info.language}")

    for segment in segments:
        print(
            f"[{segment.start:.2f} -> {segment.end:.2f}] "
            f"{segment.text}"
        )
