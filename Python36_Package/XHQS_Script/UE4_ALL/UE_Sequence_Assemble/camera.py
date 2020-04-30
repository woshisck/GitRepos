#!/usr/bin/python
# -*- coding: utf-8 -*-
#Author : HW
#--2019-08-05
import unreal_engine as ue
from unreal_engine.classes import GeometryCache,LevelSequence,SkeletalMesh,Actor,PlayerStart,SkeletalMeshActor,LevelSequenceActor
from unreal_engine.classes import MovieSceneAudioTrack, LevelSequenceFactoryNew, MovieSceneSkeletalAnimationTrack, Character, SkeletalMesh, MovieScene3DTransformTrack, CineCameraActor, AnimSequence
from unreal_engine.structs import FloatRange, FloatRangeBound, MovieSceneObjectBindingID,MovieSceneSpawnable
from unreal_engine import FTransform, FVector
from unreal_engine.enums import EMovieSceneObjectBindingSpace

def ass_cam(seq_asset,cam_fbx_path):

    frameRateDenominator = 1.0
    frameRateNumerator = 25

    #cam_fbx_path = 'H:/XHQS_Project01/3D_Project/branches/assets/Export/EP001/SC015/SC015_P001/SC015_P001_0008/EP001_SC015_P001_0008_Camera_50_674_718.fbx'

    cam_list = cam_fbx_path.split('/')[-1].split('.')[0].split('_')

    focal = cam_list[-3]
    start_frame = cam_list[-2]
    end_frame = cam_list[-1]

    seq_start = float(start_frame)/float(frameRateNumerator)
    seq_end = float(end_frame)/float(frameRateNumerator)

    spawn_cam_name = cam_list[0]+'_'+cam_list[1]+'_'+cam_list[2]+'_'+cam_list[3]+'_'+'Cam'

    world = ue.get_editor_world()
    Cam = world.actor_spawn(CineCameraActor)
    Cam.set_actor_label(spawn_cam_name)
    Cam.CameraComponent.post_edit_change()
    Cam.CameraComponent.CurrentFocalLength = int(focal)
    Cam.CameraComponent.FilmbackSettings.SensorWidth = float(36.0) 
    Cam.CameraComponent.FilmbackSettings.SensorHeight = float(20.25)
    Cam.CameraComponent.post_edit_change()
    Cam.CameraComponent.FocusSettings.FocusMethod = 0



    cam_spawnable_guid = seq_asset.sequencer_make_new_spawnable(Cam)
    Cam.actor_destroy()
    camera_cut_track = seq_asset.sequencer_add_camera_cut_track()
    section = camera_cut_track.sequencer_track_add_section()
    section.CameraBindingID = MovieSceneObjectBindingID(Guid=ue.string_to_guid(cam_spawnable_guid), Space=EMovieSceneObjectBindingSpace.Local)
    section.sequencer_set_section_range(seq_start,seq_end)

    default_track = seq_asset.MovieScene.ObjectBindings[0].Tracks[0]
    seq_asset.sequencer_remove_track(default_track)

    transform_track = seq_asset.sequencer_add_track(MovieScene3DTransformTrack, cam_spawnable_guid)
    transform_section = transform_track.sequencer_track_add_section()
    transform_section.sequencer_set_section_range(seq_start,seq_end)

    seq_asset.MovieScene.FixedFrameInterval = frameRateDenominator/frameRateNumerator

    transform_section.sequencer_import_fbx_transform(cam_fbx_path, "Camera")
    
    seq_asset.sequencer_set_playback_range(seq_start,seq_end)
    seq_asset.sequencer_set_view_range(seq_start,seq_end)
    seq_asset.sequencer_set_working_range(seq_start,seq_end)

