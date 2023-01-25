def wmarksln_script(wmarksln_path, original_project, dist_project):

    with open(wmarksln_path, 'r') as txt_file:
        a = txt_file.readlines()

    with open('uuid_key', 'r') as txt_file:
        uuid4key = txt_file.readlines()
        index_include = None
        index_ref = None

        for i, row in enumerate(a):
            if f"WMarkPlc{original_project}" in row:
                index_include = i
            if "Global" in row:
                index_ref = i
                break
        block_ref = a[index_include:index_include+2]
        tmp = []
        for i, row in enumerate(block_ref):
            if i == 0:
                tmp_str = row[:row.find('vcxproj", ')]
                tmp.append((tmp_str + 'vcxproj", ' + '"{' + str(
                    uuid4key[0]).upper() + '}"\n').replace(original_project, dist_project))
            else:
                tmp.append(row.replace(original_project, dist_project))

    a.insert(index_ref, "".join(tmp))
    print(block_ref)
    print(tmp)

    with open(wmarksln_path, 'w') as txt_file:
        txt_file.writelines(a)


# wmarksln_script('D:\\mark\\WMark.sln', "LFI174", "LFI176")
