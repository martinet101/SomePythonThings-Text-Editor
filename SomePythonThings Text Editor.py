filePath = ''
needSave = False
try:
    from ctypes import windll, pointer, wintypes
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass
actualVersion = 2.3
########################################################
def checkUpdates():
    global actualVersion 
    try:
        import struct
        import urllib.request
        response = urllib.request.urlopen("http://www.somepythonthings.tk/versions/text.html")
        response = response.read().decode("utf8")
        if float(response)>actualVersion:
            if askyesno("Version "+str(float(response))+' available!', "We found an update for SomePythonThings Text Editor!\nDo you want to go to the web to download it?\nNew version: "+str(response)+"\nActual Version: "+str(actualVersion)) == True:
                downloadUpdates()
        else:
            showinfo('Update Checker', "You have installed the lastest version (v"+str(actualVersion)+")")
    except:
        showerror("Update Checker", "Unable to reach SomePythonThings servers. Check your internet connection and try again!")
########################################################
def checkSilentUpdates():
    global actualVersion
    if True:
        import struct
        import urllib.request
        response = urllib.request.urlopen("http://www.somepythonthings.tk/versions/text.html")
        response = response.read().decode("utf8")
        if float(response)>actualVersion:
            if askyesno("Version "+str(float(response))+' available!', "We found an update for SomePythonThings Text Editor!\nDo you want to go to the web to download it?\nNew version: "+str(response)+"\nActual Version: "+str(actualVersion)) == True:
                downloadUpdates()
########################################################
def downloadUpdates():
    import webbrowser
    webbrowser.open_new('https://www.somepythonthings.tk/programs/somepythonthings-text-editor/')
########################################################
def rClicker(e):
    try:
        def rClick_Copy(e, apnd=0):
            e.widget.event_generate('<Control-c>')

        def rClick_Cut(e):
            e.widget.event_generate('<Control-x>')

        def rClick_Paste(e):
            e.widget.event_generate('<Control-v>')
        e.widget.focus()
        nclst=[
               (' Cut      (Ctrl+C)', lambda e=e: rClick_Cut(e)),
               (' Copy   (Ctrl+X)', lambda e=e: rClick_Copy(e)),
               (' Paste   (Ctrl+V)', lambda e=e: rClick_Paste(e)),
               ]
        rmenu = Menu(None, tearoff=0, takefocus=0)
        for (txt, cmd) in nclst:
            rmenu.add_command(label=txt, command=cmd)
        rmenu.tk_popup(e.x_root+40, e.y_root+10,entry="0")
    except TclError:
        pass
    return "break"
########################################################
def rClickbinder(r):
    try:
        for b in [ 'Text', 'Entry', 'Listbox', 'Label']:
            r.bind_class(b, sequence='<Button-3>', func=rClicker, add='')
    except TclError:
        pass
########################################################
def saveas():
    global filePath
    global needSaveAs
    global needSave
    needSave = False
    try:
        file = asksaveasfile(defaultextension='*.*', filetypes=[("All files", "*.*"), ("BAT script (*.bat)", ".bat"), ("CMD script (.cmd)", "*.cmd"), ("Text file (.txt)", "*.txt"), ("Python script (.py)", "*.py"), ("Shell script (.sh)", "*.sh"), ('macOS script (.command)', '*.command')])
        if not(file==None):
            try:
                filePath = file.name
                file = open(filePath, 'w')
                file.write(text.get(1.0, END))
                file.close()
            except:
                try:
                    file.close()
                except: pass
                showerror('Error', 'Error saving file')
    except: pass
########################################################
def save():
    global needSave
    needSave = False
    global needSaveAs
    if needSaveAs == True:
        needSaveAs = False
        saveas()
    else:
        global filePath
        try:
            file = open(str(filePath).replace('\\\\','\\'), 'w')
            file.write(text.get(1.0, END))
            file.close()
        except:
            showerror('Error', 'Error saving file')
            try:
                file.close()
            except: pass
########################################################
def openfile():
    global needSave
    needSave = False
    global text
    global filePath
    global needSaveAs
    needSaveAs = False
    try:
        file = askopenfile(defaultextension='.*', filetypes=[("All files", "*.*")])
        if not(file==None):
            try:
                filePath = file.name
                text.delete(1.0, END)
                text.insert(1.0, file.read())
                file.close()
                save()
            except:
                try:
                    file.close()
                except: pass
                showerror('Error', 'Error opening the file.')
    except:
        pass
########################################################
def openfileWithPath(path):
    global needSave
    needSave = False
    global text
    global filePath
    global needSaveAs
    try:
        file = open(path, 'r')
        filePath = path
        text.delete(1.0, END)
        text.insert(1.0, file.read())
        file.close()
        save()
        needSave = False
        needSaveAs = False
    except:
        needSave = True
        needSaveAs = False
        try:
            file.close()
        except: pass
        showerror('Error', 'Error opening the file.')
########################################################
def closefilename():
    global filenamecheck
########################################################
def choosefilename():
    global filename
    if filename == '':
        if '.' not in filename:
            filename += '.txt'
    return filename
