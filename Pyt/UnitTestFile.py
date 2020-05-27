import unreal
import os

AnimPath = "H:/XHQS/Cache/ANI_cache/EP001/SC001/SC001_P001/SC001_P001_0001/EP001_SC001_P001_0001_CH_Fifth_Tiger.fbx"


filelist = []
SK_content_path="/Game/Character/"
temp_path = AnimPath.split("/", AnimPath.__len__())

fileName =  temp_path[-1]

fileName = fileName[:-4]

fileNameWithOutSC = fileName.split("_", fileName.__len__())


contentFile=""
mediaName = fileNameWithOutSC[5:]
if mediaName.__len__() >1:
    for i  in mediaName:
        contentFile=contentFile+i+"_"

contentFile=contentFile[:-1]

SK_content_path = SK_content_path+contentFile+"/Meshes/"


targetDir=""
for i in fileNameWithOutSC[0:4]:
    targetDir=targetDir+'/'+i

targetDir = "/Game/Sequence"+targetDir+'/'
'''
finish target directory
'''


temp_filename = fileNameWithOutSC[4:]
SKName="SK"
for i in temp_filename:
    SKName = SKName+"_"+i
'''
finish SK Content Path
'''
SK_content_path= SK_content_path+ SKName+'_Skeleton'


def buildAnimationImportOptions(skeleton_path=''):
    options = unreal.FbxImportUI()
    # unreal.FbxImportUI
    options.set_editor_property('import_animations', True)
    options.skeleton = unreal.load_asset(skeleton_path)
    # unreal.FbxMeshImportData
    # options.anim_sequence_import_data.set_editor_property('import_translation', unreal.Vector(0.0, 0.0, 0.0))
    # options.anim_sequence_import_data.set_editor_property('import_rotation', unreal.Rotator(0.0, 0.0, 0.0))
    # options.anim_sequence_import_data.set_editor_property('import_uniform_scale', 1.0)
    # unreal.FbxAnimSequenceImportData
    options.set_editor_property('import_as_skeletal', False)
    options.set_editor_property('skeleton', unreal.load_asset(skeleton_path))
    options.set_editor_property('create_physics_asset', False)
    options.set_editor_property('import_rigid_mesh', False)
    options.set_editor_property('import_textures', False)
    options.set_editor_property('import_materials', False)
    options.set_editor_property('import_mesh', False)
    options.anim_sequence_import_data.set_editor_property('animation_length', unreal.FBXAnimationLengthImportType.FBXALIT_EXPORTED_TIME)
    options.anim_sequence_import_data.set_editor_property('remove_redundant_keys', False)
    return options

def buildImportTask(filename='', destination_path='', options=None):
    task = unreal.AssetImportTask()
    task.set_editor_property('automated', True)
    task.set_editor_property('destination_name', '')
    task.set_editor_property('destination_path', destination_path)
    task.set_editor_property('filename', filename)
    task.set_editor_property('replace_existing', True)
    # task.set_editor_property('factory', True)
    # task.set_editor_property('save', True)
    task.set_editor_property('options', options)
    return task

def executeImportTasks(tasks=[]):
    unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks(tasks)
    imported_asset_paths = []
    for task in tasks:
        for path in task.get_editor_property('imported_object_paths'):
            imported_asset_paths.append(path)
    return imported_asset_paths

# create_temp_filename
print targetDir
if not unreal.Paths.directory_exists(targetDir):
    unreal.EditorAssetLibrary.make_directory(targetDir)


animImportOption = buildAnimationImportOptions(SK_content_path)
animation_task = buildImportTask(AnimPath,targetDir, buildAnimationImportOptions(SK_content_path))
executeImportTasks([animation_task])



