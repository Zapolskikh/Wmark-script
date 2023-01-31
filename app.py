import tkinter as tk
from pathlib import Path
from uuid import uuid4
from utils.create_new_folder_project import create_new_folder_project
from utils.wmarksln_script import wmarksln_script
from utils.resourceh_script import resourceh_script
from utils.wmarkrc_script import wmarkrc_script
from utils.wmarkvcxproj_script import wmarkvcxproj_script
from utils.cplcdevice_script import cplcdevice_script
from utils.ctabplcviewclasslist import ctabplcviewclasslist_script
from utils.wmarkplclfixxxvcxproj_script import wmarkplclfixxxvcxproj_script
from tkinter import INSERT
from datetime import datetime

class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs) -> None:
        tk.Tk.__init__(self, *args, **kwargs)
        self.title('Welcome WMark new project tool')
        self.resizable(width=False, height=False)

        self.main_frame = tk.Frame(master=self, width=600, height=520)
        self.main_frame.pack()

        self.label_temp = tk.Label(master=self, text="Enter the name of the project you want to use as a template (examle: LFI174)",
                            bd=4, wraplength=170, relief="groove", width=25)
        self.label_temp.place(x=60, y=40)

        self.entry_temp = tk.Entry(master=self, font=1, justify="center", width=7)
        self.entry_temp.place(x=110, y=100)

        self.label_dist = tk.Label(master=self, text="Enter the name of the project you want to create (example: LFI175)",
                            bd=4, wraplength=170, relief="groove", width=25)
        self.label_dist.place(x=270, y=40)

        self.entry_dist = tk.Entry(master=self, font=1, justify="center", width=7)
        self.entry_dist.place(x=320, y=100)

        self.label_arrow = tk.Label(master=self, text='=======>', font=1)
        self.label_arrow.place(x=205, y=100)

        self.label_repository = tk.Label(master=self, text="Set the path to the WMark solution repository. Default is 'C:\medicomtfs2018\WMark2020'",
                                    bd=4, wraplength=400, relief="groove", width=50)
        self.label_repository.place(x=75, y=140)

        self.entry_repository = tk.Entry(master=self, width=59)
        self.entry_repository.place(x=75, y=185)

        self.button_create = tk.Button(master=self, width=10, text="Create", command= self.create_project)
        self.button_create.place(x=213, y=210)


        self.text_log = tk.Text(master=self, height=19, width=100,font=('Comic Sans MS', 7))
        self.text_log.place(x=0, y=260)

        self.label_creator = tk.Label(master=self,text="Created by Oleg Zapolskikh", font=('Comic Sans MS', 8))
        self.label_creator.place(x=450, y=230)

    def create_project(self):
        if self.entry_repository.get():
            self.repository_path = self.entry_repository.get()
        else:
            self.repository_path = 'D:\\medicomtfs2018\\WMark2020\\WMark2020Dev'

        self.run(self.entry_temp.get(), self.entry_dist.get(), self.repository_path,self.text_log)


    def run(self, old_proj_name, new_proj_name, repository_path, text_log):
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

if __name__== "__main__":
    main_window = MainWindow()
    main_window.mainloop()