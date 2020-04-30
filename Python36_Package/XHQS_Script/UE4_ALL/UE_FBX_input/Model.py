#!/usr/bin/python
# -*- coding: utf-8 -*-
#Author : HW
#--2019-07-05
import os 
import json
class UE_FBX_INPUT_MODEL(object):
	def __init__(self):
		super(UE_FBX_INPUT_MODEL, self).__init__()
		self.source_path = "H:/XHQS_Project01/3D_Project/branches/assets/Export/"
		self.save_path = os.path.expanduser('~') + "/" +"UE_input_fbx"
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

	def get_fbx_file(self,shot_path_lists):
		"""
		get fbx file list and path dictionary
		"""
		fbx_path_dict = {}
		fbx_file_lists = []
		for i in shot_path_lists:
			fbx_lists = os.listdir(i)

			for file_name in fbx_lists:
				if ".fbx" in file_name:
					fbx_file_lists.append(file_name)
					fbx_path_dict[file_name] = i + "/" + file_name
		return fbx_file_lists,fbx_path_dict

	def save_set_file(self,set_info={}):
		"""
		save seting file
		"""
		if os.path.exists(self.save_path)==False:
			os.makedirs(self.save_path)
		with open(self.save_path+"/"+"UE_input_fbx_preset.json","w+") as f:
			f.truncate()
			set_json = json.dumps(set_info)
			f.write(set_json)

	def get_preset(self):
		"""
		get preset file info
		"""
		if os.path.exists(self.save_path)==False:
			os.makedirs(self.save_path)
		with open(self.save_path+"/"+"UE_input_fbx_preset.json","a+") as f:
			f.seek(0)
			json_set = f.read()
			if json_set== '':
				set_info = None
			else :
				set_info = json.loads(json_set)
				
		return set_info