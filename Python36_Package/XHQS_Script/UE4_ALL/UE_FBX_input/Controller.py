#!/usr/bin/python
# -*- coding: utf-8 -*-
#Author : HW
#--2019-07-05
from PySide2.QtGui import *  
from PySide2.QtCore import *  
from PySide2.QtWidgets import * 

from UE_FBX_input.UE_input_fbx_ui import Ui_UE_input_Dialog
from UE_FBX_input.Model import UE_FBX_INPUT_MODEL
from UE_FBX_input.Core import UE_FBX_INPUT_SET
import ctypes
myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

class Clear_Fbx_File(QThread):
	_sel_shot_signal = Signal(list)
	def __init__(self,parent=None,clear=None,args = []):
		super(clear_fbx_file, self).__init__(parent=parent)

		self.args = args
	def run(self):
		self._sel_shot_signal.emit(self.args)

class main_window(QWidget,Ui_UE_input_Dialog):
	def __init__(self,parent=None):
		QWidget.__init__(self,parent)
		self.setupUi(self)
		self.model = UE_FBX_INPUT_MODEL()
		self.set = UE_FBX_INPUT_SET()

	def closeEvent(self, event):
		self.save_set()
		self.setAttribute(Qt.WA_DeleteOnClose)

	def Open_ue_editor(self):
		ue_editor_path = QFileDialog.getOpenFileName(self,'select file',"/", "Exe Files (*.exe);;All Files (*)")
		self.UE4Editor_path_line.setText(ue_editor_path[0])
		pass

	def Open_ue_project(self):
		ue_project_path = QFileDialog.getOpenFileName(self,'select file',"/", "Exe Files (*.uproject);;All Files (*)")
		self.UE4Project_path_line.setText(ue_project_path[0])
		pass

	def Update_ep_list(self):
		"""
		update ep  list 
		"""
		ep_lists,ep_path_dict = self.model.get_ep_list()
		self.Ep_list.addItems(ep_lists)
		# self.Ep_list.item(1).setStyleSheet('background-color：yellow')
		# self.Ep_list.setStyleSheet('color：blue; background-color：yellow')
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
		ep_sc_lists,sc_path_dict = self.model.get_sc_list(ep_path_lists)
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
		sc_pt_lists,pt_path_dict = self.model.get_pt_list(sc_path_lists)
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
		pt_shot_lists,shot_path_dict = self.model.get_shot_list(pt_path_lists)
		pt_shot_lists.sort()
		self.Shot_list.addItems(pt_shot_lists)

		global shot_dict 
		shot_dict = shot_path_dict

	def Update_file_list(self):
		"""
		update file widget list
		"""
		self.File_list.clear()
		shot_lists_ins = self.Shot_list.selectedItems()
		shot_path_lists = []
		for sel_shot in shot_lists_ins:
			shot_path_lists.append(shot_dict[sel_shot.text()])
		fbx_file_lists,file_path_dict = self.model.get_fbx_file(shot_path_lists)
		fbx_file_lists.sort()
		self.File_list.addItems(fbx_file_lists)

		global file_dict
		file_dict = file_path_dict
	def Check_ue_asset(self):

		file_lists_ins = self.File_list.selectedItems()

		file_path_lists = []
		for i in file_lists_ins:
			file_path_lists.append(file_dict[i.text()])

		UE4_project = self.UE4Project_path_line.text()
		ue_lack_list = self.set.check_ue_asset(file_path_lists,UE4_project)
		if ue_lack_list:

			QMessageBox.information(self, "Lack Asset List", "".join(ue_lack_list))
		else:
			QMessageBox.information(self, "Lack Asset List", "No assets missing ! ~")

		
	def Start_input(self):
		file_lists_ins = self.File_list.selectedItems()

		file_path_lists = []
		for i in file_lists_ins:
			file_path_lists.append(file_dict[i.text()])

		UE4_editor = self.UE4Editor_path_line.text()
		UE4_project = self.UE4Project_path_line.text()

		is_del_fbx = self.Delete_ue_ani.isChecked()# Whether to delete the FBX file under the UE import path.
		if is_del_fbx == True:
			self.set.clear_fbx_file(file_path_lists,UE4_project) 

		json_file = self.set.create_json_file(file_path_lists)
		self.set.do_input_cmd(UE4_editor,UE4_project,json_file)

	def save_set(self):
		"""
		save seting
		"""
		set_info = {}
		set_info["ue_path"] = self.UE4Editor_path_line.text()
		set_info["project_file"] = self.UE4Project_path_line.text()

		self.model.save_set_file(set_info)
		
	def set_preset(self):
		"""
		set preset info
		"""
		set_info = self.model.get_preset()
		if not set_info == None:
			self.UE4Editor_path_line.setText(set_info["ue_path"])
			self.UE4Project_path_line.setText(set_info["project_file"])



if __name__ == '__main__':
	import sys
	app = QApplication(sys.argv)
	app.setStyle("fusion")
	widget  = main_window()
	widget.show()
	widget.set_preset()
	widget.Update_ep_list()
	sys.exit(app.exec_())