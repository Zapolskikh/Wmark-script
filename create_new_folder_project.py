import shutil
import os
from pathlib import Path

def create_new_folder_project(source_folder_path, new_folder_name, old_proj_name, new_proj_name):
    project_dir = source_folder_path.parent / new_folder_name
    # all_files = list(project_dir.rglob("*.*"))
    # all_files = list(os.walk(project_dir))
    # all_files = [f for f in os.listdir(project_dir)]
    # print(project_dir)
    # print(all_files)
    try:
        project_dir = source_folder_path.parent / new_folder_name
        shutil.copytree(source_folder_path, project_dir)
        all_files = list(project_dir.rglob("*.*"))
        for x in all_files:
            if "debug" not in str(x).lower():
                os.rename(x, str(x).replace(old_proj_name, new_proj_name))
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


create_new_folder_project(Path('D:\\medicomtfs2018\\WMark2020\\WMark2020Dev\\WMarkPlcLFI174'), "WMarkPlcLFI183", "LFI174", "LFI183")
