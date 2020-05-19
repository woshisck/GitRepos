import unreal
import os
# from PySide import QtGui, QtUiTools, QtCore
#
# from PySide.QtGui import QMessageBox
# from PySide.QtGui import QFileDialog


prefixAnimationBlueprint = "animBP"
prefixAnimationSequence = "anim"
prefixAnimation = "anim"
prefixBlendSpace = "animBlnd"
prefixBlueprint = "bp"
prefixCurveFloat = "crvF"
prefixCurveLinearColor = "crvL"
prefixLevel = "lvl"
prefixMaterial = "mat"
prefixMaterialFunction = "mat_func"
prefixMaterialInstance = "mat_inst"
prefixParticleSystem = "fx"
prefixPhysicsAsset = "phsx"
prefixSkeletalMesh = "sk"
prefixSkeleton = "skln"
prefixSoundCue = "cue"
prefixSoundWave = "wv"
prefixStaticMesh = "sm"
prefixTexture2D = "tex"
prefixTextureCube = "HDRI"

workingPath = "/Game/Sequence"

Ani_cache = "H:/XHQS/Cache/ANI_cache"


#
# @unreal.uclass()
# class LevelSequenceFactory(unreal.LevelSequence):
#     pass
#
# @unreal.uclass()
# class EditorUtil(unreal.GlobalEditorUtilityBase):
#     pass
#
#
# @unreal.uclass()
# class MaterialEditingLib(unreal.MaterialEditingLibrary):
#     pass
#
#
@unreal.uclass()
class GetEditorAssetLibrary(unreal.EditorAssetLibrary):
    pass

@unreal.uclass()
class getAssetRegistry(unreal.AssetRegistry):
    pass


#
# @unreal.uclass()
# class GetEditorUtility(unreal.GlobalEditorUtilityBase):
#     pass
#
#
# @unreal.uclass()
# class GetAnimationLibrary(unreal.AnimationLibrary):
#     pass
#
# editorUtility=GetEditorUtility()
#
# levelsequenceFactory = LevelSequenceFactory
#
# def createGenericAsset(asset_path='', unique_name=True, asset_class=None, asset_factory=None):
#     if unique_name:
#         asset_path, asset_name = unreal.AssetToolsHelpers.get_asset_tools().create_unique_asset_name(base_package_name=asset_path, suffix='')
#     if not unreal.EditorAssetLibrary.does_asset_exist(asset_path=asset_path):
#         path = asset_path.rsplit('/', 1)[0]
#         name = asset_path.rsplit('/', 1)[1]
#         return unreal.AssetToolsHelpers.get_asset_tools().create_asset(asset_name=name, package_path=path, asset_class=asset_class, factory=asset_factory)
#     return unreal.load_asset(asset_path)
#
#
#
#
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



# def GetProperPrefix(className):
#     _prefix = ""
#     if className == "AnimBlueprint":
#         _prefix = prefixAnimationBlueprint
#     else:
#         _prefix = ""
#     return _prefix

AssetRegister = getAssetRegistry()

editorAssetLib = GetEditorAssetLibrary()
allAssets = editorAssetLib.list_assets(workingPath, True, False)
allAssetsCount = len(allAssets)


def functionX():


def import_cameraShot(file_path, sequence_path):
    '''
    code from the enhance importing camera
    :return: none
    '''


    '''
    set word and cineCamera spawn in level
    '''
    world = unreal.EditorLevelLibrary.get_editor_world()
    targetsequence = unreal.load_asset(sequence_path, unreal.LevelSequence)
    cine_camera = unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.CineCameraActor, unreal.Vector())
    cine_camera.set_actor_label("file_path")
    camera_binding = targetsequence.add_possessable(cine_camera)
    '''
    import option
    '''
    import_options = unreal.MovieSceneUserImportFBXSettings()
    import_options.set_editor_property('create_cameras', False)
    import_options.set_editor_property('force_front_x_axis', False)
    import_options.set_editor_property('match_by_name_only', False)
    import_options.set_editor_property('reduce_keys', True)
    import_options.set_editor_property('reduce_keys_tolerance', 0.001)

    bindings = targetsequence.get_bindings()
    unreal.SequencerTools.import_fbx(world, targetsequence, camera_bindings(), import_camera_FBX(), input_file)



input_file = "E:\\MyCamShot.fbx"
world = unreal.EditorLevelLibrary.get_editor_world()
targetsequence = unreal.load_asset('/Game/Sq', unreal.LevelSequence)
cine_camera = unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.CineCameraActor, unreal.Vector())
cine_camera.set_actor_label('MyCamShot')
binding = targetsequence.add_possessable(cine_camera)


def import_camera_FBX():
    import_options = unreal.MovieSceneUserImportFBXSettings()
    import_options.set_editor_property('create_cameras', False)
    import_options.set_editor_property('force_front_x_axis', False)
    import_options.set_editor_property('match_by_name_only', False)
    import_options.set_editor_property('reduce_keys', True)
    import_options.set_editor_property('reduce_keys_tolerance', 0.001)
    return import_options

def camera_bindings():
    bindings = targetsequence.get_bindings()
    return bindings


# world = unreal.EditorLevelLibrary.get_editor_world()
unreal.SequencerTools.import_fbx(world, targetsequence, camera_bindings(), import_camera_FBX(), input_file)

