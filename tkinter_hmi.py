import tkinter as tk
from PIL import ImageTk, Image
from run import run


window = tk.Tk()
window.resizable(width=False, height=False)

main_frame = tk.Frame(master=window, width=500, height=400,)
main_frame.pack()


greeting = tk.Label(master=main_frame,  text="Welcome to Wmark New Project Tool", bg='cyan',
                    bd=5)
greeting.place(x=145, y=0)

label_temp = tk.Label(master=main_frame, text="Enter the name of the project you want to use as a template (examle: LFI174)",
                      bd=4, wraplength=170, relief="groove", width=25)
label_temp.place(x=60, y=40)

entry_temp = tk.Entry(master=main_frame, font=1, justify="center", width=7)
entry_temp.place(x=110, y=100)
# GET VALUE tmp_proj_value = template.get()


label_dist = tk.Label(master=main_frame, text="Enter the name of the project you want to create (example: LFI175)",
                      bd=4, wraplength=170, relief="groove", width=25)
label_dist.place(x=270, y=40)

entry_dist = tk.Entry(master=main_frame, font=1, justify="center", width=7)
entry_dist.place(x=320, y=100)

label_arrow = tk.Label(master=main_frame, text='=======>', font=1)
label_arrow.place(x=205, y=100)


label_repository = tk.Label(master=main_frame, text="Set the path to the WMark solution repository. Default is 'D:\\medicomtfs2018\\WMark2020\\WMark2020LFI174'",
                            bd=4, wraplength=400, relief="groove", width=50)
label_repository.place(x=75, y=140)

entry_repository = tk.Entry(master=main_frame, width=59)
entry_repository.place(x=75, y=185)

############################
# repository_path = ''


def create_project():
    if entry_repository.get():
        repository_path = entry_repository.get()
    else:
        repository_path = 'D:\\medicomtfs2018\\WMark2020\\WMark2020Dev'

    run(entry_temp.get(), entry_dist.get(), repository_path)


button_create = tk.Button(width=10, text="Create", command=create_project)
button_create.place(x=213, y=210)

############################

text_log = tk.Text(master=main_frame, height=6, width=43)
text_log.place(x=30, y=260)

label_creator = tk.Label(
    master=main_frame, text="Created by Oleg Zapolskikh", font=('Comic Sans MS', 8))
label_creator.place(x=345, y=380)

image = Image.open("MScorp.PNG")
image = image.resize((85, 85))

test = ImageTk.PhotoImage(image)

label_image = tk.Label(master=main_frame, image=test)
label_image.place(x=390, y=265)

window.mainloop()
