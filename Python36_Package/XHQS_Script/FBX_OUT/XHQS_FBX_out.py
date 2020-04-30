#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author : HW
# --2019-7-29
import sys
import maya.cmds as mc
import maya.mel as mm
import os
import re

file_name = mc.file(q=True, sceneName=True, shortName=True)

EP = file_name.split('_')[1]

SC = file_name.split('_')[2]

PT = file_name.split('_')[3]

SHOT = file_name.split('_')[4]

get_min_start = mc.playbackOptions(q=True, min=True)
get_min_end = mc.playbackOptions(q=True, max=True)
get_max_start = mc.playbackOptions(q=True, ast=True)
get_max_end = mc.playbackOptions(q=True, aet=True)
mc.currentTime(get_max_start)
type_name = ".fbx"

source_path = "H:/XHQS/Cache/ANI_cache/{}/{}/{}_{}/{}_{}_{}/".format(EP, SC, SC, PT, SC, PT, SHOT)


def clear_file(path):
    if os.path.exists(path) == True:
        file_lists = os.listdir(path)
        if file_lists != []:
            for i in file_lists:
                os.remove(os.path.join(path, i))


if os.path.exists(source_path) == False:
    os.makedirs(source_path)
else:
    clear_file(source_path)

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


def get_char_pro():
    Asset_list = mc.ls("*:Group", "*:*:Group", "*:*:*:Group", "*:*:*:*:Group", assemblies=1)
    cha_list = []
    pro_list = []
    for x in Asset_list:
        if "CH" in x:
            cha_list.append(x)
        elif "PR" in x:
            pro_list.append(x)
        else:
            pass
    return cha_list, pro_list


def get_camera():
    shot_cam = mc.ls("SHOT_CAMERA_CAM")
    camera_name_list = mc.listRelatives(shot_cam, allDescendents=1, type="transform")
    cam = mc.rename(camera_name_list[0], 'Camera')
    if camera_name_list != None:
        mc.setAttr("{}.rotateOrder".format(cam), 0)
        return cam


def get_shot_pro():
    shot_pro = mc.ls("PROP_LOC*")
    if shot_pro:
        return shot_pro


def get_BS_mesh(check_bs_mode_grp):
    BS_mesh_list = []
    all_mode_list = mc.listRelatives(check_bs_mode_grp, allDescendents=1, type="transform", fullPath=1)
    if all_mode_list:
        for mesh_trans in all_mode_list:
            if "blendShape" in [mc.nodeType(x) for x in mc.listHistory(mesh_trans, historyAttr=1)]:
                BS_mesh_list.append(mesh_trans)
            bake_list = []
            for x in mc.listHistory(mesh_trans, historyAttr=1):
                if "blendShape" == mc.nodeType(x):
                    bake_list.append(x)
            bake_obj(bake_list)
    return BS_mesh_list


def bake_obj(obj_list):
    if obj_list:
        mc.bakeResults(obj_list, time=(get_max_start, get_max_end), animation="keysOrObjects", simulation=True, sparseAnimCurveBake=False)
    else:
        pass


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
    mm.eval("FBXExportBakeComplexStart -v " + str(get_max_start))
    mm.eval("FBXExportBakeComplexEnd -v " + str(get_max_end))
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


def get_out_cha_name(cha_name):
    asset_name = cha_name.split(":")[-2].split("_")
    if len(asset_name) == 5:

        pattern = re.compile(r'\d+')
        vison = pattern.search(asset_name[-1])

        if vison:
            out_cha_name = asset_name[2] + "_" + asset_name[3] + str(vison.group())
        else:
            out_cha_name = asset_name[2] + "_" + asset_name[3]

    elif len(asset_name) == 4:
        if "HIK" in asset_name[-1] or "Mocap" in asset_name[-1] or "Low" in asset_name[-1]:

            pattern = re.compile(r'\d+')
            vison = pattern.search(asset_name[-1])
            if vison:
                out_cha_name = asset_name[2] + vison.group()
            else:
                out_cha_name = asset_name[2]

        else:
            out_cha_name = asset_name[2] + "_" + asset_name[3]
    elif len(asset_name) == 3:
        out_cha_name = asset_name[2]

    return out_cha_name


def auto_check_file_path(source_path, EP, SC, PT, SHOT, comp, out_cha_name, type_name, Move=''):
    number = 0
    version = ''
    cha_fbx_out_path = source_path + EP + "_" + SC + "_" + PT + "_" + SHOT + "_" + comp + "_" + out_cha_name + version + Move + type_name
    while os.path.isfile(cha_fbx_out_path):
        number = number + 1
        version = str(number)
        cha_fbx_out_path = source_path + EP + "_" + SC + "_" + PT + "_" + SHOT + "_" + comp + "_" + out_cha_name + version + Move + type_name
    cha_fbx_out_path_x = cha_fbx_out_path.replace("\\", "/")
    return cha_fbx_out_path_x


