import unreal_engine as ue
from unreal_engine.classes import GeometryCache,LevelSequence,SkeletalMesh,Actor,PlayerStart,SkeletalMeshActor,LevelSequenceActor
from unreal_engine.classes import MovieSceneAudioTrack, LevelSequenceFactoryNew, MovieSceneSkeletalAnimationTrack, Character, SkeletalMesh, MovieScene3DTransformTrack, CineCameraActor, AnimSequence
from unreal_engine.structs import FloatRange, FloatRangeBound, MovieSceneObjectBindingID,MovieSceneSpawnable
from unreal_engine import FbxManager, FbxIOSettings, FbxImporter, FbxScene, FTransform, FRotator, FVector, FColor ,FQuat
from unreal_engine.enums import EMovieSceneObjectBindingSpace

cam_fbx_path = 'H:/XHQS_Project01/3D_Project/branches/assets/Export/EP001/SC015/SC015_P001/SC015_P001_0008/EP001_SC015_P001_0008_Camera_50_674_718.fbx'

# class FbxCurvesExtractor:
 
#     def __init__(self, filename):
#         self.manager = FbxManager()
#         io_settings = FbxIOSettings(self.manager, 'IOSROOT')
#         self.manager.set_io_settings(io_settings)
#         importer = FbxImporter(self.manager, 'importer')
#         importer.initialize(filename, io_settings)
#         self.scene = FbxScene(self.manager, 'scene')
#         importer._import(self.scene)
 
#     def get_objects_by_class(self, name):
#         objects = []
#         for i in range(0, self.scene.get_src_object_count()):
#             obj = self.scene.get_src_object(i)
#             if obj.get_class_name() == name:
#                 objects.append(obj)
#         return objects
 
#     def get_members_by_class(self, parent, name):
#         members = []
#         for i in range(0, parent.get_member_count()):
#             member = parent.get_member(i)
#             if member.get_class_name() == name:
#                 members.append(member)
#         return members
     
#     def get_anim_stacks(self):
#         return self.get_objects_by_class('FbxAnimStack')
 
#     def get_anim_layers(self, stack):
#         return self.get_members_by_class(stack, 'FbxAnimLayer')
 
#     def get_properties(self, obj):
#         prop = obj.get_first_property()
#         while prop:
#             yield prop
#             prop = obj.get_next_property(prop)
 
#     def get_anim_curves(self, layer):
#         curves = []
#         for i in range(0, self.scene.get_src_object_count()):
#             obj = self.scene.get_src_object(i)
#             # retrieve object properties
#             for prop in self.get_properties(obj):
#                 curve_node = prop.get_curve_node(layer)
#                 if not curve_node:
#                     continue
#                 channels = []
#                 for chan_num in range(0, curve_node.get_channels_count()):
#                     # always get the first curve
#                     curve = curve_node.get_curve(chan_num, 0)
#                     if not curve:
#                         continue
#                     keys = []
#                     for key_id in range(0, curve.key_get_count()):
#                         keys.append((curve.key_get_seconds(key_id), curve.key_get_value(key_id)))
#                     channels.append({'name': curve_node.get_channel_name(chan_num), 'keys': keys})
#                 curves.append({'object': obj.get_name(), 'class': obj.get_class_name(), 'property': prop.get_name(), 'channels': channels})
#         return curves


# def ass_cam(seq_asset,cam_fbx_path):

#     frameRateDenominator = 1.0
#     frameRateNumerator = 25

#     #cam_fbx_path = 'H:/XHQS_Project01/3D_Project/branches/assets/Export/EP001/SC015/SC015_P001/SC015_P001_0008/EP001_SC015_P001_0008_Camera_50_674_718.fbx'

#     cam_list = cam_fbx_path.split('/')[-1].split('.')[0].split('_')

#     focal = cam_list[-3]
#     start_frame = cam_list[-2]
#     end_frame = cam_list[-1]

#     seq_start = float(start_frame)/float(frameRateNumerator)
#     seq_end = float(end_frame)/float(frameRateNumerator)

#     spawn_cam_name = cam_list[0]+'_'+cam_list[1]+'_'+cam_list[2]+'_'+cam_list[3]+'_'+'Cam'

#     world = ue.get_editor_world()
#     Cam = world.actor_spawn(CineCameraActor)
#     Cam.set_actor_label(spawn_cam_name)
#     Cam.CameraComponent.post_edit_change()
#     Cam.CameraComponent.CurrentFocalLength = int(focal)
#     Cam.CameraComponent.FilmbackSettings.SensorWidth = float(36.0) 
#     Cam.CameraComponent.FilmbackSettings.SensorHeight = float(20.25)
#     Cam.CameraComponent.post_edit_change()
#     Cam.CameraComponent.FocusSettings.FocusMethod = 0



#     cam_spawnable_guid = seq_asset.sequencer_make_new_spawnable(Cam)
#     Cam.actor_destroy()
#     camera_cut_track = seq_asset.sequencer_add_camera_cut_track()
#     section = camera_cut_track.sequencer_track_add_section()
#     section.CameraBindingID = MovieSceneObjectBindingID(Guid=ue.string_to_guid(cam_spawnable_guid), Space=EMovieSceneObjectBindingSpace.Local)
#     section.sequencer_set_section_range(seq_start,seq_end)

#     default_track = seq_asset.MovieScene.ObjectBindings[0].Tracks[0]
#     seq_asset.sequencer_remove_track(default_track)

#     transform_track = seq_asset.sequencer_add_track(MovieScene3DTransformTrack, cam_spawnable_guid)
#     transform_section = transform_track.sequencer_track_add_section()
#     transform_section.sequencer_set_section_range(seq_start,seq_end)

#     seq_asset.MovieScene.FixedFrameInterval = frameRateDenominator/frameRateNumerator

#     transform_section.sequencer_import_fbx_transform(cam_fbx_path, "Camera")
    
#     seq_asset.sequencer_set_playback_range(seq_start,seq_end)
#     seq_asset.sequencer_set_view_range(seq_start,seq_end)
#     seq_asset.sequencer_set_working_range(seq_start,seq_end)


# extractor = FbxCurvesExtractor(cam_fbx_path)
# for stack in extractor.get_anim_stacks():
#     for layer in extractor.get_anim_layers(stack):
#         for curve in extractor.get_anim_curves(layer):
#             print (curve)

TargetSequence = ue.load_object(LevelSequence,"/Game/MasterSequence")

# TargetSequence.sequencer_set_playback_range(0,30)

world =ue.get_editor_world()

cine_camera = world.actor_spawn(CineCameraActor)
# cine_camera_guid = TargetSequence.sequencer_add_actor(cine_camera)


# ass_cam(TargetSequence, cam_fbx_path)
