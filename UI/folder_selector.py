from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog

class FolderSelector(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # フォルダ選択関連のUI
        self.folder_label = QLabel('サーバー配置フォルダを選択:')
        self.folder_input = QLineEdit()
        self.browse_button = QPushButton('参照')
        self.browse_button.clicked.connect(self.browse_folder)

        # レイアウトに追加
        layout.addWidget(self.folder_label)
        layout.addWidget(self.folder_input)
        layout.addWidget(self.browse_button)

        self.setLayout(layout)

    def browse_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, 'フォルダを選択')
        if folder_path:
            self.folder_input.setText(folder_path)
