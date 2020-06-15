import unreal

@unreal.uclass()
class getAbcImportSetting(unreal.AbcImportSettings):
    pass

class SequenceAbcEditor:
    def __init__(self, level_sequence, abc_file_path):
        self.targetSequence  = level_sequence
        self.abc_path = abc_file_path
        self.frame_start= 0
        self.frame_end = 0

    def _import_alembic(self, asset_path="/Game/", asset_name='AbcFile', frame_start = -1, frame_end = -1):
        options = unreal.AbcImportSettings()
        options.import_type = unreal.AlembicImportType.GEOMETRY_CACHE

        options.sampling_settings.frame_start = frame_start
        options.sampling_settings.frame_end = frame_end
        options.sampling_settings.skip_empty = True

        import_task = unreal.AssetImportTask()
        import_task.save = True
        # Set base properties on the task.
        import_task.filename = self.abc_path
        import_task.destination_path = asset_path
        import_task.destination_name = asset_name
        import_task.automated = True  # Suppress UI.
        import_task.options = options
        asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
        asset_tools.import_asset_tasks([import_task])
        print self.abc_path

    def _add_abc_into_Sequence(self, end_frame):
        self.targetSequence.add_spawnable_from_instance()
        with self.targetSequence.add_spawnable_from_instance(GeometryCache) as gc_bind:
            gc_track =gc_bind.add_track(unreal.MovieSceneGeometryCacheTrack)
            gc_section = gc_track.add_section()
            gc_param = unreal.MovieSceneGeometryCacheParams()
            gc_param.set_editor_property("geometry_cache_asset", GeometryCache)
            gc_section.set_editor_property("params", gc_param)
            gc_section.set_end_frame(end_frame)




@unreal.uclass()
class GetEditorAssetLibrary(unreal.EditorAssetLibrary):
    pass


def init_level_sequence(levelSequence, start=0.0, end=1000.0):
    '''
    inital sequence and add empty camera master track
    :param levelSequence:
    :param start: sequence start
    :param end: sequence end
    :return: None
    DIDN'T CREATE SEQUENCE!
    '''
    levelSequence.set_playback_start(start)
    levelSequence.set_playback_end(end)
    mastertrackName=[]
    for mastertrack in levelSequence.get_master_tracks():
        mastertrackName.append(mastertrack.get_display_name())
    if unreal.Text("Camera Cuts") in mastertrackName:
        pass
    else:
        levelSequence.add_master_track(unreal.MovieSceneCameraCutTrack)
def get_master_track(levelSequence):
    '''
    get camera master track in sequences
    :param levelSequence:
    :return: master track( format: MovieSceneTrack)
    '''
    for mastertrack in levelSequence.get_master_tracks():
        if mastertrack.get_display_name() ==unreal.Text("Camera Cuts"):
            return mastertrack



def importCamera(levelSequence, cameraPath, fbxCamName='UNREAL_CAMERA_SHOT'):
    '''
    import camera shot from fbx &create focus length etc
    :param levelSequence: target sequence
    :param cameraPath: fbx folder path
    :param fbxCamName: cameraName in both file and sequence
    :return: None
    '''
    cine_camera = unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.CineCameraActor, unreal.Vector())

    cine_camera.set_actor_label(fbxCamName)


    camera_comp_bind = unreal.MovieSceneSequence.add_possessable(levelSequence, cine_camera.get_cine_camera_component())
    camera_bind = unreal.MovieSceneSequence.add_spawnable_from_instance(levelSequence, cine_camera)
    camera_comp_bind.set_parent(camera_bind)

    focal_length_track = camera_comp_bind.add_track(unreal.MovieSceneFloatTrack)
    focal_length_track.set_property_name_and_path('CurrentFocalLength', 'CurrentFocalLength')

    focal_length_section = focal_length_track.add_section()
    focal_length_section.set_start_frame_bounded(0)
    focal_length_section.set_end_frame_bounded(0)

    Aperture_length_track = camera_comp_bind.add_track(unreal.MovieSceneFloatTrack)
    Aperture_length_track.set_property_name_and_path('CurrentAperture', 'CurrentAperture')

    aperture_length_section = Aperture_length_track.add_section()
    aperture_length_section.set_start_frame_bounded(0)
    aperture_length_section.set_end_frame_bounded(0)

    levelSequence.get_bindings()[0].remove()
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
    cam = unreal.SequencerTools.import_fbx(world, levelSequence, [camera_bind], import_setting, cameraPath)



