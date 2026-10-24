import yt_dlp
from pathlib import Path


def main(url: str, output_path: str = "input"):

    output_path = Path(output_path)
    output_path.mkdir(parents=True, exist_ok=True)

    options = {
        "format": "bestaudio/best",
        "outtmpl": str(output_path / "%(title)s.%(ext)s"),
        "noplaylist": True,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        info = ydl.extract_info(url, download=True)

        title = info.get("title", "unknown")
        print(f"下载完成: {title}")

    return f"{title}"