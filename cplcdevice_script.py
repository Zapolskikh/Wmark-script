def cplcdevice_script(cplcdevice_path, original_project, dist_project):

    with open(cplcdevice_path, 'r') as txt_file:
        a = txt_file.readlines()
    index_include = None
    index_ref = None
    for i, row in enumerate(a):
        if f"friend class CWMarkTabPlc{original_project}" in row:
            index_include = i
        if f"friend class CWMarkPlc{original_project}" in row:
            index_ref = i
            break
    block_ref = a[index_include:index_include+2]
    block_ref = [
        x.replace(original_project, dist_project) for x in block_ref]

    a.insert(index_ref+1, "".join(block_ref))

    with open(cplcdevice_path, 'w') as txt_file:
        txt_file.writelines(a)
