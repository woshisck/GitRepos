import unreal_engine as ue
from unreal_engine.classes import PyFbxFactory, Skeleton
from unreal_engine.enums import EFBXImportType

def analysis_file_path(file_path):
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

def fbx_import(fbx_file_path):

    EP,SC,PT,Shot,Fbx,part_name = analysis_file_path(fbx_file_path)
    
    UE_import_path = '/Game/Sequence/{}/{}/{}/{}/character'.format(EP,SC,PT,Shot)

    if part_name == "CH":
        skeleton_path = "/Game/Character/{}/Meshes/SK_CH_{}_Skeleton".format(ch_pro_name,ch_pro_name)
    elif part_name == "PR":
        skeleton_path = "/Game/Prop/{}/Meshes/SK_PR_{}_Skeleton".format(ch_pro_name,ch_pro_name)



    Skel_asset_path = '/Game/{}/{}/Meshes/SK_PR_{}_Skeleton'.format(asset_type,ch_pr_name,ch_pr_name)

    skel =ue.load_object(Skeleton,Skel_asset_path)

    anim_factory = PyFbxFactory()

    anim_factory.bReplaceExisting=True
    anim_factory.bShowOption = False

    anim_factory.ImportUI.Skeleton = skel
    anim_factory.ImportUI.MeshTypeToImport = EFBXImportType.FBXIT_Animation

    fbx_ani = anim_factory.factory_import_object(fbx_file_path, UE_import_path)
    fbx_ani.save_package()

