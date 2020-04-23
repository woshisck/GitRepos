# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UE_input_FBX.ui',
# licensing of 'UE_input_FBX.ui' applies.
#
# Created: Mon Jul 29 18:09:21 2019
#      by: pyside2-uic  running on PySide2 5.12.4
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets


# SetUE4 ->Set_ue4
# SetProject ->Set_project
# CheckAsset -> Check_asset
# Delete ue ani tick ->Delete_ue_ani
# start_button -> Input_ue


class Ui_UE_input_Dialog(object):
    def setupUi(self, UE_input_Dialog):
        UE_input_Dialog.setObjectName("UE_input_Dialog")
        UE_input_Dialog.resize(701, 804)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Download/tubiao.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        UE_input_Dialog.setWindowIcon(icon)
        UE_input_Dialog.setStyleSheet("background-color: rgb(40, 40, 40);")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(UE_input_Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.UE_input_FBX = QtWidgets.QWidget(UE_input_Dialog)
        self.UE_input_FBX.setObjectName("UE_input_FBX")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.UE_input_FBX)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(10)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setObjectName("gridLayout")
        self.UE4Editor_path_line = QtWidgets.QLineEdit(self.UE_input_FBX)
        self.UE4Editor_path_line.setMinimumSize(QtCore.QSize(0, 30))
        self.UE4Editor_path_line.setMaximumSize(QtCore.QSize(16777215, 30))
        self.UE4Editor_path_line.setSizeIncrement(QtCore.QSize(0, 20))
        self.UE4Editor_path_line.setBaseSize(QtCore.QSize(0, 20))
        self.UE4Editor_path_line.setStyleSheet("background-color: rgb(25, 25, 25);\n"
                                               "color: rgb(255, 255, 255);")
        self.UE4Editor_path_line.setObjectName("UE4Editor_path_line")
        self.gridLayout.addWidget(self.UE4Editor_path_line, 0, 0, 1, 1)
        self.Set_ue4 = QtWidgets.QPushButton(self.UE_input_FBX)
        self.Set_ue4.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Set_ue4.sizePolicy().hasHeightForWidth())
        self.Set_ue4.setSizePolicy(sizePolicy)
        self.Set_ue4.setMinimumSize(QtCore.QSize(0, 30))
        self.Set_ue4.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setUnderline(False)
        font.setBold(False)
        self.Set_ue4.setFont(font)
        self.Set_ue4.setToolTipDuration(-1)
        self.Set_ue4.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "background-color: rgb(50, 50, 50);")
        self.Set_ue4.setObjectName("Set_ue4")
        self.gridLayout.addWidget(self.Set_ue4, 0, 1, 1, 1)
        self.UE4Project_path_line = QtWidgets.QLineEdit(self.UE_input_FBX)
        self.UE4Project_path_line.setMinimumSize(QtCore.QSize(0, 30))
        self.UE4Project_path_line.setMaximumSize(QtCore.QSize(16777215, 30))
        self.UE4Project_path_line.setSizeIncrement(QtCore.QSize(0, 20))
        self.UE4Project_path_line.setBaseSize(QtCore.QSize(0, 20))
        self.UE4Project_path_line.setStyleSheet("background-color: rgb(25, 25, 25);\n"
                                                "color: rgb(255, 255, 255);")
        self.UE4Project_path_line.setObjectName("UE4Project_path_line")
        self.gridLayout.addWidget(self.UE4Project_path_line, 1, 0, 1, 1)
        self.Set_project = QtWidgets.QPushButton(self.UE_input_FBX)
        self.Set_project.setMinimumSize(QtCore.QSize(0, 0))
        self.Set_project.setMaximumSize(QtCore.QSize(16777215, 30))
        self.Set_project.setSizeIncrement(QtCore.QSize(0, 0))
        self.Set_project.setBaseSize(QtCore.QSize(0, 0))
        self.Set_project.setStyleSheet("color: rgb(255, 255, 255);\n"
                                       "background-color: rgb(50, 50, 50);")
        self.Set_project.setObjectName("Set_project")
        self.gridLayout.addWidget(self.Set_project, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.splitter_2 = QtWidgets.QSplitter(self.UE_input_FBX)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setHandleWidth(8)
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
        self.File_list.setMinimumSize(QtCore.QSize(0, 0))
        self.File_list.setBaseSize(QtCore.QSize(300, 0))
        self.File_list.setStyleSheet("color: rgb(255, 255, 255);\n"
                                     "selection-background-color: rgb(0, 170, 255);")
        self.File_list.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.File_list.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.File_list.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.File_list.setObjectName("File_list")
        self.gridLayout_2.addWidget(self.splitter_2, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Check_asset = QtWidgets.QPushButton(self.UE_input_FBX)
        self.Check_asset.setMinimumSize(QtCore.QSize(0, 30))
        self.Check_asset.setMaximumSize(QtCore.QSize(100, 30))
        self.Check_asset.setStyleSheet("color: rgb(255, 255, 255);\n"
                                       "background-color: rgb(50, 50, 50);")
        self.Check_asset.setObjectName("Check_asset")
        self.horizontalLayout.addWidget(self.Check_asset)
        self.Delete_ue_ani = QtWidgets.QCheckBox(self.UE_input_FBX)
        self.Delete_ue_ani.setMinimumSize(QtCore.QSize(0, 30))
        self.Delete_ue_ani.setMaximumSize(QtCore.QSize(100, 30))
        self.Delete_ue_ani.setStyleSheet("color: rgb(255, 255, 255);\n"
                                         "font: 10pt \"Alef\";\n"
                                         "background-color: rgb(50, 50, 50);")
        self.Delete_ue_ani.setObjectName("Delete_ue_ani")
        self.horizontalLayout.addWidget(self.Delete_ue_ani)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
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
        self.gridLayout_2.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.gridLayout_2.setRowMinimumHeight(1, 1)
        self.gridLayout_2.setRowStretch(1, 1)
        self.verticalLayout_2.addWidget(self.UE_input_FBX)

        self.retranslateUi(UE_input_Dialog)
        QtCore.QObject.connect(self.Set_project, QtCore.SIGNAL("clicked()"), UE_input_Dialog.Open_ue_project)
        QtCore.QObject.connect(self.Set_ue4, QtCore.SIGNAL("clicked()"), UE_input_Dialog.Open_ue_editor)
        QtCore.QObject.connect(self.Ep_list, QtCore.SIGNAL("itemSelectionChanged()"), UE_input_Dialog.Update_sc_list)
        QtCore.QObject.connect(self.Shot_list, QtCore.SIGNAL("itemSelectionChanged()"),
                               UE_input_Dialog.Update_file_list)
        QtCore.QObject.connect(self.Input_ue, QtCore.SIGNAL("clicked()"), UE_input_Dialog.Start_input)
        QtCore.QObject.connect(self.Check_asset, QtCore.SIGNAL("clicked()"), UE_input_Dialog.Check_ue_asset)
        QtCore.QObject.connect(self.Pt_list, QtCore.SIGNAL("itemSelectionChanged()"), UE_input_Dialog.Update_shot_list)
        QtCore.QObject.connect(self.Sc_list, QtCore.SIGNAL("itemSelectionChanged()"), UE_input_Dialog.Update_pt_list)
        QtCore.QMetaObject.connectSlotsByName(UE_input_Dialog)

    def retranslateUi(self, UE_input_Dialog):
        UE_input_Dialog.setWindowTitle(QtWidgets.QApplication.translate("UE_input_Dialog", "UE4_FBX_INPUT", None, -1))
        self.Set_ue4.setText(QtWidgets.QApplication.translate("UE_input_Dialog", "SetUE4", None, -1))
        self.Set_project.setText(QtWidgets.QApplication.translate("UE_input_Dialog", "SetProject", None, -1))
        self.Ep_list.setSortingEnabled(False)
        self.Check_asset.setWhatsThis(QtWidgets.QApplication.translate("UE_input_Dialog",
                                                                       "<html><head/><body><p>预先检测所选中需要导入UE的FBX文件是否存在相对应的UE4骨架资产，如果缺失相应资产则会导致导入动画失败。</p></body></html>",
                                                                       None, -1))
        self.Check_asset.setText(QtWidgets.QApplication.translate("UE_input_Dialog", "CheckAsset", None, -1))
        self.Delete_ue_ani.setWhatsThis(QtWidgets.QApplication.translate("UE_input_Dialog",
                                                                         "<html><head/><body><p>是否要删除与所选镜头相对应的UE4镜头文件内的动画文件。</p></body></html>",
                                                                         None, -1))
        self.Delete_ue_ani.setText(QtWidgets.QApplication.translate("UE_input_Dialog", "Del_Ue_Ani", None, -1))
        self.Input_ue.setText(QtWidgets.QApplication.translate("UE_input_Dialog", "Start", None, -1))
