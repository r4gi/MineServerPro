from PyQt5.QtWidgets import QMainWindow, QStackedWidget
from UI.version_selector import VersionSelector
from UI.folder_selector import FolderSelector

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('MineServerPro')

        # スタックウィジェットの作成と管理
        self.stacked_widget = QStackedWidget(self)
        self.setCentralWidget(self.stacked_widget)

        # 各画面を追加
        self.version_selector = VersionSelector()
        self.folder_selector = FolderSelector()

        self.stacked_widget.addWidget(self.version_selector)
        self.stacked_widget.addWidget(self.folder_selector)

        # ボタンの接続
        self.version_selector.next_button.clicked.connect(self.switch_to_folder_selector)

    def switch_to_folder_selector(self):
        self.stacked_widget.setCurrentWidget(self.folder_selector)
