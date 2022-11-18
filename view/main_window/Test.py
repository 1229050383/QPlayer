# -*- coding: utf-8 -*-

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect)
from PySide6.QtWidgets import (QMenuBar, QPushButton,
                               QStatusBar, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, main):
        if not main.objectName():
            main.setObjectName(u"QPlayer")
        main.resize(800, 600)
        self.centralwidget = QWidget(main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(180, 70, 75, 24))
        main.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(main)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        main.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(main)
        self.statusbar.setObjectName(u"statusbar")
        main.setStatusBar(self.statusbar)

        self.retranslateUi(main)

        QMetaObject.connectSlotsByName(main)

    # setupUi

    def retranslateUi(self, main):
        main.setWindowTitle(QCoreApplication.translate("main", u"QPlayer", None))
        self.pushButton.setText(QCoreApplication.translate("main", u"PushButton", None))
    # retranslateUi
