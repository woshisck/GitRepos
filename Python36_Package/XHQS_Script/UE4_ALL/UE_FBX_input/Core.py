#!/usr/bin/python
# -*- coding: utf-8 -*-
#Author : HW
#--2019-07-08
import os 
import subprocess
import json
import re
import string

class UE_FBX_INPUT_SET(object):
    def __init__(self):
        super(UE_FBX_INPUT_SET, self).__init__()
        self.json_file_path = os.path.expanduser('~') + "/" +"UE_input_fbx"
    def analysis_file_path(self,file_path):
        """
        analysis file path
        """
        part_list = file_path.split("/")
        Fbx = part_list[-1]
        EP = Fbx.split("_")[0]
        SC = Fbx.split("_")[1]
        PT = Fbx.split("_")[2]
        Shot = Fbx.split("_")[3]
        part_name = Fbx.split("_")[4]

        return EP,SC,PT,Shot,Fbx,part_name

    def create_move_dict(self,move_fbx_path):
        """
        creat movejoint dict
        """
        EP,SC,PT,Shot,Fbx,part_name = self.analysis_file_path(move_fbx_path)
        Fbx_name = Fbx.split(".")[0]
        # if len(Fbx_name.split("_"))>7:
        #     ch_move_name = Fbx_name.split("_")[5]+"_"+Fbx_name.split("_")[6]+"_"+Fbx_name.split("_")[7]
        # else:
        #     ch_move_name = Fbx_name.split("_")[5]+"_"+Fbx_name.split("_")[6]

        input_fbx_file = move_fbx_path
        input_path = "/Game/Sequence/{}/{}/{}/{}/character/Move_Joint".format(EP,SC,PT,Shot)
        skeleton_path = "/Game/Global/Move_Joint/Move_Joint_Skeleton"
        group_name = Fbx_name.split("_")[4:]
        file_path_dict = {
                "GroupName": group_name,
                "FileNames": [
                    input_fbx_file
                    ],
                    "bReplaceExisting" : "true",
                    "DestinationPath": input_path,
                    "FactoryName": "FbxFactory",
                    "ImportSettings": {
                        "meshTypeToImport": "FBXIT_Animation",
                        "bImportMesh": "false",
                        "skeleton": skeleton_path
                                    }
            }
        return file_path_dict

    def lack_ch_version(self,Fbx):
        Fbx_name = Fbx.split(".")[0]
        # if len(Fbx_name.split("_"))>6:
        #     ch_pro_name_vs = Fbx_name.split("_")[5]+"_"+Fbx_name.split("_")[6]
        # else:
        #     ch_pro_name_vs = Fbx_name.split("_")[5]
        ch_pro_name_vs = Fbx_name.split("_")[5:]
        pattern = re.compile(r'\d+')
        vison = pattern.search(ch_pro_name_vs)
        if vison:
            ch_pro_name = ch_pro_name_vs.rstrip(vison.group())
        else:
            ch_pro_name = ch_pro_name_vs

        return ch_pro_name,ch_pro_name_vs

    def create_ch_pro_dict(self,ch_pro_fbx_path):
        """
        character and prop input dict
        """
        EP,SC,PT,Shot,Fbx,part_name = self.analysis_file_path(ch_pro_fbx_path)
        ch_pro_name,ch_pro_name_vs = self.lack_ch_version(Fbx)
        input_fbx_file = ch_pro_fbx_path
        input_path = "/Game/Sequence/{}/{}/{}/{}/character".format(EP,SC,PT,Shot)
        if part_name == "CH":
            skeleton_path = "/Game/Character/{}/Meshes/SK_CH_{}_Skeleton".format(ch_pro_name,ch_pro_name)
        elif part_name == "PR":
            skeleton_path = "/Game/Prop/{}/Meshes/SK_PR_{}_Skeleton".format(ch_pro_name,ch_pro_name)
        group_name = ch_pro_name_vs
        file_path_dict = {
                "GroupName": group_name,
                "FileNames": [
                    input_fbx_file
                    ],
                    "bReplaceExisting" : "true",
                    "DestinationPath": input_path,
                    "FactoryName": "FbxFactory",
                    "ImportSettings": {
                        "meshTypeToImport": "FBXIT_Animation",
                        "bImportMesh": "false",
                        "skeleton": skeleton_path
                                    }
            }
        return file_path_dict
    def create_prop_dict(self,prop_fbx_path):
        """
        animation shot prop ani asset input dict
        """
        EP,SC,PT,Shot,Fbx,part_name = self.analysis_file_path(prop_fbx_path)

        input_fbx_file = prop_fbx_path
        input_path = "/Game/Sequence/{}/{}/{}/{}/character".format(EP,SC,PT,Shot)
        group_name = part_name +"_"+ Fbx.split(".")[0].split("_")[-1]
        file_path_dict = {
                "GroupName": group_name,
                "FileNames": [
                    input_fbx_file
                    ],
                    "bReplaceExisting" : "true",
                    "DestinationPath": input_path,
                    "FactoryName": "FbxFactory",
                    "bSkipReadOnly": 0,
                    "ImportSettings": {
                        "bImportAnimations": 1,
                        "MeshTypeToImport": 1,
                        "bCreatePhysicsAsset":0
                                    }
            }
        return file_path_dict
    def create_json_file(self,file_path_lists):
        file_list = []
        for each in file_path_lists:
            EP,SC,PT,Shot,Fbx,part_name = self.analysis_file_path(each)
            if part_name == "CH":
                if Fbx.split(".")[0].split("_")[-1] == "Move":
                    move_dict = self.create_move_dict(each)
                    file_list.append(move_dict)
                else:
                    ch_dict = self.create_ch_pro_dict(each)
                    file_list.append(ch_dict)
            elif part_name == "PR":
                pr_dict = self.create_ch_pro_dict(each)
                file_list.append(pr_dict)
            elif part_name == "PROP":
                prop_dict = self.create_prop_dict(each)
                file_list.append(prop_dict)

            else:
                pass

        if file_list !=[]:
            date_list = {'ImportGroups':file_list}
            json_date = json.dumps(date_list,indent=4)

            with open(self.json_file_path+"/"+"UE_input_fbx_setting.json","w+") as f:
                f.truncate()
                f.write(json_date)
            self.json_file = self.json_file_path+"/"+"UE_input_fbx_setting.json"

            return self.json_file

    def do_input_cmd(self,UE4_editor,UE4_project,json_file_path):

        cmd = '"{}" "{}" -run=ImportAssets -importsettings="{}" >{}/input_log.log'.format(UE4_editor,UE4_project,json_file_path,self.json_file_path)
        p = subprocess.Popen(cmd,shell=True,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        p.wait()
        os.remove(self.json_file)

    def clear_path(self,path):
        if os.path.exists(path) ==True:
                file_lists = os.listdir(path)
                if not file_lists == []:
                    for i in file_lists:
                        file_path = os.path.join(path,i)
                        if os.path.isfile(file_path):
                            os.remove(file_path)

    def clear_fbx_file(self,file_path_lists,UE4_project):
        """
        delete ue input path fbx file
        """
        ue_project_path,project_name = os.path.split(UE4_project)

        for each in file_path_lists:
            EP,SC,PT,Shot,Fbx,part_name = self.analysis_file_path(each)
            clear_ue_path = "{}/Content/Sequence/{}/{}/{}/{}/character".format(ue_project_path,EP,SC,PT,Shot)
            clear_ue_path_move = "{}/Content/Sequence/{}/{}/{}/{}/character/Move_Joint".format(ue_project_path,EP,SC,PT,Shot)
            self.clear_path(clear_ue_path)
            self.clear_path(clear_ue_path_move)
            
    def check_ue_asset(self,file_path_lists,UE4_project):
        """
        check ue asset list 
        """
        ue_project_path,project_name = os.path.split(UE4_project)
        ue_lack_list = []
        for each in file_path_lists:
            EP,SC,PT,Shot,Fbx,part_name = self.analysis_file_path(each)
            if part_name == "CH" and "Move" not in Fbx:
                ch_name,ch_pro_name_vs = self.lack_ch_version(Fbx)
                ue_ch_asset = "{}/Content/Character/{}/Meshes/SK_CH_{}_Skeleton.uasset".format(ue_project_path,ch_name,ch_name)
                if not os.path.exists(ue_ch_asset):
                    ue_lack_list.append("CH: "+ch_name+'\n')

            elif part_name == "PR":
                pro_name,ch_pro_name_vs = self.lack_ch_version(Fbx)
                ue_pro_asset = "{}/Content/Prop/{}/Meshes/SK_PR_{}_Skeleton.uasset".format(ue_project_path,pro_name,pro_name)
                if not os.path.exists(ue_pro_asset):
                    ue_lack_list.append("PR: "+pro_name+'\n')
            else:
                pass
        return ''.join(set(ue_lack_list))


