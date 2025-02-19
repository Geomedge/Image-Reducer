#All The Imports:
import time
import os
import tkinter as tk
from tkinter import messagebox, ttk
from os import system
import webbrowser
import threading
import re
#Menu GUI

text = """V2.22:
-> Added Validation To All Customisations!

-> Formatted the program

-> Resets Files If Corruption Occurs

-> Optimisations!

-> Finally Made Font Changes Work Better!

-> Fonts Still Need A Bit Of Fixing But Way Better Than Before!

V2.21:
-> New Colour System

-> GUI overhaul

-> Better Change log

-> Invalid Colours Caught - Stops Program From Crashing

-> Text Repeater - Fixed Issues With Integers

-> Added Message boxes

-> Fixed a ton of bugs

-> Added Threading - Program No Longer Crashes When Repeating Text.

Thank You For Supporting My Program!
"""


#Saves Me The hassle of changing the version number each time separately!
Version = "V2.22"
last_update = 'Last Updated : 02/09/2024'
#Empty Variables
path_list = []
#This just checks if files exists and if not - recreates them
path_start = os.path.expanduser("~")
path_mid = r"\Documents\Geomedge.inc\Text Repeater"
existing1 = path_start + r"\Documents\Geomedge.inc"
existing = os.path.exists(existing1)
if existing == True:
    print("Pass Geomedge.Inc Folder")
else:
    os.mkdir(existing1)

#This if statement is different!
file = path_start + path_mid
existing = os.path.exists(file)
if existing == True:
    print("Pass", file)
else:
    os.mkdir(file)
path_end = [r"\Theme.txt",r"\Changelog.txt",r"\Font.txt",r"\FontSize.txt",r"\FontEdit.txt"]
for i in range (len(path_end)):
    path = path_start + path_mid + path_end[i]
    path_list.append(path)

#New User Data Generation:
def reset_file(i):
    print("Rebuilding", path_list[i])
    myfile=open(path_list[i], "w")
    match i:
        case 0:
            myfile.write("pink,black,brown,white")
        case 1:
            myfile.write(text)
        case 2:
            myfile.write("none,none,helvetica,helvetica")
        case 3:
            myfile.write("18,12,9,9")
        case 4:
            myfile.write("bold,bold,bold,none")
        case _:
            master = tk.Tk()
            master.withdraw()
            messagebox.showerror("Error - Can't Launch Program", "Error Code 1 - Can't load file!")
            master.destroy()
            quit()
    myfile.close()

#Reading Data For Global Variables
##Verify Files Exist
for i in range(len(path_end)):
    existing = os.path.exists(path_list[i])
    if existing == True:
        print("Pass", path_list[i])
    else:
        print("Fail", path_list[i])
        reset_file(i)
#Ended Checks!

#This just splits the strings - Themes, fonts, font styles etc etc
def Convert(string):
            li = list(string.split(","))
            return li


#Reading + Assigning all the themes accordingly!
def changes():
##Start Reading
    global theme1
    global theme2
    global theme3
    global theme4
    global Title
    global Subtext
    global Button_Txt
    global Credits_Txt
    global changes2
    for i in range(len(path_end)):
        myfile = open(path_list[i], "r")
        a = myfile.read()
        myfile.close()

        match i:
            case 0: #Themes
                theme = Convert(a)
                theme1 = theme[0]
                theme2 = theme[1]
                theme3 = theme[2]
                theme4 = theme[3]
            case 1: #Unused! - This is used for a different program
                changes2 = a
            case 2: #Font
                font1 = Convert(a)
                font11 = font1[0]
                font12 = font1[1]
                font13 = font1[2]
                font14 = font1[3]
            case 3: #Size
                font2 = Convert(a)
                font21 = font2[0]
                font22 = font2[1]
                font23 = font2[2]
                font24 = font2[3]
            case 4: #Extras
                font3 = Convert(a)
                font31 = font3[0]
                font32 = font3[1]
                font33 = font3[2]
                font34 = font3[3]

    Titl = font11 + " " + font21
    Subte = font12 + " " + font22
    Butto = font13 + " " + font23
    Credi = font14 + " " + font24

    #Title
    if font31 == "none":
        Title = Titl
    else:
        Title = Titl + " " + font31
    #SubText
    if font32 == "none":
        Subtext = Subte
    else:
        Subtext = Subte + " " + font32
    #Button Text
    if font33 == "none":
        Button_Txt = Butto
    else:
        Button_Txt = Butto + " " + font33
    #Credits Text
    if font34 == "none":
        Credits_Txt = Credi
    else:
        Credits_Txt = Credi + " " + font34

