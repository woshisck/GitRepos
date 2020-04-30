#!/usr/bin/python
# -*- coding: utf-8 -*-
#Author : HW
#--2019-7-29

# 工具实现的主要功能：
# 根据获取到的镜头文件名称解析出镜头号信息，输出镜头文件所需的动画数据。
# 相机- 按照规范拾取镜头文件中的 ‘SHOT_CAMERA_CAM’ 组，从而获取组中的相机，并重命名为‘Camera’以备UE导入相机时使用（导入相机的时候需要知道fbx文件中相机的名称）

# 角色-按照绑定结构规范，获取模型的’HightMesh‘ 层级并筛选出里面的blendshape模型。加上‘Anim_Joint’骨骼层级，同时选中输出。

# 道具-道具理论上跟角色的输出逻辑相同，其中动画师K的场景临时道具会特别处理 。



import sys 
import maya.cmds as mc
import maya.mel as mm
import os
import re
file_name = mc.file(q=True,sceneName=True,shortName=True) #获取maya镜头文件名称。
#解析出 集数 场次 次级场次 镜头号 
EP = file_name.split('_')[1]

SC = file_name.split('_')[2]

PT = file_name.split('_')[3]

SHOT = file_name.split('_')[4]
#获取时间滑条范围
get_min_start = mc.playbackOptions(q=True,min=True)
get_min_end = mc.playbackOptions(q=True,max=True)
get_max_start = mc.playbackOptions(q=True,ast=True)
get_max_end = mc.playbackOptions(q=True,aet=True)
mc.currentTime(get_max_start) #将动画当前帧初始化到起始帧，这样会避免镜头动画输出的很多bug

type_name = ".fbx"  #输出文件的类型

source_path = "H:/XHQS/Cache/ANI_cache/{}/{}/{}_{}/{}_{}_{}/".format(EP,SC,SC,PT,SC,PT,SHOT)  #根据镜头解析数据，拼接出镜头输出路径
#镜头输出前，清理输出路径中之前存在的动画数据。
def clear_file(path):
    if os.path.exists(path) ==True:
        file_lists = os.listdir(path)
        if file_lists != []:
            for i in file_lists:
                os.remove(os.path.join(path,i))
#判断输出路径是否存在，从而执行创建路径或者清理动作。
if os.path.exists(source_path)==False:
    os.makedirs(source_path)
else:
    clear_file(source_path)

#加载fbx和xgen插件（之前陈默的文件残留xgen表达式，需要启动插件执行，如果清理干净可以不加载xgen插件）

if not (mc.pluginInfo("fbxmaya", query=True, loaded=True)):
    try:
        mc.loadPlugin("fbxmaya.mll")
    except:
        print("waring! fbx plugin con`t load")
if not (mc.pluginInfo("xgenToolkit", query=True, loaded=True)):
    try:
        mc.loadPlugin("xgenToolkit.mll")
    except:
        print("waring! xgenToolkit plugin con`t load")
#获取角色或者道具，并返回大组列表。
def get_char_pro():   
    Asset_list = mc.ls("*:Group","*:*:Group","*:*:*:Group","*:*:*:*:Group",assemblies=1)
    cha_list =[]
    pro_list =[]
    for x in Asset_list:
        if "CH" in x:
            cha_list.append(x)
        elif "PR" in x:
            pro_list.append(x)  
        else:
            pass
    return cha_list,pro_list
#获取场景中要输出的相机
def get_camera():
    shot_cam = mc.ls("SHOT_CAMERA_CAM")
    camera_name_list = mc.listRelatives(shot_cam,allDescendents=1,type="transform")
    
    if camera_name_list != None:
        cam = mc.rename(camera_name_list[0],'Camera')
        mc.setAttr("{}.rotateOrder".format(cam),0)
        return cam
#获取场景中动画师临时K的场景道具。
def get_shot_pro():
    shot_pro = mc.ls("PROP_LOC*")
    if shot_pro:
        return shot_pro
#获取模型组中所有带有BS的模型 
def get_BS_mesh(check_bs_mode_grp):
    BS_mesh_list = []
    all_mode_list = mc.listRelatives(check_bs_mode_grp,allDescendents=1,type="transform",fullPath=1)
    for mesh_trans in all_mode_list:
        if "blendShape" in [mc.nodeType(x) for x in mc.listHistory(mesh_trans,historyAttr=1)]:
            BS_mesh_list.append(mesh_trans)
        bake_list = []
        for x in mc.listHistory(mesh_trans,historyAttr=1):
            if "blendShape" == mc.nodeType(x):
                bake_list.append(x)
        bake_obj(bake_list)
    return BS_mesh_list
