from pathlib import Path
from uuid import uuid4
from create_new_folder_project import create_new_folder_project
from wmarksln_script import wmarksln_script
from resourceh_script import resourceh_script
from wmarkrc_script import wmarkrc_script
from wmarkvcxproj_script import wmarkvcxproj_script
from cplcdevice_script import cplcdevice_script
from ctabplcviewclasslist import ctabplcviewclasslist_script

# repository_path = 'C:\\medicomtfs2018\\WMark2020\\WMark2020LFI174'

def run(old_proj_name, new_proj_name, repository_path):
    #Create uuid4key
    uuid4key = str(uuid4())
    # NEW PROJECT CREATE
    create_new_folder_project(
        Path(f"{repository_path}\\WmarkPlc{old_proj_name}"), f"WMarkPlc{new_proj_name}",old_proj_name, new_proj_name)
    # HMI
    wmarkrc_script(f"{repository_path}\\WMark.rc",
                   old_proj_name, new_proj_name)
    resourceh_script(f"{repository_path}\\resource.h",
                     old_proj_name, new_proj_name)
    # WAMRK REFERENCES
    wmarkvcxproj_script(f"{repository_path}\\WMark.vcxproj",
                        old_proj_name, new_proj_name, uuid4key)
    wmarksln_script(f"{repository_path}\\WMark.sln",
                    old_proj_name, new_proj_name, uuid4key)
    # WmarkPLC
    cplcdevice_script(
        f"{repository_path}\\WMarkPlc\\CPlcDevice.h", old_proj_name, new_proj_name)
    ctabplcviewclasslist_script(
        f"{repository_path}\\WMarkPlc\\CTabPlcViewClassList.cpp", old_proj_name, new_proj_name)


# run("LFI174", "LFI176", repository_path)
