import time
import tkinter
import customtkinter
from PIL import Image
import random
import json


mode = 1 #1 for normal, 2 for semi advanced and 3 for advanced # will be implemented
version = 1.2
sidebarmode = 1 #1 for normal and 2 for options got it ya boi?

listofops = ['%', '+', '-', '*', '/', '.']
listofopswithoutdot = ['%', '+', '-', '*', '/']
aftereval = False
playsounds = False


def addnum(num):
    global aftereval
    if aftereval:
        showtext.set("")
        aftereval = False
    showtext.set(showtext.get() + num)




def addop(op):
    global aftereval
    current_value = showtext.get()

    if aftereval:
        aftereval = False


    if not current_value:
        return

    if op == '.':
        last_operator_index = max(current_value.rfind(op) for op in "+-*/")

        if last_operator_index == -1:
            current_segment = current_value
        else:
            current_segment = current_value[last_operator_index + 1:]

        if '.' in current_segment:
            return
        else:
            showtext.set(current_value + '.')
            return

    if op == ')':
        if current_value[-1] in listofops:
            current_value = current_value[:-1]
            if current_value.count('(')  > current_value.count(')'):
                if (current_value + op)[-2:] != '()':
                    showtext.set(current_value + op)
                    return
                else:
                    return
            else:
                return
        else:
            if current_value.count('(')  > current_value.count(')'):
                if (current_value + op)[-2:] != '()':
                    showtext.set(current_value + op)
                    return
                else:
                    return
            else:
                return

    if op == '(':
        if current_value[-1] in listofops:
            showtext.set(current_value + op)
            return
        else:
            return




    if current_value and current_value[-1] in listofops:
        if current_value[-2:] == '**':
            showtext.set(current_value)
        else:
            showtext.set(current_value[:-1] + op)
    else:
        showtext.set(current_value + op)


def starclicked():
    addop("*")
def oneclicked():
    addnum("1")
def twoclicked():
    addnum("2")
def threeclicked():
    addnum("3")
def fourclicked():
    addnum("4")
def fiveclicked():
    addnum("5")
def sixclicked():
    addnum("6")
def sevenclicked():
    addnum("7")
def eightclicked():
    addnum("8")
def nineclicked():
    addnum("9")
def zeroclicked():
    addnum("0")
def negateclicked():
    current_value = showtext.get()
    operators = ['+', '-', '*', '/']
    last_opindex = max(current_value.rfind(op) for op in operators)
    if last_opindex == -1:
        negated_value = str(int(current_value) * -1)
        anewandcorrectvalue = negated_value.replace('--', '')
        showtext.set(anewandcorrectvalue)
    else:
        before_operator = current_value[:last_opindex + 1]
        last_number = current_value[last_opindex + 1:]
        negated_value = str(int(last_number) *-1)
        anewvalue = before_operator + negated_value
        anewandcorrectvalue = anewvalue.replace('--', '')
        showtext.set(anewandcorrectvalue)
def plusclicked():
    addop("+")
def dotclicked():
    addop('.')
def deletecompletely():
    showtext.set("")
def slashclicked():
    addop("/")
def minusclicked():
    addop("-")
def deletelastdigit():
    current_value = showtext.get()
    showtext.set(current_value[:-1])

def openparantez():
    addop('(')
def closeparantez():
    addop(')')

def hatclicked():
    addop('**')

def moduloclicked():
    addop('%')

def switchbetweenadv():
    global mode
    if mode == 1:
        basicnumbers4.configure(text="(", command=openparantez)
        basicnumbers8.configure(text=")", command=closeparantez)
        basicnumbers12.configure(text="^", command=hatclicked)
        basicnumbers16.configure(text="%", command=moduloclicked)

        mode = 2
    elif mode == 2:
        basicnumbers4.configure(text="/", command=slashclicked)
        basicnumbers8.configure(text="*", command=starclicked)
        basicnumbers12.configure(text="-", command=minusclicked)
        basicnumbers16.configure(text="+", command=plusclicked)
        mode = 1

def evaluation():
    global aftereval
    final_value = showtext.get()
    if final_value:
        try:
            result = eval(final_value)
            showtext.set(str(round(result, 10)))
            aftereval = True
        except Exception as e:
            showtext.set("Error")
            print(f"Error evaluating expression: {e}")

def keyboardinteraction(button):
    global playsounds
    fcolor = button.cget("fg_color")
    hovcolor = button.cget("hover_color")
    button.configure(fg_color = hovcolor)
    app.after(150, lambda: button.configure(fg_color = fcolor))







