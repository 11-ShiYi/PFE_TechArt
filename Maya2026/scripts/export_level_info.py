'''
Connect vscode with maya
run mel script:
commandPort -name "localhost:7001" -sourceType "mel" 
'''
import maya.api.OpenMaya as om
import maya.cmds as cmds
import os
import utils
import math

ignore_list = ['persp', 'top', 'front', 'side']

# def get_selection():
#     return cmds.ls(sl = 1)

def get_standard_meshes():
    standard_mesh_list = []
    top_level_nodes = cmds.ls(assemblies=True)
    for node in top_level_nodes:
        if node in ignore_list or node.endswith("Group"):
            continue
        standard_mesh_list.append(node)
    return standard_mesh_list

def get_group():
    group_list = []
    top_level_nodes = cmds.ls(assemblies=True)
    for node in top_level_nodes:
        if node in ignore_list or not node.endswith("Group"):
            continue
        group_list.append(node)
    return group_list


def convert_translate_to_unreal(maya_translate) -> tuple:
    """
    Convert translation from Maya (Y-up) to Unreal (Z-up) coordinate system.
    
    Maya: (X, Y, Z)
    Unreal: (X, Z, -Y)
    """
    return (maya_translate[0], maya_translate[2], -maya_translate[1])

def convert_scale_to_unreal(maya_scale) -> tuple:
    """
    Convert translation from Maya (Y-up) to Unreal (Z-up) coordinate system.
    
    Maya: (X, Y, Z)
    Unreal: (X, Z, -Y)
    """
    return (maya_scale[0], maya_scale[2], maya_scale[1])

def convert_rotate_to_unreal(maya_rotation) -> tuple:
    """
    Convert rotation from Maya (Y-up) to Unreal (Z-up) coordinate system.
    
    This is done by applying a -90 degree rotation around the X-axis.
    """
    maya_rotation = om.MEulerRotation(
    math.radians(maya_rotation[0]),
    math.radians(maya_rotation[1]),
    math.radians(maya_rotation[2])
    )

    # Step 1: Convert to quaternion
    quat = maya_rotation.asQuaternion()

    # Step 2: Apply coordinate system change: rotate -90 degrees around X-axis
    axis_convert = om.MQuaternion(math.radians(-90), om.MVector(1, 0, 0))
    rotated_quat = axis_convert * quat

    # Step 3: Convert from right-handed to left-handed (invert Z axis)
    # Mirror across YZ plane: negate the X component of the quaternion
    mirrored_quat = om.MQuaternion(
        rotated_quat.x,  # invert X
        -rotated_quat.y,
        -rotated_quat.z,
        rotated_quat.w   # also negate W to maintain same rotation
    )

    # Step 4: Convert back to Euler
    unreal_euler = mirrored_quat.asEulerRotation()

    # Step 5: Convert to degrees
    return tuple(math.degrees(a) for a in (unreal_euler.x, unreal_euler.y, unreal_euler.z))

# def convert_rotate_to_unreal(rotation_deg: tuple) -> tuple:
#     """
#     Convert a rotation from Maya (right-handed Y-up) to Unreal (left-handed Z-up),
#     and apply additional +90 degrees X-axis rotation to match Unreal's expected orientation.

#     :param rotation_deg: Rotation in degrees (X, Y, Z) from Maya
#     :return: Converted rotation as a tuple in degrees (X, Y, Z) for Unreal
#     """

#     # Step 1: Convert to radians and create MEulerRotation
#     rot_rad = [math.radians(a) for a in rotation_deg]
#     maya_euler = om.MEulerRotation(rot_rad[0], rot_rad[1], rot_rad[2], om.MEulerRotation.kXYZ)

#     # Step 2: Get rotation matrix from Euler
#     maya_matrix = maya_euler.asMatrix()

#     # Step 3: Coordinate system conversion matrix (Y-up -> Z-up, and handness flip)
#     axis_conversion = om.MMatrix([
#         [1,  0,  0, 0],
#         [0,  0,  1, 0],  # Swap Y and Z
#         [0, -1,  0, 0],  # Mirror Z axis (right- to left-handed)
#         [0,  0,  0, 1]
#     ])

