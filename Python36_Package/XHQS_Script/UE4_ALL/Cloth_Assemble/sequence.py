#!/usr/bin/python
# -*- coding: utf-8 -*-
 

# 该模块是ue中sequence组装的所有功能模块
# 包括导入ue python相应的包


import unreal_engine as ue
from unreal_engine.classes import LevelSequence,SkeletalMesh,Actor,PlayerStart,SkeletalMeshActor,LevelSequenceActor
from unreal_engine.classes import LevelSequenceFactoryNew, MovieSceneSkeletalAnimationTrack, SkeletalMesh, MovieScene3DTransformTrack, CineCameraActor, AnimSequence
from unreal_engine.structs import FloatRange, FloatRangeBound, MovieSceneObjectBindingID,MovieSceneSpawnable
from unreal_engine.enums import EMovieSceneObjectBindingSpace
import re

class Sequence(object):
    def __init__(self, seq_info_cam, Clear_shot, camera= None, ch_pr= None):
        super(Sequence,self).__init__()
        #定义镜头帧数率
        self.frameRateDenominator = 1.0
        self.frameRateNumerator = 25.0
        #从相机获取镜头名称
        self.seq_info_cam = seq_info_cam.split('_')
        self.seq_shot_name = self.seq_info_cam[:4]

        self.Clear_shot = Clear_shot
        self.camera = camera
        self.ch_pr = ch_pr
        #从相机获取 焦距 镜头起始帧和结束帧。
        self.focal = self.seq_info_cam[-3]
        self.start_frame = 0#self.seq_info_cam[-2]
        self.start_frame_p = self.seq_info_cam[-2]
        self.end_frame = self.seq_info_cam[-1].split('.')[0]
        #通过帧速率 和 起始帧 结束帧 换算sequence 的开始时间和结束时间。
        self.seq_start = float(self.start_frame)/float(self.frameRateNumerator)
        self.seq_start_p = float(self.start_frame_p)/float(self.frameRateNumerator)
        self.seq_end = float(self.end_frame)/float(self.frameRateNumerator)

    def get_ass_seq(self,seq_shot_name): # 获取要组装的sequence ue资产
        #seq_shot_name = ['EP','SC','P','SHOT',]
        seq_shot = '_'.join(seq_shot_name)
        seq_path = '/Game/Sequence/'
        for i in seq_shot_name:
            seq_path = seq_path + i + '/'

        seq_loction = seq_path +'CFX/'+ seq_shot + '_CFX'  #定位sequence

        exist = ue.find_asset(seq_loction) #读取ue资产
        #如果不存在就生成一个新的。
        if exist:
            seq_asset = ue.load_object(LevelSequence, seq_loction)
        else:
            factory = LevelSequenceFactoryNew()
            seq_asset = factory.factory_create_new(seq_loction)
        return seq_asset

    def set_seq_range(self,seq_asset): #设置sequence的播放速率和播放器各种范围 
        seq_asset.MovieScene.FixedFrameInterval = 1.0/self.frameRateNumerator
        seq_asset.sequencer_set_playback_range(self.seq_start_p,self.seq_end)
        seq_asset.sequencer_set_view_range(self.seq_start_p,self.seq_end)
        seq_asset.sequencer_set_working_range(self.seq_start_p,self.seq_end)

    def clear_seq_cam(self,seq_asset):#清理sequence中的相机部件 包括相机剪辑 和相机部件轨道
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

    def clear_seq_char(self,seq_asset,char_path): #清理sequence中的角色
        char_name = char_path.split('/')[-1]
        try:
            for x in seq_asset.MovieScene.ObjectBindings:
                if char_name == x.BindingName:
                    guid = ue.guid_to_string(x.ObjectGuid)
                    seq_asset.sequencer_remove_spawnable(guid)
                    seq_asset.sequencer_changed(True)
        except:
            pass 

    def clear_seq(self,seq_asset):#当GUI中的Clear_shot 复选框被勾选时 会启动该功能，在组装资产之前清理sequence

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

    def assemble_cam(self,seq_asset,cam_fbx_path): #组装相机功能 

        #cam_fbx_path = 'H:/XHQS_Project01/3D_Project/branches/assets/Export/EP001/SC015/SC015_P001/SC015_P001_0008/EP001_SC015_P001_0008_Camera_50_674_718.fbx'

        cam_list = cam_fbx_path.split('/')[-1].split('.')[0].split('_') #根据相机fbx文件拆分出相机信息。

        spawn_cam_name = cam_list[0]+'_'+cam_list[1]+'_'+cam_list[2]+'_'+cam_list[3]+'_'+'Cam' #用于相机命名
        #获取世界关卡
        world = ue.get_editor_world()
        #在关卡中创建相机
        Cam = world.actor_spawn(CineCameraActor)
        Cam.set_actor_label(spawn_cam_name)
        Cam.CameraComponent.post_edit_change()
        #设置相机焦距，画面纵横，关闭景深。
        Cam.CameraComponent.CurrentFocalLength = float(self.focal)
        Cam.CameraComponent.FilmbackSettings.SensorWidth = float(36.0) 
        Cam.CameraComponent.FilmbackSettings.SensorHeight = float(20.25)
        Cam.CameraComponent.post_edit_change()
        Cam.CameraComponent.FocusSettings.FocusMethod = 0
        #将相机添加进sequence
        cam_spawnable_guid = seq_asset.sequencer_make_new_spawnable(Cam)
        Cam.actor_destroy()

        camera_cut_track = seq_asset.sequencer_add_camera_cut_track()#添加相机剪辑
        section = camera_cut_track.sequencer_track_add_section()#给相机剪辑添加轨道
        #将相机跟相机剪辑关联 
        section.CameraBindingID = MovieSceneObjectBindingID(Guid=ue.string_to_guid(cam_spawnable_guid), Space=EMovieSceneObjectBindingSpace.Local)
        section.sequencer_set_section_range(self.seq_start,self.seq_end)

        #清理之前的相机

        for i in seq_asset.MovieScene.ObjectBindings:

            if '_Cam' in i.BindingName:

                default_track = i.Tracks[0]

                seq_asset.sequencer_remove_track(default_track)

        #添加相机轨道设置范围
        transform_track = seq_asset.sequencer_add_track(MovieScene3DTransformTrack, cam_spawnable_guid)
        transform_section = transform_track.sequencer_track_add_section()
        transform_section.sequencer_set_section_range(self.seq_start,self.seq_end)
        #导入相机fbx的动画数据。
        transform_section.sequencer_import_fbx_transform(cam_fbx_path, "Camera")
        seq_asset.sequencer_changed(True)
        seq_asset.save_package()

    def get_cha_pro_asset(self,ue_ani_asset_path):#获取角色道具的UE骨架资产
        # ue_ani_name = ue_ani_asset_path.split('/')[-1]
        # lis = ue_ani_name.split('_') 
        #*******************************************判定是角色或者道具
        # if lis[4] =='CH' or lis[4] == 'PR':
        #     lens = len(lis[5:])
        #     # 获得角色或者道具名称+版本号
        #     if lens == 2:
        #         ch_pro_name_vs = lis[-2] +  '_' + lis[-1]
        #     elif lens ==1:
        #         ch_pro_name_vs = lis[-1]
        #     else:
        #         pass
        #     #通过正则 提取版本号 从而获得角色道具名称
        #     pattern = re.compile(r'\d+')
        #     vison = pattern.search(ch_pro_name_vs)
        #     if vison:
        #         ch_pro_name = ch_pro_name_vs.rstrip(vison.group())
        #     else:
        #         ch_pro_name = ch_pro_name_vs


        #     # 获取角色道具相应资产
        #     if lis[4] =='CH':
        #         skel_asset_loction = '/Game/Character/{}/Meshes/SK_CH_{}'.format(ch_pro_name,ch_pro_name)
        #         return skel_asset_loction

        #     elif lis[4] == 'PR':
        #         skel_asset_loction = '/Game/Prop/{}/Meshes/SK_CH_{}'.format(ch_pro_name,ch_pro_name)
        #         return skel_asset_loction
        #     else:
        #         pass
        #*********************************** 否则是场景道具部件（从ue镜头路径下拾取骨架资产，之后需要材质部门单独上材质）
        # elif lis[4] == 'PROP':

        skel_asset_loction = ue_ani_asset_path[:-10]
 
        return skel_asset_loction


    def assemble_char(self,seq_asset,ue_ani_asset_path): #组装角色 
    
        #ue_ani_asset_path = '/Game/Sequence/EP001/SC015/P001/0008/character/EP001_SC015_P001_0008_CH_ChenMo_DesertOld'

        skel_asset_loction = self.get_cha_pro_asset(ue_ani_asset_path) #获取相应的角色道具骨架资产
        #'/Game/Character/ChenMo_DesertOld/Meshes/SK_CH_ChenMo_DesertOld'
        fbx_skel = ue.load_object(SkeletalMesh,skel_asset_loction) #获取加载骨架资产 
        #获取当前世界关卡
        world = ue.get_editor_world()

        fbx_ani = ue.load_object(AnimSequence,ue_ani_asset_path[:-10]+'.'+ue_ani_asset_path.split('/')[-1]) # 获取加载动画资源

        #在世界关卡中生成演员并命名
        character = world.actor_spawn(SkeletalMeshActor)
        cha_name = ue_ani_asset_path.split('/')[-1]
        character.set_actor_label(cha_name)
        character.modify()
        #将骨架资产填充到关卡中演员的骨架插槽中
        comp = character.get_property('SkeletalMeshComponent')
        comp.set_property('SkeletalMesh', fbx_skel)
        comp.BoundsScale = 100
        character.post_edit_change()

        #将演员放入sequence 并启用引用关系
        guid = seq_asset.sequencer_make_new_spawnable(character)
        character.actor_destroy() # 干掉非引用性质演员
        #为sequence中的演员添加轨道，设置范围，添加动画数据。
        anim = seq_asset.sequencer_add_track(MovieSceneSkeletalAnimationTrack, guid)
        anim_sequence = anim.sequencer_track_add_section()
        anim_sequence.sequencer_set_section_range(self.seq_start,self.seq_end)
        anim_sequence.Params.Animation = fbx_ani

        seq_asset.sequencer_changed(True)
        seq_asset.save_package()

    def Assemble_seq(self): #该组装类的启动函数。

        seq_asset = self.get_ass_seq(self.seq_shot_name) #获取要组装的sequence
        self.set_seq_range(seq_asset) # 设置一些列范围
        # 判定组装选项需求。并执行组装
        if self.Clear_shot == True:
            self.clear_seq(seq_asset)
        if self.camera != None:
            pass
            # self.clear_seq_cam(seq_asset)
            # self.assemble_cam(seq_asset,self.camera)
        if self.ch_pr != None:
            self.clear_seq_char(seq_asset,self.ch_pr)
            self.assemble_char(seq_asset,self.ch_pr)
