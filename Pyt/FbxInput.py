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

workingPath = "/Game/"
RootPath = "/Game/"
TestPath ="/Game/SkeletalMesh/"
Ani_cache = "H:/XHQS/Cache/ANI_cache"

def GetProperPrefix(className):
    _prefix = ""
    if className == "AnimBlueprint":
        _prefix = prefixAnimationBlueprint
    elif className == "AnimSequence":
        _prefix = prefixAnimationSequence
    elif className == "Animation":
        _prefix = prefixAnimation
    elif className == "BlendSpace1D":
        _prefix = prefixBlendSpace
    elif className == "Blueprint":
        _prefix = prefixBlueprint
    elif className == "CurveFloat":
        _prefix = prefixCurveFloat
    elif className == "CurveLinearColor":
        _prefix = prefixCurveLinearColor
    elif className == "Material":
        _prefix = prefixMaterial
    elif className == "MaterialFunction":
        _prefix = prefixMaterialFunction
    elif className == "MaterialInstance":
        _prefix = prefixMaterialInstance
    elif className == "ParticleSystem":
        _prefix = prefixParticleSystem
    elif className == "PhysicsAsset":
        _prefix = prefixPhysicsAsset
    elif className == "SkeletalMesh":
        _prefix = prefixSkeletalMesh
    elif className == "Skeleton":
        _prefix = prefixSkeleton
    elif className == "SoundCue":
        _prefix = prefixSoundCue
    elif className == "SoundWave":
        _prefix = prefixSoundWave
    elif className == "StaticMesh":
        _prefix = prefixStaticMesh
    elif className == "Texture2D":
        _prefix = prefixTexture2D
    elif className == "TextureCube":
        _prefix = prefixTextureCube
    else:
        _prefix = ""

    return _prefix


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


assetRegistry = getAssetRegistry()
print assetRegistry.get_assets_by_path( "/Game/A/", False, False)
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
# #     if not unreal.EditorAssetLibrary.does_asset_exist(asset_path=asset_path):
# #         path = asset_path.rsplit('/', 1)[0]
# #         name = asset_path.rsplit('/', 1)[1]
# #         return unreal.AssetToolsHelpers.get_asset_tools().create_asset(asset_name=name, package_path=path, asset_class=asset_class, factory=asset_factory)
# #     return unreal.load_asset(asset_path)
# #
# #
# #
#
# #
# # def createGenerateAssetExample():
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


'''
check all the asset (EditorAssetLibrary)
'''
@unreal.uclass()
class pathFactory(unreal.Paths):
    pass

def pathFind():
    filePath = pathFactory.get_project_file_path()
    relativePath = pathFactory.convert_relative_path_to_full(filePath)
    return relativePath

print (pathFind())
# AssetRegister = getAssetRegistry()
#
# editorAssetLib = GetEditorAssetLibrary()
# allAssets = editorAssetLib.list_assets(workingPath, True, False)
# allAssetsCount = len(allAssets)
#
#
# selectedAssetPath = workingPath
#
# with unreal.ScopedSlowTask(allAssetsCount, selectedAssetPath) as slowTask:
#     slowTask.make_dialog(True)
#     for asset in allAssets:
#         _assetData = editorAssetLib.find_asset_data(asset)
#         _assetName = _assetData.get_asset().get_name()
#         _assetPathName = _assetData.get_asset().get_path_name()
#         _assetClassName = _assetData.get_asset().get_class().get_name()
#
#
#         '''
#         Check if the asset is Skeletal mesh and duplicated it to certain root
#         '''
#         if _assetClassName == "SkeletalMesh":
#             editorAssetLib.duplicate_asset(_assetPathName, TestPath+_assetName)
#
#         _assetPathOnly = _assetPathName.replace((_assetName + "." + _assetName), "")
#         print ("Name: "+_assetPathOnly+" class name: "+_assetClassName+'\n')
#
#
#         if slowTask.should_cancel():
#             break
#         slowTask.enter_progress_frame(1,asset)

        #need prefix name
        # _assetPrefix = GetProperPrefix(_assetClassName)


##########################################################################################################################
# '''
# hard code of making sequence & import camera fbx
# '''
# input_file = "E:\\MyCamShot.fbx"
# world = unreal.EditorLevelLibrary.get_editor_world()
# targetsequence = unreal.load_asset('/Game/Sq', unreal.LevelSequence)
# cine_camera = unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.CineCameraActor, unreal.Vector())
# cine_camera.set_actor_label('MyCamShot')
# binding = targetsequence.add_possessable(cine_camera)
#
#
# def import_camera_FBX():
#     import_options = unreal.MovieSceneUserImportFBXSettings()
#     import_options.set_editor_property('create_cameras', True)
#     import_options.set_editor_property('force_front_x_axis', False)
#     import_options.set_editor_property('match_by_name_only', False)
#     import_options.set_editor_property('reduce_keys', True)
#     import_options.set_editor_property('reduce_keys_tolerance', 0.001)
#     return import_options
#
# def camera_bindings():
#     bindings = targetsequence.get_bindings()
#     return bindings
#
# unreal.SequencerTools.import_fbx(world, targetsequence, camera_bindings(), import_camera_FBX(), input_file)

##########################################################################################################################





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