#Calls the function to assign starter theme
changes()

#Skip to the bottom!

#Pre Set Themes!
def message_1(theme):
    string = "Your theme was changed to " + theme + "."
    print("Users Theme Changed To : ", string)
    changes()

#light mode
def light():
    myfile=open(path_list[0], "w")
    myfile.write("pink,black,brown,white")
    myfile.close()
    message_1("Light Theme")

#dark mode
def dark():
    myfile=open(path_list[0], "w")
    myfile.write("#23272a,#7289da,#99aab5,#36393f")
    myfile.close()
    message_1("Dark Theme")

#Hacker mode
def hacker():
    myfile=open(path_list[0], "w")
    myfile.write("#000000,#20C20E,#000000,#20C20E")
    myfile.close()
    message_1("Hacker Theme")

#Mellow
def mellow():
    myfile=open(path_list[0], "w")
    myfile.write("#fceea7,#000000,#fceea7,#000000")
    myfile.close()
    message_1("Mellow Theme")

def exit_app():
    quit()

#Uninstall
def delete():
    for i in range(len[path_list]):
        os.remove(path_list[i])
    os.remove(os.getcwd())
    print("done")


#Confirmation For Uninstalling
def confirm():
    message1 = "Are you sure you want to delete Text Repeater " + Version + "?"
    command = messagebox.askquestion(title="Are you sure?", message=message1)
    if command == "yes":
        delete()
    elif command == "no":
        settings()


def bug_report():
    confirm = tk.Tk()
    confirm.eval('tk::PlaceWindow . centre')
    confirm.title("Bug Fix")
    canvas1 = tk.Canvas(confirm, width=500, height=200, relief='raised', bg = theme1)
    canvas1.pack()

    def callback(url):
        webbrowser.open_new(url)

    title5 = tk.Label(confirm, text="Discord Server", fg="blue", cursor="hand2")
    canvas1.create_window(350, 75, window=title5)
    title6 = tk.Label(confirm, text="Bug Report Form", fg="blue", cursor="hand2")
    canvas1.create_window(150, 75, window=title6)
    canvas1.pack()
    title5.bind("<Button-1>", lambda e: callback("https://discord.gg/QN5HrTAYYs"))
    title6.bind("<Button-1>", lambda e: callback("https://forms.office.com/r/x7Le5d2bbE"))
    
    title = tk.Label(confirm, text='Report Bugs', bg = theme1, fg = theme2)
    title.config(font=(Title))
    canvas1.create_window(250, 25, window=title)

    title1 = tk.Label(confirm, text='Select any link below to get started.', bg = theme1, fg = theme2)
    title1.config(font=('none 9 bold'))
    canvas1.create_window(250, 50, window=title1)

    button7 = tk.Button(confirm, text='Back', command=lambda:[confirm.destroy(), menu()], bg=theme3, fg=theme4, font=(Button_Txt), width=10, height=1)
    canvas1.create_window(50, 175, window=button7)


def changelog():
    changelog = tk.Tk()
    changelog.eval('tk::PlaceWindow . centre')
    changelog.title("Changelog")
    canvas1 = tk.Canvas(changelog, width=500, height=400, relief='raised', bg = theme1)
    canvas1.pack()

    title = tk.Label(changelog, text='Changelog', bg = theme1, fg = theme2, font=('none 18 bold'))
    canvas1.create_window(250, 25, window=title)



    text_widget = tk.Text(changelog, wrap='word', height=20, width=80,bg = theme1, fg = theme2, font =('segoe UI', 9), borderwidth=0)
    canvas1.create_window(250,200, window = text_widget)
    sample_text = changes2
    text_widget.insert(tk.END, sample_text)
    text_widget.config(state=tk.DISABLED)

    scrollbar = ttk.Scrollbar(orient=tk.VERTICAL, command=text_widget.yview)
    text_widget.config(yscrollcommand=scrollbar.set)
    canvas1.create_window(430, 200, window=scrollbar, height=300)

    l2 = tk.Label(changelog, text=last_update, bg = theme1, fg = theme2)
    canvas1.create_window(430, 385, window=l2)
    
    button7 = tk.Button(changelog, text='Back', command=lambda:[changelog.destroy(), menu()], bg=theme3, fg=theme4, font=(Button_Txt), width=10, height=1)
    canvas1.create_window(50, 385, window=button7)


#Customisation

