import sys
import os
import unreal


sys.path.append('C:/Python27/Lib/site-packages')

sys.path.append('C:/Python27/Lib/site-packages')

from UE_input_FBX import Ui_UE_input_Dialog
from PySide import QtGui, QtUiTools, QtCore

from PySide.QtGui import QMessageBox
from PySide.QtGui import QFileDialog

import unreal


class MainWindow(QtGui.QWidget, Ui_UE_input_Dialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        # self.widget = QtUiTools.QUiLoader().load(UI_Path)
        self.Ui_UE_input_Dialog.activateWindow()
        self.Ui_UE_input_Dialog.show()

    def on_context_menu(self, point):

        self.popMenu.exec_(self.File_list.mapToGlobal(point))

    def open_file_path(self):

        file_cam = self.File_list.selectedItems()
        path = file_dict[file_cam[0].text()]
        self.model.path_file(path)

    def closeEvent(self, event):
        self.save_set()
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

    def Open_ue_editor(self):
        ue_editor_path = QFileDialog.getOpenFileName(self, 'select file', "/", "Exe Files (*.exe);;All Files (*)")
        self.UE4Editor_path_line.setText(ue_editor_path[0])
        pass

    def Open_ue_project(self):
        ue_project_path = QFileDialog.getOpenFileName(self, 'select file', "/", "Exe Files (*.uproject);;All Files (*)")
        self.UE4Project_path_line.setText(ue_project_path[0])
        pass

    def Update_ep_list(self):
        """
        update ep  list
        """
        ep_lists, ep_path_dict = self.model.get_ep_list()
        self.Ep_list.addItems(ep_lists)
        global ep_dict
        ep_dict = ep_path_dict

    def Update_sc_list(self):
        """
        update sc widget list
        """
        self.Sc_list.clear()
        ep_lists_ins = self.Ep_list.selectedItems()
        ep_path_lists = []
        for sel_ep in ep_lists_ins:
            ep_path_lists.append(ep_dict[sel_ep.text()])
        ep_sc_lists, sc_path_dict = self.model.get_sc_list(ep_path_lists)
        ep_sc_lists.sort()
        self.Sc_list.addItems(ep_sc_lists)

        global sc_dict
        sc_dict = sc_path_dict

    def Update_pt_list(self):

        self.Pt_list.clear()
        sc_lists_ins = self.Sc_list.selectedItems()
        sc_path_lists = []
        for sel_sc in sc_lists_ins:
            sc_path_lists.append(sc_dict[sel_sc.text()])
        sc_pt_lists, pt_path_dict = self.model.get_pt_list(sc_path_lists)
        sc_pt_lists.sort()
        self.Pt_list.addItems(sc_pt_lists)

        global pt_dict
        pt_dict = pt_path_dict

    def Update_shot_list(self):
        """
        update shot widget list
        """

        self.Shot_list.clear()
        pt_lists_ins = self.Pt_list.selectedItems()
        pt_path_lists = []
        for sel_pt in pt_lists_ins:
            pt_path_lists.append(pt_dict[sel_pt.text()])
        pt_shot_lists, shot_path_dict = self.model.get_shot_list(pt_path_lists)
        pt_shot_lists.sort()
        self.Shot_list.addItems(pt_shot_lists)

        global shot_dict
        shot_dict = shot_path_dict

    def Update_file_list(self):
        """
        update file widget list
        """
        self.File_list.clear()
        shot_lists_ins = self.Shot_list.selectedItems()
        shot_path_lists = []
        for sel_shot in shot_lists_ins:
            shot_path_lists.append(shot_dict[sel_shot.text()])
        fbx_file_lists, file_path_dict = self.model.get_fbx_file(shot_path_lists)
        fbx_file_lists.sort()
        self.File_list.addItems(fbx_file_lists)

        global file_dict
        file_dict = file_path_dict

    def Check_ue_asset(self):

        file_lists_ins = self.File_list.selectedItems()

        file_path_lists = []
        for i in file_lists_ins:
            file_path_lists.append(file_dict[i.text()])

        UE4_project = self.UE4Project_path_line.text()
        ue_lack_list = self.set.check_ue_asset(file_path_lists, UE4_project)
        if ue_lack_list:

            QMessageBox.information(self, "Lack Asset List", "".join(ue_lack_list))
        else:
            QMessageBox.information(self, "Lack Asset List", "No assets missing ! ~")

    def Start_input(self):
        file_lists_ins = self.File_list.selectedItems()

        file_path_lists = []
        for i in file_lists_ins:
            file_path_lists.append(file_dict[i.text()])

        UE4_editor = self.UE4Editor_path_line.text()
        UE4_project = self.UE4Project_path_line.text()

        is_del_fbx = self.Delete_ue_ani.isChecked()  # Whether to delete the FBX file under the UE import path.
        if is_del_fbx == True:
            self.set.clear_fbx_file(file_path_lists, UE4_project)

        json_file = self.set.create_json_file(file_path_lists)
        self.set.do_input_cmd(UE4_editor, UE4_project, json_file)

    def save_set(self):
        """
        save seting
        """
        set_info = {}
        set_info["ue_path"] = self.UE4Editor_path_line.text()
        set_info["project_file"] = self.UE4Project_path_line.text()

        self.model.save_set_file(set_info)

    def set_preset(self):
        """
        set preset info
        """
        set_info = self.model.get_preset()
        if not set_info == None:
            self.UE4Editor_path_line.setText(set_info["ue_path"])
            self.UE4Project_path_line.setText(set_info["project_file"])


# class Core():
#     def __init__(self):
#         super(Core, self).__init__()
#
#     def buildImportTask(filename='', destination_path='', options=None):
#         task = unreal.AssetImportTask()
#         task.set_editor_property('automated', True)
#         task.set_editor_property('destination_name', '')
#         task.set_editor_property('destination_path', destination_path)
#         task.set_editor_property('filename', filename)
#         task.set_editor_property('replace_existing', True)
#         task.set_editor_property('save', True)
#         task.set_editor_property('options', options)
#         return task
#
#     # tasks: obj List : The import tasks object. You can get them from buildImportTask()
#     # return: str List : The paths of successfully imported assets
#     def executeImportTasks(tasks=[]):
#         unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks(tasks)
#         imported_asset_paths = []
#         for task in tasks:
#             for path in task.get_editor_property('imported_object_paths'):
#                 imported_asset_paths.append(path)
#         return imported_asset_paths
#
#     def SMImportOption(self):
#         options = unreal.FbxImportUI()
#         options.set_editor_property('import_mesh', True)
#         options.set_editor_property('import_textures', False)
#         options.set_editor_property('import_materials', False)
#         options.set_editor_property('import_as_skeletal', False)
#
#         options.static_mesh_import_data.set_editor_property('combine_meshes', True)
#         options.static_mesh_import_data.set_editor_property('generate_lightmap_u_vs', True)
#         options.static_mesh_import_data.set_editor_property('auto_generate_collision', True)
#         return options
#
#     def SkImportOption(self):
#         options = unreal.FbxImportUI()
#         options.set_editor_property('import_mesh', True)
#         options.set_editor_property('import_textures', False)
#         options.set_editor_property('import_materials', False)
#         options.set_editor_property('import_as_skeletal', True)
#
#         return options
#
#     def AnimImportOption(self):
#         options = unreal.FbxImportUI()
#         options.set_editor_property('import_mesh', False)
#         options.set_editor_property('import_animations', True)
#         options.set_editor_property()
#         options.set_editor_property()
#
#         return options
#
#     # def importMyAssets(self):
#     #     static_mesh_task = buildImportTask(static_mesh_fbx, '/Game/StaticMeshes', SMImportOption())
#     #     skeletal_mesh_task = buildImportTask(skeletal_mesh_fbx, '/Game/StaticMeshes', SkImportOption())
#     #     executeImportTasks([static_mesh_task, skeletal_mesh_task])


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
