import maya.cmds as cmds

import export_level_info
import export_fbx


def build_menu():
    # if cmds.menu("MyProjectMenu", exists=True):
    #     cmds.deleteUI("MyProjectMenu", menu=True)

    cmds.menu('PFEMenu', label='PFE', parent='MayaWindow')
    cmds.menuItem(label='Export Level', parent='PFEMenu', command=lambda *_: export_level_info.main())
    cmds.menuItem(label='Export FBX', parent='PFEMenu', command=lambda *_: export_fbx.main())


cmds.evalDeferred('build_menu()', lowestPriority=True)