def font_set3():
    confirm = tk.Tk()
    confirm.eval('tk::PlaceWindow . centre')
    confirm.title("Font Settings")
    canvas1 = tk.Canvas(confirm, width=500, height=300, relief='raised', bg = theme1)
    canvas1.pack()

    title = tk.Label(confirm, text='Change Font Extras (Itallics, Bold, etc)', bg = theme1, fg = theme2)
    title.config(font=('none 12 bold'))
    canvas1.create_window(250, 25, window=title)

    title1 = tk.Label(confirm, text='Input Title Extras', bg = theme1, fg = theme2)
    title1.config(font=('none 9 bold'))
    canvas1.create_window(250, 50, window=title1)

    entry5 = tk.Entry(confirm, font=Subtext)
    canvas1.create_window(250, 75, window=entry5)

    title2 = tk.Label(confirm, text='Input Text Extras', bg = theme1, fg = theme2)
    title2.config(font=('none 9 bold'))
    canvas1.create_window(250, 100, window=title2)

    entry6 = tk.Entry(confirm, font=Subtext)
    canvas1.create_window(250, 125, window=entry6)

    title3 = tk.Label(confirm, text='Input Button Extras', bg = theme1, fg = theme2)
    title3.config(font=('none 9 bold'))
    canvas1.create_window(250, 150, window=title3)

    entry7 = tk.Entry(confirm, font=Subtext)
    canvas1.create_window(250, 175, window=entry7)

    title4 = tk.Label(confirm, text='Input Every Other Font Extras', bg = theme1, fg = theme2)
    title4.config(font=('none 9 bold'))
    canvas1.create_window(250, 200, window=title4)

    entry8 = tk.Entry(confirm, font=Subtext)
    canvas1.create_window(250, 225, window=entry8)
    

    def get2(var1, var2, var3, var4):
        new = [var1,var2,var3,var4]
        print(new)
        new_list = []
        for i in range(len(new)):
            print(new[i])
            x = new[i].get().lower()
            if x == "none" or x == "bold" or x == "italics":
                new_list.append(x)
            else:  
                print("Invalid Choice")
                string = f"Invalid Choice : {x}, Is not a valid option!"
                messagebox.showerror("Error!", string)
                return False
                
        return new_list




    def theme_switch4():
        new_list = get2(entry5,entry6,entry7,entry8)
        if new_list == False:
            print("Failed!")
            messagebox.showinfo("Didn't Make Changes!", "Font Edit Failed!")
        else:
            myfile=open(path_list[4], "w")
            string = ",".join(new_list) + ","
            myfile.write(string)
            myfile.close()
            messagebox.showinfo("Done!", "Changes To Font Made!")
        

    button1 = tk.Button(confirm, text='Change!', command=lambda:[theme_switch4(), confirm.destroy(), font_set3()], bg=theme3, fg=theme4, font=(Button_Txt), width=10, height=1)
    canvas1.create_window(250, 260, window=button1)

    button7 = tk.Button(confirm, text='Back', command=lambda:[settings(), confirm.destroy()], bg=theme3, fg=theme4, font=(Button_Txt), width=10, height=1)
    canvas1.create_window(50, 275, window=button7)

def font_set2():
    confirm = tk.Tk()
    confirm.eval('tk::PlaceWindow . centre')
    confirm.title("Font Settings")
    canvas1 = tk.Canvas(confirm, width=500, height=300, relief='raised', bg = theme1)
    canvas1.pack()

    title = tk.Label(confirm, text='Change Font Size', bg = theme1, fg = theme2)
    title.config(font=('none 12 bold'))
    canvas1.create_window(250, 25, window=title)

    title1 = tk.Label(confirm, text='Input Title Size', bg = theme1, fg = theme2)
    title1.config(font=('none 9 bold'))
    canvas1.create_window(250, 50, window=title1)

    entry5 = tk.Entry(confirm, font=Subtext)
    canvas1.create_window(250, 75, window=entry5)

    title2 = tk.Label(confirm, text='Input Text Size', bg = theme1, fg = theme2)
    title2.config(font=('none 9 bold'))
    canvas1.create_window(250, 100, window=title2)

    entry6 = tk.Entry(confirm, font=Subtext)
    canvas1.create_window(250, 125, window=entry6)

    title3 = tk.Label(confirm, text='Input Button Size', bg = theme1, fg = theme2)
    title3.config(font=('none 9 bold'))
    canvas1.create_window(250, 150, window=title3)

    entry7 = tk.Entry(confirm, font=Subtext)
    canvas1.create_window(250, 175, window=entry7)

    title4 = tk.Label(confirm, text='Input Every Other Font Size', bg = theme1, fg = theme2)
    title4.config(font=('none 9 bold'))
    canvas1.create_window(250, 200, window=title4)

    entry8 = tk.Entry(confirm, font=Subtext)
    canvas1.create_window(250, 225, window=entry8)
    
    def theme_switch3():
        x5 = entry5.get().lower()
        x6 = entry6.get().lower()
        x7 = entry7.get().lower()
        x8 = entry8.get().lower()
        try:
            x = int(x5)
            x = int(x6)
            x = int(x7)
            x = int(x8)
            myfile=open(path_list[3], "w")
            string = x5 + "," + x6 + "," + x7 + "," + x8 + ","
            myfile.write(string)
            myfile.close()
            print("Done!")
            confirm.destroy()
            font_set3()
        except:
            messagebox.showerror("Error", "Invalid Characters - Number Input!")

        

    button1 = tk.Button(confirm, text='Change!', command=lambda:[theme_switch3()], bg=theme3, fg=theme4, font=(Button_Txt), width=10, height=1)
    canvas1.create_window(250, 260, window=button1)

    button7 = tk.Button(confirm, text='Back', command=lambda:[settings(), confirm.destroy()], bg=theme3, fg=theme4, font=(Button_Txt), width=10, height=1)
    canvas1.create_window(50, 275, window=button7)

