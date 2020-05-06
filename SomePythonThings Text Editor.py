filePath = ''
needSave = False
from ctypes import windll, pointer, wintypes
windll.shcore.SetProcessDpiAwareness(1)
actualVersion = 2.2
def checkUpdates():
    global actualVersion 
    try:
        import struct
        import urllib.request
        response = urllib.request.urlopen("http://www.somepythonthings.tk/versions/windows/text.html")
        response = response.read().decode("utf8")
        if float(response)>actualVersion:
            if askyesno("New version available!","Do you want to go to download it?\nNew version: "+str(response)+"\nActual Version: "+str(actualVersion)) == True:
                downloadUpdates()
        else:
            showinfo('Update Checker', "You have installed the last version (v"+str(actualVersion)+")")
    except:
        showerror("Update Checker", "Unable to reach SomePythonThings servers. Try your internet connection and try again!")

def checkSilentUpdates():
    global actualVersion
    if True:
        import struct
        import urllib.request
        response = urllib.request.urlopen("http://www.somepythonthings.tk/versions/windows/text.html")
        response = response.read().decode("utf8")
        if float(response)>actualVersion:
            if askyesno("New version available!","Do you want to go to download it?\nNew version: "+str(response)+"\nActual Version: "+str(actualVersion)) == True:
                downloadUpdates()

def downloadUpdates():
    import webbrowser
    webbrowser.open_new('https://www.somepythonthings.tk/programs/somepythonthings-text-editor/')
def rClicker(e):
    ''' right click context menu for all Tk Entry and Text widgets
    '''

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
        print(' - rClick menu, something wrong')
        pass

    return "break"


def rClickbinder(r):

    try:
        for b in [ 'Text', 'Entry', 'Listbox', 'Label']: #
            r.bind_class(b, sequence='<Button-3>',
                         func=rClicker, add='')
    except TclError:
        print(' - rClickbinder, something wrong')
        pass


def saveas():
    global filePath
    global needSaveAs
    global needSave
    needSave = False
    file = asksaveasfile(defaultextension='.*', filetypes=[("All files", "*.*"), ("BAT script", "*.bat"), ("CMD script", "*.cmd"), ("Text file", "*.txt"), ("Python script", "*.py"), ("Javascript script", "*.js")])
    filePath = file.name
    file = open(filePath, 'w')
    try:
        file.write(text.get(1.0, END))
        file.close()
    except:
        file.close()
        showerror('Error', 'Error saving file')

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
            print(filePath)
            file = open(str(filePath).replace('\\\\','\\'), 'w')
            file.write(text.get(1.0, END))
            file.close()
        except:
            showerror('Error', 'Error saving file')
            file.close()
    
def openfile():
    global needSave
    needSave = False
    global text
    global filePath
    global needSaveAs
    needSaveAs = False
    try:
        file = askopenfile(defaultextension='.*', filetypes=[("All files", "*.*")])
        filePath = file.name
    except: pass
    try:
        text.delete(1.0, END)
        text.insert(1.0, file.read())
        file.close()
        save()
    except:
        file.close()
        showerror('Error', 'Error opening the file.')
    
def openfileWithPath(path):
    global needSave
    needSave = False
    global text
    global filePath
    global needSaveAs
    needSaveAs = False
    try:
        file = open(path, 'r')
        filePath = path
    except: pass
    try:
        text.delete(1.0, END)
        text.insert(1.0, file.read())
        file.close()
        save()
        needSave = False
    except:
        needSave = True
        file.close()
        showerror('Error', 'Error opening the file.')
def closefilename():
    global filenamecheck
    
def choosefilename():
    global filename
    if filename == '':
        if '.' not in filename:
            filename += '.txt'
    return filename
def new():
    global text
    global needSave
    global needSaveAs
    if needSave and askyesno('Continue?', "You will lose any unsaved change. Do you want to continue?"):
        needSaveAs = True
        needSave = False
        text.configure(state='normal')
        text.delete(1.0, END)

def quitAll():
    global needSave
    if needSave and askyesno('Unsaved changes!', 'Do you want to save any unsaved changes?'):
        save()
    app.destroy()

def saveAndExit(dialog):
    save()
    dialog.destroy()

def dontSaveAndExit(dialog):
    dialog.destroy()

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

text = tk.Text(app, yscrollcommand = scrollbarY.set, xscrollcommand = scrollbarX.set, border=0)
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

'''import os

from tkinter import PhotoImage
iSave = PhotoImage(file="save.png")
iSaveAs = PhotoImage(file="saveAs.png")
iOpen = PhotoImage(file="open.png")
iNew = PhotoImage(file="new.png")

frame = Frame(app)
frame.pack(expand=False);
bSave = ttk.Button(frame, image=iSave)
bSave.grid(row=0, column=0)
bSaveAs = ttk.Button(frame,image=iSaveAs)
bSaveAs.grid(row=0, column=1)
bOpen = ttk.Button(frame,image=iOpen)
bOpen.grid(row=0, column=2)
bNew = ttk.Button(frame,image=iNew)
bNew.grid(row=0, column=3)

buttonBar = ttk.Style()
buttonBar.configure(Save, background="#FFFFFF", border=0, height=20, width=20)
bSave.config(style=iSave)'''

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
