#!/usr/bin/python
# -*- coding: utf-8 -*-
#Author : HW
#--2019-08-05
import os
from UE_Sequence_Assemble import asset

class Folder_path(object):
    def __init__(self):
        super(Folder_path, self).__init__()
        source_path = asset.Get_assets().uproject_path
        #source_path = 'D:/UE4_test/UE4_test-419/python_test/Content/'

        self.source_path = source_path + 'Sequence/'
        self.fbx_shource_path  = "H:/XHQS/Cache/ANI_cache/"

    def get_ep_list(self):
        """
        get ep file list and  dictionary
        """
        fbx_file_path = self.source_path
        ep_list = os.listdir(fbx_file_path)

        ep_lists = []
        ep_path_dict = {}
        for x in ep_list:
            j = fbx_file_path + x
            if os.path.isdir(j):
                ep_lists.append(x)
                ep_path_dict[x] = j
        return ep_lists,ep_path_dict

    def get_sc_list(self,ep_path_lists):
        """
        get sc file list and path dictionary
        """
        sc_path_dict = {}
        ep_sc_lists = []
        for ep_path in ep_path_lists:
            sc_list = os.listdir(ep_path)
            
            for sc_name in sc_list:
                sc_path = ep_path +"/"+ sc_name
                if os.path.isdir(sc_path):
                    ep_sc_lists.append(sc_name)
                    sc_path_dict[sc_name] = sc_path
        return ep_sc_lists,sc_path_dict

    def get_pt_list(self,sc_path_lists):
        """
        get shot file list and path dictionary
        """
        pt_path_dict = {}
        pt_shot_lists = []
        for sc_path in sc_path_lists:
            pt_lists = os.listdir(sc_path)
            
            for pt_name in pt_lists:
                pt_path = sc_path +"/"+ pt_name
                if os.path.isdir(pt_path):
                    pt_shot_lists.append(pt_name)
                    pt_path_dict[pt_name] = pt_path
        return pt_shot_lists,pt_path_dict

    def get_shot_list(self,pt_path_lists):
        """
        get shot file list and path dictionary
        """
        shot_path_dict = {}
        sc_shot_lists = []
        for sc_path in pt_path_lists:
            shot_lists = os.listdir(sc_path)
            
            for shot_name in shot_lists:
                shot_path = sc_path +"/"+ shot_name
                if os.path.isdir(shot_path):
                    sc_shot_lists.append(shot_name)
                    shot_path_dict[shot_name] = shot_path
        return sc_shot_lists,shot_path_dict

    def shot_path_connect(self,shot_path):
        lists = shot_path.split("/")
        lists_slice = lists[-5:]
        ue_shot_path = '/Game/'
        for i in lists_slice:
            ue_shot_path = ue_shot_path + i + '/'
        ue_shot_path = ue_shot_path + "character" 
        return ue_shot_path


    def cam_path_connect(self,shot_path_info):
        #lists = shot_path.split("/")
        lists_slice = shot_path_info

        
        cam_shot_path = '{0}{1}/{2}/{2}_{3}/{2}_{3}_{4}/'.format(self.fbx_shource_path,lists_slice[0],lists_slice[1],lists_slice[2],lists_slice[3])

        return cam_shot_path

    def get_cam_fbx(self,cam_shot_path):
        cam_path_dict = {}
        cam_file_lists = []

        if os.path.exists(cam_shot_path):
            for i in os.listdir(cam_shot_path):
                if len(i.split('_')) >= 5:
                    if i.split('_')[4] == 'Camera' :
                        cam_file_lists.append(i)
                        cam_path_dict[i] = cam_shot_path + '/' + i

        return cam_file_lists,cam_path_dict