def change_font():
    confirm = tk.Tk()
    confirm.eval('tk::PlaceWindow . centre')
    confirm.title("Font Settings")
    canvas1 = tk.Canvas(confirm, width=500, height=300, relief='raised', bg = theme1)
    canvas1.pack()

    title = tk.Label(confirm, text='Change Fonts (Write None If Default Font)', bg = theme1, fg = theme2)
    title.config(font=('none 12 bold'))
    canvas1.create_window(250, 25, window=title)

    title1 = tk.Label(confirm, text='Input Title Font (Example : Helvetica)', bg = theme1, fg = theme2)
    title1.config(font=('none 9 bold'))
    canvas1.create_window(250, 50, window=title1)

    entry5 = tk.Entry(confirm, font=Subtext)
    canvas1.create_window(250, 75, window=entry5)

    title2 = tk.Label(confirm, text='Input Text Font', bg = theme1, fg = theme2)
    title2.config(font=('none 9 bold'))
    canvas1.create_window(250, 100, window=title2)

    entry6 = tk.Entry(confirm, font=Subtext)
    canvas1.create_window(250, 125, window=entry6)

    title3 = tk.Label(confirm, text='Input Button Font', bg = theme1, fg = theme2)
    title3.config(font=('none 9 bold'))
    canvas1.create_window(250, 150, window=title3)

    entry7 = tk.Entry(confirm, font=Subtext)
    canvas1.create_window(250, 175, window=entry7)

    title4 = tk.Label(confirm, text='Input Every Other Font', bg = theme1, fg = theme2)
    title4.config(font=('none 9 bold'))
    canvas1.create_window(250, 200, window=title4)

    entry8 = tk.Entry(confirm, font=Subtext)
    canvas1.create_window(250, 225, window=entry8)
    
    def test(x9,x10,x11,x12):
            try:
                test_fonts = [x9,x10,x11,x12]
                print(test_fonts)
                confirm = tk.Tk()
                confirm.title("Test")
                canvas1 = tk.Canvas(confirm, width=500, height=300, relief='raised', bg = theme1)
                canvas1.pack()

                title = tk.Label(confirm, text='test')
                for i in range(4):
                    font_test = test_fonts[i] + " 12 bold"
                    print(test_fonts[i])
                    title.config(font=(font_test))
                    canvas1.create_window(250, 25, window=title)
                confirm.withdraw()
                return True
            except:
                confirm.withdraw()
                messagebox.showerror("INVALID FONT!", "Invalid font selected!")
                return False

    def theme_switch2():
        x9 = entry5.get().lower()
        x10 = entry6.get().lower()
        x11 = entry7.get().lower()
        x12 = entry8.get().lower()
        if test(x9,x10,x11,x12) == True:
            myfile=open(path_list[2], "w")
            string = x9 + "," + x10 + "," + x11 + "," + x12 + ","
            myfile.write(string)
            myfile.close()
            messagebox.showinfo(title="Done!", message="Successfully Changed Font!")
            print("Done!")
            font_set2()
        else:
            change_font()
        

    button1 = tk.Button(confirm, text='Change!', command=lambda:[theme_switch2(), confirm.destroy()], bg=theme3, fg=theme4, font=(Button_Txt), width=10, height=1)
    canvas1.create_window(250, 260, window=button1)

    button7 = tk.Button(confirm, text='Back', command=lambda:[settings(), confirm.destroy()], bg=theme3, fg=theme4, font=(Button_Txt), width=10, height=1)
    canvas1.create_window(50, 275, window=button7)


