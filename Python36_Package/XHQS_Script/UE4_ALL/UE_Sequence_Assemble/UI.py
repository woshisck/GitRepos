# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UE_Sequence_Assemble.ui',
# licensing of 'UE_Sequence_Assemble.ui' applies.
#
# Created: Wed Aug  7 14:31:05 2019
#      by: pyside2-uic  running on PySide2 5.12.4
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Seq_Assemble(object):
    def setupUi(self, Seq_Assemble):
        Seq_Assemble.setObjectName("Seq_Assemble")
        Seq_Assemble.resize(838, 687)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Seq_Assemble.setWindowIcon(icon)
        Seq_Assemble.setStyleSheet("background-color: rgb(40, 40, 40);")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Seq_Assemble)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.UE_input_FBX = QtWidgets.QWidget(Seq_Assemble)
        self.UE_input_FBX.setObjectName("UE_input_FBX")
        self.gridLayout = QtWidgets.QGridLayout(self.UE_input_FBX)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.splitter_2 = QtWidgets.QSplitter(self.UE_input_FBX)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.Ep_list = QtWidgets.QListWidget(self.splitter)
        self.Ep_list.setEnabled(True)
        self.Ep_list.setBaseSize(QtCore.QSize(100, 0))
        self.Ep_list.setStyleSheet("color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(0, 170, 255);")
        self.Ep_list.setObjectName("Ep_list")
        self.Sc_list = QtWidgets.QListWidget(self.splitter)
        self.Sc_list.setBaseSize(QtCore.QSize(100, 0))
        self.Sc_list.setStyleSheet("color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(0, 170, 255);")
        self.Sc_list.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.Sc_list.setObjectName("Sc_list")
        self.Pt_list = QtWidgets.QListWidget(self.splitter)
        self.Pt_list.setStyleSheet("color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(0, 170, 255);")
        self.Pt_list.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.Pt_list.setObjectName("Pt_list")
        self.Shot_list = QtWidgets.QListWidget(self.splitter)
        self.Shot_list.setBaseSize(QtCore.QSize(100, 0))
        self.Shot_list.setStyleSheet("color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(0, 170, 255);")
        self.Shot_list.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.Shot_list.setObjectName("Shot_list")
        self.File_list = QtWidgets.QListWidget(self.splitter_2)
        self.File_list.setEnabled(True)
        self.File_list.setMinimumSize(QtCore.QSize(200, 0))
        self.File_list.setBaseSize(QtCore.QSize(300, 0))
        self.File_list.setStyleSheet("color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(0, 170, 255);")
        self.File_list.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.File_list.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.File_list.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.File_list.setObjectName("File_list")
        self.horizontalLayout_2.addWidget(self.splitter_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.Camera = QtWidgets.QCheckBox(self.UE_input_FBX)
        self.Camera.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(50, 50, 50);")
        self.Camera.setObjectName("Camera")
        self.verticalLayout.addWidget(self.Camera)
        self.Ue_asset = QtWidgets.QCheckBox(self.UE_input_FBX)
        self.Ue_asset.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(50, 50, 50);")
        self.Ue_asset.setObjectName("Ue_asset")
        self.verticalLayout.addWidget(self.Ue_asset)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Clear_shot = QtWidgets.QCheckBox(self.UE_input_FBX)
        self.Clear_shot.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(50, 50, 50);")
        self.Clear_shot.setChecked(True)
        self.Clear_shot.setObjectName("Clear_shot")
        self.horizontalLayout.addWidget(self.Clear_shot)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.Input_ue = QtWidgets.QPushButton(self.UE_input_FBX)
        self.Input_ue.setMinimumSize(QtCore.QSize(0, 30))
        self.Input_ue.setMaximumSize(QtCore.QSize(100, 30))
        self.Input_ue.setSizeIncrement(QtCore.QSize(0, 0))
        self.Input_ue.setBaseSize(QtCore.QSize(0, 0))
        self.Input_ue.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.Input_ue.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.Input_ue.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(50, 50, 50);")
        self.Input_ue.setObjectName("Input_ue")
        self.horizontalLayout.addWidget(self.Input_ue)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.UE_input_FBX)

        self.retranslateUi(Seq_Assemble)
        QtCore.QObject.connect(self.Ep_list, QtCore.SIGNAL("itemSelectionChanged()"), Seq_Assemble.Update_sc_list)
        QtCore.QObject.connect(self.Shot_list, QtCore.SIGNAL("itemSelectionChanged()"), Seq_Assemble.Update_file_list)
        QtCore.QObject.connect(self.Pt_list, QtCore.SIGNAL("itemSelectionChanged()"), Seq_Assemble.Update_shot_list)
        QtCore.QObject.connect(self.Sc_list, QtCore.SIGNAL("itemSelectionChanged()"), Seq_Assemble.Update_pt_list)
        QtCore.QObject.connect(self.Input_ue, QtCore.SIGNAL("clicked()"), Seq_Assemble.Start_assemble)
        QtCore.QObject.connect(self.Camera, QtCore.SIGNAL("clicked()"), Seq_Assemble.Update_type)
        QtCore.QObject.connect(self.Ue_asset, QtCore.SIGNAL("clicked()"), Seq_Assemble.Update_type)
        QtCore.QMetaObject.connectSlotsByName(Seq_Assemble)

    def retranslateUi(self, Seq_Assemble):
        Seq_Assemble.setWindowTitle(QtWidgets.QApplication.translate("Seq_Assemble", "UE_Sequence_Assemble", None, -1))
        self.Ep_list.setSortingEnabled(False)
        self.Camera.setText(QtWidgets.QApplication.translate("Seq_Assemble", "Camera", None, -1))
        self.Ue_asset.setText(QtWidgets.QApplication.translate("Seq_Assemble", "Ue_asset", None, -1))
        self.Clear_shot.setText(QtWidgets.QApplication.translate("Seq_Assemble", "Clear_shot", None, -1))
        self.Input_ue.setText(QtWidgets.QApplication.translate("Seq_Assemble", "Assemble", None, -1))

