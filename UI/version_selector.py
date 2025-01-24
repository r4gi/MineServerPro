from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QComboBox, QPushButton

class VersionSelector(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # サーバーの種類を選択
        self.type_label = QLabel('サーバーの種類を選択:')
        self.type_combo = QComboBox()
        self.type_combo.addItems(['Vanilla', 'Paper', 'Fabric', 'Forge'])

        # サーバーのバージョンを選択
        self.version_label = QLabel('サーバーのバージョンを選択:')
        self.version_combo = QComboBox()
        self.version_combo.addItems(['1.21.0', '1.20.2', '1.19.4', '1.18.2'])

        # 次へボタン
        self.next_button = QPushButton('次へ')

        # レイアウトに追加
        layout.addWidget(self.type_label)
        layout.addWidget(self.type_combo)
        layout.addWidget(self.version_label)
        layout.addWidget(self.version_combo)
        layout.addWidget(self.next_button)

        self.setLayout(layout)
