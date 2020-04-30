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

def ass_char(seq_asset,fbx_path,start_frame,end_frame):
    

    fbx_path = '/Game/Sequence/EP001/SC015/P001/0008/character/EP001_SC015_P001_0008_CH_ChenMo_DesertOld'

    fbx_skel = ue.load_object(SkeletalMesh,'/Game/Character/ChenMo_DesertOld/Meshes/SK_CH_ChenMo_DesertOld')

    world = ue.get_editor_world()
    fbx_ani = ue.load_object(AnimSequence,fbx_path)

    character = world.actor_spawn(SkeletalMeshActor)
    cha_name = fbx_path.split('/')[-1]
    character.set_actor_label(cha_name)
    character.modify()

    comp = character.get_property('SkeletalMeshComponent')
    comp.set_property('SkeletalMesh', fbx_skel)
    comp.BoundsScale = 100
    character.post_edit_change()

    guid = seq_asset.sequencer_make_new_spawnable(character)
    character.actor_destroy()

    anim = seq_asset.sequencer_add_track(MovieSceneSkeletalAnimationTrack, guid)
    anim_sequence = anim.sequencer_track_add_section()
    anim_sequence.sequencer_set_section_range(float(start_frame)/float(25),float(end_frame)/float(25))
    anim_sequence.Params.Animation = fbx_ani

    seq_asset.sequencer_changed(True)
    seq_asset.save_package()