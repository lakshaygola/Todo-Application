# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(716, 235)
        self.Dialoglabel = QtWidgets.QLabel(Dialog)
        self.Dialoglabel.setGeometry(QtCore.QRect(210, 20, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.Dialoglabel.setFont(font)
        self.Dialoglabel.setAlignment(QtCore.Qt.AlignCenter)
        self.Dialoglabel.setObjectName("Dialoglabel")
        self.newTaskLine = clickableLineEdit(Dialog)
        self.newTaskLine.setText('')
        self.newTaskLine.setGeometry(QtCore.QRect(40, 70, 621, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(14)
        self.newTaskLine.setFont(font)
        self.newTaskLine.setClearButtonEnabled(True)
        self.newTaskLine.setObjectName("newTaskLine")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(390, 110, 271, 61))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addButton = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.addButton.setFont(font)
        self.addButton.setObjectName("addButton")
        self.horizontalLayout.addWidget(self.addButton)
        self.cancelButton = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cancelButton.setFont(font)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Dialoglabel.setText(_translate("Dialog", "Enter new task here"))
        self.addButton.setText(_translate("Dialog", "Add"))
        self.cancelButton.setText(_translate("Dialog", "Cancel"))

from clickableLineEdit import clickableLineEdit
