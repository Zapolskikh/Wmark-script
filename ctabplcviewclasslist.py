repository_path = 'C:\\medicomtfs2018\\WMark2020\\WMark2020LFI174'


def ctabplcviewclasslist_script(cplcdevice_path, original_project, dist_project):

    with open(cplcdevice_path, 'r') as txt_file:
        a = txt_file.readlines()
    index_include1 = None
    index_include2 = None
    index_ref = None
    index_ref_insert = None
    for i, row in enumerate(a):
        if f'#include "..\WMarkPlc{original_project}\CWMarkTabPlc' in row:
            index_include1 = i
        if f'#include "..\WMarkPlc{original_project}\CWMarkPlc' in row:
            index_include2 = i
        if f'AddTabPlcViewClassList("NONE",					"No PLC",' in row:
            index_ref = i
        if f'{original_project}' in row:
            index_ref_insert = i

    block_include1 = a[index_include1:index_include1+1]
    block_include2 = a[index_include2:index_include2+1]
    block_ref = a[index_ref:index_ref+1]

    print(block_include1)
    print(block_include2)
    print(block_ref)

    block_include1 = [x.replace(original_project, dist_project)
                      for x in block_include1]
    block_include2 = [x.replace(original_project, dist_project)
                      for x in block_include2]
    block_ref = [x.replace('"NONE",					"No PLC",				nullptr,								RUNTIME_CLASS(CWMarkPlc),			""',
                           f'"PLC {dist_project}", "PLC {dist_project}", RUNTIME_CLASS(CWMarkTabPlc{dist_project}), RUNTIME_CLASS(CWMarkPlc{dist_project}),	"PLC {dist_project}"')
                 for x in block_ref]

    a.insert(index_include1+1, "".join(block_include1))
    a.insert(index_include2+1, "".join(block_include2))
    a.insert(index_ref_insert+1, "".join(block_ref))

    with open(cplcdevice_path, 'w') as txt_file:
        txt_file.writelines(a)
