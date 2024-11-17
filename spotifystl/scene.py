import bpy, bmesh
import tempfile, zipfile

def generate_stl(svg_content, output_path):
    # Selecciona y elimina todos los objetos en la escena
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)

    # Purga huérfanos
    bpy.ops.outliner.orphans_purge()
    bpy.ops.outliner.orphans_purge()
    bpy.ops.outliner.orphans_purge()
    
    with tempfile.NamedTemporaryFile(suffix=".svg", delete=False) as tmp_file:
        tmp_file.write(svg_content)
        tmp_file_path = tmp_file.name

    # Importar el SVG como curva
    bpy.ops.import_curve.svg(filepath=tmp_file_path)

    # Borra el rectángulo
    obj = bpy.data.objects[0]
    obj.select_set(True)
    bpy.ops.object.delete() 

    bpy.ops.object.select_all(action='DESELECT')

    # Convertir todas las curvas importadas a malla
    for obj in bpy.data.objects:
        obj.select_set(True)
        bpy.context.view_layer.objects.active = obj
            
    bpy.ops.object.convert(target='MESH')
    bpy.ops.object.join()

    code1 = bpy.context.active_object

    bpy.context.view_layer.objects.active = code1
    code1.select_set(True)
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_mode(type="FACE")
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.object.mode_set(mode='OBJECT')

    # Añadir modificador de solidificación
    solidify_modifier = code1.modifiers.new(name="Solidify", type='SOLIDIFY')
    solidify_modifier.thickness = 0.0005
    bpy.ops.object.modifier_apply(modifier="Solidify")

    code1.location = (0, 0, 0.25)
    bpy.ops.transform.resize(value=(500, 500, 500))

    #duplicate and move
    bpy.ops.object.duplicate()
    code2 = bpy.context.active_object
    code2.location = (0, 0, 1)


    code1.select_set(True)
    bpy.ops.object.join()

    codes = bpy.context.active_object

    bpy.ops.object.transform_apply(scale=True)

    # Añade rectángulo
    bpy.ops.mesh.primitive_cube_add(location=(45, 11.25, 0.5))
    bpy.ops.transform.resize(value=(45, 11.25, 0.5))
    bpy.ops.object.transform_apply(scale=True)

    # bevel
    obj = bpy.context.active_object

    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action='DESELECT')

    bm = bmesh.from_edit_mesh(obj.data)
    bm.edges.ensure_lookup_table()

    [bm.edges[i].select_set(True) for i in [1,3,6,9]]
    bpy.ops.mesh.bevel(offset=5, segments=15, profile=0.5, affect='EDGES')

    # Salir del modo edición
    bpy.ops.object.mode_set(mode='OBJECT')

    bool_one = obj.modifiers.new(type="BOOLEAN", name="bool 1")
    bool_one.object = codes
    bool_one.operation = 'DIFFERENCE'

    #añadir cosa del llavero
    bpy.ops.mesh.primitive_cylinder_add(location=(3.75, 18.5, 0))
    cyl = bpy.context.active_object
    bpy.ops.transform.resize(value=(1.5,1.5,3))

    bool_one = obj.modifiers.new(type="BOOLEAN", name="bool 3")
    bool_one.object = cyl
    bool_one.operation = 'DIFFERENCE'


    # Exportar archivos STL
    with tempfile.NamedTemporaryFile(suffix=".stl", delete=False) as codes_tmp, \
        tempfile.NamedTemporaryFile(suffix=".stl", delete=False) as rectangle_tmp:

        codes_stl_path = codes_tmp.name
        rectangle_stl_path = rectangle_tmp.name

        bpy.ops.object.select_all(action='DESELECT')

        codes.select_set(True)
        bpy.ops.export_mesh.stl(filepath=codes_stl_path, use_selection=True)

        bpy.ops.object.select_all(action='DESELECT')
        obj.select_set(True)
        bpy.ops.export_mesh.stl(filepath=rectangle_stl_path, use_selection=True)

        # Crear archivo ZIP y añadir los archivos STL
        with zipfile.ZipFile(output_path, 'w') as zipf:
            zipf.write(codes_stl_path, 'codes.stl')
            zipf.write(rectangle_stl_path, 'rectangle.stl')