def basic_colour_settings():
    confirm = tk.Tk()
    confirm.eval('tk::PlaceWindow . centre')
    confirm.title("Colour Settings")
    canvas1 = tk.Canvas(confirm, width=500, height=300, relief='raised', bg = theme1)
    canvas1.pack()

    title = tk.Label(confirm, text='Colour Settings', bg = theme1, fg = theme2)
    title.config(font=('none 18 bold'))
    canvas1.create_window(250, 25, window=title)

    title1 = tk.Label(confirm, text='Background colour', bg = theme1, fg = theme2)
    title1.config(font=('none 9 bold'))
    canvas1.create_window(125, 50, window=title1)

    selected_option1 = tk.StringVar()
    selected_option2 = tk.StringVar()
    selected_option3 = tk.StringVar()
    selected_option4 = tk.StringVar()
    options = ["Black","White","Red","Orange","Pink","Blue","Magenta","Yellow","Cyan","Green"]
    menu_len = len(max(options, key=len)) + 1
    entry5 = tk.OptionMenu(confirm, selected_option1, *options)
    entry5.config(width = menu_len)
    canvas1.create_window(125, 75, window=entry5)

    title2 = tk.Label(confirm, text='Colour of the text', bg = theme1, fg = theme2)
    title2.config(font=('none 9 bold'))
    canvas1.create_window(375, 50, window=title2)

    entry6 = tk.OptionMenu(confirm, selected_option2, *options)
    entry6.config(width = menu_len)
    canvas1.create_window(375, 75, window=entry6)

#    title3 = tk.Label(confirm, text='Background of buttons', bg = theme1, fg = theme2)
#    title3.config(font=('none 9 bold'))
#    canvas1.create_window(375, 125, window=title3)

#    entry7 = tk.OptionMenu(confirm, selected_option3, *options)
#    entry7.config(width=25)
#    canvas1.create_window(375, 150, window=entry7)

#    title4 = tk.Label(confirm, text='Text Colour of buttons', bg = theme1, fg = theme2)
#    title4.config(font=('none 9 bold'))
#    canvas1.create_window(250, 210, window=title4)

#    entry8 = tk.OptionMenu(confirm, selected_option4, *options)
#    canvas1.create_window(250, 240, window=entry8)




    def theme_switch():
        x13 = selected_option1.get().lower()
        x14 = selected_option2.get().lower()
        x15 = selected_option3.get().lower()
        x16 = selected_option4.get().lower()
        if x13 == "" or x14 == "" or x15 == "" or x16 == "":
            messagebox.showerror("Can't apply changes!", "Please Ensure All Boxes Have Been Selected!")
        else:
            myfile=open(path_list[0], "w")
            string = x13 + "," + x14 + "," + x15 + "," + x16 + ","
            myfile.write(string)
            myfile.close()
            print("Done!")
            changes()
            messagebox.showinfo("Done!", "Changes Applied")
            quit
        

    button1 = tk.Button(confirm, text='Change!', command=lambda:[theme_switch(), confirm.destroy(), basic_colour_settings()], bg=theme3, fg=theme4, font=(Button_Txt), width=10, height=1)
    canvas1.create_window(250, 265, window=button1)

    button7 = tk.Button(confirm, text='Back', command=lambda:[colour_settings_menu(), confirm.destroy()], bg=theme3, fg=theme4, font=(Button_Txt), width=10, height=1)
    canvas1.create_window(50, 275, window=button7)

