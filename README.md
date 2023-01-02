### Decimator - Blender Addon

This Add-on is actually a macro for Blender that uses the already existing <a href="https://docs.blender.org/manual/en/latest/modeling/modifiers/generate/decimate.html">Decimate Modifier</a> in Planar mode for asset optimization and polygon decimation. I developed it for personal use to improve performance on larger scenes, specially when they are imported from other software and formats, such as *.fbx or Autodesk Revit architectural files, for example.

## How to use it

After the Add-on is installed on <a href="https://www.blender.org/">Blender</a>, in Object Mode press Ctrl+Shift+D to bring the Decimator pie menu and select the desired Angle Limit.
For simple objects, 5° Angle Limit is more than enough.

![decimate](https://user-images.githubusercontent.com/108239558/210245413-3ad654c9-e687-4985-ac7e-70565422c42e.gif)
The addon has an Angle Limit range from 5° to 90°. Users should be careful to apply the 90° Angle Limit because it can be a bit extreme depending on the geometry and desired effect. For most cases the range of 5° to 30° is enough to decimate polys and still keep the overall geometry intact.

Besides that, I also recommend using Blender's Tris to Quads function under the Edit Mode (Shortcut: Alt+J on Edit Mode). Sometimes it will have the same result as this addon; it's up to you to decide which one is better or can generate the desired effect.

## How to install this Add-on
To be able to use this feature inside Blender, you need first to download Blender Software at it's [Official Website Download Page](https://www.blender.org/download/). You can also download at the [Windows App Store](https://apps.microsoft.com/store/detail/blender/9PP3C07GTVRH) if you're using Windows 10/11.

1. Download this repository Zip folder;
2. Open up Blender Preferences in Edit > Preferences;
3. Under the 'Add-ons' tab select Install and select the Zip folder from this repository. You'll have to mark the checkbox to enable it as any other Add-on.

- As mentioned, this Add-on is currently binded on the Ctrl+Shift+D hotkey. You can change the keymapping to any other you like most by accessing Blender Preferences > Keymap > 3D View (Global):


![image](https://user-images.githubusercontent.com/108239558/210252075-614e3851-cb6a-4d94-a9bf-28b5a1e4c5e2.png)

> GPL License.
You can fork this project and create your own version of it without notifying me.