########################################################
def new():
    global text
    global needSave
    global needSaveAs
    if needSave and askyesno('Continue?', "You will lose any unsaved changes. Do you want to continue?"):
        needSaveAs = True
        needSave = False
        text.configure(state='normal')
        text.delete(1.0, END)
########################################################
def quitAll():
    global needSave
    if needSave:
        action = askyesnocancel('Unsaved changes!', 'Do you want to save any unsaved changes?')
    else:
        action = False
    if needSave and (True == action):
        try:
            save()
        except:
            pass
        app.destroy()
    elif str(action) == 'None':
        print()
    elif not(needSave) or (False == action):
        app.destroy()
########################################################
def saveAndExit(dialog):
    save()
    dialog.destroy()
########################################################
def dontSaveAndExit(dialog):
    dialog.destroy()
########################################################
def howtouse():
    info=tk.Tk()
    try:
        info.iconbitmap('text.ico')
    except: pass
    info.configure(background="#FFFFFF")
    info.resizable(False, False)
    info.title('How to use SPT Text Editor')
    infotext = Text(info, width=100, height=18, border=0)
    infotext.configure(state='normal', highlightbackground='#FFFFFF', highlightcolor='#000000', font='Consolas 11')
    infotext.insert(1.0, '\nSomePythonThings Text Editor\n\nHow to use:\n  To save:\n    1. Click on "File" menu, and then on "Save as"\n  To create a new file:\n    1. Click on "File" menu, and then on "New". The old file is going to be lost if it was not             saved.\n  To quit the program:\n    1. Click on "File" menu, and then on "Quit". The old file is going to be saved automatically           before quitting.\n\n - To view this info again, click on "Help" menu and on the "How to use" entry.\nAll copyrights to SomePythonThings. 2020.\n https://www.somepythonthings.tk')
    infotext.configure(state='disabled')
    infotext.pack()
########################################################
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import *
from tkinter.messagebox import *
filePath = ''
needSaveAs = False

app =tk.Tk()
app.title('SomePythonThings Text Editor')
app.configure(background="#FFFFFF")
try:
    app.iconbitmap('text.ico')
except: pass
scrollbarY = Scrollbar(app, orient='vertical')
scrollbarY.pack(side=RIGHT, fill=Y )

scrollbarX = Scrollbar(app, orient='horizontal')
scrollbarX.pack(side=BOTTOM, fill=X)

text = tk.Text(app,highlightthickness=0, yscrollcommand = scrollbarY.set, xscrollcommand = scrollbarX.set, border=0)
text.config(state='normal', font='Consolas 11')


def saveFM(event):
    save()
def saveAsFM(event):
    saveas()
def quitFM(event):
    quitAll()
def openFM(event):
    openfile()
def newFM(event):
    new()

def helpFM(event):
    howtouse()

def copyFM():
    text.event_generate('<Control-c>')
def cutFM():
    text.event_generate('<Control-x>')
def pasteFM():
    text.event_generate('<Control-v>')
def needSaveIsTrue(event):
    global needSave
    needSave = True

text.bind("<Control-s>", saveFM)
text.bind("<Control-Shift-s>", saveAsFM)
text.bind("<Control-o>", openFM)
text.bind("<Control-n>", newFM)
text.bind("<Control-q>", quitFM)
text.bind("<Control-h>", helpFM)
text.bind("<Key>", needSaveIsTrue)

text.pack(side=LEFT, expand=YES, fill=BOTH)
text.config(height=20, width=100, wrap=NONE)

scrollbarX.config( command = text.xview )
scrollbarY.config( command = text.yview )

menubar= Menu(app)

filemenu= Menu(menubar, tearoff=0)
filemenu.add_command(label='Save        (Ctrl+S)', command=save)
filemenu.add_command(label='Save As   ', command=saveas)
filemenu.add_command(label='Open      (Ctrl+O)', command=openfile)
filemenu.add_command(label='New        (Ctrl+N)', command=new)
filemenu.add_command(label='Quit        (Ctrl+Q)', command=quitAll)

helpmenu= Menu(menubar, tearoff=0)
helpmenu.add_command(label='How to use                  (Ctrl+H)', command=howtouse)
helpmenu.add_command(label='Check for updates', command=checkUpdates)

editmenu= Menu(menubar, tearoff=0)
editmenu.add_command(label='Cut      (Ctrl+X)', command=cutFM)
editmenu.add_command(label='Copy   (Ctrl+C)', command=copyFM)
editmenu.add_command(label='Paste   (Ctrl+V)', command=pasteFM)

menubar.add_cascade(label='File', menu=filemenu)
menubar.add_cascade(label='Edit', menu=editmenu)
menubar.add_cascade(label='Help', menu=helpmenu)
app.config(menu=menubar)
menubar.config(bg='#121212', fg='#bbbbbb')

app.bind('<Button-3>',rClicker, add='')

checkSilentUpdates()
text.configure(state='normal')
import sys
if len(sys.argv) == 2:
    openfileWithPath(str(sys.argv[1]))
else:
    needSaveAs = True
app.protocol( 'WM_DELETE_WINDOW', quitAll)
text.configure(state='normal')
app.mainloop()