# fbx_source_path = "H:/XHQS/Cache/ANI_cache/"
# ep_list = os.listdir(fbx_shource_path)
#
# ep_lists = []
# ep_path_dict = {}
# for x in ep_list:
#     j = fbx_shource_path + x
#     if os.path.isdir(j):
#         ep_lists.append(x)
#         ep_path_dict[x] = j
#
#
# for i in ep_path_dict:
#     print i + "\n"
# RootPath = unreal.Paths.project_content_dir()
# Package_Path = "/Game/"
# print unreal.Paths.directory_exists(RootPath+'Sequences')
#
# createAsset = unreal.AssetToolsHelpers.get_asset_tools().create_asset("TestMaterial", Package_Path+"/A/"+"/B/"+"/C/", unreal.Material, unreal.MaterialFactoryNew(), "None")
#
# SequencePath = unreal.Paths.directory_exists(RootPath+'Sequences/')
#
#
# # SequenceAsset = unreal.AssetToolsHelpers.get_asset_tools().create_asset('SequenceMaster', Package_Path+'Sequences/', unreal.LevelSequence,
# #                                                                    unreal.LevelSequenceFactoryNew())
#
# def createGenericAsset(asset_path='', unique_name=True, asset_class=None, asset_factory=None):
#     if unique_name:
#         asset_path, asset_name = unreal.AssetToolsHelpers.get_asset_tools().create_unique_asset_name(base_package_name=asset_path, suffix='')
#     if not unreal.EditorAssetLibrary.does_asset_exist(asset_path=asset_path):
#         path = asset_path.rsplit('/', 1)[0]
#         name = asset_path.rsplit('/', 1)[1]
#         return unreal.AssetToolsHelpers.get_asset_tools().create_asset(asset_name=name, package_path=path, asset_class=asset_class, factory=asset_factory)
#     return unreal.load_asset(asset_path)





# def createGenerateAssetExample():
#     base_path = '/Game/GenericAssets'
#     generate_assets = [
#         [base_path+'sequence', unreal.LevelSequence, unreal.LevelSequenceFactoryNew()],
#         [base_path+'material', unreal.Material, unreal.MaterialFactoryNew()],
#         [base_path+'world', unreal.World, unreal.WorldFactory()]
#     ]
#
# base_path = '/Game/GenericAssets'
# generate_assets = [
#     [base_path+'sequence', unreal.LevelSequence, unreal.LevelSequenceFactoryNew()],
#     [base_path+'material', unreal.Material, unreal.MaterialFactoryNew()],
#     [base_path+'world', unreal.World, unreal.WorldFactory()]
# ]

# asset = generate_assets[0]
#
# TargetSequence = createGenericAsset(asset[0], True, asset[1],asset[2])



