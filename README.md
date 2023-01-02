### Decimator - Blender Addon

This addon is actually a macro for Blender that uses the already existing <a href="https://docs.blender.org/manual/en/latest/modeling/modifiers/generate/decimate.html">Decimate Modifier</a> for asset optimization and polygon decimation. I developed it for personal use to improve performance on larger scenes, specially when they are imported from other software and formats, such as *.fbx or Autodesk Revit architectural files, for example.

## How to use it

After the addon is installed on <a href="https://www.blender.org/">Blender</a>, in Object Mode press Ctrl+Shift+D to bring the Decimator pie menu and select the desired Angle Limit.
For simple objects, 5° Angle Limit is more than enough.
![decimate](https://user-images.githubusercontent.com/108239558/210245413-3ad654c9-e687-4985-ac7e-70565422c42e.gif)
The addon has an Angle Limit range from 5° to 90°. Users should be careful to apply the 90° Angle Limit because it can be a bit extreme depending on the geometry and desired effect. For most cases the range of 5° to 30° is enough to decimate polys and still keep the overall geometry intact.

Besides that, I also recommend using Blender's Tris to Quads function under the Edit Mode (Shortcut: Alt+J on Edit Mode). Sometimes it will have the same result as this addon; it's up to you to decide which one is better or can generate the desired effect.

> GPL License.
You can fork this project and create your own version of it without notifying me.
