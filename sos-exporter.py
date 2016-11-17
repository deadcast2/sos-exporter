import bpy

def write_object_data(context, filepath):
    f = open(filepath, 'w', encoding='utf-8')
    f.write("Hello World")
    f.close()
    return {'FINISHED'}

from bpy_extras.io_utils import ExportHelper
from bpy.props import StringProperty
from bpy.types import Operator

class ExportObjectData(Operator, ExportHelper):
    """Save a Simple Object Structure file"""
    bl_idname = "export_sos.object_data"
    bl_label = "Export SOS"
    filename_ext = ".sos"
    filter_glob = StringProperty(
            default="*.sos",
            options={'HIDDEN'},
            maxlen=255
            )

    def execute(self, context):
        return write_object_data(context, self.filepath)

def menu_func_export(self, context):
    self.layout.operator(ExportObjectData.bl_idname, text="SOS (.sos)")

def register():
    bpy.utils.register_class(ExportObjectData)
    bpy.types.INFO_MT_file_export.append(menu_func_export)

def unregister():
    bpy.utils.unregister_class(ExportObjData)
    bpy.types.INFO_MT_file_export.remove(menu_func_export)

if __name__ == "__main__":
    register()

    # test call
    bpy.ops.export_sos.object_data('INVOKE_DEFAULT')
