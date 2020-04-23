# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QtWindowOne.ui'
#
# Created: Thu Apr 23 19:35:17 2020
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(325, 120)
        Form.setStyleSheet("QWidget#Form {\n"
"    background-color:#262626;\n"
"    color:white;\n"
"}")
        self.verticalLayout_2 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lbl_Title = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbl_Title.setFont(font)
        self.lbl_Title.setStyleSheet("color:white;")
        self.lbl_Title.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_Title.setObjectName("lbl_Title")
        self.verticalLayout_2.addWidget(self.lbl_Title)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white;")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lbl_Seconds = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_Seconds.setFont(font)
        self.lbl_Seconds.setStyleSheet("color: white;")
        self.lbl_Seconds.setObjectName("lbl_Seconds")
        self.horizontalLayout.addWidget(self.lbl_Seconds)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.button_MoveRandom = QtGui.QPushButton(Form)
        self.button_MoveRandom.setObjectName("button_MoveRandom")
        self.verticalLayout_2.addWidget(self.button_MoveRandom)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_Title.setText(QtGui.QApplication.translate("Form", "Window One", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Time While This Window Is Open: ", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_Seconds.setText(QtGui.QApplication.translate("Form", "0 Seconds", None, QtGui.QApplication.UnicodeUTF8))
        self.button_MoveRandom.setText(QtGui.QApplication.translate("Form", "Move Random Actor In Scene", None, QtGui.QApplication.UnicodeUTF8))

