import sys
import os
import unreal


sys.path.append('C:/Python27/Lib/site-packages')

sys.path.append('C:/Python27/Lib/site-packages')



from UE_input_FBX import Ui_UE_input_Dialog
from PySide import QtGui, QtUiTools, QtCore

from PySide.QtGui import QMessageBox
from PySide.QtGui import QFileDialog


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

