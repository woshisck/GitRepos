# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UE_Sequence_Assemble.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

class Ui_Seq_Assemble(object):
    def setupUi(self, Seq_Assemble):
        if Seq_Assemble.objectName():
            Seq_Assemble.setObjectName(u"Seq_Assemble")
        Seq_Assemble.resize(838, 687)
        icon = QIcon()
        icon.addFile(u"../Download/tubiao.png", QSize(), QIcon.Normal, QIcon.Off)
        Seq_Assemble.setWindowIcon(icon)
        Seq_Assemble.setStyleSheet(u"background-color: rgb(40, 40, 40);")
        self.verticalLayout_2 = QVBoxLayout(Seq_Assemble)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.UE_input_FBX = QWidget(Seq_Assemble)
        self.UE_input_FBX.setObjectName(u"UE_input_FBX")
        self.gridLayout = QGridLayout(self.UE_input_FBX)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.splitter_2 = QSplitter(self.UE_input_FBX)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.splitter = QSplitter(self.splitter_2)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.Ep_list = QListWidget(self.splitter)
        self.Ep_list.setObjectName(u"Ep_list")
        self.Ep_list.setEnabled(True)
        self.Ep_list.setBaseSize(QSize(100, 0))
        self.Ep_list.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(0, 170, 255);")
        self.Ep_list.setSortingEnabled(False)
        self.splitter.addWidget(self.Ep_list)
        self.Sc_list = QListWidget(self.splitter)
        self.Sc_list.setObjectName(u"Sc_list")
        self.Sc_list.setBaseSize(QSize(100, 0))
        self.Sc_list.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(0, 170, 255);")
        self.Sc_list.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.splitter.addWidget(self.Sc_list)
        self.Pt_list = QListWidget(self.splitter)
        self.Pt_list.setObjectName(u"Pt_list")
        self.Pt_list.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(0, 170, 255);")
        self.Pt_list.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.splitter.addWidget(self.Pt_list)
        self.Shot_list = QListWidget(self.splitter)
        self.Shot_list.setObjectName(u"Shot_list")
        self.Shot_list.setBaseSize(QSize(100, 0))
        self.Shot_list.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(0, 170, 255);")
        self.Shot_list.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.splitter.addWidget(self.Shot_list)
        self.splitter_2.addWidget(self.splitter)
        self.File_list = QListWidget(self.splitter_2)
        self.File_list.setObjectName(u"File_list")
        self.File_list.setEnabled(True)
        self.File_list.setMinimumSize(QSize(200, 0))
        self.File_list.setBaseSize(QSize(300, 0))
        self.File_list.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(0, 170, 255);")
        self.File_list.setFrameShape(QFrame.StyledPanel)
        self.File_list.setFrameShadow(QFrame.Sunken)
        self.File_list.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.splitter_2.addWidget(self.File_list)

        self.horizontalLayout_2.addWidget(self.splitter_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Camera = QCheckBox(self.UE_input_FBX)
        self.Camera.setObjectName(u"Camera")
        self.Camera.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(50, 50, 50);")

        self.verticalLayout.addWidget(self.Camera)

        self.Ue_asset = QCheckBox(self.UE_input_FBX)
        self.Ue_asset.setObjectName(u"Ue_asset")
        self.Ue_asset.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(50, 50, 50);")

        self.verticalLayout.addWidget(self.Ue_asset)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.ass_seq = QPushButton(self.UE_input_FBX)
        self.ass_seq.setObjectName(u"ass_seq")
        self.ass_seq.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(50, 50, 50);")

        self.verticalLayout.addWidget(self.ass_seq)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Clear_shot = QCheckBox(self.UE_input_FBX)
        self.Clear_shot.setObjectName(u"Clear_shot")
        self.Clear_shot.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(50, 50, 50);")
        self.Clear_shot.setChecked(False)

        self.horizontalLayout.addWidget(self.Clear_shot)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.Input_ue = QPushButton(self.UE_input_FBX)
        self.Input_ue.setObjectName(u"Input_ue")
        self.Input_ue.setMinimumSize(QSize(0, 30))
        self.Input_ue.setMaximumSize(QSize(100, 30))
        self.Input_ue.setSizeIncrement(QSize(0, 0))
        self.Input_ue.setBaseSize(QSize(0, 0))
        self.Input_ue.setFocusPolicy(Qt.StrongFocus)
        self.Input_ue.setLayoutDirection(Qt.RightToLeft)
        self.Input_ue.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(50, 50, 50);")

        self.horizontalLayout.addWidget(self.Input_ue)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.UE_input_FBX)


        self.retranslateUi(Seq_Assemble)
        self.Ep_list.itemSelectionChanged.connect(Seq_Assemble.Update_sc_list)
        self.Shot_list.itemSelectionChanged.connect(Seq_Assemble.Update_file_list)
        self.Pt_list.itemSelectionChanged.connect(Seq_Assemble.Update_shot_list)
        self.Sc_list.itemSelectionChanged.connect(Seq_Assemble.Update_pt_list)
        self.Input_ue.clicked.connect(Seq_Assemble.Start_assemble)
        self.Camera.clicked.connect(Seq_Assemble.Update_type)
        self.Ue_asset.clicked.connect(Seq_Assemble.Update_type)
        self.ass_seq.clicked.connect(Seq_Assemble.Ass_all_seq)

        QMetaObject.connectSlotsByName(Seq_Assemble)
    # setupUi

    def retranslateUi(self, Seq_Assemble):
        Seq_Assemble.setWindowTitle(QCoreApplication.translate("Seq_Assemble", u"UE_Sequence_Assemble", None))
        self.Camera.setText(QCoreApplication.translate("Seq_Assemble", u"Camera", None))
        self.Ue_asset.setText(QCoreApplication.translate("Seq_Assemble", u"Ue_asset", None))
        self.ass_seq.setText(QCoreApplication.translate("Seq_Assemble", u"Ass_Seq", None))
        self.Clear_shot.setText(QCoreApplication.translate("Seq_Assemble", u"Clear_shot", None))
        self.Input_ue.setText(QCoreApplication.translate("Seq_Assemble", u"Assemble", None))
    # retranslateUi

