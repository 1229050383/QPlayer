# -*- coding: utf-8 -*-
import sys

from PySide6.QtWidgets import QApplication, QWidget, QMainWindow
from view.Test import Ui_MainWindow


class QPlayer(QMainWindow):
    '''fjskjieskj'''
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QPlayer()
    window.show()
    sys.exit(app.exec())
