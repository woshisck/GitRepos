#!/usr/bin/python
# -*- coding: utf-8 -*-


# 该模块是ue中sequence组装的所有功能模块
# 包括导入ue python相应的包


import re
import unreal_engine as ue
from unreal_engine.classes import LevelSequence,SkeletalMesh,Actor,PlayerStart,SkeletalMeshActor,LevelSequenceActor,MovieSceneSubTrack
from unreal_engine.classes import LevelSequenceFactoryNew, MovieSceneSkeletalAnimationTrack, SkeletalMesh, MovieScene3DTransformTrack, CineCameraActor, AnimSequence
from unreal_engine.classes import Blueprint
from unreal_engine import FTransform, FVector, FRotator
from unreal_engine.classes import MovieScene3DAttachTrack
from unreal_engine.classes import WorldFactory
from unreal_engine.structs import FloatRange, FloatRangeBound, MovieSceneObjectBindingID,MovieSceneSpawnable
#from unreal_engine.classes import LevelStreamingKismet
from unreal_engine.enums import EMovieSceneObjectBindingSpace
from unreal_engine.structs import RichCurve, RichCurveKey
from unreal_engine.classes import MovieSceneFadeTrack

from ANI_Cha_Assemble import camera
from imp import reload

reload(camera)

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
        self.anim_movie_guid = None
        #从相机获取 焦距 镜头起始帧和结束帧。
        self.focal = self.seq_info_cam[-3]
        self.start_frame = self.seq_info_cam[-2]
        self.end_frame = self.seq_info_cam[-1].split('.')[0]
        #通过帧速率 和 起始帧 结束帧 换算sequence 的开始时间和结束时间。
        self.seq_start = float(self.start_frame)/float(self.frameRateNumerator)
        self.seq_end = float(self.end_frame)/float(self.frameRateNumerator)
        self.level_template = '/Game/Sequence/{EP_Number}/{SC_Number}/{P_Number}/{Shot_Number}'
        self.level_name_template = '{EP_Number}_{SC_Number}_{P_Number}_{Shot_Number}_MAP'

    def get_ani_seq(self,seq_shot_name): # 获取要组装的sequence ue资产
        #seq_shot_name = ['EP','SC','P','SHOT',]
        seq_shot = '_'.join(seq_shot_name)
        seq_path = '/Game/Sequence/'
        for i in seq_shot_name:
            seq_path = seq_path + i + '/'

        seq_loction = seq_path +'Animation/'+ seq_shot + '_Animation'   #定位sequence

        exist = ue.find_asset(seq_loction) #读取ue资产
        #如果不存在就生成一个新的。
        if exist:
            seq_asset = ue.load_object(LevelSequence, seq_loction)
        else:
            factory = LevelSequenceFactoryNew()
            seq_asset = factory.factory_create_new(seq_loction)
        return seq_asset

    def get_total_seq(self,seq_shot_name): # 获取要组装的sequence ue资产
        #seq_shot_name = ['EP','SC','P','SHOT',]
        seq_shot = '_'.join(seq_shot_name)
        seq_path = '/Game/Sequence/'
        for i in seq_shot_name:
            seq_path = seq_path + i + '/'

        seq_loction = seq_path + seq_shot #定位sequence

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
        seq_asset.sequencer_set_playback_range(self.seq_start,self.seq_end)
        seq_asset.sequencer_set_view_range(self.seq_start,self.seq_end)
        seq_asset.sequencer_set_working_range(self.seq_start,self.seq_end)

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
        cha_channel = [True,False,False]

        seq_asset.sequencer_changed(True)
        world = ue.get_editor_world()
        all_actors = world.all_actors()
        for char in all_actors:
            if char_name in char.get_name() and '_Move' not in char.get_name():
                if not char.has_property('SkeletalMeshComponent'):
                    continue
                comp = char.get_property('SkeletalMeshComponent')
                cha_channel[0] = comp.LightingChannels.bChannel0
                cha_channel[1] = comp.LightingChannels.bChannel1
                cha_channel[2] = comp.LightingChannels.bChannel2


        for x in seq_asset.MovieScene.ObjectBindings:
            if char_name == x.BindingName:
                guid = ue.guid_to_string(x.ObjectGuid)
                seq_asset.sequencer_remove_spawnable(guid)
                seq_asset.sequencer_changed(True)

        return cha_channel

    def clear_seq_move(self,seq_asset,char_path): #清理sequence中的角色的 move骨骼
        char_move_name = char_path.split('/')[-1] + '_Move'
        try:
            for x in seq_asset.MovieScene.ObjectBindings:
                if char_move_name == x.BindingName:
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

        #清理默认的相机  transform

        for i in seq_asset.MovieScene.ObjectBindings:

            if '_Cam' in i.BindingName:
                # i.bIsLocked = True

                default_track = i.Tracks[0]

                seq_asset.sequencer_remove_track(default_track)

        #添加相机轨道设置范围
        transform_track = seq_asset.sequencer_add_track(MovieScene3DTransformTrack, cam_spawnable_guid)
        transform_section = transform_track.sequencer_track_add_section()
        transform_section.sequencer_set_section_range(self.seq_start,self.seq_end)
        transform_section.bIsLocked = True
        for obj in seq_asset.MovieScene.ObjectBindings:
            if obj.BindingName == 'CameraComponent':

                for x in obj.tracks:
                    if x.sequencer_get_display_name() == 'CurrentFocalLength':
                        for j in x.sequencer_track_sections():
                            camera_section = j

                            j.StartTime = 0
                            j.EndTime = 20000
                            # j.sequencer_section_add_key(5.8,30)

        #导入相机fbx的动画数据。
        camera.set_cam_key(camera_section,cam_fbx_path)
        transform_section.sequencer_import_fbx_transform(cam_fbx_path, "Camera")

        for obj in seq_asset.MovieScene.ObjectBindings:
            # if '_Cam' in i.BindingName:
            #     for x in obj.tracks:
            #         x.IsNodeLocked = True
                    # for j in x.sequencer_track_sections():
                    #     j.bIsLocked = True


            if obj.BindingName == 'CameraComponent':
                for x in obj.tracks:
                    for j in x.sequencer_track_sections():
                        j.bIsLocked = True




        seq_asset.sequencer_changed(True)
        seq_asset.save_package()

    def get_cha_pro_asset(self,ue_ani_asset_path):#获取角色道具的UE骨架资产
        ue_ani_name = ue_ani_asset_path.split('/')[-1]
        lis = ue_ani_name.split('_')
 
        fbx_ani = ue.load_object(AnimSequence,ue_ani_asset_path)
        character_sk = fbx_ani.Skeleton
        sk_path = character_sk.get_path_name().split('.')[0].rsplit('_',1)[0]
        #*******************************************判定是角色或者道具
        if lis[4] =='CH' or lis[4] == 'PR':
            lens = len(lis[5:])
            # 获得角色或者道具名称+版本号
            if lens == 2:
                ch_pro_name_vs = lis[-2] +  '_' + lis[-1]
            elif lens ==1:
                ch_pro_name_vs = lis[-1]
            else:
                pass
            #通过正则 提取版本号 从而获得角色道具名称
            pattern = re.compile(r'\d+')
            vison = pattern.search(ch_pro_name_vs)
            if vison:
                ch_pro_name = ch_pro_name_vs.rstrip(vison.group())
            else:
                ch_pro_name = ch_pro_name_vs


            # 获取角色道具相应资产
            if lis[4] =='CH':
                #skel_asset_loction = '/Game/Character/{}/SKMesh/SK_CH_{}'.format(ch_pro_name,ch_pro_name)
                skel_asset_loction = sk_path
                print('-----------------------------------get CH SK Mesh path-----------------------------------------------',sk_path)
                return skel_asset_loction

            elif lis[4] == 'PR':
                #skel_asset_loction = '/Game/Prop/{}/SKMesh/SK_CH_{}'.format(ch_pro_name,ch_pro_name)
                skel_asset_loction = sk_path
                print('-----------------------------------get PR SK Mesh path-----------------------------------------------',sk_path)
                return skel_asset_loction
            else:
                pass
        #*********************************** 否则是场景道具部件（从ue镜头路径下拾取骨架资产，之后需要材质部门单独上材质）
        elif lis[4] == 'PROP':

            skel_asset_loction = ue_ani_asset_path[:-5]
            return skel_asset_loction
        else:
            pass

    def assemble_char(self,seq_asset,ue_ani_asset_path,cha_channel): #组装角色

        #ue_ani_asset_path = '/Game/Sequence/EP001/SC015/P001/0008/character/EP001_SC015_P001_0008_CH_ChenMo_DesertOld'

        skel_asset_loction = self.get_cha_pro_asset(ue_ani_asset_path) #获取相应的角色道具骨架资产
        #'/Game/Character/ChenMo_DesertOld/Meshes/SK_CH_ChenMo_DesertOld'
        fbx_skel = ue.load_object(SkeletalMesh,skel_asset_loction) #获取加载骨架资产
        #获取当前世界关卡
        world = ue.get_editor_world()

        fbx_ani = ue.load_object(AnimSequence,ue_ani_asset_path) # 获取加载动画资源

        #在世界关卡中生成演员并命名
        character = world.actor_spawn(SkeletalMeshActor)

        cha_name = ue_ani_asset_path.split('/')[-1]
        character.set_actor_label(cha_name)
        character.modify()
        #将骨架资产填充到关卡中演员的骨架插槽中
        comp = character.get_property('SkeletalMeshComponent')
        comp.set_property('SkeletalMesh', fbx_skel)
        comp.BoundsScale = 100

        comp.LightingChannels.bChannel0 = cha_channel[0]
        comp.LightingChannels.bChannel1 = cha_channel[1]
        comp.LightingChannels.bChannel2 = cha_channel[2]

        character.post_edit_change()

        #将演员放入sequence 并启用引用关系
        guid = seq_asset.sequencer_make_new_spawnable(character)
        character.actor_destroy() # 干掉非引用性质演员
        #为sequence中的演员添加轨道，设置范围，添加动画数据。

        for i in seq_asset.MovieScene.ObjectBindings:

            if cha_name == i.BindingName:

                trans_track = i.Tracks[0]
                ani_track = i.Tracks[1]
                seq_asset.sequencer_remove_track(trans_track)
                seq_asset.sequencer_remove_track(ani_track)

        anim = seq_asset.sequencer_add_track(MovieSceneSkeletalAnimationTrack, guid)
        anim_sequence = anim.sequencer_track_add_section()
        anim_sequence.sequencer_set_section_range(self.seq_start,self.seq_end)
        anim_sequence.Params.Animation = fbx_ani
        anim_sequence.bIsLocked = True

        if self.anim_movie_guid:
            transform_track = seq_asset.sequencer_add_track(
                MovieScene3DTransformTrack, guid
            )
            transform_section = transform_track.sequencer_track_add_section()

            transform_section.sequencer_set_section_range(self.seq_start, self.seq_end)
            rich_curve = RichCurveKey(Time=self.seq_start, Value=-90, InterpMode=2)
            transform_section.Rotation.Keys = [rich_curve]
            transform_section.bIsLocked = True

            attach_node = seq_asset.sequencer_add_track(MovieScene3DAttachTrack, guid)
            attach_sequence = attach_node.sequencer_track_add_section()

            attach_sequence.sequencer_set_section_range(self.seq_start, self.seq_end)
            attach_sequence.AttachSocketName = 'Move_Joint'
            attach_sequence.ConstraintBindingID = MovieSceneObjectBindingID(
                Guid=ue.string_to_guid(self.anim_movie_guid), Space=EMovieSceneObjectBindingSpace.Local
            )
            attach_sequence.bIsLocked = True


        seq_asset.sequencer_changed(True)
        seq_asset.save_package()



    def create_level(self, level_path, world):
        cur_world = ue.get_editor_world()

        level_base_name = level_path.rsplit('/', 1)[-1]
        level_full_path = '.'.join([level_path, level_base_name])
        level_world = ue.find_asset(level_full_path)
        level_package = ue.find_asset(level_path)
        
        if not level_package:
            factory = WorldFactory()
            level_world = factory.factory_create_new(level_path)
            level_world.save_package()
        
        if world:
            child_worlds = []
            for streaming_level in cur_world.StreamingLevels:
                if streaming_level.LoadedLevel is not None:
                    if streaming_level.LoadedLevel.get_outermost() == level_package:
                        child_worlds.append(streaming_level.LoadedLevel.get_outermost())

            if level_package not in child_worlds:
                ue.add_level_to_world(cur_world, level_world.get_path_name(),False) #LevelStreamingKismet

        level = level_world.PersistentLevel
        return level,level_world


    ## add for tc


    def create_hairworks_world(self, hairworks_level_path):
        world = ue.get_editor_world()

        hairworks_level_base_name = hairworks_level_path.rsplit('/', 1)[-1]
        hairworks_level_full_path = '.'.join(
            [hairworks_level_path, hairworks_level_base_name]
        )
        ue.log(hairworks_level_path)
        ue.log(hairworks_level_full_path)

        hairworks_level_world = ue.find_asset(hairworks_level_full_path)
        hairworks_level_package = ue.find_asset(hairworks_level_path)
        if not hairworks_level_package:
            factory = WorldFactory()
            hairworks_level_world = factory.factory_create_new(hairworks_level_path)
            hairworks_level_world.save_package()

        child_worlds = []
        for streaming_level in world.StreamingLevels:
            if streaming_level.LoadedLevel is not None:
                if streaming_level.LoadedLevel.get_outermost() == hairworks_level_package:
                    child_worlds.append(streaming_level.LoadedLevel.get_outermost())

        if hairworks_level_package not in child_worlds:
            added_streaming_level = ue.add_level_to_world(
                world, hairworks_level_world.get_path_name(), False
            )


        return hairworks_level_world


    def get_hairworks_node(self, skel_asset_loction):
        hairworks = None
        skeletion_reference_paths = ue.get_asset_referencers(skel_asset_loction)
        for skeletion_reference_path in skeletion_reference_paths:
            skeletion_reference_basename = skeletion_reference_path.rsplit('/', 1)[-1]
            skeleton_reference_full_path = '.'.join(
                [skeletion_reference_path, skeletion_reference_basename]
            )
            skeleton_reference_asset = ue.find_asset(skeleton_reference_full_path)
            if skeleton_reference_asset.is_a(Blueprint):
                if skeletion_reference_basename.lower().endswith('hairworks'):
                    hairworks = skeleton_reference_asset
                    break
        return hairworks

    def find_or_crate_main_level(self):
        world = ue.get_editor_world()
        EP_Number, SC_Number, P_Number, Shot_Number = self.seq_shot_name
        main_level_path_format = self.level_template.format(**locals())
        main_level_name_format = self.level_name_template.format(**locals())
        main_level_path = '/'.join([main_level_path_format, main_level_name_format])
        main_level_full_path = '.'.join([main_level_path, main_level_name_format])
        ue.log(main_level_path)
        main_world = ue.find_asset(main_level_full_path)
        if not main_world:
            factory = WorldFactory()
            main_world = factory.factory_create_new(main_level_path)
            main_world.save_package()

        if world.PersistentLevel != main_world.PersistentLevel:
            world.save_package()
            ue.open_editor_for_asset(main_world)
        return main_level_path_format, main_level_name_format

    def assemble_hairworks(self, seq_asset, ue_ani_asset_path):
        # 获取相应的角色道具骨架资产
        skel_asset_loction = self.get_cha_pro_asset(ue_ani_asset_path)
        hairworks_node = self.get_hairworks_node(skel_asset_loction)
        if not hairworks_node:
            return
        hairworks_actor_label = '{}_hairwork'.format(ue_ani_asset_path.rsplit('/', 1)[-1])
        hairworks_node.get_display_name()
        for object_binding in seq_asset.MovieScene.ObjectBindings:
            if object_binding.BindingName == hairworks_actor_label:
                guid = ue.guid_to_string(object_binding.ObjectGuid)
                seq_asset.sequencer_remove_possessable(guid)
        seq_asset.save_package()

        main_level_path_format, main_level_name_format = self.find_or_crate_main_level()
        world = ue.get_editor_world()
        current_level = world.get_current_level()
        level_mode = 'CFX'
        cfx_level_name = '_'.join([main_level_name_format, level_mode])

        hairworks_level_path = '/'.join([main_level_path_format, level_mode, cfx_level_name])
        ue.log(hairworks_level_path)
        hairworks_level_world = self.create_hairworks_world(hairworks_level_path)
        hairworks_level = hairworks_level_world.PersistentLevel
        world.set_current_level(hairworks_level)
        level_actors = ue.get_editor_world().all_actors()
        for level_actor in level_actors:
            if level_actor.get_actor_label() == hairworks_actor_label:
                level_actor.actor_destroy()
        hairworks_node_actor = ue.get_editor_world().actor_spawn(hairworks_node.GeneratedClass)
        hairworks_node_actor.set_actor_label(hairworks_actor_label)
        seq_asset.sequencer_changed(True)
        hairworks_node_guid = seq_asset.sequencer_add_actor(hairworks_node_actor)
        ue.get_editor_world().set_current_level(current_level)
        hairworks_level_world.save_package()

        # 获取加载动画资源
        fbx_ani = ue.load_object(AnimSequence, ue_ani_asset_path)
        anim = seq_asset.sequencer_add_track(MovieSceneSkeletalAnimationTrack, hairworks_node_guid)
        anim_sequence = anim.sequencer_track_add_section()
        anim_sequence.sequencer_set_section_range(self.seq_start, self.seq_end)
        anim_sequence.Params.Animation = fbx_ani
        anim_sequence.bIsLocked = True

        if self.anim_movie_guid:
            transform_track = seq_asset.sequencer_add_track(
                MovieScene3DTransformTrack, hairworks_node_guid
            )
            transform_section = transform_track.sequencer_track_add_section()
            transform_section.sequencer_set_section_range(self.seq_start, self.seq_end)
            rich_curve = RichCurveKey(Time=self.seq_start, Value=-90, InterpMode=2)
            transform_section.Rotation.Keys = [rich_curve]
            transform_section.bIsLocked = True

            attach_node = seq_asset.sequencer_add_track(MovieScene3DAttachTrack, hairworks_node_guid)
            attach_sequence = attach_node.sequencer_track_add_section()
            attach_sequence.sequencer_set_section_range(self.seq_start, self.seq_end)
            attach_sequence.AttachSocketName = 'Move_Joint'
            attach_sequence.ConstraintBindingID = MovieSceneObjectBindingID(
                Guid=ue.string_to_guid(self.anim_movie_guid), Space=EMovieSceneObjectBindingSpace.Local
            )
            attach_sequence.bIsLocked = True
            
        seq_asset.sequencer_changed(True)
        seq_asset.save_package()

    def assemble_move(self,seq_asset,ue_ani_asset_path): #组装角色 move 骨骼。

        #ue_ani_asset_path = '/Game/Sequence/EP001/SC015/P001/0008/Animation/EP001_SC015_P001_0008_CH_ChenMo_DesertOld'
        move_ani_asset_list = ue_ani_asset_path.split('/')
        move_ani_asset_list.insert(-1,'Move_Joint')
        move_ani_asset_path = '/'.join(move_ani_asset_list)

 
        #'/Game/Character/ChenMo_DesertOld/Meshes/SK_CH_ChenMo_DesertOld'
        skeleton_path = "/Game/Global/Move_Joint/Move_Joint"
        fbx_skel = ue.load_object(SkeletalMesh,skeleton_path) #获取加载骨架资产


        #获取当前世界关卡
        world = ue.get_editor_world()
        exist = ue.find_asset(move_ani_asset_path + '_Move')
        ue.log(exist)
        if exist:
            move_fbx_ani = ue.load_object(AnimSequence,move_ani_asset_path + '_Move') # 获取加载对应角色的Move动画资源
        else:
            move_fbx_ani = None

        if move_fbx_ani:
            #在世界关卡中生成演员并命名
            character = world.actor_spawn(SkeletalMeshActor)
            cha_name = move_ani_asset_path.split('/')[-1] + '_Move'
            character.set_actor_label(cha_name)
            character.modify()
            #将骨架资产填充到关卡中演员的骨架插槽中
            comp = character.get_property('SkeletalMeshComponent')
            comp.set_property('SkeletalMesh', fbx_skel)
            comp.BoundsScale = 100
            character.post_edit_change()

            #将演员放入sequence 并启用引用关系
            guid = seq_asset.sequencer_make_new_spawnable(character)
            self.anim_movie_guid = guid
            character.actor_destroy() # 干掉非引用性质演员
            for i in seq_asset.MovieScene.ObjectBindings:

                if cha_name == i.BindingName:

                    trans_track = i.Tracks[0]
                    ani_track = i.Tracks[1]
                    seq_asset.sequencer_remove_track(trans_track)
                    seq_asset.sequencer_remove_track(ani_track)

            #为sequence中的演员添加轨道，设置范围，添加动画数据。
            anim = seq_asset.sequencer_add_track(MovieSceneSkeletalAnimationTrack, guid)
            anim_sequence = anim.sequencer_track_add_section()
            anim_sequence.sequencer_set_section_range(self.seq_start,self.seq_end)
            anim_sequence.Params.Animation = move_fbx_ani
            anim_sequence.bIsLocked = True
            seq_asset.sequencer_changed(True)
            seq_asset.save_package()

    def Assemble_seq(self): #该组装类的启动函数。

        seq_asset = self.get_ani_seq(self.seq_shot_name) #获取要组装的sequence
        self.set_seq_range(seq_asset) # 设置一些列范围
        # 判定组装选项需求。并执行组装
        if self.Clear_shot == True:
            self.clear_seq(seq_asset)


        if self.camera != None:
            pass
            # self.clear_seq_cam(seq_asset)
            # self.assemble_cam(seq_asset,self.camera)


        if self.ch_pr != None:
            cha_channel = self.clear_seq_char(seq_asset,self.ch_pr)
            self.clear_seq_move(seq_asset,self.ch_pr)

            self.assemble_move(seq_asset,self.ch_pr)
            self.assemble_char(seq_asset,self.ch_pr,cha_channel)
            if self.anim_movie_guid:
                self.assemble_hairworks(seq_asset,self.ch_pr)
    def assemble_subseq(self,total_seq_asset):
        '''
        组装各部门sequence到总sequence中去。
        '''
        all_seq_list = self.get_all_seq(self.seq_shot_name)

        for i in all_seq_list:
            self.set_seq_range(i)

        sub_scenes_track = total_seq_asset.sequencer_master_tracks()
        FadeTrack = None
        for x in sub_scenes_track:
            track_name = x.get_display_name()
            if 'MovieSceneFadeTrack' in track_name.split('_'):
                FadeTrack = True


        if not FadeTrack:
            fade_track = total_seq_asset.sequencer_add_master_track(MovieSceneFadeTrack)
            fade_section = fade_track.sequencer_track_add_section()

            fade_section.StartTime = 0
            fade_section.EndTime = 20000

            fade_section.sequencer_section_add_key((float(self.start_frame)-5.0)/float(self.frameRateNumerator),1)
            fade_section.sequencer_section_add_key(float(self.start_frame)/float(self.frameRateNumerator),0)
            fade_section.sequencer_section_add_key(float(self.end_frame)/float(self.frameRateNumerator),0)
            fade_section.sequencer_section_add_key((float(self.end_frame)+5.0)/float(self.frameRateNumerator),1)



        section_name_list = []
        if sub_scenes_track:
            for i in sub_scenes_track:
                try:
                    section_name_list.append(i.Sections[0].SubSequence.get_display_name())
                except:
                    pass

        for seq in all_seq_list:
            if seq.get_display_name() not in section_name_list:
                sub_scenes_track = total_seq_asset.sequencer_add_master_track(MovieSceneSubTrack)
                subb = sub_scenes_track.sequencer_track_add_section()
                self.sub_seq_end = float(int(self.end_frame)+1)/float(self.frameRateNumerator)
                subb.sequencer_set_section_range(self.seq_start,self.sub_seq_end)
                subb.SubSequence= seq
                subb.bIsLocked = True
        total_seq_asset.sequencer_changed(True)
        total_seq_asset.save_package()


    def assemble_all_level(self):

        seq_shot = '_'.join(self.seq_shot_name)
        seq_path = '/Game/Sequence/'
        for i in self.seq_shot_name:
            seq_path = seq_path + i + '/'


        ep_sc_path = '/Game/Sequence/'
        ep_sc = self.seq_shot_name[:2]
        sc_name = self.seq_shot_name[1]
        for x in ep_sc:
            ep_sc_path = ep_sc_path + x + '/'


        shot_level_loction = seq_path + seq_shot +'_MAP' 
        shot_level,level_world = self.create_level(shot_level_loction,None)

        ue.open_editor_for_asset(level_world)
        
        ani_level_loction = seq_path +'Animation/'+ seq_shot + '_MAP_Animation' #定位sequence
        ani_level = self.create_level(ani_level_loction,shot_level)

        cfx_level_loction = seq_path +'CFX/'+ seq_shot + '_MAP_CFX'
        cfx_level = self.create_level(cfx_level_loction,shot_level)

        lig_level_loction = seq_path +'Light/'+ seq_shot + '_MAP_Light'
        lig_level = self.create_level(lig_level_loction,shot_level)

        vfx_level_loction = seq_path +'VFX/'+ seq_shot + '_MAP_VFX'
        vfx_level = self.create_level(vfx_level_loction,shot_level)