def fbx_out(cha_grp, comp):
    cha_name = cha_grp[:-5]
    hig_mod_grp = mc.ls(cha_name + "HightMesh")
    if hig_mod_grp:
        bs_mesh_list = get_BS_mesh(hig_mod_grp)
    else:
        bs_mesh_list = []
    Joint_Group = mc.ls(cha_name + "Anim_Joint")
    if Joint_Group:
        joint_list = mc.listRelatives(Joint_Group, ad=1, type="transform", f=1)
        joint_list.append(Joint_Group[0])
        bake_obj(joint_list)

    out_cha_name = get_out_cha_name(cha_name)
    if bs_mesh_list + Joint_Group:
        mc.select(bs_mesh_list + Joint_Group)
        # cha_fbx_out_path = source_path + EP + "_" + SC + "_" + PT + "_" + SHOT + "_" + comp + "_" + out_cha_name + type_name
        # cha_fbx_out_path_x = cha_fbx_out_path.replace("\\","/")
        cha_fbx_out_path_x = auto_check_file_path(source_path, EP, SC, PT, SHOT, comp, out_cha_name, type_name)
        mm.eval("FBXExport -f \"" + cha_fbx_out_path_x + "\" -s")
        mc.select(clear=1)


def move_out(cha_grp, comp):
    cha_name = cha_grp[:-5]
    move_joint = mc.ls(cha_name + "Move_Joint")
    if move_joint:
        bake_obj(move_joint)
        out_cha_name = get_out_cha_name(cha_name)
        mc.select(move_joint)
        # cha_fbx_out_path = source_path + EP + "_" + SC + "_" + PT + "_" + SHOT + "_" + comp + "_" + out_cha_name + "_Move"  + type_name
        # cha_fbx_out_path_x = cha_fbx_out_path.replace("\\","/")
        cha_fbx_out_path_x = auto_check_file_path(source_path, EP, SC, PT, SHOT, comp, out_cha_name, type_name, Move='_Move')
        mm.eval("FBXExport -f \"" + cha_fbx_out_path_x + "\" -s")
        mc.select(clear=1)


def camera_out(cam_nam=None):
    bake_obj(cam_nam)
    mc.parent(cam_nam, world=True)
    mc.select(cam_nam)
    FocalLength = int(mc.getAttr('{}Shape.focalLength'.format(cam_nam)))
    cha_fbx_out_path = source_path + EP + "_" + SC + "_" + PT + "_" + SHOT + "_" + "Camera" + "_" + str(FocalLength) + "_" + str(int(get_max_start)) + "_" + str(int(get_max_end)) + type_name
    cha_fbx_out_path_x = cha_fbx_out_path.replace("\\", "/")
    mm.eval("FBXExport -f \"" + cha_fbx_out_path_x + "\" -s")
    mc.select(clear=1)


def shot_pro_ani_out(prop_loc):
    trans_list = mc.listRelatives(prop_loc, ad=1, type="transform", f=1)
    if trans_list != None:
        bake_obj(trans_list)
        mc.select(prop_loc)
        cha_fbx_out_path = source_path + EP + "_" + SC + "_" + PT + "_" + SHOT + "_" + prop_loc + type_name
        cha_fbx_out_path_x = cha_fbx_out_path.replace("\\", "/")
        mm.eval("FBXExport -f \"" + cha_fbx_out_path_x + "\" -s")
        mc.select(clear=1)


# go ~~~~
def do():
    print "------------------------------------------ start output {} ".format(file_name)
    setExportFlags()
    cha, pro = get_char_pro()
    cam = get_camera()
    shot_pro = get_shot_pro()

    if cam != None:
        print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>  start output Cam  ---fbx"
        camera_out(cam)
    else:
        print file_name, '>>>>>>>>>>>>>>>>>>>>>>>> in scenes can`t find shot camera'

    if shot_pro != None:
        for k in shot_pro:
            print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>  start output Shot_Pro {} ---fbx".format(k)
            shot_pro_ani_out(k)
    if pro != []:
        comp = "PR"
        for j in pro:
            print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>  start output PR {} ---fbx".format(j)
            fbx_out(j, comp)
    if cha != []:
        comp = "CH"
        for i in cha:
            print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>  start output CH {} ---fbx".format(i)
            fbx_out(i, comp)
            move_out(i, comp)

    print "============================================= {} file output end ".format(file_name)


do()
