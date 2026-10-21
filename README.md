# AI Subtitle Generator

Pythonを用いて、動画の音声ダウンロードから音声認識による字幕生成までを行う個人開発プロジェクトです。

*A personal Python project for downloading video audio and generating subtitles using speech recognition.*

> **開発状況：開発中（Work in Progress）**  
> 現在はコマンドラインから音声ダウンロードと字幕生成を実行できます。字幕編集機能は独立したPythonモジュールとして実装しており、GUIは今後の開発予定です。

## 主な機能（Features）

### 1. 音声ダウンロード
- `yt-dlp` を用いて動画の音声をダウンロード
- `FFmpeg` を用いてMP3形式に変換
- ダウンロードしたファイルを `input/` に保存

### 2. 字幕の自動生成
- `faster-whisper` を用いて日本語音声を文字起こし
- 各字幕の開始・終了時刻を付与
- SRT形式の字幕ファイルを `output/` に保存
- 現在の設定：`small` モデル、CPU実行（`int8`）、認識言語は日本語固定

### 3. 字幕編集用モジュール
`subtitle_editor.py` に以下の関数を実装しています。
- 字幕ファイルの読み込み・保存
- テキストの修正
- 隣接する字幕の結合
- 字幕の分割、挿入、削除
- 字幕の表示時刻の変更

**注意：** 字幕編集機能は現時点では通常のコマンドライン実行フローに統合されていません。Pythonコードから関数を呼び出して使用する構成です。

## 使用技術（Tech Stack）

| 分類 | 技術 |
| --- | --- |
| 言語 | Python |
| 音声ダウンロード | yt-dlp |
| 音声認識 | faster-whisper |
| 字幕編集 | pysubs2 |
| 音声変換 | FFmpeg |
| バージョン管理 | Git / GitHub |

## ファイル構成（Project Structure）

```text
AI-subtitle-generator/
├── start.py                   # コマンドラインからの実行
├── download_youtube_files.py  # 音声ダウンロード・MP3変換
├── generate_subtitles.py      # 音声認識・SRT生成
├── subtitle_editor.py         # 字幕編集用関数
├── requirements.txt           # Pythonライブラリ一覧
└── README.md
```

`input/`（音声ファイル）と `output/`（字幕ファイル）は処理実行時に作成されます。

## インストール（Installation）

### 必要な環境
- Python 3
- Git
- FFmpeg（別途インストールし、コマンドラインから使用できるようにしてください）
- 初回モデル取得時のインターネット接続

```bash
git clone https://github.com/Lunami-Yachiyo/AI-subtitle-generator.git
cd AI-subtitle-generator

python -m venv .venv
source .venv/bin/activate  # Linux / macOS
# Windowsの場合: .venv\Scripts\activate

pip install -r requirements.txt
```

FFmpegは `requirements.txt` に含まれていないため、別途導入が必要です。

## 実行方法（Usage）

### 動画URLから字幕を生成

```bash
python start.py --url "https://www.youtube.com/watch?v=VIDEO_ID"
```

`VIDEO_ID` は対象動画のIDに置き換えてください。

処理の流れ：

1. 動画の音声をダウンロードし、MP3に変換
2. `input/` に音声ファイルを保存
3. `faster-whisper` で日本語音声を文字起こし
4. `output/` にSRT字幕ファイルを保存

出力例（ファイル名は動画タイトルによって異なります）：

```text
input/動画タイトル.mp3
output/動画タイトル.srt
```

生成されたSRTファイルは、対応する動画プレーヤーや字幕編集ソフトで確認できます。

## 現時点での制約（Current Limitations）

- 字幕生成の認識言語は日本語に固定しています。
- GUIは未実装で、基本操作はコマンドラインで行います。
- 字幕編集機能は独立したモジュールであり、`start.py` には未統合です。
- 動画の取得可否や音声認識精度は、元動画・実行環境・外部ツールの動作に依存します。
- 動画タイトルやファイル名によっては、保存したMP3のパスを正しく参照できない場合があります。

## 今後の開発予定（Roadmap）

- [ ] PySide6を用いたGUIの追加
- [ ] ダウンロード・字幕生成・編集の操作をひとつの画面に統合
- [ ] 字幕のプレビューと編集操作の改善
- [ ] エラー処理と入力チェックの強化
- [ ] 動作確認・テストの整備

## 開発目的（Motivation）

音声認識技術を実際のソフトウェアとして活用することを目的に、個人で開発しています。機能ごとにPythonモジュールを分割し、処理の流れを整理しながら、継続的な機能追加とコードの改善に取り組んでいます。

## 利用上の注意

動画や音声は、権利者の許諾や利用規約を確認したうえで取り扱ってください。