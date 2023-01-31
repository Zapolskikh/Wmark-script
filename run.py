from pathlib import Path
from uuid import uuid4
from create_new_folder_project import create_new_folder_project
from wmarksln_script import wmarksln_script
from resourceh_script import resourceh_script
from wmarkrc_script import wmarkrc_script
from wmarkvcxproj_script import wmarkvcxproj_script
from cplcdevice_script import cplcdevice_script
from ctabplcviewclasslist import ctabplcviewclasslist_script
from wmarkplclfixxxvcxproj_script import wmarkplclfixxxvcxproj_script
from tkinter import INSERT
from datetime import datetime

def run(old_proj_name, new_proj_name, repository_path, text_log):
    # Create uuid4key
    uuid4key = str(uuid4())
    # NEW PROJECT CREATE
    try:
        create_new_folder_project(
            Path(f"{repository_path}\\WmarkPlc{old_proj_name}"), f"WMarkPlc{new_proj_name}", old_proj_name, new_proj_name,text_log)
        # HMI
        wmarkrc_script(f"{repository_path}\\WMark.rc",
                    old_proj_name, new_proj_name,text_log)
        resourceh_script(f"{repository_path}\\resource.h",
                        old_proj_name, new_proj_name,text_log)
        # WAMRK REFERENCES
        wmarkvcxproj_script(f"{repository_path}\\WMark.vcxproj",
                            old_proj_name, new_proj_name, uuid4key,text_log)
        wmarksln_script(f"{repository_path}\\WMark.sln",
                        old_proj_name, new_proj_name, uuid4key,text_log)
        # WmarkPLC
        cplcdevice_script(
            f"{repository_path}\\WMarkPlc\\CPlcDevice.h", old_proj_name, new_proj_name,text_log)
        ctabplcviewclasslist_script(
            f"{repository_path}\\WMarkPlc\\CTabPlcViewClassList.cpp", old_proj_name, new_proj_name,text_log)
        # WMarlPLCLfiXXXProj
        wmarkplclfixxxvcxproj_script(
            f'{repository_path}\\WMarkPlc{new_proj_name}\\WMarkPlc{new_proj_name}.vcxproj', new_proj_name, uuid4key, text_log)
    except Exception as e:
        text_log.insert(INSERT,f'[{datetime.now()}] {e}\n')
        return
