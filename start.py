import generate_subtitles
import download_youtube_files

if __name__ == '__main__':
    url = "https://www.youtube.com/watch?v=5HQoswdE6iU"

    file_name = download_youtube_files.main(url=url)
    generate_subtitles.main(file_name=file_name)