import sys

import unreal

sys.path.append('C:/Python27/Lib/site-packages')
import PySide

from PySide import QtGui, QtUiTools, QtCore

static_mesh_fbx = 'E:/Asset/StaticMesh/0101.FBX'
skeletal_mesh_fbx = 'E:/Asset/SkeletalMesh/Game/Character/ChenMo_Armour/Meshes/SK_CH_ChenMo_Armour.FBX'

UI_Path = 'D:/Python_Project/Pyt/QtWindowOne.ui'


def __QtWindowClosed__(window=None):
    if window in opened_windows:
        opened_windows.remove(window)


class MainWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.aboutToClose = None  # This is used to stop the tick when the window is closed
        self.widget = QtUiTools.QUiLoader().load(UI_Path)
        self.widget.setParent(self)

        self.setGeometry(100, 100, self.widget.width(), self.widget.height())
        self.initialiseWidget()

    def initialiseWidget(self):
        self.time_while_this_window_is_open = 0.0
        self.random_actor = None
        self.random_actor_is_going_up = True
        self.widget.button_MoveRandom.clicked.connect(self.moveRandomActorInScene)


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
def executeImportTasks(tasks=[]):
    unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks(tasks)
    imported_asset_paths = []
    for task in tasks:
        for path in task.get_editor_property('imported_object_paths'):
            imported_asset_paths.append(path)
    return imported_asset_paths


def SMImportOption():
    options = unreal.FbxImportUI()
    options.set_editor_property('import_mesh', True)
    options.set_editor_property('import_textures', False)
    options.set_editor_property('import_materials', False)
    options.set_editor_property('import_as_skeletal', False)

    options.static_mesh_import_data.set_editor_property('combine_meshes', True)
    options.static_mesh_import_data.set_editor_property('generate_lightmap_u_vs', True)
    options.static_mesh_import_data.set_editor_property('auto_generate_collision', True)
    return options


def SkImportOption():
    options = unreal.FbxImportUI()
    options.set_editor_property('import_mesh', True)
    options.set_editor_property('import_textures', False)
    options.set_editor_property('import_materials', False)
    options.set_editor_property('import_as_skeletal', True)

    return options


def AnimImportOption():
    options = unreal.FbxImportUI()
    options.set_editor_property('import_mesh', False)
    options.set_editor_property('import_animations', True)
    options.set_editor_property()
    options.set_editor_property()

    return options


def print_table(**kwargs):
    for key, value in kwargs.items():
        print(key, value)


def lazy_sum(*wtf, **wtfisthat):
    def sum():
        ax = 0
        for n in wtf:
            ax = ax + n
        return ax

    return sum


############################ IMPORT ASSET ############################
def importMyAssets():
    static_mesh_task = buildImportTask(static_mesh_fbx, '/Game/StaticMeshes', SMImportOption())
    skeletal_mesh_task = buildImportTask(skeletal_mesh_fbx, '/Game/StaticMeshes', SkImportOption())
    executeImportTasks([static_mesh_task, skeletal_mesh_task])


# print 'TestRunning'
#
# importMyAssets()

def spawnQtWindow(desired_window_class=None):
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


unreal_app = QtGui.QApplication.instance()
if not unreal_app:
    unreal_app = QtGui.QApplication(sys.argv)
    # tick_handle = unreal.register_slate_post_tick_callback(__QtAppTick__)
    # unreal_app.aboutToQuit.connect(__QtAppQuit__)
    existing_windows = {}
    opened_windows = []
    spawnQtWindow(MainWindow.MainWindow)