# world = unreal.EditorLevelLibrary.get_editor_world()
#
# sequencer_asset_path = '/Game/Sq'
# sequence = unreal.load_asset(sequencer_asset_path)
# input_file = "E:\\MyCamShot.fbx"
#
#
# def import_camera_FBX():
#     import_options = unreal.MovieSceneUserImportFBXSettings()
#     import_options.set_editor_property('create_cameras', False)
#     import_options.set_editor_property('force_front_x_axis', False)
#     import_options.set_editor_property('match_by_name_only', False)
#     import_options.set_editor_property('reduce_keys', False)
#     import_options.set_editor_property('reduce_keys_tolerance', 0.001)
#     return import_options
#
# def camera_bindings():
#     bindings = sequence.get_bindings()
#     return bindings
#
# unreal.SequencerTools.import_fbx(world, sequence, camera_bindings(), import_camera_FBX(), input_file)

# print targetsequence.get_bindings()
# print targetsequence.get_master_tracks()
# Camera = targetsequence.add_spawnable_from_class(unreal.CineCameraActor)
# print len(targetsequence.get_spawnables())



# cine_camera = unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.CineCameraActor, unreal.Vector())
# cine_camera.set_actor_label('EP001_SC001_P001_0001_Camera_35_101_381')
# binding = targetsequence.add_possessable(cine_camera)
# targetsequence.add_possessable(cine_camera.get_cine_camera_component())

'''
set the camera cut track 
'''
# camera_id = unreal.MovieSceneObjectBindingID()
# camera_id.set_editor_property('guid', binding.get_id())
# camera_cut_track = targetsequence.add_master_track(unreal.MovieSceneCameraCutTrack)
# camera_section = camera_cut_track.add_section()
# camera_section.set_range(0.0, 100.0)
# camera_section.set_camera_binding_id(camera_id)

# import_setting = unreal.MovieSceneUserImportFBXSettings()
# import_setting.set_editor_property('create_cameras', False)
# import_setting.set_editor_property('force_front_x_axis', False)
# import_setting.set_editor_property('match_by_name_only', True)
# import_setting.set_editor_property('reduce_keys', False)
# import_setting.set_editor_property('reduce_keys_tolerance', 0.001)

# world = unreal.EditorLevelLibrary.get_editor_world()
# unreal.SequencerTools.import_fbx(world, targetsequence, [binding], import_setting, "H:/XHQS/Cache/ANI_cache/EP001/SC001/SC001_P001/SC001_P001_0001/EP001_SC001_P001_0001_Camera_35_101_381.fbx")


# for i in allAssets:
#     print i

# print allAssetsCount

# editorUtil = EditorUtil()
# materialEditingLib = MaterialEditingLib()
#
# SelectedAssets =editorUtil.get_selected_assets()
# factory =unreal.MaterialInstanceConstantFactoryNew()
# asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
#
#
# for selectedAsset in SelectedAssets:
#     newAssetName = selectedAsset.get_name() + "_%s_%d"
#     print newAssetName
#     sourceAssetPath = selectedAsset.get_path_name()
#     print sourceAssetPath


# def work_for_all(func):
#     def inner_func(*args, **kwargs):
#         print("I cam work for all function?")
#         return func(*args, **kwargs)
#     return inner_func
#
# def T_Param(func):
#     def inner_func(A,B):
#         if (A <=0):
#             print ("A is lower than zero")
#         return func(A,B)
#     return inner_func
#
# def T_Param_(func):
#     def inner_func(A,B):
#         if(B==5):
#             print ("B is 5")
#         return func(A,B)
#     return inner_func
#
#
#
# @T_Param
# @T_Param_
# def DIVID(A,B):
#     return A/B
#
# @work_for_all
# def divide(a,b):
#     return a+b
#
# print divide(3,4)
#
# def fun_func(*args):
#     return args
#
#
#
#
# print( DIVID(0,5))
#

# level_sequence = unreal.LevelSequence.cast(unreal.AssetToolsHelpers.get_asset_tools().create_asset(
#     asset_name='my_level_sequence_name',
#     package_path='/Game/',
#     asset_class=unreal.LevelSequence,
#     factory=unreal.LevelSequenceFactoryNew()
# ))
#
# cine_camera = unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.CineCameraActor, unreal.Vector())
# # Make sure your camera label is the same as in fbx file
# cine_camera.set_actor_label('MyCamShot')
#
# binding = level_sequence.add_possessable(cine_camera)
# level_sequence.add_possessable(cine_camera.get_cine_camera_component())
#
# camera_id = unreal.MovieSceneObjectBindingID()
# camera_id.set_editor_property('guid', binding.get_id())
# camera_cut_track = level_sequence.add_master_track(unreal.MovieSceneCameraCutTrack)
# camera_section = camera_cut_track.add_section()
# camera_section.set_range(0.0, 100.0)
# camera_section.set_camera_binding_id(camera_id)
#
# import_setting = unreal.MovieSceneUserImportFBXSettings()
# import_setting.set_editor_property('create_cameras', False)
# import_setting.set_editor_property('force_front_x_axis', False)
# import_setting.set_editor_property('match_by_name_only', True)
# import_setting.set_editor_property('reduce_keys', False)
# import_setting.set_editor_property('reduce_keys_tolerance', 0.001)
#
# world = unreal.EditorLevelLibrary.get_editor_world()
# unreal.SequencerTools.import_fbx(world, level_sequence, [binding], import_setting, "E:\\MyCamShot.fbx")
#
