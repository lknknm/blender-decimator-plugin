 ##### BEGIN GPL LICENSE BLOCK #####
#
#  Decimator, a Blender addon
#  (c) 2022 Lucas M.
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

import bpy
from bpy.types import Menu
from math import pi as PI, radians

bl_info = {
    "name": "Decimator",
    "author": "lknknm, lowpolypalmtree",
    "version": (0, 1, 0),
    "blender": (3, 40, 0),
    "location": "View3D > Add > Mesh",
    "description": "Macro for Decimate modifier in Planar mode",
    "category": "Object",
    "doc_url": "https://github.com/lknknm/blender-decimator-plugin"
    }

deg5 = radians(5)
deg30 = radians(30)
deg45 = radians(45)
deg60 = radians(60)
deg90 = radians(90)
deg120 = radians(120)
deg150 = radians(150)
deg180 = radians(180)

def apply_decimate_modifier(degrees):
        bpy.ops.object.modifier_add(type='DECIMATE')
        bpy.context.object.modifiers["Decimate"].decimate_type = 'DISSOLVE'
        bpy.context.object.modifiers["Decimate"].angle_limit = degrees
        bpy.ops.object.modifier_apply(modifier="Decimate", report=True, single_user=True)

#defines class for the Angle Limit of 5 degrees.
class decimate_5degrees(bpy.types.Operator):
    """
    Set Planar Mode Angle Limit to 5°
    """

    bl_idname = "decimate.5degrees"
    bl_label = "Angle Limit: 5°"
    
    @classmethod
    def poll(cls, context):
        return context.active_object is not None and context.active_object.select_get() is True and context.active_object.type == 'MESH'
    
    def execute(self, context):
        apply_decimate_modifier(deg5)
        return {'FINISHED'}
    
#defines class for the Angle Limit of 30 degrees.
class decimate_30degrees(bpy.types.Operator):
    """
    Set Planar Mode Angle Limit to 30°
    """

    bl_idname = "decimate.30degrees"
    bl_label = "Angle Limit: 30°"
    
    @classmethod
    def poll(cls, context):
        return context.active_object is not None and context.active_object.select_get() is True and context.active_object.type == 'MESH'
    
    def execute(self, context):
        apply_decimate_modifier(deg30)
        return {'FINISHED'}

#defines class for the Angle Limit of 45 degrees.
class decimate_45degrees(bpy.types.Operator):
    """
    Set Planar Mode Angle Limit to 45°
    """

    bl_idname = "decimate.45degrees"
    bl_label = "Angle Limit: 45°"
    
    @classmethod
    def poll(cls, context):
        return context.active_object is not None and context.active_object.select_get() is True and context.active_object.type == 'MESH'
    
    def execute(self, context):
        apply_decimate_modifier(deg45)
        return {'FINISHED'}

#defines class for the Angle Limit of 60 degrees.
class decimate_60degrees(bpy.types.Operator):
    """
    Set Planar Mode Angle Limit to 60°
    """

    bl_idname = "decimate.60degrees"
    bl_label = "Angle Limit: 60°"
    
    @classmethod
    def poll(cls, context):
        return context.active_object is not None and context.active_object.select_get() is True and context.active_object.type == 'MESH'
    
    def execute(self, context):
        apply_decimate_modifier(deg60)
        return {'FINISHED'}

#defines class for the Angle Limit of 90 degrees.
class decimate_90degrees(bpy.types.Operator):
    """
    Set Planar Mode Angle Limit to 90°
    """

    bl_idname = "decimate.90degrees"
    bl_label = "Angle Limit: 90°"
    
    @classmethod
    def poll(cls, context):
        return context.active_object is not None and context.active_object.select_get() is True and context.active_object.type == 'MESH'
    
    def execute(self, context):
        apply_decimate_modifier(deg90)
        return {'FINISHED'}
 
class VIEW3D_MT_PIE_decimator(Menu):
    bl_label = "Decimator"
    bl_idname = "VIEW3D_MT_PIE_decimator"

    def draw(self, context):
        layout = self.layout

        pie = layout.menu_pie()
        pie.operator("decimate.5degrees", icon="MOD_DECIM")
        pie.operator("decimate.90degrees", icon="MOD_DECIM")
        pie.separator() # Skip South position
        pie.operator("decimate.45degrees", icon="MOD_DECIM")
        pie.operator("decimate.30degrees", icon="MOD_DECIM")
        pie.operator("decimate.60degrees", icon="MOD_DECIM")
        pie.separator() # Skip Southwest position
        pie.separator() # Skip Southeast position

classes = (
    VIEW3D_MT_PIE_decimator, 
    decimate_5degrees, 
    decimate_30degrees, 
    decimate_45degrees, 
    decimate_60degrees, 
    decimate_90degrees
    )

addon_keymaps = []

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    # Add hotkey to Ctrl+Shift+D on 3D View (Global) - Hotkey can be customized within Blender settings
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = kc.keymaps.new(name='3D View', space_type='VIEW_3D')
        kmi = km.keymap_items.new(
                                    "wm.call_menu_pie", 
                                    type='D', 
                                    value='PRESS', 
                                    shift=True, 
                                    ctrl=True
                                    )
        kmi.properties.name = "VIEW3D_MT_PIE_decimator"
        addon_keymaps.append((km, kmi))


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

    # Remove the hotkey
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()


if __name__ == "__main__":
    register()

    bpy.ops.wm.call_menu_pie(name="VIEW3D_MT_PIE_decimator")
