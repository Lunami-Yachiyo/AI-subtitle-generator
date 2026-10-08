import yt_dlp
from pathlib import Path


def main(url: str = "", output_dir: str = "downloads"):
    url = "https://www.youtube.com/watch?v=5HQoswdE6iU"

    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    ydl_opts = {
        # 优先获取最佳音频
        "format": "bestaudio/best",

        # 文件保存格式：
        # downloads/视频标题.扩展名
        "outtmpl": str(output_path / "%(title)s.%(ext)s"),

        # 用 ffmpeg 转换为 mp3
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],

        # 不下载整个播放列表
        "noplaylist": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)

        title = info.get("title", "unknown")
        print(f"下载完成: {title}")