#bake物体命令 
def bake_obj(obj_list):
    if obj_list:
        mc.bakeResults(obj_list, time=(get_max_start, get_max_end), animation="keysOrObjects", simulation=True, sparseAnimCurveBake=False)
    else:
        pass
#设置fbx输出设置的关键命令
def setExportFlags():
    mm.eval("FBXExportSmoothingGroups -v true")
    mm.eval("FBXExportHardEdges -v false")
    mm.eval("FBXExportTangents -v true")
    mm.eval("FBXExportInstances -v false")
    mm.eval("FBXExportInAscii -v false")
    mm.eval("FBXExportSmoothMesh -v false")
    mm.eval("FBXExportTriangulate -v false")
    mm.eval("FBXExportBakeResampleAnimation -v false")
    mm.eval("FBXExportBakeComplexAnimation -v true")
    mm.eval("FBXExportBakeComplexStart -v "+str(get_max_start))
    mm.eval("FBXExportBakeComplexEnd -v "+str(get_max_end))
    mm.eval("FBXExportReferencedAssetsContent -v true")
    mm.eval("FBXExportBakeComplexStep -v 1")
    mm.eval("FBXExportUseSceneName -v false")
    mm.eval("FBXExportQuaternion -v quaternion")
    mm.eval("FBXExportShapes -v true")
    mm.eval("FBXExportSkins -v true")
    mm.eval("FBXExportQuaternion -v resample")
    mm.eval("FBXExportUpAxis y")
    mm.eval("FBXExportConstraints -v false")
    mm.eval("FBXExportCameras -v true")
    mm.eval("FBXExportLights -v false")
    mm.eval("FBXExportEmbeddedTextures -v false")
    mm.eval("FBXExportInputConnections -v false")
# 获取 角色或者道具输出的名称 ，通过拆解空间名称，从而解析出角色道具的输出名称
def get_out_cha_name(cha_name):
    asset_name = cha_name.split(":")[-2].split("_")
    if len(asset_name)==5:

        pattern = re.compile(r'\d+')
        vison = pattern.search(asset_name[-1])
        
        if vison:
            out_cha_name = asset_name[2]+"_"+asset_name[3] + str(vison.group())
        else:
            out_cha_name = asset_name[2]+"_"+asset_name[3]

    elif len(asset_name)==4:
        if "HIK" in asset_name[-1] or "Mocap" in asset_name[-1] or "Low" in asset_name[-1]: # 用于过滤功能后缀 
        
            pattern = re.compile(r'\d+')
            vison = pattern.search(asset_name[-1])
            if vison:
                out_cha_name =asset_name[2] + vison.group()
            else:
                out_cha_name = asset_name[2]
        
        else:
            out_cha_name = asset_name[2]+"_"+asset_name[3]
    elif len(asset_name)==3:
        out_cha_name = asset_name[2]
        
    return out_cha_name
# 当镜头内存在多个相同角色的时候 启用 检查文件 如果重复 会自动递增版本号。
def auto_check_file_path(source_path,EP,SC,PT,SHOT,comp,out_cha_name,type_name,Move = ''):
    number = 0
    version = ''
    cha_fbx_out_path = source_path + EP + "_" + SC + "_" + PT + "_" + SHOT + "_" + comp + "_" + out_cha_name + version + Move + type_name
    while os.path.isfile(cha_fbx_out_path):
        number = number + 1
        version = str(number)
        cha_fbx_out_path = source_path + EP + "_" + SC + "_" + PT + "_" + SHOT + "_" + comp + "_" + out_cha_name + version + Move + type_name
    cha_fbx_out_path_x = cha_fbx_out_path.replace("\\","/")
    return cha_fbx_out_path_x