def colour_settings():
    confirm = tk.Tk()
    confirm.eval('tk::PlaceWindow . centre')
    confirm.title("Colour Settings")
    canvas1 = tk.Canvas(confirm, width=500, height=300, relief='raised', bg = theme1)
    canvas1.pack()

    title = tk.Label(confirm, text='Enter Desired Colours!', bg = theme1, fg = theme2)
    title.config(font=('none 10 bold'))
    canvas1.create_window(250, 25, window=title)

    title1 = tk.Label(confirm, text='Input Theme 1 (Background of window)', bg = theme1, fg = theme2)
    title1.config(font=('none 9 bold'))
    canvas1.create_window(250, 50, window=title1)

    entry5 = tk.Entry(confirm, font=Subtext, width=25)
    canvas1.create_window(250, 75, window=entry5)

    title2 = tk.Label(confirm, text='Input Theme 2 (Text Colour of window)', bg = theme1, fg = theme2)
    title2.config(font=('none 9 bold'))
    canvas1.create_window(250, 100, window=title2)

    entry6 = tk.Entry(confirm, font=Subtext, width=25)
    canvas1.create_window(250, 125, window=entry6)

    title3 = tk.Label(confirm, text='Input Theme 3 (Background of buttons)', bg = theme1, fg = theme2)
    title3.config(font=('none 9 bold'))
    canvas1.create_window(250, 150, window=title3)

    entry7 = tk.Entry(confirm, font=Subtext, width=25)
    canvas1.create_window(250, 175, window=entry7)

    title4 = tk.Label(confirm, text='Input Theme 4 (Text Colour of buttons)', bg = theme1, fg = theme2)
    title4.config(font=('none 9 bold'))
    canvas1.create_window(250, 200, window=title4)

    entry8 = tk.Entry(confirm, font=Subtext, width=25)
    canvas1.create_window(250, 225, window=entry8)

    def Colour_Check(test):
        rex = re.compile("^#{1}[0-9]{6}$")
        if rex.match(test):
            return True
        else:
            colour_list = ["black","white","red","orange","pink","blue","magenta","yellow","cyan","green"]
            for i in range(len(colour_list)):
                if colour_list[i] == test:
                    return True
        return False



    def theme_switch():
        #Gets All The Entry Boxes
        x13 = entry5.get().lower()
        x14 = entry6.get().lower()
        x15 = entry7.get().lower()
        x16 = entry8.get().lower()
        #Colour_Check checks for any invalid colours!
        if Colour_Check(x13) == False or Colour_Check(x14) == False or Colour_Check(x15) == False or Colour_Check(x16) == False:
            messagebox.showerror("INVALID COLOUR!", "Invalid colour selected!") 
        else:
            myfile=open(path_list[0], "w")
            string = x13 + "," + x14 + "," + x15 + "," + x16 + ","
            myfile.write(string)
            myfile.close()
            print("Done!")
            changes()
            messagebox.showinfo("Done!", "Changes Made!")

        

    button1 = tk.Button(confirm, text='Change!', command=lambda:[theme_switch(), confirm.destroy(), colour_settings()], bg=theme3, fg=theme4, font=(Button_Txt), width=10, height=1)
    canvas1.create_window(250, 260, window=button1)

    button7 = tk.Button(confirm, text='Back', command=lambda:[colour_settings_menu(), confirm.destroy()], bg=theme3, fg=theme4, font=(Button_Txt), width=10, height=1)
    canvas1.create_window(50, 275, window=button7)

def colour_settings_menu():
    colour = tk.Tk()
    colour.eval('tk::PlaceWindow . centre')
    colour.title("Settings")
    colour.configure(bg = theme1)
    canvas1 = tk.Canvas(colour, width=400, height=105, relief='raised', bg = theme1, bd=0, highlightthickness=0)
    canvas1.pack()

    title = tk.Label(colour, text='Settings', bg = theme1, fg = theme2)
    title.config(font=(Title))
    canvas1.create_window(200, 25, window=title)
    
    label1 = tk.Label(colour, text='Made By Geomedge', bg = theme1, fg = theme2)
    label1.config(font=(Credits_Txt))
    canvas1.create_window(340, 125, window=label1)

    button1 = tk.Button(colour, text='Preset Colour Settings', command=lambda:[basic_colour_settings(), colour.destroy()], bg=theme3, fg= theme4, font=(Button_Txt), width=25, height=1)
    canvas1.create_window(100, 60, window=button1)

    button2 = tk.Button(colour, text='Advanced Colour Settings', command=lambda:[colour_settings(), colour.destroy()], bg=theme3, fg=theme4, font=(Button_Txt), width=25, height=1)
    canvas1.create_window(300, 60, window=button2)

    button7 = tk.Button(colour, text='Back', command=lambda:[colour.destroy(), settings()], bg=theme3, fg=theme4, font=(Button_Txt), width=10, height=1)
    canvas1.create_window(48, 90, window=button7)


