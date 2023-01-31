from tkinter import INSERT
from datetime import datetime

def wmarkplclfixxxvcxproj_script(wmarkplclfixxxvcxproj_path, new_proj_name, uuid4key, text_log):
    text_log.insert(INSERT,f'[{datetime.now()}] Modify WMarkPlc{new_proj_name}.vcxproj (add new uuid4key)\n')

    with open(wmarkplclfixxxvcxproj_path, 'r') as txt_file:
        a = txt_file.readlines()

    index_include = None

    for i, row in enumerate(a):
        if "<ProjectGuid>" in row:
            index_include = i
            break
    a.pop(index_include)

    a.insert(index_include,
             f'    <ProjectGuid>{uuid4key}</ProjectGuid>\n')
    with open(wmarkplclfixxxvcxproj_path, 'w') as txt_file:
        txt_file.writelines(a)
