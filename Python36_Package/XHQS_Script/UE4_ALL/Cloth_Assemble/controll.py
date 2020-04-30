#!/usr/bin/python
# -*- coding: utf-8 -*-
 


from PySide2.QtGui import *  
from PySide2.QtCore import *  
from PySide2.QtWidgets import * 

# 导入包里的四个功能模块
from Cloth_Assemble.UI import Ui_Seq_Assemble
from Cloth_Assemble import path as asset_path      #资产路径处理模块 包括UE内部资产和服务器镜头资产
from Cloth_Assemble import asset as get_asset        #UE资产读取模块
from Cloth_Assemble import sequence  as seq_ass  #UE组装功能模块



from imp import reload 

reload(asset_path)
reload(get_asset)
reload(seq_ass)
class main_window(QWidget,Ui_Seq_Assemble):
    def __init__(self,parent=None):
        QWidget.__init__(self,parent)
        self.setupUi(self)

        # 实例化两个功能类  
        self.path = asset_path.Folder_path()
        self.asset = get_asset.Get_assets()
        
    def Update_ep_list(self):  #更新集数列表框 （所有的列表框更新都会返回全局字典变量 用于 下游 列表框更新调用）
        """
        update ep  list 
        """
        ep_lists,ep_path_dict = self.path.get_ep_list()
        self.Ep_list.addItems(ep_lists)
        global ep_dict 
        ep_dict = ep_path_dict

    def Update_sc_list(self): #更新场次列表框
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

    def Update_pt_list(self): #更新次级场次列表框

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

    def Update_shot_list(self): #更新镜头列表框
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

    def Update_type(self):  # 相机 资产 复选框从而更新 文件列表框
        self.Update_file_list()

    def Update_file_list(self): # 更新文件列表框 
        """
        update file widget list
        """
        #先清理文件列表框
        self.File_list.clear()
        shot_lists_ins = self.Shot_list.selectedItems()

        file_path_dict = {}
        asset_file_lists = []

        for sel_shot in shot_lists_ins:

            shot_path = shot_dict[sel_shot.text()]

            #根据镜头的ue本机路径转换到相机的服务器路径读取相机
            shot_path_info = shot_path.split('/')[-4:]
            cam_shot_path = self.path.cam_path_connect(shot_path_info)
            cam_file_lists,cam_path_dict = self.path.get_cam_fbx(cam_shot_path) #通过路径获取服务器相机的fbx文件

            #通过镜头本机路径转换到ue内部路径 并通过asset模块读取ue内部资产
            ue_shot_path = self.path.shot_path_connect(shot_path)
            ani_seq_list,path_dict = self.asset.get_ani_asset(ue_shot_path)
            #将每一个镜头路径的 ue资产字典和相机字典更新到字典中
            file_path_dict.update(path_dict)
            file_path_dict.update(cam_path_dict)
            asset_file_lists = asset_file_lists  + cam_file_lists + ani_seq_list # 收集资产文件列表
        #检查 相机和UE资产复选框勾选情况


        # Camera = self.Camera.isChecked()
        # Ue_asset = self.Ue_asset.isChecked()
#将相机 和 ue资产收集到列表中 
        Camera_list = []
        Ue_asset_list = []

        # if Camera == True:
        #     for i in asset_file_lists:
        #         if "Camera" in i:
        #             Camera_list.append(i)
        # if Ue_asset == True:
        #     for j in asset_file_lists:
        #         if "CH_" in j or "PR_" in j or "PROP_" in j:
        #             Ue_asset_list.append(j)

#检查 收集的 情况 更新到文件列表框中 
        check_file_lists = Camera_list + Ue_asset_list
        if check_file_lists ==[]:
            check_file_lists = asset_file_lists

        check_file_lists.sort()
        self.File_list.addItems(check_file_lists)

        global file_dict
        file_dict = file_path_dict


    def Start_assemble(self):  #组装资产主函数 
        #获取被选中的文件列表 
        file_lists_ins = self.File_list.selectedItems()
        vs_shot_name = ''
        # clear_shot = self.Clear_shot.isChecked()#检查清理功能是否启用 
        #循环组装被选中的资产 （每一次都要优先获取镜头相机从而读取帧数范围信息，否则不能组装）
        for i in file_lists_ins:
            file_name = i.text()
            shot_name = "_".join(file_name.split("_")[:4])
            #通过判断循环中是否是相同的镜头从而决定是否清除sequence信息。
            if vs_shot_name == shot_name:
                seq_clear = False
            else:
                vs_shot_name = shot_name
                seq_clear = False
            #获取相机文件用于实例化sequence
            shot_path_info = shot_name.split('_')
            cam_shot_path = self.path.cam_path_connect(shot_path_info)
 
            cam_file_lists,cam_path_dict = self.path.get_cam_fbx(cam_shot_path)
            
            if cam_path_dict !={}: #判定相机是否存在 
                file_path = file_dict[file_name]
                #判定要组装的是相机还是角色
                if file_name.split('_')[4] == 'Camera':
                    camera = file_path
                    ch_pr = None
                else:
                    ch_pr = file_path
                    camera = None
                self.sequence = seq_ass.Sequence(cam_file_lists[0],seq_clear,camera,ch_pr)  #实例化sequence 执行镜头组装
                self.sequence.Assemble_seq()#执行组装动作。
            else:
                print (">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>: can`t find shot cam ")



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    widget  = main_window()
    widget.show()
    widget.Update_ep_list()
    sys.exit(app.exec_())