#Themes
def theme():
    theme_app = tk.Tk()
    theme_app.title("Theme")
    theme_app.eval('tk::PlaceWindow . centre')
    canvas1 = tk.Canvas(theme_app, width=400, height=140, relief='raised', bg = theme1)
    canvas1.pack()

    title = tk.Label(theme_app, text='Select Your Theme', bg = theme1, fg = theme2)
    title.config(font=(Title))
    canvas1.create_window(200, 25, window=title)

    button1 = tk.Button(theme_app, text='Light Theme', command=lambda:[light(), theme_app.destroy(), theme()], bg=theme3, fg=theme4, font=(Button_Txt), width=25, height=1)
    canvas1.create_window(100, 60, window=button1)

    button2 = tk.Button(theme_app, text='Dark Theme', command=lambda:[dark(), theme_app.destroy(), theme()], bg=theme3, fg=theme4, font=(Button_Txt), width=25, height=1)
    canvas1.create_window(300, 60, window=button2)

    button3 = tk.Button(theme_app, text='Hacker Theme', command=lambda:[hacker(), theme_app.destroy(), theme()], bg=theme3, fg=theme4, font=(Button_Txt), width=25, height=1)
    canvas1.create_window(100, 90, window=button3)

    button4 = tk.Button(theme_app, text='Mellow Theme', command=lambda:[mellow(), theme_app.destroy(), theme()], bg=theme3, fg=theme4, font=(Button_Txt), width=25, height=1)
    canvas1.create_window(300, 90, window=button4)
    
    button7 = tk.Button(theme_app, text='Back', command=lambda:[settings(), theme_app.destroy()], bg=theme3, fg=theme4, font=(Button_Txt), width=10, height=1)
    canvas1.create_window(48, 120, window=button7)


#text repeater app
def text_rep():
    root= tk.Tk()
    root.eval('tk::PlaceWindow . centre')
    root.title("Repeater App")
    
    canvas1 = tk.Canvas(root, width=400, height=275, relief='raised', bg = theme1)
    canvas1.pack()

    label1 = tk.Label(root, text='Text Repeater', bg = theme1, fg = theme2)
    label1.config(font=('none 18 bold'))
    canvas1.create_window(200, 25, window=label1)

    label2 = tk.Label(root, text='Type your Message:', font="none 12 bold", bg = theme1, fg = theme2)
    canvas1.create_window(200, 70, window=label2)

    entry1 = tk.Entry(root, font="none 12 bold") 
    canvas1.create_window(200, 100, window=entry1)

    label3 = tk.Label(root, text='How many times should it be repeated?', font="none 12 bold", bg = theme1, fg = theme2)
    canvas1.create_window(200, 130, window=label3)

    entry2 = tk.Entry(root, font="none 12 bold")
    canvas1.create_window(200, 160, window=entry2)
    
    def a():
        try:
            x1 = entry1.get()
            try:
                x2 = int(entry2.get())
                myfile = open(r'C:\Users\Public\Videos\Repeated text.txt', "a")
                for i in range(x2):
                    myfile.write(x1)
                    myfile.write("\n")
                myfile.close
                messagebox.showinfo("Done!", "Task Completed Successfully!")
            except:
                messagebox.showerror("Error", "Invalid Number Selected / No Number Found!")
        except:
            messagebox.showerror("Error!", "Invalid Text!")
            
    def thread_1():
        t1 = threading.Thread(target = a)
        t1.start()
    
    button1 = tk.Button(root, text='Create File!', command=thread_1, bg = theme3, fg = theme4, font=('helvetica', 9, 'bold'))
    canvas1.create_window(200, 220, window=button1)

    button7 = tk.Button(root, text='Back', command=lambda:[root.destroy(), menu()], bg=theme3, fg=theme4, font=('helvetica', 9, 'bold'), width=10, height=1)
    canvas1.create_window(50, 250, window=button7)

    label2 = tk.Label(root, text='Made By Geomedge', bg = theme1, fg = theme2)
    label2.config(font=('helvetica', 9))
    canvas1.create_window(340, 265, window=label2)


#settings
def settings():
    setting = tk.Tk()
    setting.eval('tk::PlaceWindow . centre')
    setting.title("Settings")
    setting.configure(bg = theme1)
    canvas1 = tk.Canvas(setting, width=400, height=135, relief='raised', bg = theme1, bd=0, highlightthickness=0)
    canvas1.pack()

    title = tk.Label(setting, text='Settings', bg = theme1, fg = theme2)
    title.config(font=(Title))
    canvas1.create_window(200, 25, window=title)
    
    label1 = tk.Label(setting, text='Made By Geomedge', bg = theme1, fg = theme2)
    label1.config(font=(Credits_Txt))
    canvas1.create_window(340, 125, window=label1)

    button1 = tk.Button(setting, text='Change Fonts', command=lambda:[change_font(), setting.destroy()], bg=theme3, fg= theme4, font=(Button_Txt), width=25, height=1)
    canvas1.create_window(100, 60, window=button1)

    button2 = tk.Button(setting, text='Change Theme', command=lambda:[theme(), setting.destroy()], bg=theme3, fg=theme4, font=(Button_Txt), width=25, height=1)
    canvas1.create_window(100, 90, window=button2)

    button5 = tk.Button(setting, text='Uninstall Python Scripts', command=lambda:[confirm(), setting.destroy()], bg=theme3, fg=theme4, font=(Button_Txt), width=25, height=1)
    canvas1.create_window(300, 60, window=button5)

    button3 = tk.Button(setting, text='Colour settings', command=lambda:[colour_settings_menu(), setting.destroy()], bg=theme3, fg=theme4, font=(Button_Txt), width=25, height=1)
    canvas1.create_window(300, 90, window=button3)

    button7 = tk.Button(setting, text='Back', command=lambda:[setting.destroy(), menu()], bg=theme3, fg=theme4, font=(Button_Txt), width=10, height=1)
    canvas1.create_window(48, 120, window=button7)


