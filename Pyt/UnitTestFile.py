import unreal

# sequence = unreal.AssetToolsHelpers.get_asset_tools().create_asset('SequenceMaster', '/Game/', unreal.LevelSequence,
#                                                                    unreal.LevelSequenceFactoryNew())
#
targetSequence = unreal.load_object(None, "/Game/SequenceMaster")

# print "Y"
#
#
# def create_level_sequence(asset_name, package_path='/Game/'):
#     sequence = unreal.AssetToolsHelpers.get_asset_tools().create_asset(asset_name, package_path, unreal.LevelSequence,
#                                                                        unreal.LevelSequenceFactoryNew())
#
#
#     return sequence