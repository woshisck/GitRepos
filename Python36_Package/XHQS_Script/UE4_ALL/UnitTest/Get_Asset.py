#!/usr/bin/python
# -*- coding: utf-8 -*-
 

# 该模块主要用来获取ue内部资产


import unreal_engine as ue
from unreal_engine.classes import AnimSequence

class Get_assets(object):

    def __init__(self):
        super(Get_assets,self).__init__()

        self.uproject_path = ue.get_content_dir()

    def get_ani_asset(self,ue_shot_path): #获取ue镜头路径下的aniue资产
        asset_list = ue.get_assets(ue_shot_path)
        path_dict = {}
        ani_seq_list = []
        #print (" join  ue asset model>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",asset_list)
        for i in asset_list:
            if i.get_class().get_name() == 'AnimSequence':
                asset_name = i.get_name()
                ani_seq_list.append(asset_name)
                path_dict[asset_name] = ue_shot_path + '/' + asset_name

        return ani_seq_list,path_dict



