import argparse

import generate_subtitles
import download_youtube_files
import subtitle_editor

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--url")
    args = parser.parse_args()
    url = args.url

    # Download YouTube files
    file_name = download_youtube_files.main(url=url)
    # Generate subtitles
    generate_subtitles.main(file_name=file_name)

def test_subtitle_editor():
    file_name = "枕のPRを頼んだらショートスリーパーだった"
    # Open .srt file
    subs = subtitle_editor.load_subtitles(file_name)

    # Close .srt file
    subtitle_editor.save_subtitles(subs, title=file_name)


if __name__ == '__main__':
    main()
    #test_subtitle_editor()