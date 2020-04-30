#!/usr/bin/python
# -*- coding: utf-8 -*-
#Author : HW
#--2019-08-05
import unreal_engine as ue
from unreal_engine.classes import LevelSequence,SkeletalMesh,Actor,PlayerStart,SkeletalMeshActor,LevelSequenceActor
from unreal_engine.classes import LevelSequenceFactoryNew, MovieSceneSkeletalAnimationTrack, SkeletalMesh, MovieScene3DTransformTrack, CineCameraActor, AnimSequence
from unreal_engine.structs import FloatRange, FloatRangeBound, MovieSceneObjectBindingID,MovieSceneSpawnable
from unreal_engine.enums import EMovieSceneObjectBindingSpace
import re

class Sequence(object):
    def __init__(self, seq_info_cam, Clear_shot, camera= None, ch_pr= None):
        super(Sequence,self).__init__()
        self.frameRateDenominator = 1.0
        self.frameRateNumerator = 25.0
        self.seq_info_cam = seq_info_cam.split('_')
        self.seq_shot_name = self.seq_info_cam[:4]
        self.Clear_shot = Clear_shot
        self.camera = camera
        self.ch_pr = ch_pr

        self.focal = self.seq_info_cam[-3]
        self.start_frame = self.seq_info_cam[-2]
        self.end_frame = self.seq_info_cam[-1].split('.')[0]

        self.seq_start = float(self.start_frame)/float(self.frameRateNumerator)
        self.seq_end = float(self.end_frame)/float(self.frameRateNumerator)

    def get_ass_seq(self,seq_shot_name):
        #seq_shot_name = ['EP','SC','P','SHOT',]
        seq_path = '/Game/Sequence/'
        for i in seq_shot_name:
            seq_path = seq_path + i + '/'

        seq_loction = seq_path + seq_shot_name[3] + '_1'

        exist = ue.find_asset(seq_loction)

        if exist:
            seq_asset = ue.load_object(LevelSequence, seq_loction)
        else:
            factory = LevelSequenceFactoryNew()
            seq_asset = factory.factory_create_new(seq_loction)
        return seq_asset

    def set_seq_range(self,seq_asset):
        seq_asset.MovieScene.FixedFrameInterval = 1.0/self.frameRateNumerator
        seq_asset.sequencer_set_playback_range(self.seq_start,self.seq_end)
        seq_asset.sequencer_set_view_range(self.seq_start,self.seq_end)
        seq_asset.sequencer_set_working_range(self.seq_start,self.seq_end)

    def clear_seq_cam(self,seq_asset):
        #print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>:  clear sequence camera -------------------------------------')
        try:
            cam = seq_asset.sequencer_get_camera_cut_track()
            seq_asset.sequencer_remove_camera_cut_track(cam)
            seq_asset.sequencer_changed(True)
        except:
            pass 
        seq_cam_lis = ['','']
        for i in seq_asset.MovieScene.ObjectBindings:
            guid = ue.guid_to_string(i.ObjectGuid)
            if '_Cam' in i.BindingName:
                seq_cam_lis[0] = guid

            elif i.BindingName == 'CameraComponent':
                seq_cam_lis[1] = guid

        if seq_cam_lis[0] !='':
            #print ('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>:  clear sequence _Cam -------------------------------------')
            seq_asset.sequencer_remove_spawnable(seq_cam_lis[0])
        if seq_cam_lis[1] !='':
            #print ('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>:  clear sequence CameraComponent -------------------------------------')
            seq_asset.sequencer_remove_possessable(seq_cam_lis[1])
            
        seq_asset.sequencer_changed(True)

    def clear_seq_char(self,seq_asset,char_path):
        char_name = char_path.split('/')[-1]
        try:
            for x in seq_asset.MovieScene.ObjectBindings:
                if char_name == x.BindingName:
                    guid = ue.guid_to_string(x.ObjectGuid)
                    seq_asset.sequencer_remove_spawnable(guid)
                    seq_asset.sequencer_changed(True)
        except:
            pass 

    def clear_seq(self,seq_asset):

        self.clear_seq_cam(seq_asset)

        try:
            for i in seq_asset.sequencer_possessables_guid():
                seq_asset.sequencer_remove_possessable(i)
        except:
            pass
        guid_list = []
        for i in seq_asset.MovieScene.ObjectBindings:
            guid = ue.guid_to_string(i.ObjectGuid)
            guid_list.append(guid)
        if guid_list:
            for x in guid_list:
                seq_asset.sequencer_remove_spawnable(x)
        seq_asset.sequencer_changed(True)

    def assemble_cam(self,seq_asset,cam_fbx_path):

        #cam_fbx_path = 'H:/XHQS_Project01/3D_Project/branches/assets/Export/EP001/SC015/SC015_P001/SC015_P001_0008/EP001_SC015_P001_0008_Camera_50_674_718.fbx'

        cam_list = cam_fbx_path.split('/')[-1].split('.')[0].split('_')

        spawn_cam_name = cam_list[0]+'_'+cam_list[1]+'_'+cam_list[2]+'_'+cam_list[3]+'_'+'Cam'

        world = ue.get_editor_world()
        Cam = world.actor_spawn(CineCameraActor)
        Cam.set_actor_label(spawn_cam_name)
        Cam.CameraComponent.post_edit_change()
        Cam.CameraComponent.CurrentFocalLength = float(self.focal)
        Cam.CameraComponent.FilmbackSettings.SensorWidth = float(36.0) 
        Cam.CameraComponent.FilmbackSettings.SensorHeight = float(20.25)
        Cam.CameraComponent.post_edit_change()
        Cam.CameraComponent.FocusSettings.FocusMethod = 0

        cam_spawnable_guid = seq_asset.sequencer_make_new_spawnable(Cam)
        Cam.actor_destroy()
        camera_cut_track = seq_asset.sequencer_add_camera_cut_track()
        section = camera_cut_track.sequencer_track_add_section()
        section.CameraBindingID = MovieSceneObjectBindingID(Guid=ue.string_to_guid(cam_spawnable_guid), Space=EMovieSceneObjectBindingSpace.Local)
        section.sequencer_set_section_range(self.seq_start,self.seq_end)


        for i in seq_asset.MovieScene.ObjectBindings:

            if '_Cam' in i.BindingName:

                default_track = i.Tracks[0]

                seq_asset.sequencer_remove_track(default_track)

        transform_track = seq_asset.sequencer_add_track(MovieScene3DTransformTrack, cam_spawnable_guid)
        transform_section = transform_track.sequencer_track_add_section()
        transform_section.sequencer_set_section_range(self.seq_start,self.seq_end)

        transform_section.sequencer_import_fbx_transform(cam_fbx_path, "Camera")
        seq_asset.sequencer_changed(True)
        seq_asset.save_package()

    def get_cha_pro_asset(self,ue_ani_asset_path):
        ue_ani_name = ue_ani_asset_path.split('/')[-1]
        lis = ue_ani_name.split('_')
        if lis[4] =='CH' or lis[4] == 'PR':
            lens = len(lis[5:])
            if lens == 2:

                ch_pro_name_vs = lis[-2] +  '_' + lis[-1]
            elif lens ==1:
                ch_pro_name_vs = lis[-1]
            else:
                pass

            pattern = re.compile(r'\d+')
            vison = pattern.search(ch_pro_name_vs)
            if vison:
                ch_pro_name = ch_pro_name_vs.rstrip(vison.group())
            else:
                ch_pro_name = ch_pro_name_vs

            if lis[4] =='CH':
                skel_asset_loction = '/Game/Character/{}/Meshes/SK_CH_{}'.format(ch_pro_name,ch_pro_name)
                return skel_asset_loction

            elif lis[4] == 'PR':
                skel_asset_loction = '/Game/Prop/{}/Meshes/SK_PR_{}'.format(ch_pro_name,ch_pro_name)
                return skel_asset_loction
            else:
                pass

        elif lis[4] == 'PROP':

            skel_asset_loction = ue_ani_asset_path[:-5]
            return skel_asset_loction
        else:
            pass

    def assemble_char(self,seq_asset,ue_ani_asset_path):
    
        #ue_ani_asset_path = '/Game/Sequence/EP001/SC015/P001/0008/character/EP001_SC015_P001_0008_CH_ChenMo_DesertOld'

        skel_asset_loction = self.get_cha_pro_asset(ue_ani_asset_path)
        #'/Game/Character/ChenMo_DesertOld/Meshes/SK_CH_ChenMo_DesertOld'
        fbx_skel = ue.load_object(SkeletalMesh,skel_asset_loction)

        world = ue.get_editor_world()
        fbx_ani = ue.load_object(AnimSequence,ue_ani_asset_path)

        character = world.actor_spawn(SkeletalMeshActor)
        cha_name = ue_ani_asset_path.split('/')[-1]
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
        anim_sequence.sequencer_set_section_range(self.seq_start,self.seq_end)
        anim_sequence.Params.Animation = fbx_ani

        seq_asset.sequencer_changed(True)
        seq_asset.save_package()

    def Assemble_seq(self):
        seq_asset = self.get_ass_seq(self.seq_shot_name)
        self.set_seq_range(seq_asset)
        if self.Clear_shot == True:
            self.clear_seq(seq_asset)
        if self.camera != None:
            self.clear_seq_cam(seq_asset)
            self.assemble_cam(seq_asset,self.camera)
        if self.ch_pr != None:
            self.clear_seq_char(seq_asset,self.ch_pr)
            self.assemble_char(seq_asset,self.ch_pr)
