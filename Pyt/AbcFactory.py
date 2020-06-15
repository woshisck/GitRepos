import unreal

# @unreal.uclass()
# class getAbcImportSetting(unreal.AbcImportSettings):
#     pass
first_time_run = True
class SequenceAbcEditor:
    def __init__(self):
        '''
        初始化 sequence和要导入的abc的路径
        :param level_sequence_path: sequence路径
        :param abc_file_path: abc路径
        '''
        self.Sequence = None
        self.frame_start= 0
        self.frame_end =0
        self.GeometryCache=None
        self.option=None
        self.task =None
        self.gc_path =None
        self.bind=None
        self.track=None
        self.Section=None

    def _set_geometry_caceh_file(self,asset_path=""):
        self.GeometryCache =unreal.EditorAssetLibrary.load_asset(asset_path)

    def _get_option(self):
        print self.option.import_type
        print self.option.sampling_settings.skip_empty
        print self.option.sampling_settings.frame_end

    def _set_option(self, frame_start =0, frame_end=0):
        options = unreal.AbcImportSettings()
        conversion = unreal.AbcConversionSettings()
        rotation = unreal.Vector(0.0, 90, 0.0)

        conversion.set_editor_property("rotation", rotation)
        options.set_editor_property("conversion_settings", conversion)

        options.import_type = unreal.AlembicImportType.SKELETAL
        options.sampling_settings.frame_start = frame_start
        options.sampling_settings.frame_end = frame_end
        options.sampling_settings.skip_empty = True
        #未解决 初始帧无法读取的问题前先用0代替
        # self.frame_start = frame_start
        self.frame_end =frame_end
        self.option = options
        # print options.import_type
        # print options.sampling_settings.skip_empty
        # print options.sampling_settings.frame_end


    def _import_alembic_manual(self, asset_path="/Game/", asset_name="AbcFile",frame_start = -1, frame_end = -1, abc_file_path=""):
        '''
        先初始化import option, 再用函数import_asset_tasks([import_task])
        :param asset_path:资产存放路径
        :param asset_name:资产名字
        :param frame_start:初始帧
        :param frame_end:结束帧
        :return:
        '''
        global first_time_run

        import_task = unreal.AssetImportTask()
        import_task.save = True
        # Set base properties on the task.
        import_task.filename = abc_file_path
        import_task.destination_path = asset_path
        import_task.destination_name = asset_name

        import_task.automated = False


        self.gc_path =asset_path+asset_name
        ##Option
        options = unreal.AbcImportSettings()
        conversion = unreal.AbcConversionSettings()
        rotation = unreal.Vector(0.0, 90, 0.0)

        conversion.set_editor_property("rotation", rotation)
        options.set_editor_property("conversion_settings", conversion)

        if self.option is not None:
            import_task.options = self.option
            #
            # asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
            print import_task
            unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([import_task])
            # self.GeometryCache = unreal.EditorAssetLibrary.load_asset(asset_path+asset_name)


    def _import_alembic_auto(self, asset_path="/Game/", asset_name="AbcFile",frame_start = -1, frame_end = -1, abc_file_path=""):
        '''
        先初始化import option, 再用函数import_asset_tasks([import_task])
        :param asset_path:资产存放路径
        :param asset_name:资产名字
        :param frame_start:初始帧
        :param frame_end:结束帧
        :return:
        '''
        global first_time_run

        import_task = unreal.AssetImportTask()
        import_task.save = True
        # Set base properties on the task.
        import_task.filename = abc_file_path
        import_task.destination_path = asset_path
        import_task.destination_name = asset_name

        import_task.automated = True

        self.gc_path =asset_path+asset_name
        ##Option
        options = unreal.AbcImportSettings()
        conversion = unreal.AbcConversionSettings()
        rotation = unreal.Vector(0.0, 90, 0.0)

        conversion.set_editor_property("rotation", rotation)
        options.set_editor_property("conversion_settings", conversion)

        if self.option is not None:
            import_task.options = self.option
            #
            # asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
            print import_task
            unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([import_task])
            # self.GeometryCache = unreal.EditorAssetLibrary.load_asset(asset_path+asset_name)


    def _add_abc_into_Sequence(self, level_sequence_path="", gc_path =""):
        '''
        导入sequence顺序: bind->track->section
        :return:
        '''

        self.GeometryCache = unreal.EditorAssetLibrary.load_asset(gc_path)
        self.Sequence = unreal.EditorAssetLibrary.load_asset(level_sequence_path)
        self.frame_start =  self.Sequence.get_playback_start()
        self.frame_end =self.Sequence.get_playback_end()

        self.bind=self.Sequence.add_spawnable_from_instance(self.GeometryCache)
        self.track=self.bind.add_track(unreal.MovieSceneGeometryCacheTrack)
        self.Section=self.track.add_section()

        GCParam = unreal.MovieSceneGeometryCacheParams()
        GCParam.set_editor_property("geometry_cache_asset", self.GeometryCache)

        self.Section.set_editor_property("params", GCParam)
        self.Section.set_range(self.frame_start, self.frame_end)

    def set_sequence(self, sequennPath):
        self.Sequence = unreal.EditorAssetLibrary.load_asset(sequennPath)
        self.frame_start =self.Sequence.get_playback_start()
        self.frame_end =self.Sequence.get_playback_end()


    def set_GeometryCache(self, GCPath):
        self.GeometryCache = unreal.EditorAssetLibrary.load_asset(GCPath)

    def clear_abc_track(self, abcTrackName):
        '''
        删除Sequence里的abc 绑定,需要提前设置好self.sequence
        :param abcTrackName: abc绑定名字
        :return:
        '''
        if self.Sequence is not None:
            for bind in self.Sequence.get_bindings():
                if bind.get_name() ==abcTrackName:
                    unreal.MovieSceneBindingExtensions.remove(bind)


