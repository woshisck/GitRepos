import unreal

prefixAnimationBlueprint = "animBP"
prefixAnimationSequence = "anim"
prefixAnimation = "anim"
prefixBlendSpace = "animBlnd"
prefixBlueprint = "bp"
prefixCurveFloat = "crvF"
prefixCurveLinearColor = "crvL"
prefixLevel = "lvl"
prefixMaterial = "mat"
prefixMaterialFunction = "mat_func"
prefixMaterialInstance = "mat_inst"
prefixParticleSystem = "fx"
prefixPhysicsAsset = "phsx"
prefixSkeletalMesh = "sk"
prefixSkeleton = "skln"
prefixSoundCue = "cue"
prefixSoundWave = "wv"
prefixStaticMesh = "sm"
prefixTexture2D = "tex"
prefixTextureCube = "HDRI"


@unreal.uclass()
class GetEditorAssetLibrary(unreal.EditorAssetLibrary):
    pass


@unreal.uclass()
class GetEditUtil(unreal.EditorUtilityLibrary):
    pass


class SkeletalMeshEditor():
    def __init__(self):
        self.SK_list = []
        self.selected_skMesh_list = []
        self.selected_material_list = []
        self.editorAssetLib = GetEditorAssetLibrary()
        self.editorAssetUtil = GetEditUtil()

    def checkAssetList(self):
        self.selected_skMesh_list = self.editorAssetUtil.get_selected_assets()
        for i in self.selected_skMesh_list:
            _className = unreal.Object.get_full_name(i)
            print _className[0]

    def GetProperPrefix(self, className):
        _prefix = ""
        if className == "AnimBlueprint":
            _prefix = prefixAnimationBlueprint
        elif className == "AnimSequence":
            _prefix = prefixAnimationSequence
        elif className == "Animation":
            _prefix = prefixAnimation
        elif className == "BlendSpace1D":
            _prefix = prefixBlendSpace
        elif className == "Blueprint":
            _prefix = prefixBlueprint
        elif className == "CurveFloat":
            _prefix = prefixCurveFloat
        elif className == "CurveLinearColor":
            _prefix = prefixCurveLinearColor
        elif className == "Material":
            _prefix = prefixMaterial
        elif className == "MaterialFunction":
            _prefix = prefixMaterialFunction
        elif className == "MaterialInstance":
            _prefix = prefixMaterialInstance
        elif className == "ParticleSystem":
            _prefix = prefixParticleSystem
        elif className == "PhysicsAsset":
            _prefix = prefixPhysicsAsset
        elif className == "SkeletalMesh":
            _prefix = prefixSkeletalMesh
        elif className == "Skeleton":
            _prefix = prefixSkeleton
        elif className == "SoundCue":
            _prefix = prefixSoundCue
        elif className == "SoundWave":
            _prefix = prefixSoundWave
        elif className == "StaticMesh":
            _prefix = prefixStaticMesh
        elif className == "Texture2D":
            _prefix = prefixTexture2D
        elif className == "TextureCube":
            _prefix = prefixTextureCube
        else:
            _prefix = ""

        return _prefix



# SK_class = SkeletalMeshEditor()
# SK_class.checkAssetList()

editorAssetLib = GetEditorAssetLibrary()
editorUtil = GetEditUtil()
selectedAssets = editorUtil.get_selected_asset_data()
allAssets = editorAssetLib.list_assets("/Game/TestShot", True, False)
# for i in selectedAssets:
#     print unreal.AssetData.get_full_name(i)
print unreal.AssetData.get_full_name(selectedAssets[0])