def key_pressed(event):
    global mode
    key = event.keysym
    if key == "1":
        keyboardinteraction(basicnumbers5)
        oneclicked()
    elif key == "2":
        keyboardinteraction(basicnumbers6)
        twoclicked()
    elif key == "3":
        keyboardinteraction(basicnumbers7)
        threeclicked()
    elif key == "asterisk":
        if mode == 1:
            keyboardinteraction(basicnumbers8)
        starclicked()
    elif key == "4":
        keyboardinteraction(basicnumbers9)
        fourclicked()
    elif key == "5":
        keyboardinteraction(basicnumbers10)
        fiveclicked()
    elif key == "6":
        keyboardinteraction(basicnumbers11)
        sixclicked()
    elif key == "minus":
        if mode == 1:
            keyboardinteraction(basicnumbers12)
        minusclicked()
    elif key == "7":
        keyboardinteraction(basicnumbers13)
        sevenclicked()
    elif key == "8":
        keyboardinteraction(basicnumbers14)
        eightclicked()
    elif key == "9":
        keyboardinteraction(basicnumbers15)
        nineclicked()
    elif key == "plus":
        if mode == 1:
            keyboardinteraction(basicnumbers16)
        plusclicked()
    elif key == "0":
        keyboardinteraction(basicnumbers18)
        zeroclicked()
    elif key == "period":
        keyboardinteraction(basicnumbers19)
        dotclicked()
    elif key == "Return":
        keyboardinteraction(basicnumber20)
        evaluation()
    elif key == "BackSpace":
        keyboardinteraction(basicnumbers1)
        deletelastdigit()
    elif key == "Delete":
        keyboardinteraction(basicnumbers2)
        deletecompletely()
    elif key == "Tab":
        keyboardinteraction(basicnumbers3)
        switchbetweenadv()
    elif key == "parenleft":
        if mode == 2:
            keyboardinteraction(basicnumbers4)
        openparantez()
    elif key == "slash":
        if mode == 1:
            keyboardinteraction(basicnumbers4)
        slashclicked()
    elif key == "parenright":
        if mode == 2:
            keyboardinteraction(basicnumbers8)
        closeparantez()
    elif key == "asciicircum":
        if mode == 2:
            keyboardinteraction(basicnumbers12)
        hatclicked()
    elif key == "percent":
        if mode == 2:
            keyboardinteraction(basicnumbers16)
        moduloclicked()







def themedefault():
    basicnumbers3.configure(image=None, text="ADV")
    themeupdate("#1f6aa5", "#144870")

def themepurple():
    basicnumbers3.configure(image=None, text="ADV")
    themeupdate("#A75FE4", "#8B50BF")

def themedarkerblue():
    basicnumbers3.configure(image=None, text="ADV")
    themeupdate("#033240", "#02252f")

def themelambdaorange():
    global lambdaeasteregg
    basicnumbers3.configure(image=None, text="ADV")
    if random.randint(1,50) <= 10:
        basicnumbers3.configure(image=lambdaeasteregg,text="")
    themeupdate("#f27b1f", "#d96e1c")

def themelambdagreen():
    global lambdaeasteregg
    basicnumbers3.configure(image=None, text="ADV")
    if random.randint(1, 50) <= 10:
        basicnumbers3.configure(image=lambdaeasteregg,text="")
    themeupdate("#11d11a", "#0fbf18")


def themereddish():
    basicnumbers3.configure(image=None, text="ADV")
    themeupdate("#b91a41", "#800020")

def themegold():
    basicnumbers3.configure(image=None, text="ADV")
    themeupdate("#FCC200", "#C6930A")

def themeupdate(fcolor, hovcolor):
    basicnumbers1.configure(fg_color=fcolor, hover_color=hovcolor)
    basicnumbers2.configure(fg_color=fcolor, hover_color=hovcolor)
    basicnumbers3.configure(fg_color=fcolor, hover_color=hovcolor)
    basicnumbers4.configure(fg_color=fcolor, hover_color=hovcolor)
    basicnumbers5.configure(fg_color=fcolor, hover_color=hovcolor)
    basicnumbers6.configure(fg_color=fcolor, hover_color=hovcolor)
    basicnumbers7.configure(fg_color=fcolor, hover_color=hovcolor)
    basicnumbers8.configure(fg_color=fcolor, hover_color=hovcolor)
    basicnumbers9.configure(fg_color=fcolor, hover_color=hovcolor)
    basicnumbers10.configure(fg_color=fcolor, hover_color=hovcolor)
    basicnumbers11.configure(fg_color=fcolor, hover_color=hovcolor)
    basicnumbers12.configure(fg_color=fcolor, hover_color=hovcolor)
    basicnumbers13.configure(fg_color=fcolor, hover_color=hovcolor)
    basicnumbers14.configure(fg_color=fcolor, hover_color=hovcolor)
    basicnumbers15.configure(fg_color=fcolor, hover_color=hovcolor)
    basicnumbers16.configure(fg_color=fcolor, hover_color=hovcolor)
    basicnumbers17.configure(fg_color=fcolor, hover_color=hovcolor)
    basicnumbers18.configure(fg_color=fcolor, hover_color=hovcolor)
    basicnumbers19.configure(fg_color=fcolor, hover_color=hovcolor)
    basicnumber20.configure(fg_color=fcolor, hover_color=hovcolor)




