#!/usr/bin/python
# -*- coding: utf-8 -*-
#Author : HW
#--2019-6-30
import sys 
import maya.cmds as mc
import maya.mel as mm
import os

file_name = mc.file(q=True,sceneName=True,shortName=True)

EP = file_name.split('_')[1]

SC = file_name.split('_')[2]

PT = file_name.split('_')[3]

SHOT = file_name.split('_')[4]

get_min_start = mc.playbackOptions(q=True,min=True)
get_min_end = mc.playbackOptions(q=True,max=True)
get_max_start = mc.playbackOptions(q=True,ast=True)
get_max_end = mc.playbackOptions(q=True,aet=True)
mc.currentTime(get_max_start)
type_name = ".fbx"

source_path = "H:/XHQS/Cache/ANI_cache/{}/{}/{}_{}/{}_{}_{}/".format(EP,SC,SC,PT,SC,PT,SHOT)

if os.path.exists(source_path)==False:
    os.makedirs(source_path)
else:
    pass

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


def get_camera():
    shot_cam = mc.ls("SHOT_CAMERA_CAM")
    camera_name_list = mc.listRelatives(shot_cam,allDescendents=1,type="transform")
    cam = mc.rename(camera_name_list[0],'Camera')
    if camera_name_list != None:
        mc.setAttr("{}.rotateOrder".format(cam),0)
        return cam


def bake_obj(obj_list):
    if obj_list:
        mc.bakeResults(obj_list, time=(get_max_start, get_max_end), animation="keysOrObjects", simulation=True, sparseAnimCurveBake=False)
    else:
        pass

def setExportFlags():
    # Mesh
    mm.eval("FBXExportSmoothingGroups -v true")
    mm.eval("FBXExportHardEdges -v false")
    mm.eval("FBXExportTangents -v true")
    mm.eval("FBXExportInstances -v false")
    mm.eval("FBXExportInAscii -v false")
    mm.eval("FBXExportSmoothMesh -v false")
    mm.eval("FBXExportTriangulate -v false")
    # Animation
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
    ##garbage we don't want
    # Constraints   
    mm.eval("FBXExportConstraints -v false")
    # Cameras   
    mm.eval("FBXExportCameras -v true")
    # Lights
    mm.eval("FBXExportLights -v false")
    # Embed Media
    mm.eval("FBXExportEmbeddedTextures -v false")
    # Connections
    mm.eval("FBXExportInputConnections -v false")

def camera_out(cam_nam=None):
    print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>start camera out put !!!!!"
    bake_obj(cam_nam)
    
    mc.parent(cam_nam,world=True)
    mc.select(cam_nam)
    FocalLength = int(mc.getAttr('{}Shape.focalLength'.format(cam_nam)))
    cha_fbx_out_path = source_path + EP + "_" + SC + "_" + PT + "_" + SHOT + "_" + "Camera" + "_" + str(FocalLength) + "_" + str(int(get_max_start)) + "_" + str(int(get_max_end)) + type_name
    cha_fbx_out_path_x = cha_fbx_out_path.replace("\\","/")
    mm.eval("FBXExport -f \""+ cha_fbx_out_path_x +"\" -s")
    mc.select(clear=1)


# go ~~~~
def do():
    print ">>>>>>>>>>>>>>>>> start output {} ".format(file_name)
    setExportFlags()    

    cam = get_camera()

    if cam != None:
        camera_out(cam)
    else:
        print file_name,'>>>>>>>>>>>>>>>>>>>>>>>> in scenes can`t find shot camera'
    print "================= {} file output end ".format(file_name)
do()









