from pathlib import Path
import shutil
import os


def create_new_folder_project(source_folder_path, new_folder_name):
    try:
        project_dir = source_folder_path.parent / new_folder_name
        shutil.copytree(source_folder_path, project_dir)
        all_files = list(project_dir.rglob("*.*"))
        for x in all_files:
            if "debug" not in str(x).lower():
                os.rename(x, str(x).replace('LFI174', 'LFI176'))
    except FileExistsError:
        pass

    all_files = list(project_dir.rglob("*.*"))

    for x in all_files:
        if "debug" not in str(x).lower():
            with open(x, 'r') as txt_file:
                print(x)
                a = txt_file.readlines()
                file = [x.replace('LFI174', 'LFI176') for x in a]

            with open(x, 'w') as txt_file:
                txt_file.writelines(file)


# create_new_folder_project(Path('D:\\mark\\WMarkPlcLFI174'), "WMarkPlcLFI176")
