import os
import pathlib
from collections import defaultdict


def sort_and_format_result(dct: dict) -> str:
    final_result = ""
    for key, value in sorted(dct.items()):
        final_result += f"{key}\n"
        for v in sorted(value):
            final_result += f"- - - {v + key}\n"
    return final_result


DIR_SEPARATOR = os.path.sep
# path = os.getcwd()
path = input()
extensions = defaultdict(list)

for dir_paths, dir_names, file_names in os.walk(path):
    if not dir_paths.count(DIR_SEPARATOR) > 1:
        for file_name in file_names:
            name, extension = os.path.splitext(file_name)
            extensions[extension].append(name)

desktop_path = pathlib.Path.home() / 'Desktop'
file_to_save_path = os.path.join(desktop_path, "report.txt")

with open(file_to_save_path, "w") as wf:
    wf.write(sort_and_format_result(extensions))

