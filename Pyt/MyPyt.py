import sys
import os
import unreal

sys.path.append('C:/Python27/Lib/site-packages')
from ShotPath import Folder_path
from UE_input_FBX import Ui_UE_input_Dialog
from PySide import QtGui, QtUiTools, QtCore

from UE_input_FBX import Ui_UE_input_Dialog
from PySide import QtGui, QtUiTools, QtCore

from PySide.QtGui import QMessageBox
from PySide.QtGui import QFileDialog



static_mesh_fbx = 'E:/Asset/StaticMesh/0101.FBX'
skeletal_mesh_fbx = 'E:/Asset/SkeletalMesh/Game/Character/ChenMo_Armour/Meshes/SK_CH_ChenMo_Armour.FBX'

rootpath = os.path.dirname(os.path.abspath(__file__))
UI_Path = rootpath + '\QtWindowOne.ui'

@unreal.uclass()
class LevelSequenceFactory(unreal.LevelSequence):
    pass

@unreal.uclass()
class EditorUtil(unreal.GlobalEditorUtilityBase):
    pass


@unreal.uclass()
class MaterialEditingLib(unreal.MaterialEditingLibrary):
    pass


@unreal.uclass()
class GetEditorAssetLibrary(unreal.EditorAssetLibrary):
    pass

@unreal.uclass()
class getAssetRegistry(unreal.AssetRegistry):
    pass



class MainWindow(QtGui.QWidget, Ui_UE_input_Dialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        # self.widget = QtUiTools.QUiLoader().load(UI_Path)

        self.activateWindow()
        self.show()
        self.path = Folder_path()

        self.currentPath = ""


    def on_context_menu(self, point):

        self.popMenu.exec_(self.File_list.mapToGlobal(point))
        print "on_context_menu"

    def open_file_path(self):

        # file_cam = self.File_list.selectedItems()
        # path = file_dict[file_cam[0].text()]
        # self.model.path_file(path)
        print "open_file_path"
    def closeEvent(self, event):
        '''
        close window event
        :param event:
        :return:
        '''
        print "closeEvent"
        self.save_set()
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)


    def Open_ue_editor(self):
        '''
        SetUE4 button function binding
        :return: void
        '''
        # ue_editor_path = QFileDialog.getOpenFileName(self, 'select file', "/", "Exe Files (*.exe);;All Files (*)")
        # self.UE4Editor_path_line.setText(ue_editor_path[0])
        # pass
        print "Open_ue_editor"

    def Open_ue_project(self):
        '''
        SetProject button function binding
        :return: void
        '''
        # ue_project_path = QFileDialog.getOpenFileName(self, 'select file', "/", "Exe Files (*.uproject);;All Files (*)")
        # self.UE4Project_path_line.setText(ue_project_path[0])
        # pass
        print "Open_ue_project"

    def Update_ep_list(self):
        """
        update ep  list
        """
        # ep_lists, ep_path_dict = self.model.get_ep_list()
        # self.Ep_list.addItems(ep_lists)
        # global ep_dict
        # ep_dict = ep_path_dict

        ep_lists = self.path.get_ep_list()
        self.Ep_list.addItems(ep_lists)

        # ep_dict = ep_path_dict

    def Update_sc_list(self):
        """
        update sc widget list
        """
        self.Sc_list.clear()
        ep_lists_ins = self.Ep_list.selectedItems()
        self.currentPath="H:/XHQS/Cache/ANI_cache/"+self.Ep_list.currentItem().text()+"/"
        print (self.currentPath)
                           # self.Sc_list.currentItem().text()+"/"+\
                           # self.Pt_list.currentItem().text()+"/"+\
                           # self.Shot_list.currentItem())

        ep_path_lists = []
        # for sel_ep in ep_lists_ins:
        #     ep_path_lists.append(ep_dict[sel_ep.text()])
        # ep_sc_lists, sc_path_dict = self.model.get_sc_list(ep_path_lists)
        # ep_sc_lists.sort()
        # self.Sc_list.addItems(ep_sc_lists)
        #
        # global sc_dict
        # sc_dict = sc_path_dict

        # ep_sc_lists,sc_path_dict = self.path.get_sc_list(ep_path_lists)
        # ep_sc_lists.sort()
        # self.Sc_list.addItem(ep_sc_lists)
        # print self.currentPath
        print "Update_sc_list"

    def Update_pt_list(self):

        # self.Pt_list.clear()
        # sc_lists_ins = self.Sc_list.selectedItems()
        # sc_path_lists = []
        # for sel_sc in sc_lists_ins:
        #     sc_path_lists.append(sc_dict[sel_sc.text()])
        # sc_pt_lists, pt_path_dict = self.model.get_pt_list(sc_path_lists)
        # sc_pt_lists.sort()
        # self.Pt_list.addItems(sc_pt_lists)
        #
        # global pt_dict
        # pt_dict = pt_path_dict
        print "Update_pt_list"

    def Update_shot_list(self):
        """
        update shot widget list
        """

        # self.Shot_list.clear()
        # pt_lists_ins = self.Pt_list.selectedItems()
        # pt_path_lists = []
        # for sel_pt in pt_lists_ins:
        #     pt_path_lists.append(pt_dict[sel_pt.text()])
        # pt_shot_lists, shot_path_dict = self.model.get_shot_list(pt_path_lists)
        # pt_shot_lists.sort()
        # self.Shot_list.addItems(pt_shot_lists)
        #
        # global shot_dict
        # shot_dict = shot_path_dict
        print "Update_shot_list"

    def Update_file_list(self):
        """
        update file widget list
        """
        # self.File_list.clear()
        # shot_lists_ins = self.Shot_list.selectedItems()
        # shot_path_lists = []
        # for sel_shot in shot_lists_ins:
        #     shot_path_lists.append(shot_dict[sel_shot.text()])
        # fbx_file_lists, file_path_dict = self.model.get_fbx_file(shot_path_lists)
        # fbx_file_lists.sort()
        # self.File_list.addItems(fbx_file_lists)
        #
        # global file_dict
        # file_dict = file_path_dict
        print "Update_file_list"

    def Check_ue_asset(self):

        # file_lists_ins = self.File_list.selectedItems()
        #
        # file_path_lists = []
        # for i in file_lists_ins:
        #     file_path_lists.append(file_dict[i.text()])
        #
        # UE4_project = self.UE4Project_path_line.text()
        # ue_lack_list = self.set.check_ue_asset(file_path_lists, UE4_project)
        # if ue_lack_list:
        #
        #     QMessageBox.information(self, "Lack Asset List", "".join(ue_lack_list))
        # else:
        #     QMessageBox.information(self, "Lack Asset List", "No assets missing ! ~")
        QMessageBox.information(self, "Lack Asset List", "No assets missing ! ~")

    def Start_input(self):
        '''
        Start button binding function
        :return: click event
        '''
        # file_lists_ins = self.File_list.selectedItems()
        #
        # file_path_lists = []
        # for i in file_lists_ins:
        #     file_path_lists.append(file_dict[i.text()])
        #
        # UE4_editor = self.UE4Editor_path_line.text()
        # UE4_project = self.UE4Project_path_line.text()
        #
        # is_del_fbx = self.Delete_ue_ani.isChecked()  # Whether to delete the FBX file under the UE import path.
        # if is_del_fbx == True:
        #     self.set.clear_fbx_file(file_path_lists, UE4_project)
        #
        # json_file = self.set.create_json_file(file_path_lists)
        # self.set.do_input_cmd(UE4_editor, UE4_project, json_file)

        print "Button Pressed"

    def save_set(self):
        """
        save seting after close window
        """
        # set_info = {}
        # set_info["ue_path"] = self.UE4Editor_path_line.text()
        # set_info["project_file"] = self.UE4Project_path_line.text()
        #
        # self.model.save_set_file(set_info)
        print "save_set"

    def set_preset(self):
        """
        set preset info
        """
        # set_info = self.model.get_preset()
        # if not set_info == None:
        #     self.UE4Editor_path_line.setText(set_info["ue_path"])
        #     self.UE4Project_path_line.setText(set_info["project_file"])
        print "set_preset"

    def buildImportTask(filename='', destination_path='', options=None):
        task = unreal.AssetImportTask()
        task.set_editor_property('automated', True)
        task.set_editor_property('destination_name', '')
        task.set_editor_property('destination_path', destination_path)
        task.set_editor_property('filename', filename)
        task.set_editor_property('replace_existing', True)
        task.set_editor_property('save', True)
        task.set_editor_property('options', options)
        return task


