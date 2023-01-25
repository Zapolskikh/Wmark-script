def wmarkvcxproj_script(wmarkvcxproj_path: str, original_project, dist_project_name, uuid4key):
    
    with open(wmarkvcxproj_path, 'r') as txt_file:
        a = txt_file.readlines()
        index_include = None
        index_ref = None
        for i, row in enumerate(a):
            if "<AdditionalIncludeDirectories>$(SolutionDir)" in row:
                index_include = i
            if f'<ProjectReference Include="WMarkPlc{original_project}\WMarkPlc{original_project}.vcxproj">' in row:
                index_ref = i

        tmp = a[index_include].replace("</AdditionalIncludeDirectories>",
                                       f";$(SolutionDir)WMarkPlc{dist_project_name}</AdditionalIncludeDirectories>")
        a.pop(index_include)
        a.insert(index_include, tmp)
        block_ref = a[index_ref:index_ref+3]
        tmp = []
        for i, row in enumerate(block_ref):

            if i == 1:
                tmp_key_str = row[:row.find("}<")]
                tmp.append(tmp_key_str[:-36] + uuid4key + '}</Project>\n')
            else:
                tmp.append(row.replace(original_project, dist_project_name))
        a.insert(index_ref+3, "".join(tmp))

    with open(wmarkvcxproj_path, 'w') as txt_file:
        txt_file.writelines(a)



# wmarkvcxproj_script('D:\\mark\\WMark.vcxproj', "LFI174", "LFI176")