def appearancemodechange(event):
    newappearancemode = appearancemodevar.get()
    if newappearancemode == "Dark":
        settingbutton.configure(hover_color="#2e2e2e", text_color="#dce4ee")
        importbutton.configure(fg_color='#323232', hover_color='#393939', text_color="#dce4ee")
        exportbutton.configure(fg_color='#323232', hover_color='#393939', text_color="#dce4ee")
        savebutton.configure(fg_color='#323232', hover_color='#393939', text_color="#dce4ee")
        customtkinter.set_appearance_mode("dark")
    else:
        settingbutton.configure(hover_color="#e1e1e1", text_color="#36383b")
        importbutton.configure(hover_color="#c6c6c6", fg_color="#cdcdcd", text_color="#36383b")
        exportbutton.configure(hover_color="#c6c6c6", fg_color="#cdcdcd", text_color="#36383b")
        savebutton.configure(hover_color="#c6c6c6", fg_color="#cdcdcd", text_color="#36383b")
        customtkinter.set_appearance_mode("light")



def importcalc():
    global version
    importpath = tkinter.filedialog.askopenfilename(title='Import',filetypes=[(f"Calculator {version}", "*.calc")])

    if importpath:
        try:
            with open(importpath,'r') as file:
                values = json.load(file)
                showtext.set(values["result"])
        except FileNotFoundError:
            oldshowtext = showtext.get()
            showtext.set("Import failed")
            time.sleep(3)
            showtext.set(oldshowtext)

def exportcalc():
    global exportpath
    global version

    exportingvalues = {
        "result": f"{showtext.get()}",
        "version": f"{version}"
    }




    exportpath = tkinter.filedialog.asksaveasfilename(title='Export',filetypes=[(f'Calculator {version}', "*.calc")])

    if exportpath:
        if not exportpath.endswith(".calc"):
            exportpath += ".calc"
            try:
                with open(exportpath,'w') as file:
                    json.dump(exportingvalues, file, indent=4)
                    savebutton.configure(state="normal")
            except FileExistsError:
                oldshowtext = showtext.get()
                showtext.set("Export success")
                time.sleep(3)
                showtext.set(oldshowtext)
        else:
            try:
                with open(exportpath,'w') as file:
                    json.dump(exportingvalues, file, indent=4)
            except FileExistsError:
                oldshowtext = showtext.get()
                showtext.set("Export success")
                time.sleep(3)
                showtext.set(oldshowtext)


def savecalc():
    global version
    global exportpath

    exportingvalues = {
        "result": f"{showtext.get()}",
        "version": f"{version}"
    }



    try:
        with open(exportpath,'w') as file:
            json.dump(exportingvalues, file, indent=4)
    except:
        print("uhuhuoh")



def sidebarswitch():
    global sidebarmode

    if sidebarmode == 1:
        normalsidebarframe.place_forget()
        sidebarframe.place(x=540,y=7)
        sidebarmode = 2
    else:
        sidebarframe.place_forget()
        normalsidebarframe.place(x=540,y=7)
        sidebarmode = 1