# AssetTools = unreal.AssetToolsHelpers.get_asset_tools()
#
# AssetImportTask =unreal.AssetImportTask()
# AssetImportTask.set_editor_property('filename', "THE NAME OF THE FILE")
# AssetImportTask.set_editor_property('destination_path','/Game/Tex')
#
#
# CameraTrack = 'H:/XHQS/Cache/ANI_cache/EP001/SC001/SC001_P001/SC001_P001_0003/EP001_SC001_P001_0003_Camera_50_101_266.fbx'
#
#
# def build_SkeletalMesh_import():
#     options = unreal.FbxImportUI()
#     options.set_editor_property("import_mesh", True)
#     options.set_editor_property("import_textures", False)
#     options.set_editor_property("import_materials", False)
#     options.set_editor_property("import_as_skeletal", True)  # Skeletal Mesh
#     # options.skeletal_mesh_import_data.set_editor_property('import_translation', unreal.Vector(0.0, 0.0, 0.0))
#     # options.skeletal_mesh_import_data.set_editor_property('import_rotation', unreal.Rotator(0.0, 0.0, 0.0))
#     # options.skeletal_mesh_import_data.set_editor_property('import_uniform_scale', 1.0)
#     # options.skeletal_mesh_import_data.set_editor_property('import_morph_targets', True)
#     # options.skeletal_mesh_import_data.set_editor_property('update_skeleton_reference_pose', False)
#     return options
#
#
#
# # def addCameraAnimationTrackOnPossessable(CameraTrack, possessable=None):
# #      track_type = unreal.MovieSceneUserImportFBXSettings()
#
#
# def executeSlowTask():
#     '''
#     Testing Delayed Function
#     :return:
#     '''
#     quantity_steps_in_slow_task = 1000  # 步数
#     with unreal.ScopedSlowTask(quantity_steps_in_slow_task, 'My Slow Task Text ...') as slow_task:
#         slow_task.make_dialog(True)  # 可设置是否添加取消键
#         for x in range(quantity_steps_in_slow_task):
#             if slow_task.should_cancel():  # 按取消会触发到这个函数
#                 break
#             #             # 进入循环帧
#             slow_task.enter_progress_frame(
#                 1, 'My Slow Task Text ...' + str(x) + '/' + str(quantity_steps_in_slow_task))  # 这里可填入每帧的显示
#             time.sleep(1)
#
#
# # executeSlowTask()
#
# # sequence = unreal.AssetToolsHelpers.get_asset_tools().create_asset('SequenceMaster', '/Game/', unreal.LevelSequence,
# #                                                                    unreal.LevelSequenceFactoryNew())
# #
#
# def HardCode_importSkeletalMesh():
#     targetSequence = unreal.load_object(None, "/Game/SequenceMaster")
#     SkeletalMeshTrack = 'H:/XHQS/scenes/Asset/Character/Fifth_Tiger/Rig/FBX/SK_CH_Fifth_Tiger.fbx'
#     SkMeshTask = buildImportTask(SkeletalMeshTrack, '/Game/SkeletalMeshes', build_SkeletalMesh_import())
#     executeImportTasks([SkMeshTask])
#
#
# def create_level_sequence(asset_name, package_path='/Game/'):
#     '''
#     create Single Sequence with Root package_path
#
#     :param asset_name: sequence name
#     :param package_path: root of the sequence
#     :return: sequence
#     '''
#     sequence = unreal.AssetToolsHelpers.get_asset_tools().create_asset(asset_name, package_path, unreal.LevelSequence,
#                                                                        unreal.LevelSequenceFactoryNew())
#
#     return sequence
#
#
# target_sequence = create_level_sequence('MasterSequence')
# CameraTrack = 'H:/XHQS/Cache/ANI_cache/EP001/SC001/SC001_P001/SC001_P001_0003/EP001_SC001_P001_0003_Camera_50_101_266.fbx'
# world = unreal.EditorLevelLibrary.get_editor_world()
# cine_camera = unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.CineCameraActor, unreal.Vector())
#
#
# level_actors = unreal.EditorLevelLibrary.get_all_level_actors()
# camera_import_options = unreal.MovieSceneUserImportFBXSettings()
# camera_import_options.set_editor_property("reduce_keys", True)
# camera_import_options.set_editor_property("create_cameras", True)
# camera_import_options.set_editor_property("force_front_x_axis", False)
# camera_import_options.set_editor_property("match_by_name_only", False)
#
# cine_camera_comp = target_sequence.add_possessable(cine_camera)
# bindings = target_sequence.get_bindings()
#
#
# target_sequence.add_spawnable_from_instance(cine_camera) #make Camera Spawnable
#
#
#
#
# world = unreal.EditorLevelLibrary.get_editor_world()
# unreal.SequencerTools.import_fbx(world, target_sequence, bindings, camera_import_options, CameraTrack)
#
# currentSequence =unreal.EditorAssetLibrary.load_asset('/Game/MasterSequence')
#
# sequence_asset = unreal.MovieSceneSequence.cast(currentSequence)
#
# # possessable = sequence_asset.add_possessable(None)
#
# binding = sequence_asset.get_bindings()
#
#
# ID = sequence_asset.find_binding_by_name('CineCameraActor14')
#
# ID_object = unreal.MovieSceneBindingExtensions.get_object_template(ID)
# # print ID.get_child_possessables()
# print ID_object