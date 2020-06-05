import unreal

@unreal.uclass()
class GetEditorAssetLibrary(unreal.EditorAssetLibrary):
    pass



def createCamera(levelSequence, cameraPath, fbxCamName='UNREAL_CAMERA_SHOT'):


    cine_camera = unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.CineCameraActor, unreal.Vector())

    cine_camera.set_actor_label(fbxCamName)

    # add spawnable camera with label
    unreal.MovieSceneSequenceExtensions.add_spawnable_from_instance(levelSequence, cine_camera)
    # unreal.MovieSceneSequenceExtensions.add_spawnable_from_class(levelSequence, cine_camera.get_cine_camera_component().get_class())

    cameraBind = levelSequence.add_possessable(cine_camera)
    componentBind = levelSequence.add_possessable(cine_camera.get_cine_camera_component())
    binding = levelSequence.get_bindings()

    # camera_id = unreal.MovieSceneObjectBindingID()
    # camera_id.set_editor_property('guid', binding.get_id())
    # camera_cut_track = levelSequence.add_master_track(unreal.MovieSceneCameraCutTrack)
    # camera_section = camera_cut_track.add_section()
    # camera_section.set_range(0.0, 1000.0)
    # camera_section.set_camera_binding_id(camera_id)
    #
    #
    # # possessable = levelSequence.add_spawnable_from_class(wo)
    #
    #
    import_setting = unreal.MovieSceneUserImportFBXSettings()
    import_setting.set_editor_property('create_cameras', False)
    import_setting.set_editor_property('force_front_x_axis', False)
    import_setting.set_editor_property('match_by_name_only', True)
    import_setting.set_editor_property('reduce_keys', False)
    import_setting.set_editor_property('reduce_keys_tolerance', 0.001)
    #
    world = unreal.EditorLevelLibrary.get_editor_world()
    cam = unreal.SequencerTools.import_fbx(world, levelSequence, [cameraBind], import_setting, cameraPath)
    #componentBind.set_parent(binding[0])
    return

targetSequence = unreal.EditorAssetLibrary.load_asset("/Game/mySequence")

#createCamera(targetSequence, cameraPath="D:/UNREAL_CAMERA_SHOT.fbx")

#print targetSequence.get_bindings()[2].get_name()
# track = targetSequence.get_possessables()[1].get_tracks()
# targetBind = targetSequence.get_bindings()[0]
# targetBin
# d.add_track(track)
print  (targetSequence.get_possessables()[1].get_tracks()[0].get_display_name())