# tasks: obj List : The import tasks object. You can get them from buildImportTask()
# return: str List : The paths of successfully imported assets


############################ IMPORT ASSET ############################
# def importMyAssets():
#     static_mesh_task = buildImportTask(static_mesh_fbx, '/Game/StaticMeshes', SMImportOption())
#     skeletal_mesh_task = buildImportTask(skeletal_mesh_fbx, '/Game/StaticMeshes', SkImportOption())
#     executeImportTasks([static_mesh_task, skeletal_mesh_task])


# print 'TestRunning'
#
# importMyAssets()


class VolumeSlider(QtGui.QDialog):
    def __init__(self, parent=None):
        super(VolumeSlider, self).__init__(parent)
        self.setWindowTitle("Volume Slider")
        self.slider = QtGui.QSlider()
        self.slider.sliderMoved.connect(self.slider_fn)
        self.slider.setRange(0, 100)
        self.slider.setValue(100)

        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.slider)
        self.setLayout(layout)

        # load the master SoundClass
        # self.master_sound_class = unreal.load_asset(None, name='D:/UE_4.24/Engine/Content/EngineSounds/Master')

    def slider_fn(self):
        volume_float = self.slider.value() / 100.00
        # set the volume to the desired value
        # self.master_sound_class.properties.set_editor_property(name='volume', value=volume_float)


if __name__ == "__main__":
    APP = None
    if not QtGui.QApplication.instance():
        APP = QtGui.QApplication(sys.argv)

    # main_window = QtWindow()
    # main_window.show()
    tempUI = Ui_UE_input_Dialog
    main_window = MainWindow()
    main_window.Update_ep_list()
    main_window.show()

    # print (os.path.dirname(os.path.abspath(__file__)))
    # print(__file__)

    # print type(__name__)
    # print __name__
############################################################################################################

# unreal_app = QtGui.QApplication.instance()
# if not unreal_app:
#     unreal_app = QtGui.QApplication(sys.argv)
#     tick_handle = unreal.register_slate_post_tick_callback(__QtAppTick__)
#     unreal_app.aboutToQuit.connect(__QtAppQuit__)
#     existing_windows = {}
#     opened_windows = []
#
#     window = existing_windows.get(QtWindow, None)
#     if not window:
#         window = QtWindow.QtWindow
#         existing_windows[QtWindow.QtWindow] = window
#         window.aboutToClose = __QtWindowClosed__
#     if window not in opened_windows:
#         opened_windows.append(window)
#     window.show()
#     window.activateWindow()
#     return window
