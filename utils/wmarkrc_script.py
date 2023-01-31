from tkinter import INSERT
from datetime import datetime

def find_index_dialog(wmarkrc_path: str, source: str):
    with open(wmarkrc_path, 'r', encoding='utf8') as txt_file:
        a = txt_file.readlines()
        index_start = 0
        index_end = 0
        for i, row in enumerate(a):
            if f'IDD_TAB{source}, DIALOG' in row:
                index_start = i
        for i in range(index_start, 9999):
            if 'END' in a[i]:
                index_end = i
                break
    return index_start, index_end

def find_index_layout(wmarkrc_path: str, source: str):
    with open(wmarkrc_path, 'r', encoding='utf8') as txt_file:
        a = txt_file.readlines()
        index_start = 0
        index_end = 0
        for i, row in enumerate(a):
            if f'IDD_TAB{source} AFX_DIALOG_LAYOUT' in row:
                index_start = i
        for i in range(index_start, 9999):
            if 'END' in a[i]:
                index_end = i
                break
    return index_start, index_end

def find_index_dialogEX(wmarkrc_path: str, source: str):
    with open(wmarkrc_path, 'r', encoding='utf8') as txt_file:
        a = txt_file.readlines()
        index_start = 0
        index_end = 0
        for i, row in enumerate(a):
            if f'IDD_TAB{source} DIALOGEX' in row:
                index_start = i
        for i in range(index_start, 9999):
            if 'END' in a[i]:
                index_end = i
                break
    return index_start, index_end

def wmarkrc_script(wmarkrc_path, source: str, destination: str,text_log):
    text_log.insert(INSERT,f'[{datetime.now()}] Create new {source} screen\n')
    with open(wmarkrc_path, 'r', encoding='utf8') as txt_file:
        a = txt_file.readlines()

        insexes_dialog = find_index_dialog(wmarkrc_path, source)
        new_block_of_HMI_dialog = a[insexes_dialog[0]:insexes_dialog[1]+1]
        new_block_of_HMI_dialog = [
            x.replace(source, destination) for x in new_block_of_HMI_dialog]

        insexes_layout = find_index_layout(wmarkrc_path, source)
        new_block_of_HMI_layout = a[insexes_layout[0]:insexes_layout[1]+1]
        new_block_of_HMI_layout = [
            x.replace(source, destination) for x in new_block_of_HMI_layout]

        insexes_dialogEX = find_index_dialogEX(wmarkrc_path, source)
        new_block_of_HMI_dialogEX = a[insexes_dialogEX[0]:insexes_dialogEX[1]+1]
        new_block_of_HMI_dialogEX = [
            x.replace(source, destination) for x in new_block_of_HMI_dialogEX]

    a.insert(insexes_dialog[1]+1, " ".join(new_block_of_HMI_dialog)+"\n")
    a.insert(insexes_layout[1]+3, " ".join(new_block_of_HMI_layout)+"\n")
    a.insert(insexes_dialogEX[1]+1, " ".join(new_block_of_HMI_dialogEX)+"\n")

    with open(wmarkrc_path, 'w', encoding='utf8') as txt_file:
        txt_file.writelines(a)
