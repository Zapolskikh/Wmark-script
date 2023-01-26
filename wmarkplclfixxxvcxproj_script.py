def wmarkplclfixxxvcxproj_script(wmarkplclfixxxvcxproj_path, uuid4key):

    with open(wmarkplclfixxxvcxproj_path, 'r') as txt_file:
        a = txt_file.readlines()

    index_include = None
    # index_ref = None
    for i, row in enumerate(a):
        if "<ProjectGuid>" in row:
            index_include = i
            break
    a.pop(index_include)

    # print(index_include)
    a.insert(index_include,
             f'    <ProjectGuid>{uuid4key}</ProjectGuid>\n')
    with open(wmarkplclfixxxvcxproj_path, 'w') as txt_file:
        txt_file.writelines(a)


# wmarkplclfixxxvcxproj_script(
#     'C:\\medicomtfs2018\\WMark2020\\mark\\WMarkPlcLFI176\\WMarkPlcLFI176.vcxproj', uuid4key)