#fbx输出的主函数，
def fbx_out(cha_grp,comp):
    cha_name = cha_grp[:-5] #从角色grp名称获取角色的名称
    hig_mod_grp = mc.ls(cha_name + "HightMesh") #拾取‘HightMesh’的组
    if hig_mod_grp:
        bs_mesh_list = get_BS_mesh(hig_mod_grp)
    else:
        bs_mesh_list = []
        #拾取骨骼‘Anim_Joint’组
    Joint_Group = mc.ls(cha_name + "Anim_Joint")
    if Joint_Group:
        joint_list = mc.listRelatives(Joint_Group,ad=1,type="transform",f=1)
        joint_list.append(Joint_Group[0])
        bake_obj(joint_list)
    
    out_cha_name = get_out_cha_name(cha_name) # 定义输出命名
    if bs_mesh_list+Joint_Group :
        mc.select(bs_mesh_list+Joint_Group)
        # cha_fbx_out_path = source_path + EP + "_" + SC + "_" + PT + "_" + SHOT + "_" + comp + "_" + out_cha_name + type_name
        # cha_fbx_out_path_x = cha_fbx_out_path.replace("\\","/")
        cha_fbx_out_path_x = auto_check_file_path(source_path,EP,SC,PT,SHOT,comp,out_cha_name,type_name) #检查版本号
        mm.eval("FBXExport -f \""+ cha_fbx_out_path_x +"\" -s") #fbx输出命令
        mc.select(clear=1)
#move骨骼点输出 
def move_out(cha_grp,comp):
    cha_name = cha_grp[:-5]
    move_joint = mc.ls(cha_name + "Move_Joint")
    if move_joint:
        bake_obj(move_joint)
        out_cha_name = get_out_cha_name(cha_name)
        mc.select(move_joint)
        # cha_fbx_out_path = source_path + EP + "_" + SC + "_" + PT + "_" + SHOT + "_" + comp + "_" + out_cha_name + "_Move"  + type_name
        # cha_fbx_out_path_x = cha_fbx_out_path.replace("\\","/")
        cha_fbx_out_path_x = auto_check_file_path(source_path,EP,SC,PT,SHOT,comp,out_cha_name,type_name,Move = '_Move')
        mm.eval("FBXExport -f \""+ cha_fbx_out_path_x +"\" -s")
        mc.select(clear=1)
#相机输出函数
def camera_out(cam_nam=None):
    bake_obj(cam_nam)
    mc.parent(cam_nam,world=True)
    mc.select(cam_nam)
    FocalLength = int(mc.getAttr('{}Shape.focalLength'.format(cam_nam))) #读取相机焦距 
    #拼接出相机输出名称  并将 焦距  镜头起始帧结束帧 写入后缀以便UE镜头组装时调用
    cha_fbx_out_path = source_path + EP + "_" + SC + "_" + PT + "_" + SHOT + "_" + "Camera" + "_" + str(FocalLength) + "_" + str(int(get_max_start)) + "_" + str(int(get_max_end)) + type_name
    cha_fbx_out_path_x = cha_fbx_out_path.replace("\\","/")
    mm.eval("FBXExport -f \""+ cha_fbx_out_path_x +"\" -s")
    mc.select(clear=1)
# 场景道具的输出 
def shot_pro_ani_out(prop_loc):
    trans_list = mc.listRelatives(prop_loc,ad=1,type="transform",f=1)
    if trans_list != None:
        bake_obj(trans_list)
        mc.select(prop_loc)
        cha_fbx_out_path = source_path + EP + "_" + SC + "_" + PT + "_" + SHOT + "_" + prop_loc  + type_name
        cha_fbx_out_path_x = cha_fbx_out_path.replace("\\","/")
        mm.eval("FBXExport -f \""+ cha_fbx_out_path_x +"\" -s")
        mc.select(clear=1)
# go ~~~~
def do():
    print "------------------------------------------ start output {} ".format(file_name)
    setExportFlags()    
    cha,pro = get_char_pro()
    cam = get_camera()
    shot_pro = get_shot_pro()
    
    if cam != None:
        print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>  start output Cam  ---fbx"
        camera_out(cam)
    else:
        print file_name,'>>>>>>>>>>>>>>>>>>>>>>>> in scenes can`t find shot camera'
        
    if shot_pro != None:
        for k in shot_pro:
            print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>  start output Shot_Pro {} ---fbx".format(k)
            shot_pro_ani_out(k)
    if pro !=[]:
        comp = "PR"
        for j in pro:
            print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>  start output PR {} ---fbx".format(j)
            fbx_out(j,comp)
    if cha !=[]:
        comp = "CH"
        for i in cha:
            print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>  start output CH {} ---fbx".format(i)
            fbx_out(i,comp)
            move_out(i,comp)

    print "============================================= {} file output end ".format(file_name)
do()