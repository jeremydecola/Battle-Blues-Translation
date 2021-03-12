from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import tkinter as tk
import os
project_root = os.path.dirname(os.path.abspath(__file__))
import bbtools

root = Tk()
root.geometry("600x849")
root.iconbitmap(default=project_root+"\\graphics\\grenade.ico")
root.configure(bg = "black")

bg = ImageTk.PhotoImage(Image.open(project_root+"\\graphics\\bb_pinup_ds.jpg"))
my_label = Label(root, image=bg)
my_label.place(x=0,y=0, relwidth=1, relheight=1)

bottomframe = Frame(root, bg = "black")
bottomframe.pack(side=BOTTOM)
topframe = Frame(root, bg = "black")
topframe.pack(side=TOP)
midframe = Frame(root, bg = "yellow")
midframe.place(in_=root, anchor="sw", relx=.5, rely=.5)

title_label = Label(topframe, text="BATTLE BLUES PATCH AND BALANCE TOOL!")
title_label.configure(font=("Monaco", 18, "bold"), bg = "black", fg = "white")
title_label.pack()

progress_label = Label(topframe, text="Current Progress:")
progress_label.configure(font=("Monaco", 14, "bold"), bg = "black", fg = "white")
progress_label.pack()
progress = Label(topframe, text="[Waiting For User Input]")
progress.configure(font=("Monaco", 14, "bold"), bg = "black", foreground = "red")
progress.pack()

def browseForPath():
    progress['text'] = "   Browsing for path...    "
    filePath.delete(0, END) # CLEAR ANY EXISTING TEXT
    thepath = filedialog.askopenfilename(initialdir ="/", title = "Select A File", filetype =
    (("ISO files","*.iso"),("IMG files","*.img")) )
    thepath = os.path.abspath(thepath)
    if ("iso" in thepath) or ("img" in thepath):
        filePath.insert(0, thepath)
        progress['text'] = "Chose a Difficulty and press \"PATCH\""
    else:
        progress['text'] = "Invalid/Missing path."

def enableOnText(*_):
    if filePath.var.get() and (".iso" in filePath.var.get() or ".img" in filePath.var.get()):
        progress['text'] = "Chose a Difficulty and press \"PATCH\""
        patchButton['state'] = 'normal'
    else:
        progress['text'] = "Invalid/Missing path."
        patchButton['state'] = 'disabled'

def execute_patch():
    path = filePath.get()
    bbtools.decompile(path)
    bbtools.patch(path,0)
    bbtools.compile(path)
    bbtools.sign(path)
    progress['text'] = "Patching Complete!"

label_browse = Label(topframe, text="[STEP 1] Browse for your Battle Blues image file:")
label_browse.configure(font=("Monaco", 14, "bold"), bg = "black", fg = "white")
label_browse.pack()
filePath = Entry(root, width = 60)
filePath.pack(padx = 5, pady = 5)
filePath.var = tk.StringVar()
filePath['textvariable'] = filePath.var
filePath.var.trace_add('write', enableOnText)
browseButton = Button(root, text="BROWSE", command = browseForPath,
               height = 1, width = 8, font = ("Monaco", 16, "bold"),
               bg = "black", fg = "white")
browseButton.pack(padx=3, pady=3)

label_patch = Label(bottomframe, text="[STEP 3] Press the Patch Button:")
label_patch.configure(font=("Monaco", 14, "bold"), bg = "black", fg = "white")
label_patch.pack()
label_warning = Label(bottomframe, text="WARNING! DO NOT TOUCH YOUR KEYBOARD WHILE PATCHING.")
label_warning.configure(font=("Monaco", 14, "bold"), bg = "black", fg = "white")
label_warning.pack()
patchButton = Button(bottomframe, text="PATCH", command = execute_patch, state = "disabled",
                     height = 1, width = 8, font = ("Monaco",16,"bold"),
                     bg = "black", fg = "white")
patchButton.pack(padx=3, pady=3)

def sel():
    selection = choice.get()
    if selection == 1:
        print("Difficulty set to Easy.")
        Easy.select()
    elif selection == 2:
        print("Difficulty set to Normal.")
        Normal.select()
    elif selection == 3:
        print("Difficulty set to Hard.")
        Hard.select()
    elif selection == 4:
        print("Difficulty set to Impossible.")
        Impossible.select()

#Difficulty Select
label_ds = Label(midframe, text="[STEP 2] Difficulty Select:")
label_ds.configure(font=("Monaco", 14, "bold"), bg = "black", fg = "white")
label_ds.pack()

choice = IntVar(value = 2)
Easy = Radiobutton(midframe, text="EASY", variable = choice, value = 1,
                         command = sel, justify = "left", bg = "yellow", activebackground = "yellow")
Easy.configure(font=("Monaco", 14, "bold"))
Easy.pack(padx = 5, pady = 5, anchor = W)
Normal = Radiobutton(midframe, text="NORMAL", variable = choice, value = 2,
                         command = sel, justify = "left", bg = "yellow", activebackground = "yellow")
Normal.configure(font=("Monaco", 14, "bold"))
Normal.pack(padx = 5, pady = 5, anchor = W)
Hard = Radiobutton(midframe, text="HARD", variable = choice, value = 3,
                         command = sel, justify = "left", bg = "yellow", activebackground = "yellow")
Hard.configure(font=("Monaco", 14, "bold"))
Hard.pack(padx = 5, pady = 5, anchor = W)
Impossible = Radiobutton(midframe, text="IMPOSSIBLE", variable = choice, value = 4,
                         command = sel, justify = "left", bg = "yellow", activebackground = "yellow")
Impossible.configure(font=("Monaco", 14, "bold"))
Impossible.pack(padx = 5, pady = 5, anchor = W)

root.title("Battle Blues Patch and Balance Tool v0.2")
root.resizable(False,False)
root.mainloop()