#----------------------------如果要使用三位数的场次号请将下面横线间部分注释掉--------------------------------------
        sc = sc_name
        number = sc[-2:]
        sc_name = "SC" + number
#----------------------------------------------------------------------------------------------------------
        sc_level_location = ep_sc_path + sc_name
        sc_level = self.create_level(sc_level_location,shot_level)
 

    def get_all_seq(self,seq_shot_name): # 获取要组装的sequence ue资产
        #seq_shot_name = ['EP','SC','P','SHOT',]
        seq_shot = '_'.join(seq_shot_name)
        seq_path = '/Game/Sequence/'
        all_seq_list = []

        for i in seq_shot_name:
            seq_path = seq_path + i + '/'
        ani_seq_loction = seq_path +'Animation/'+ seq_shot + '_Animation' #定位sequence
        cfx_seq_loction = seq_path +'CFX/'+ seq_shot + '_CFX'
        lig_seq_loction = seq_path +'Light/'+ seq_shot + '_Light'
        vfx_seq_loction = seq_path +'VFX/'+ seq_shot + '_VFX'

        seq_loc_list = [ani_seq_loction,cfx_seq_loction,lig_seq_loction,vfx_seq_loction]

        for seq in seq_loc_list:
            exist = ue.find_asset(seq)
            if exist:
                seq_asset = ue.load_object(LevelSequence, seq)
            else:
                factory = LevelSequenceFactoryNew()
                seq_asset = factory.factory_create_new(seq)
            all_seq_list.append(seq_asset)

        return all_seq_list

    def Seq_merge(self):
        total_asset = self.get_total_seq(self.seq_shot_name) #获取要组装的sequence
        self.set_seq_range(total_asset) # 设置一些列范围
        # 判定组装选项需求。并执行组装
        if self.Clear_shot == True:
            self.clear_seq(total_asset)

        if self.camera != None:
            self.assemble_all_level()
            self.clear_seq_cam(total_asset)
            self.assemble_subseq(total_asset)
            self.assemble_cam(total_asset,self.camera)
