#!/usr/bin/python
# -*- coding: utf-8 -*-
#Author : HW
#--2019-08-05
from PySide2.QtGui import *  
from PySide2.QtCore import *  
from PySide2.QtWidgets import * 
from UE_Sequence_Assemble.UI import Ui_Seq_Assemble
from UE_Sequence_Assemble import path
from UE_Sequence_Assemble import asset
from UE_Sequence_Assemble import sequence
from imp import reload 

reload(path)
reload(asset)
reload(sequence)
class main_window(QWidget,Ui_Seq_Assemble):
    def __init__(self,parent=None):
        QWidget.__init__(self,parent)
        self.setupUi(self)
        self.path = path.Folder_path()
        self.asset = asset.Get_assets()
        
    def Update_ep_list(self):
        """
        update ep  list 
        """
        ep_lists,ep_path_dict = self.path.get_ep_list()
        self.Ep_list.addItems(ep_lists)
        global ep_dict 
        ep_dict = ep_path_dict

    def Update_sc_list(self):
        """
        update sc widget list
        """
        self.Sc_list.clear()
        ep_lists_ins = self.Ep_list.selectedItems()
        ep_path_lists = []
        for sel_ep in ep_lists_ins:
            ep_path_lists.append(ep_dict[sel_ep.text()])
        ep_sc_lists,sc_path_dict = self.path.get_sc_list(ep_path_lists)
        ep_sc_lists.sort()
        self.Sc_list.addItems(ep_sc_lists)

        global sc_dict 
        sc_dict = sc_path_dict

    def Update_pt_list(self):

        self.Pt_list.clear()
        sc_lists_ins = self.Sc_list.selectedItems()
        sc_path_lists = []
        for sel_sc in sc_lists_ins:
            sc_path_lists.append(sc_dict[sel_sc.text()])
        sc_pt_lists,pt_path_dict = self.path.get_pt_list(sc_path_lists)
        sc_pt_lists.sort()
        self.Pt_list.addItems(sc_pt_lists)

        global pt_dict 
        pt_dict = pt_path_dict

    def Update_shot_list(self):
        """
        update shot widget list
        """
        self.Shot_list.clear()
        pt_lists_ins = self.Pt_list.selectedItems()
        pt_path_lists = []
        for sel_pt in pt_lists_ins:
            pt_path_lists.append(pt_dict[sel_pt.text()])
        pt_shot_lists,shot_path_dict = self.path.get_shot_list(pt_path_lists)
        pt_shot_lists.sort()
        self.Shot_list.addItems(pt_shot_lists)

        global shot_dict 
        shot_dict = shot_path_dict

    def Update_type(self):
        self.Update_file_list()

    def Update_file_list(self):
        """
        update file widget list
        """
        self.File_list.clear()
        shot_lists_ins = self.Shot_list.selectedItems()

        file_path_dict = {}
        asset_file_lists = []

        for sel_shot in shot_lists_ins:

            shot_path = shot_dict[sel_shot.text()]

            shot_path_info = shot_path.split('/')[-4:]
            cam_shot_path = self.path.cam_path_connect(shot_path_info)
            cam_file_lists,cam_path_dict = self.path.get_cam_fbx(cam_shot_path)

            ue_shot_path = self.path.shot_path_connect(shot_path)

            ani_seq_list,path_dict = self.asset.get_ani_asset(ue_shot_path)

            file_path_dict.update(path_dict)
            file_path_dict.update(cam_path_dict)
            asset_file_lists = asset_file_lists  + cam_file_lists + ani_seq_list

        Camera = self.Camera.isChecked()
        Ue_asset = self.Ue_asset.isChecked()

        Camera_list = []
        Ue_asset_list = []

        if Camera == True:
            for i in asset_file_lists:
                if "Camera" in i:
                    Camera_list.append(i)
        if Ue_asset == True:
            for j in asset_file_lists:
                if "CH_" in j or "PR_" in j or "PROP_" in j:
                    Ue_asset_list.append(j)

        check_file_lists = Camera_list + Ue_asset_list
        if check_file_lists ==[]:
            check_file_lists = asset_file_lists

        check_file_lists.sort()
        self.File_list.addItems(check_file_lists)

        global file_dict
        file_dict = file_path_dict


    def Start_assemble(self):
        file_lists_ins = self.File_list.selectedItems()
        vs_shot_name = ''
        clear_shot = self.Clear_shot.isChecked()

        for i in file_lists_ins:
            file_name = i.text()
            shot_name = "_".join(file_name.split("_")[:4])
            if vs_shot_name == shot_name:
                seq_clear = False
            else:
                vs_shot_name = shot_name
                seq_clear = clear_shot

            shot_path_info = shot_name.split('_')
            #print ('shot_path_info>>>>>>>>>>>>>>>>>>>>>>>>',shot_path_info)
            cam_shot_path = self.path.cam_path_connect(shot_path_info)
            #print ('shot_path_info>>>>>>>>>>>>>>>>>>>>>>>>',cam_shot_path)
            cam_file_lists,cam_path_dict = self.path.get_cam_fbx(cam_shot_path)

            if cam_path_dict !={}:
                file_path = file_dict[file_name]
                if file_name.split('_')[4] == 'Camera':
                    camera = file_path
                    ch_pr = None
                else:
                    ch_pr = file_path
                    camera = None
                self.sequence = sequence.Sequence(cam_file_lists[0],seq_clear,camera,ch_pr)
                self.sequence.Assemble_seq()
            else:
                print (">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>: can`t find shot cam ")



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    widget  = main_window()
    widget.show()
    widget.Update_ep_list()
    sys.exit(app.exec_())
