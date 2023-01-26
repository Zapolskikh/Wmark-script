import shutil
import os
import re


def create_new_folder_project(source_folder_path, new_folder_name, old_proj_name, new_proj_name):
    project_dir = source_folder_path.parent / new_folder_name

    counter_old_name = re.findall(old_proj_name, str(source_folder_path), re.I)
    counter = len(counter_old_name) - 1
    try:
        project_dir = source_folder_path.parent / new_folder_name
        shutil.copytree(source_folder_path, project_dir)
        all_files = list(project_dir.rglob("*.*"))
        for x in all_files:
            if "debug" not in str(x).lower():
                os.rename(x, str(x).replace(old_proj_name, new_proj_name).replace(
                    new_proj_name, old_proj_name, counter))
    except FileExistsError:
        pass

    all_files = list(project_dir.rglob("*.*"))

    for x in all_files:
        if "debug" not in str(x).lower():
            with open(x, 'r') as txt_file:
                print(x)
                a = txt_file.readlines()
                file = [x.replace(old_proj_name, new_proj_name) for x in a]

            with open(x, 'w') as txt_file:
                txt_file.writelines(file)


# create_new_folder_project(Path(
#     'C:\\medicomtfs2018\\WMark2020\\WMark2020LFI174\\WMarkPlcLFI174'), "WMarkPlcLFI191", "LFI174", "LFI191")
