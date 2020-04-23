import sys
import os
import unreal
import QtWindowOne
import Core
sys.path.append('C:/Python27/Lib/site-packages')
import PySide
from UE_input_FBX import Ui_UE_input_Dialog



from PySide import QtGui, QtUiTools, QtCore

static_mesh_fbx = 'E:/Asset/StaticMesh/0101.FBX'
skeletal_mesh_fbx = 'E:/Asset/SkeletalMesh/Game/Character/ChenMo_Armour/Meshes/SK_CH_ChenMo_Armour.FBX'

rootpath = os.path.dirname(os.path.abspath(__file__))
UI_Path = rootpath+'\QtWindowOne.ui'


def __QtAppTick__(delta_seconds):
    for window in opened_windows:
        window.eventTick(delta_seconds)


# This function will be called when the application is closing.
def __QtAppQuit__():
    unreal.unregister_slate_post_tick_callback(tick_handle)


# This function is called by the windows when they are closing. (Only if the connection is properly made.)
def __QtWindowClosed__(window=None):
    if window in opened_windows:
        opened_windows.remove(window)

class MainWindow(QtGui.QWidget, Ui_UE_input_Dialog):
    def __init__(self, parent =None):
        QtGui.QWidget.__init__(self,parent)
        self.setupUi(self)
        # self.widget = QtUiTools.QUiLoader().load(UI_Path)
        # self.Ui_UE_input_Dialog.activateWindow()
        # self.UE_input_FBX.show()


    def on_context_menu(self, point):  # 关联右键菜单

        self.popMenu.exec_(self.File_list.mapToGlobal(point))


    def open_file_path(self):  # 打开路径函数

        file_cam = self.File_list.selectedItems()
        path = file_dict[file_cam[0].text()]
        self.model.path_file(path)


    def closeEvent(self, event):  # 关闭窗口时  触发设置保存
        # self.save_set()
        # self.setAttribute(Qt.WA_DeleteOnClose)


    def Open_ue_editor(self):  # 拾取 UE客户端

        # ue_editor_path = QFileDialog.getOpenFileName(self, 'select file', "/", "Exe Files (*.exe);;All Files (*)")
        # self.UE4Editor_path_line.setText(ue_editor_path[0])
        # pass


    def Open_ue_project(self):  # 拾取 ue项目工程文件
        # ue_project_path = QFileDialog.getOpenFileName(self, 'select file', "/", "Exe Files (*.uproject);;All Files (*)")
        # self.UE4Project_path_line.setText(ue_project_path[0])
        # pass
        #

    def Update_ep_list(self):  # 更新集数列表， 在打开软件时直接根据 定义的动画数据路径 获取集数列表
        """
        update ep  list
        """
        # ep_lists, ep_path_dict = self.model.get_ep_list()  # 动画数据跟目录固定在model模块里
        # self.Ep_list.addItems(ep_lists)
        # global ep_dict
        # ep_dict = ep_path_dict
        #

    def Update_sc_list(self):  # 根据集数选择，刷新场次列表
        """
        update sc widget list
        """
        # self.Sc_list.clear()
        # ep_lists_ins = self.Ep_list.selectedItems()
        # ep_path_lists = []
        # for sel_ep in ep_lists_ins:
        #     ep_path_lists.append(ep_dict[sel_ep.text()])
        # ep_sc_lists, sc_path_dict = self.model.get_sc_list(ep_path_lists)
        # ep_sc_lists.sort()
        # self.Sc_list.addItems(ep_sc_lists)
        #
        # global sc_dict
        # sc_dict = sc_path_dict


    def Update_pt_list(self):  # 根据场次选择，刷新次级场次列表

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


    def Update_shot_list(self):  # 根据次级场次选择， 刷新镜头列表
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


    def Update_file_list(self):  # 根据镜头列表选择  刷新镜头内的动画数据
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


    def Check_ue_asset(self):  # 检查ue 资产的功能函数

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


    def Start_input(self):  # 开始导入的 功能函数
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


    def save_set(self):  # 保存页面设置
        """
        save seting
        """
        # set_info = {}
        # set_info["ue_path"] = self.UE4Editor_path_line.text()
        # set_info["project_file"] = self.UE4Project_path_line.text()
        #
        # self.model.save_set_file(set_info)


    def set_preset(self):  # 读取预设
        """
        set preset info
        """
        # set_info = self.model.get_preset()
        # if not set_info == None:
        #     self.UE4Editor_path_line.setText(set_info["ue_path"])
        #     self.UE4Project_path_line.setText(set_info["project_file"])


class QtWindow(QtGui.QWidget):
    def __init__(self, parent= None):
        super(QtWindow, self).__init__()

        self.aboutToClose = None  # This is used to stop the tick when the window is closed
        self.widget = QtUiTools.QUiLoader().load(UI_Path)
        self.setWindowTitle('FbxFactory')
        self.widget.setParent(self)
        self.setGeometry(100, 100, self.widget.width(), self.widget.height())

        self.initializeWidget()

    def closeEvent(self, event):
        if self.aboutToClose:
            self.aboutToClose(self)
        event.accept()

    def eventTick(self, delta_seconds):
        self.myTick(delta_seconds)

    def initializeWidget(self):
        self.time_while_this_window_is_open = 0.0
        self.random_actor = None
        self.random_actor_is_going_up = True

        self.widget.button_MoveRandom.clicked.conncet(self.moveRandomActorInScene)

    def moveRandomActorInScene(self):
        import random
        import WorldFunctions
        all_actors = WorldFunctions.getAllActors(use_selection=False, actor_class=unreal.StaticMeshActor,
                                                 actor_tag=None)
        rand = random.randrange(0, len(all_actors))
        self.random_actor = all_actors[rand]



# class QtWindow(QtGui.QWidget):
#     def __init__(self, parent=None):
#         super(QtWindow, self).__init__(parent)
#         self.aboutToClose = None  # This is used to stop the tick when the window is closed
#         self.widget = QtUiTools.QUiLoader().load(UI_Path)
#         self.widget.setParent(self)
#         self.setGeometry(100, 100, self.widget.width(), self.widget.height())
#


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
def importMyAssets():
    static_mesh_task = buildImportTask(static_mesh_fbx, '/Game/StaticMeshes', SMImportOption())
    skeletal_mesh_task = buildImportTask(skeletal_mesh_fbx, '/Game/StaticMeshes', SkImportOption())
    executeImportTasks([static_mesh_task, skeletal_mesh_task])


# print 'TestRunning'
#
# importMyAssets()

def spawnQtWindow(desired_window_class):
    unreal_app = QtGui.QApplication.instance()
    if not unreal_app:
        unreal_app = QtGui.QApplication(sys.argv)
        tick_handle = unreal.register_slate_post_tick_callback(__QtAppTick__)
        unreal_app.aboutToQuit.connect(__QtAppQuit__)
        existing_windows = {}
        opened_windows = []
        window = existing_windows.get(desired_window_class, None)
        if not window:
            window = desired_window_class()
            existing_windows[desired_window_class] = window
            window.aboutToClose = __QtWindowClosed__
        if window not in opened_windows:
            opened_windows.append(window)
        window.show()
        window.activateWindow()
        return window


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
    main_window = MainWindow()
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





