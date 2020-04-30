#!/usr/bin/python
# -*- coding: utf-8 -*-
 
from unreal_engine import FbxManager, FbxIOSettings, FbxImporter, FbxScene, FTransform, FRotator, FVector, FColor ,FQuat
from unreal_engine import FbxManager, FbxIOSettings, FbxImporter, FbxScene, FTransform, FRotator, FVector, FColor
import unreal_engine as ue

class FbxCurvesExtractor:
 
    def __init__(self, filename):
        self.manager = FbxManager()
        io_settings = FbxIOSettings(self.manager, 'IOSROOT')
        self.manager.set_io_settings(io_settings)
        importer = FbxImporter(self.manager, 'importer')
        importer.initialize(filename, io_settings)
        self.scene = FbxScene(self.manager, 'scene')
        importer._import(self.scene)
 
    def get_objects_by_class(self, name):
        objects = []
        for i in range(0, self.scene.get_src_object_count()):
            obj = self.scene.get_src_object(i)
            if obj.get_class_name() == name:
                objects.append(obj)
        return objects
 
    def get_members_by_class(self, parent, name):
        members = []
        for i in range(0, parent.get_member_count()):
            member = parent.get_member(i)
            if member.get_class_name() == name:
                members.append(member)
        return members
     
    def get_anim_stacks(self):
        return self.get_objects_by_class('FbxAnimStack')
 
    def get_anim_layers(self, stack):
        return self.get_members_by_class(stack, 'FbxAnimLayer')
 
    def get_properties(self, obj):
        prop = obj.get_first_property()
        while prop:
            yield prop
            prop = obj.get_next_property(prop)
 
    def get_anim_curves(self, layer):
        curves = []
        for i in range(0, self.scene.get_src_object_count()):
            obj = self.scene.get_src_object(i)
            # retrieve object properties
            for prop in self.get_properties(obj):
                curve_node = prop.get_curve_node(layer)
                if not curve_node:
                    continue
                channels = []
                for chan_num in range(0, curve_node.get_channels_count()):
                    # always get the first curve
                    curve = curve_node.get_curve(chan_num, 0)
                    if not curve:
                        continue
                    keys = []
                    for key_id in range(0, curve.key_get_count()):
                        keys.append((curve.key_get_seconds(key_id), curve.key_get_value(key_id)))
                    channels.append({'name': curve_node.get_channel_name(chan_num), 'keys': keys})
                curves.append({'object': obj.get_name(), 'class': obj.get_class_name(), 'property': prop.get_name(), 'channels': channels})
        return curves

 
def set_cam_key(focal_length_section,filename):

    extractor = FbxCurvesExtractor(filename)

    stack = extractor.get_anim_stacks()

    layers = extractor.get_anim_layers(stack[0])

    curves = extractor.get_anim_curves(layers[0])
    try:
        if curves[2]['property'] == 'FocalLength':
            FocalLength = curves[2]['channels']

            for idx,i in enumerate(FocalLength[0]['keys']):
                frame = i[0]#*25
                velum = FocalLength[0]['keys'][idx][1] 
                focal_length_section.sequencer_section_add_key(frame,velum)
    except:
        pass