# -*- coding: utf-8 -*-
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from view.main_window.Main import Main


class QPlayer(QMainWindow):
    '''223'''
    def __init__(self):
        super().__init__()
        self.ui = Main()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QPlayer()
    window.show()
    sys.exit(app.exec())