#Credits
def credit():
    credit = tk.Tk()
    credit.eval('tk::PlaceWindow . centre')
    credit.eval('tk::PlaceWindow . centre')
    credit.configure(bg = theme1)
    credit.title("Credits")
    canvas2 = tk.Canvas(credit, width=300, height=100, relief='raised', bg = theme1, bd=0, highlightthickness=0)
    canvas2.pack()

    label1 = tk.Label(credit, text='Made By Geomedge', bg = theme1, fg = theme2)
    label1.config(font=('helvetica', 12, 'bold'))
    canvas2.create_window(150, 25, window=label1)

    label1 = tk.Label(credit, text='Thank you for using the app!', bg = theme1, fg = theme2)
    label1.config(font=('helvetica', 12, 'bold'))
    canvas2.create_window(150, 50, window=label1)
    
    button2 = tk.Button(credit, text='Back', command=lambda:[credit.destroy(), menu()], bg=theme3, fg=theme4, font=(Button_Txt), width=10, height=1)
    canvas2.create_window(50, 85, window=button2)

#Menu
def menu():
    #Basic Menu!
    menu = tk.Tk()
    menu.eval('tk::PlaceWindow . centre')
    menu.configure(bg = theme1)
    menu.title("Text Repeater")
    canvas1 = tk.Canvas(menu, width=400, height=160, relief='raised', bg = theme1, bd=0, highlightthickness=0)
    canvas1.pack()

    label1 = tk.Label(menu, text='Text Repeater By Geomedge', bg = theme1, fg = theme2)
    label1.config(font=(Title))
    canvas1.create_window(200, 25, window=label1)

    button1 = tk.Button(menu, text='Text Repeater', command=lambda:[menu.destroy(), text_rep()], bg=theme3, fg=theme4, font=(Button_Txt), width=25, height=1)
    canvas1.create_window(100, 60, window=button1)

    button2 = tk.Button(menu, text='Settings', command=lambda:[menu.destroy(), settings()], bg=theme3, fg=theme4, font=(Button_Txt), width=25, height=1)
    canvas1.create_window(100, 90, window=button2)

    button3 = tk.Button(menu, text='Changelog', command=lambda:[menu.destroy(), changelog()], bg=theme3, fg=theme4, font=(Button_Txt), width=25, height=1)
    canvas1.create_window(100, 120, window=button3)
    
    button4 = tk.Button(menu, text='Report Bug', command=lambda:[menu.destroy(), bug_report()], bg=theme3, fg=theme4, font=(Button_Txt), width=25, height=1)
    canvas1.create_window(300, 60, window=button4)
    
    button5 = tk.Button(menu, text='Credits', command=lambda:[menu.destroy(), credit()], bg=theme3, fg=theme4, font=(Button_Txt), width=25, height=1)
    canvas1.create_window(300, 90, window=button5)

    button6 = tk.Button(menu, text='Quit', command=exit_app, bg=theme3, fg=theme4, font=(Button_Txt), width=25, height=1)
    canvas1.create_window(300, 120, window=button6)

    label2 = tk.Label(menu, text='Made By Geomedge', bg = theme1, fg = theme2)
    label2.config(font=(Credits_Txt))
    canvas1.create_window(330, 150, window=label2)

    label3 = tk.Label(menu, text= Version, bg = theme1, fg = theme2)
    label3.config(font=(Credits_Txt))
    canvas1.create_window(20, 150, window=label3)
    menu.mainloop()



#Simple Null / Invalid Values Catcher - Resets all preset values if app cannot load (Bit overkill but I can't think of anything else)
try:
    try:
        menu()
    except:
        menu.withdraw()
        for i in range(5):
            reset_file(i)
        #Calls the reset_file function which restarts all files to original state set by me / any other dev
        changes()
        #Calls this function to update all the theme and font values
        menu()
        #Can Load Menu With Default Settings!
except:
    print("Something went really wrong loading this file.")
    print("Error 2 - Can't Load Menu Even After Resetting Files!")
    print(":(")