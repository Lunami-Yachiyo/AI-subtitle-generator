from PySide6.QtWidgets import (
    QWidget, QLineEdit, QPushButton, QVBoxLayout, QLabel, QApplication
)

from PySide6.QtCore import QThread, Signal
import sys
import download_youtube_files

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        # Window
        self.setWindowTitle("YouTube Downloader")
        self.resize(800, 600)

        # Url input
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("Enter URL")

        # Download button
        self.download_button = QPushButton("Download")
        self.download_button.clicked.connect(self.download_youtube_file)

        # Download status
        self.status_label = QLabel("Waiting...")


        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.url_input)
        layout.addWidget(self.download_button)
        layout.addWidget(self.status_label)

        self.setLayout(layout)

        self.worker = None

    def download_youtube_file(self):
        url = self.url_input.text().strip()
        if not url:
            return

        self.status_label.setText("Downloading")
        self.download_button.setEnabled(False)

        # Signals
        self.worker = DownloadWorker(url)
        self.worker.completed.connect(self.download_finished)
        self.worker.failed.connect(self.download_failed)

        # Restart button
        self.worker.finished.connect(
            lambda: self.download_button.setEnabled(True)
        )

        self.worker.start()

    def download_finished(self, title):
        self.status_label.setText(f"Done: {title}")

    def download_failed(self, error):
        self.status_label.setText(f"Error: {error}")

class DownloadWorker(QThread):

    completed = Signal(str)
    failed = Signal(str)

    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        try:
            title = download_youtube_files.main(url=self.url)
            self.completed.emit(title)

        except Exception as e:
            self.failed.emit(str(e))

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())