def add_master_track(folder, start=0.0, end=1000.0):
    # camera_id = unreal.MovieSceneObjectBindingID()
    # camera_id.set_editor_property('guid', binding.get_id())
    camera_cut_track=folder.add_child_master_track(unreal.MovieSceneCameraCutTrack)
    camera_section = camera_cut_track.add_section()
    camera_section.set_range(start, end)
    # camera_section.set_camera_binding_id(camera_id)

def set_color(R, G, B, A):
    '''
    set unreal.Color val
    :param R: R
    :param G: G
    :param B: B
    :param A: A
    :return: unreal.Color instance
    '''
    tempColor = unreal.Color()
    tempColor.set_editor_property("a" ,A)
    tempColor.set_editor_property("b",B)
    tempColor.set_editor_property("g",G)
    tempColor.set_editor_property("r", R)
    return tempColor

def get_camera_by_name(levelSequence, CameraName=""):
    '''
    get camera binding name from sequence
    :param levelSequence: target sequence
    :param CameraName: camera name(need unreal.Text() format)
    :return: binding
    '''
    for bind in levelSequence.get_bindings():
        if bind.get_display_name() == unreal.Text(CameraName):
            return bind


def add_camera_to_cut(masterTrack, binding, start=0.0, end=1000.0):
    '''
    add camera bind to camera cut section
    :param masterTrack: camera cut master track
    :param binding: camera binding
    :param start: start range (need to get from fbx)
    :param end: end range (need to get from fbx)
    :return: None
    '''
    camera_id = unreal.MovieSceneObjectBindingID()
    camera_id.set_editor_property('guid', binding.get_id())
    camera_section = masterTrack.add_section()
    camera_section.set_range(start, end)
    camera_section.set_camera_binding_id(camera_id)
    # camera_id = unreal.MovieSceneObjectBindingID()
    # camera_id.set_editor_property('guid', binding.get_id())
# camera_section.set_camera_binding_id(camera_id)

def clear_cut(levelSequence):
    '''
    clear the master track
    :param levelSequence: target sequence
    :return: None
    '''
    cam_cut = get_master_track(levelSequence)
    for section in cam_cut.get_sections():
        cam_cut.remove_section(section)


def get_camera_bind(levelSequence, bindName='UNREAL_CAMERA_SHOT'):
    for bind in levelSequence.get_bindings():
        if bind.get_display_name() == unreal.Text(bindName):
            return bind

def get_camera_transform(bind):
    for track in bind.get_tracks():
        if track.get_display_name() == unreal.Text('Transform'):
            return track


targetSequence = unreal.EditorAssetLibrary.load_asset("/Game/mySequence")



'''
Function using example
'''
init_level_sequence(targetSequence)
importCamera(targetSequence, 'D://UNREAL_CAMERA_SHOT.fbx')
camerabind = get_camera_bind(targetSequence)
masterTrack = get_master_track(targetSequence)
add_camera_to_cut(masterTrack,camerabind)



# camera_id = unreal.MovieSceneObjectBindingID()
# camera_id.set_editor_property('guid', binding.get_id())
# camera_cut_track = levelSequence.add_master_track(unreal.MovieSceneCameraCutTrack)
# camera_section = camera_cut_track.add_section()
# camera_section.set_range(0.0, 1000.0)
# camera_section.set_camera_binding_id(camera_id)
#