element = customtkinter
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")
app = customtkinter.CTk()
app.geometry("750x800")
app.title(f"Calculator {version}")
app.iconbitmap('_internal//calc.ico')
bigtextbox = element.CTkScrollableFrame(app, orientation="horizontal", width=500, height=160)
bigtextbox.place(x=15, y=40)
showtext= tkinter.StringVar(value="")
appearancemodevar = tkinter.StringVar(value="System")
image23 = Image.open('_internal//setting.png')
image46 = Image.open('_internal//settingdark.png')
settingicon = element.CTkImage(dark_image=image23, light_image=image46, size=(55,55))
settingiconsmall = element.CTkImage(dark_image=image23, light_image=image46, size=(40,40))
lambda1123 = Image.open('_internal//lambda.png')
lambdaeasteregg = element.CTkImage(dark_image=lambda1123, size=(96,96))
calculator1123 = Image.open('_internal//calc.png')
calculator1146 = Image.open('_internal//calcdark.png')
calculatoricon = element.CTkImage(dark_image=calculator1146,light_image=calculator1123,size=(30,40))
pallete12 = Image.open('_internal//palette.png')
pallete24 = Image.open('_internal//palettedark.png')
importicon23 = Image.open('_internal//import.png')
importicondark23 = Image.open('_internal//importdark.png')
exporticon23 = Image.open('_internal//export.png')
exporticondark23 = Image.open('_internal//exportdark.png')
importicon = element.CTkImage(dark_image=importicondark23, light_image=importicon23, size=(26,30))
exporticon = element.CTkImage(dark_image=exporticondark23, light_image=exporticon23, size=(26,30))
paletteicon = element.CTkImage(dark_image=pallete12, light_image=pallete24, size=(32,32))
bigresultthing = element.CTkLabel(bigtextbox, textvariable=showtext, font=("", 100), fg_color="transparent")
bigresultthing.grid(row=200, column=20, pady=40)
settingbutton = element.CTkButton(app, width=200, height=75, image=settingicon, anchor="w",font=("", 24), text="Settings", fg_color="transparent", hover_color="#2e2e2e", command=sidebarswitch)
settingbutton.place(x=540, y=715)
settingbutton.bind("<Enter>", lambda e, b=settingbutton: underlinetext(e, b))
settingbutton.bind("<Leave>", lambda e, b=settingbutton: ununderlinetext(e, b))
def underlinetext(e, button):
    button.configure(font=("", 24, "underline"))
def ununderlinetext(e, button):
    button.configure(font=("", 24))
