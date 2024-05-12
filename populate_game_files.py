import os
import json
import pathlib

self_directory = os.path.dirname(__file__)
json_path = os.path.join(self_directory, "addonsettings.json")

outfile_template = '''[configuration]

entry_symbol = "gdextension_init"
compatibility_minimum = 4.2

[libraries]

windows.debug.x86_32 = "res://addons/*addon_name*/bin/lib*addon_name*.windows.template_debug.x86_32.dll"
windows.release.x86_32 = "res://addons/*addon_name*/bin/lib*addon_name*.windows.template_release.x86_32.dll"
windows.debug.x86_64 = "res://addons/*addon_name*/bin/lib*addon_name*.windows.template_debug.x86_64.dll"
windows.release.x86_64 = "res://addons/*addon_name*/bin/lib*addon_name*.windows.template_release.x86_64.dll"'''

def format_extension_file(addon_name_actual: str) -> str:
    output_content = outfile_template.replace('*addon_name*', addon_name_actual)
    return output_content

with open(json_path, 'r') as json_file:
    # populate files in the game folder
    json_obj = json.load(json_file)
    extension_file_parent = os.path.join(json_obj['game_folder'], "addons", json_obj['addon_name'])
    extension_file_path = os.path.join(extension_file_parent, f'{json_obj["addon_name"]}.gdextension')
    extension_file_content = format_extension_file(json_obj['addon_name'])
    if not os.path.exists(extension_file_parent):
        pathlib.Path(extension_file_parent).mkdir(parents=True)
    with open(extension_file_path, 'w') as extension_file:
        extension_file.write(extension_file_content)
    