#     # Step 4: Apply axis conversion to Maya rotation matrix
#     unreal_matrix = maya_matrix * axis_conversion

#     # Step 5: Add additional +90 degrees rotation around X-axis
#     x90_quat = om.MEulerRotation(math.radians(90), 0, 0).asMatrix()
#     unreal_matrix = x90_quat * unreal_matrix

#     # Step 6: Extract Euler rotation from final matrix
#     unreal_euler = om.MTransformationMatrix(unreal_matrix).rotation().asEulerRotation()

#     # Step 7: Convert radians to degrees
#     return tuple(math.degrees(a) for a in (unreal_euler.x, unreal_euler.y, unreal_euler.z))

def get_transform():
    '''
    data: {
        'SM_Cube_00': [
        (translate), (rotate), (scale),
        (translate), (rotate), (scale)
        ],
        'SM_Cube_01": [
        ]
    }
    '''
    data = {}
    group_list = get_group()
    for group in group_list:
        mesh_group = '_'.join(group.split('_')[:-1]) # get mesh name
        mesh_list = cmds.listRelatives(mesh_group, children = 1)

        subgroup_list = cmds.listRelatives(group, children = 1)
        transform_list = []

        for subgroup in subgroup_list:
            # if a mesh group has several meshes
            # 1: transform = group_transform + mesh_transform
            # 0: transform = group_transform
            if len(mesh_list) == 1:
                mesh = cmds.listRelatives(subgroup, children = 1)[0]
                mesh = group + '|' + subgroup + '|' + mesh
                subgroup = group + '|' + subgroup
                mesh_translate = cmds.getAttr(mesh + '.translate')[0]
                mesh_rotate = cmds.getAttr(mesh + ".rotate")[0]
                mesh_scale = cmds.getAttr(mesh + ".scale")[0]
                subgroup_translate = cmds.getAttr(subgroup + '.translate')[0]
                subgroup_rotate = cmds.getAttr(subgroup + '.rotate')[0]
                subgroup_scale = cmds.getAttr(subgroup + '.scale')[0]
                translate = (mesh_translate[0] + subgroup_translate[0], mesh_translate[1] + subgroup_translate[1], mesh_translate[2] + subgroup_translate[2])
                rotate = (mesh_rotate[0] + subgroup_rotate[0], mesh_rotate[1] + subgroup_rotate[1], mesh_rotate[2] + subgroup_rotate[2])
                scale = (mesh_scale[0] * subgroup_scale[0], mesh_scale[1] * subgroup_scale[1], mesh_scale[2] * subgroup_scale[2])
                
                translate = convert_translate_to_unreal(translate)
                rotate = convert_rotate_to_unreal(rotate)
                scale = convert_scale_to_unreal(scale)
                transform_list.append(translate)
                transform_list.append(rotate)
                transform_list.append(scale)
            else:
                subgroup = group + '|' + subgroup
                subgroup_translate = cmds.getAttr(subgroup + '.translate')[0]
                subgroup_rotate = cmds.getAttr(subgroup + '.rotate')[0]
                subgroup_scale = cmds.getAttr(subgroup + '.scale')[0]

                subgroup_translate = convert_translate_to_unreal(subgroup_translate)
                subgroup_rotate = convert_rotate_to_unreal(subgroup_rotate)
                subgroup_scale = convert_scale_to_unreal(subgroup_scale)
                transform_list.append(subgroup_translate)
                transform_list.append(subgroup_rotate)
                transform_list.append(subgroup_scale)

        data[mesh_group] = transform_list
    
    return data


def main():
    data = get_transform()
    json_file_name = 'level_info.json'
    base_dir = "D:/"
    json_file_path = os.path.join(base_dir, 'Json', json_file_name)
    json_dir = os.path.dirname(json_file_path)

    if not os.path.exists(json_dir):
        os.makedirs(json_dir)

    print(json_file_path)
    utils.write_json(data, json_file_path)

main()