sidebarframe = element.CTkFrame(app, width=200, height=700)
sidebarframe.place(x=540, y=7)
sidebarframe.place_forget()
normalsidebarframe = element.CTkFrame(app, width=200,height=700)
normalsidebarframe.place(x=540, y=7)
basicnumbers1 = element.CTkButton(app, width=120, height=105, text="CE", font=("", 48), command=deletelastdigit)
basicnumbers1.place(x=25, y=234)
basicnumbers2 = element.CTkButton(app, width=120, height=105, text="C", font=("", 48), command=deletecompletely)
basicnumbers2.place(x=151, y=234)
basicnumbers3 = element.CTkButton(app, width=120, height=105, text="ADV", font=("", 48), command=switchbetweenadv)
basicnumbers3.place(x=277, y=234)
basicnumbers4 = element.CTkButton(app, width=120, height=105, text="/", font=("", 48), command=slashclicked)
basicnumbers4.place(x=403, y=234)
basicnumbers5 = element.CTkButton(app, width=120, height=105, text="1", font=("", 48), command=oneclicked)
basicnumbers5.place(x=25, y=344)
basicnumbers6 = element.CTkButton(app, width=120, height=105, text="2", font=("", 48), command=twoclicked)
basicnumbers6.place(x=151, y=344)
basicnumbers7 = element.CTkButton(app, width=120, height=105, text="3", font=("", 48), command=threeclicked)
basicnumbers7.place(x=277, y=344)
basicnumbers8 = element.CTkButton(app, width=120, height=105, text="*", font=("", 48), command=starclicked)
basicnumbers8.place(x=403, y=344)
basicnumbers9 = element.CTkButton(app, width=120, height=105, text="4", font=("", 48), command=fourclicked)
basicnumbers9.place(x=25, y=454)
basicnumbers10 = element.CTkButton(app, width=120, height=105, text="5", font=("", 48), command=fiveclicked)
basicnumbers10.place(x=151, y=454)
basicnumbers11 = element.CTkButton(app, width=120, height=105, text="6", font=("", 48), command=sixclicked)
basicnumbers11.place(x=277, y=454)
basicnumbers12 = element.CTkButton(app, width=120, height=105, text="-", font=("", 48), command=minusclicked)
basicnumbers12.place(x=403, y=454)
basicnumbers13 = element.CTkButton(app, width=120, height=105, text="7", font=("", 48), command=sevenclicked)
basicnumbers13.place(x=25, y=564)
basicnumbers14 = element.CTkButton(app, width=120, height=105, text="8", font=("", 48), command=eightclicked)
basicnumbers14.place(x=151, y=564)
basicnumbers15 = element.CTkButton(app, width=120, height=105, text="9", font=("", 48), command=nineclicked)
basicnumbers15.place(x=277, y=564)
basicnumbers16 = element.CTkButton(app, width=120, height=105, text="+", font=("", 48), command=plusclicked)
basicnumbers16.place(x=403, y=564)
basicnumbers17 = element.CTkButton(app, width=120, height=105, text="+/-", font=("", 48), command=negateclicked)
basicnumbers17.place(x=25, y=674)
basicnumbers18 = element.CTkButton(app, width=120, height=105, text="0", font=("", 48), command=zeroclicked)
basicnumbers18.place(x=151, y=674)
basicnumbers19 = element.CTkButton(app, width=120, height=105, text=".", font=("", 48), command=dotclicked)
basicnumbers19.place(x=277, y=674)
basicnumber20 = element.CTkButton(app, width=120, height=105, text="=", font=("", 48), command=evaluation)
basicnumber20.place(x=403, y=674)
appearancelabel = element.CTkLabel(sidebarframe, text="Options", font=("Segoe UI", 35), )
appearancelabel.place(x=65, y=4)
appearancelabel2 = element.CTkLabel(sidebarframe, text="", image=settingiconsmall)
appearancelabel2.place(x=15, y=10)
appearancelabel3 = element.CTkLabel(sidebarframe, text="Appearance", font=("Segoe UI", 24), )
appearancelabel3.place(x=65, y=115)
appearancelabel4 = element.CTkLabel(sidebarframe, text="", image=paletteicon)
appearancelabel4.place(x=15, y=115)
appearancemodeswitch = element.CTkComboBox(sidebarframe, state="readonly", values=["Dark", "Light"], variable=appearancemodevar)
appearancemodeswitch.place(x=20, y=65)
appearancemodevar.trace_add("write", lambda *args: appearancemodechange(None))
sidebar1 = element.CTkButton(sidebarframe,width=72, height=72, corner_radius=40, border_width=2, border_color="gray",  text='', command=themedefault)
sidebar1.place(x=21, y=165)
sidebar2 = element.CTkButton(sidebarframe,width=72, height=72, corner_radius=36, border_width=2, border_color="gray", fg_color="#A75FE4", hover_color="#8B50BF", text='',command=themepurple)
sidebar2.place(x=108, y=165)
sidebar3 = element.CTkButton(sidebarframe,width=72, height=72, corner_radius=36, border_width=2, border_color="gray", fg_color="#033240", hover_color="#02252f", text='',command=themedarkerblue)
sidebar3.place(x=21, y=165+86)
sidebar4 = element.CTkButton(sidebarframe,width=72, height=72, corner_radius=36, border_width=2,border_color="gray", fg_color="#FCC200", hover_color="#C6930A", text='',command=themegold)
sidebar4.place(x=108, y=165+86)
sidebar5 = element.CTkButton(sidebarframe,width=72, height=72, corner_radius=36, border_width=2,border_color="gray", fg_color="#b91a41", hover_color="#800020", text='',command=themereddish)
sidebar5.place(x=21, y=165+172)
sidebar6 = element.CTkButton(sidebarframe,width=72, height=72, corner_radius=36, border_width=2,border_color="gray", fg_color="#11d11a", hover_color="#0fbf18", text='',command=themelambdagreen)
sidebar6.place(x=108, y=165+172)
sidebar7 = element.CTkButton(sidebarframe,width=72, height=72, corner_radius=36, border_width=2,border_color="gray", fg_color="#f27b1f", hover_color="#d96e1c", text='',command=themelambdaorange)
sidebar7.place(x=21, y=165+86+86+86)
sidebarversionlabel = element.CTkLabel(sidebarframe, text=f"Version : {version}")
sidebarversionlabel.place(x=60, y=675)
calculatoriconlabel = element.CTkLabel(normalsidebarframe,text='', image=calculatoricon)
calculatoriconlabel.place(x=15, y=10)
calculatorlabel = element.CTkLabel(normalsidebarframe,text='Calculator', font=("Segoe UI", 31))
calculatorlabel.place(x=55,y=8)
importbutton = element.CTkButton(normalsidebarframe,height=36,text='Import',font=("Bahnschrift",25),image=importicon,fg_color='#323232', hover_color='#393939', command=importcalc)
importbutton.place(x=25,y=75)
exportbutton = element.CTkButton(normalsidebarframe,height=36,text='Export',font=("Bahnschrift",25),image=exporticon,fg_color='#323232', hover_color='#393939', command=exportcalc)
exportbutton.place(x=25,y=129)
savebutton = element.CTkButton(normalsidebarframe,height=36,text='Save',state="disabled",font=("Bahnschrift",25),image=exporticon,fg_color='#323232', hover_color='#393939', command=savecalc)
savebutton.place(x=25,y=183)
app.bind("<Key>", key_pressed)
app.mainloop()