'''
案例使用
'''
editor=SequenceAbcEditor()
option = editor._set_option()


editor._import_alembic_manual(frame_start=808, frame_end=2320, abc_file_path="D://AbcSample2.abc")
#
editor._add_abc_into_Sequence(level_sequence_path="/Game/mySequence", gc_path="/Game/AbcFile")
editor.clear_abc_track("EP005 SC001 P001 0001 Clytl Jianbu")
########################################################################################################################
# def build_abc_import_setting():
#     option = unreal.AbcImportSettings()
#     conversion = unreal.AbcConversionSettings()
#     option.set_editor_property("conversion_settings", conversion)
#     option.sampling_settings.frame_start = 0
#     option.sampling_settings.frame_end = 2320
#     # import_task.options.sampling_settings.skip_empty = True
#     option.import_type = unreal.AlembicImportType.GEOMETRY_CACHE
#     option.conversion_settings = unreal.AbcConversionSettings()
#     option.conversion_settings.rotation = unreal.Vector(0.0, 90, 0.0)
#     return option
#
# options = unreal.AbcImportSettings()
# conversion = unreal.AbcConversionSettings()
# rotation = unreal.Vector(0.0, 90, 0.0)
#
# conversion.set_editor_property("rotation", rotation)
# options.set_editor_property("conversion_settings", conversion)
#
#
# import_task = unreal.AssetImportTask()
# # import_task.save = True
# # Set base properties on the task.
# import_task.filename = "D://AbcSample2.abc"
# import_task.destination_path = "/Game/"
# import_task.destination_name = "AbcFile"
# import_task.automated = True# Suppress UI.
#
# import_task.options = build_abc_import_setting()
#
# factory = unreal.AlembicImportFactory()
# factory.asset_import_task = import_task
# import_task.factory = factory
#
# abcFactory = unreal.AlembicImportFactory()
#
#
# print import_task.options.import_type
#
# fbx_asset_importTask = unreal.AssetImportTask()
# fbx_asset_importTask.set_editor_property('import_as_skeletal', True)
# fbx_asset_importTask.set_editor_property('import_materials', False)
# fbx_asset_importTask.set_editor_property('import_animations', True)
#
# FBXSceneFactory = unreal.FbxSceneImportFactory()
#
# FBXSceneFactory.asset_import_task = import_task
#
# assetTool = unreal.AssetToolsHelpers.get_asset_tools()
# assetTool.import_asset_tasks([import_task])
########################################################################################################################





##Option
# options = unreal.AbcImportSettings()
# conversion = unreal.AbcConversionSettings()
# rotation = unreal.Vector(0.0, 90, 0.0)
#
# conversion.set_editor_property("rotation", rotation)
# options.set_editor_property("conversion_settings", conversion)
# with import_task.options('options', options) as finish:
#     print import_task.options.import_type
# unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([import_task])

