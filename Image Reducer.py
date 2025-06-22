#All The Imports:
import shutil
import time
import os
from tkinter import *
from tkinter import messagebox, ttk
from os import system
import webbrowser
import threading
import re
from tkinter import filedialog
import sys
from PIL import Image
from SAUIGeo import SAU

sauvernr = "1.03.5"
version = "V1.02.1"
sauver = "SAU" + str(sauvernr)
release_date = "21/06/2025"

global l5
global l8

#SAU Import
SAU.check()
var = SAU.start()
default = var[0]
button = var[1]
cred = var[3]
scale = var[4]
title = var[5]
window_ui = var[6]

user_path = os.path.expanduser("~")

def openlink(link):
    link_list = ["https://github.com/Geomedge/Camera-Quality-Reducer", "https://forms.office.com/r/x7Le5d2bbE", "https://discord.gg/QN5HrTAYYs"]
    webbrowser.open(link_list[link])

def version_info():
    ver_win = Tk()
    ver_win.minsize(250, 100)
    ver_win.title("Version")
    ver_win.config(background="#333")

    l1 = Label(ver_win, text="Version Information", **title)
    l1.pack(side="top", anchor="nw")

    l2 = Label(ver_win, text=f"{version}", **cred)
    l2.pack(side="top")

    l3 = Label(ver_win, text=f"{sauver}", **cred)
    l3.pack(side="top")

    l4 = Label(ver_win, text=f"Release Date : {release_date}", **cred)
    l4.pack(side="top")

#Image Quality Reducer app
def converter():
    root= Tk()
    root.eval('tk::PlaceWindow . centre')
    root.title("Image Reducer")
    root.configure(background="#333")
    root.minsize(500, 525)

#MENU BAR
     #MENU BAR
    menubar = Menu(root, **window_ui)

    #File Settings
    filemenu = Menu(menubar, tearoff=0, **cred)
    filemenu.add_command(label="Exit", command=root.quit)

    #Settings
    settingsmenu = Menu(menubar, tearoff=0, **cred)

#Theme Menu
    thememenu = Menu(settingsmenu, tearoff=0, **cred)
    thememenu.add_command(label="Light", command=lambda:[SAU.set(0)])
    thememenu.add_command(label="Dark", command=lambda:[SAU.set(1)])
    thememenu.add_command(label="Mellow", command=lambda:[SAU.set(2)])
    thememenu.add_command(label="Hacker", command=lambda:[SAU.set(3)])

    #Theme Settings
    settingsmenu.add_cascade(label="Choose Theme (Experimental)", menu=thememenu)

    #Help Menu
    helpmenu = Menu(menubar, tearoff=0, **cred)
    helpmenu.add_command(label="Open Discord Support Page", command=lambda:[openlink(2)])
    helpmenu.add_command(label="Open Github Page", command=lambda:[openlink(0)])
    helpmenu.add_separator()
    helpmenu.add_command(label="Report Bugs", command=lambda:[openlink(1)])
    helpmenu.add_separator()
    helpmenu.add_command(label="Version", command=lambda:[version_info()])
    
    #Menubar Itself
    menubar.add_cascade(label="File", menu=filemenu)
    menubar.add_cascade(label="Settings", menu=settingsmenu)
    menubar.add_cascade(label="Help", menu=helpmenu)
    

    root.config(menu=menubar)




    l1 = Label(root, text='Image Quality Reducer', **title)
    l1.pack(side="top", anchor="nw", pady=1, padx=2)


#Load Files
    def b():
            global file_path
            pathload = user_path + "/pictures"
            file_path = filedialog.askdirectory(mustexist=True, initialdir=pathload)
            textl = "Selected Directory : " + file_path
            l5.config(text=textl)

    f1 = Frame(root, bg="#111")
    l2 = Label(f1, text='Select File:', **default)
    l2.pack(side="top", anchor="nw")
        
    button3 = Button(f1, text='Select Folder', command=b, **button)
    button3.pack(padx=175, pady=15)

    l5 = Label(f1, text="No Path Selected", **default)
    l5.pack(side="bottom")

    f1.pack(pady=10)
    

#SAVE Files
    f2 = Frame(root, bg="#111")

    l7 = Label(f2, text='Save File:', **default)
    l7.pack(side="top", anchor="nw")

    def c():
        global save_path
        pathload = user_path + "/pictures"
        save_path = filedialog.askdirectory(mustexist=True, initialdir=pathload)
        textl = "Selected Directory : " + save_path
        l8.config(text=textl)
        
    button4 = Button(f2, text='Select Folder', command=c, **button)
    button4.pack(padx=175, pady=15)

    l8 = Label(f2, text="No Path Selected", **default)
    l8.pack()

    f2.pack(pady=10)

#Select Horizontal Resolution
    f3 = Frame(root, bg="#111")
    l3 = Label(f3, text='Horizontal Resolution:', **default)
    l3.pack(side="top", anchor="nw")

    e1 = Entry(f3, **button) 
    e1.pack(pady=10)

    

    def convert(found_files, file):
        x1 = e1.get()
        for i in range(len(found_files)):
            base_width = int(x1)
            img = Image.open(found_files[i])
            wpercent = (base_width / float(img.size[0]))
            hsize = int((float(img.size[1]) * float(wpercent)))
            img = img.resize((base_width, hsize), Image.Resampling.LANCZOS)
            path = save_path + "/" + file[i]
            img.save(path)
            print(f"{path} Saved!")
            a = (i + 1)
            progress = a / int(len(found_files))
            progress = progress * 100
            progress2.set(float(progress))
            progress = round(progress, 1)
            progresstext = f"Current Progress : {str(progress)}%"
            progresslabel.config(text=progresstext)
            if progress == 100:
                messagebox.showinfo("Done!", "Finished Downloading!")

    def check():
        found_files = []
        directory = []
        for root, dirs, files in os.walk(file_path):
            for file in files:
                extensions = [".png",".jpeg",".jpg",".bmp"]
                for i in range(len(extensions)):
                    ext = extensions[i]
                    if file.endswith(ext):
                        found_files.append(os.path.join(root, file))
                        directory.append(file)
        convert(found_files, directory)
       
        


    def test_fields():
        try:
            x1 = int(e1.get())
            x1 = x1 + 1
            existing = os.path.exists(file_path)
            existing1 = os.path.exists(save_path)
            if existing == True and existing1 == True and x1 != None:
                check()
            else:
                messagebox.showerror("Error - Invalid Directory", "Error Code 5 - Can't load the directory!")
        except:
            messagebox.showerror("Error - Invalid Resolution", "Error Code 6 - Can't load the resolution!")
    
    button1 = Button(f3, text='Reduce Quality!', command=threading.Thread(target = test_fields).start, **button)
    button1.pack(padx=165, pady=10)

    f3.pack(pady=10)




    progress2 = IntVar()
    progressbar = ttk.Progressbar(root, variable=progress2)
    progressbar.pack(side="bottom", fill="x")

    progresslabel = Label(root, text='Current Progress : 0.0%', **default)
    progresslabel.config(bg="#333")
    progresslabel.pack(side="left", anchor="sw")

    l2 = Label(root, text='Made By Geomedge', **cred)
    l2.pack(anchor="se", side="bottom")


    root.mainloop()

converter()