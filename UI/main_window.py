from PyQt5.QtWidgets import (
    QMainWindow, QLabel, QLineEdit, QSpinBox, QPushButton, QVBoxLayout, QWidget, QFileDialog
)
from PyQt5.QtCore import Qt
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../utils"))
from server_downloader import download_server

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("MineServerPro")
        self.setGeometry(100, 100, 400, 300)

        # メインウィジェット
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # レイアウト
        layout = QVBoxLayout()

        # サーバータイプ選択
        self.server_type_label = QLabel("サーバータイプを選択してください:", self)
        self.server_type_input = QLineEdit(self)  # 入力形式に変更
        self.server_type_input.setPlaceholderText("例: paper または fabric")
        layout.addWidget(self.server_type_label)
        layout.addWidget(self.server_type_input)

        # バージョン入力
        self.version_label = QLabel("バージョンを入力してください:", self)
        self.version_input = QLineEdit(self)  # 入力形式に変更
        self.version_input.setPlaceholderText("例: 1.21")
        layout.addWidget(self.version_label)
        layout.addWidget(self.version_input)

        # RAMサイズ設定
        self.ram_label = QLabel("RAMサイズ (GB) を設定してください:", self)
        self.ram_spinbox = QSpinBox(self)
        self.ram_spinbox.setRange(1, 32)  # 最小1GB、最大32GB
        self.ram_spinbox.setValue(4)  # デフォルト値
        layout.addWidget(self.ram_label)
        layout.addWidget(self.ram_spinbox)

        # フォルダ選択
        self.folder_label = QLabel("保存先フォルダを選択してください:", self)
        self.folder_button = QPushButton("フォルダを選択", self)
        self.folder_button.clicked.connect(self.select_folder)
        layout.addWidget(self.folder_label)
        layout.addWidget(self.folder_button)

        # フォルダパス表示
        self.folder_path_label = QLabel("未選択", self)
        self.folder_path_label.setAlignment(Qt.AlignLeft)
        layout.addWidget(self.folder_path_label)

        # ダウンロードボタン
        self.download_button = QPushButton("サーバーをダウンロード", self)
        self.download_button.clicked.connect(self.start_download)
        layout.addWidget(self.download_button)

        # ステータス表示
        self.status_label = QLabel("", self)
        layout.addWidget(self.status_label)

        # レイアウトを設定
        central_widget.setLayout(layout)

    def select_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "保存先フォルダを選択")
        if folder_path:
            self.folder_path_label.setText(folder_path)
        else:
            self.folder_path_label.setText("未選択")

    def start_download(self):
        server_type = self.server_type_input.text().strip().lower()
        version = self.version_input.text().strip()
        ram_size = self.ram_spinbox.value()
        folder_path = self.folder_path_label.text()

        if not server_type:
            self.status_label.setText("サーバータイプを入力してください。")
            return

        if not version:
            self.status_label.setText("バージョンを入力してください。")
            return

        if folder_path == "未選択":
            self.status_label.setText("フォルダを選択してください。")
            return

        self.status_label.setText("ダウンロード中...")
        self.status_label.repaint()  # ステータスを即座に更新

        # サーバーをダウンロード
        server_file = download_server(server_type, version, folder_path, ram_size)
        if server_file:
            self.status_label.setText(f"サーバーのダウンロードが完了しました: {server_file}")
        else:
            self.status_label.setText("ダウンロードに失敗しました。")
