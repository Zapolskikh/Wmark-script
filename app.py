import tkinter as tk
from run import run

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

        run(self.entry_temp.get(), self.entry_dist.get(), self.repository_path,self.text_log)

main_window = MainWindow()
main_window.mainloop()