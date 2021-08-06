# This file is to make the lineedit customizable -- This help to clear out the lineedit space after each entry

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QLineEdit

class clickableLineEdit(QLineEdit):
    clicked = pyqtSignal()

    def mousePressEvent(self, event):
        self.clicked.emit()
        QLineEdit.mousePressEvent(self, event)