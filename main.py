# Tkinter Components
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import tkinter as tk
import pyautogui as pag, datetime, os

import author

authorController = author.Author("PS Notepad")
authorController.echoAuthor()

class NotePad:

    def __init__(self):

        self.DefaultBg = "#000"
        self.DefaultFg = "#fff"

        self.CustomBg = "#fff"
        self.CustomFg = "#000"

        self.ThemeColor = False
        
        self.NPWind = Tk()
        self.NPWind.geometry("800x700+200+60")
        self.NPWind.title("PS Notepad")
        self.NPWind.resizable(0, 0)
        self.NPWind.iconbitmap("logo.ico")
        
        self.fileVal = tk.StringVar()
        
        self.textEditor = Text(self.NPWind, wrap=tk.WORD, height=27, bg=self.DefaultBg, foreground=self.DefaultFg, insertbackground=self.DefaultFg)
        self.textEditor.pack(side="top")
        
        self.fileName = Label(self.NPWind, text= "File Name ")
        self.fileName.place(x = 5, y = 612)

        self.fileNameEntry = Entry(self.NPWind, textvariable=self.fileVal)
        self.fileNameEntry.place(x = 95, y = 612)

        self.SaveBtn = Button(self.NPWind, text="Save", width=8, command=self._saveFile)
        self.SaveBtn.place(x = 315, y = 610)

        self.ClrBtn = Button(self.NPWind, text="Clear", width=8, command = self._clearEditor)
        self.ClrBtn.place(x = 407, y = 610)

        self.HelpBtn = Button(self.NPWind, text="Help", width=8, command=self._helpNotepad)
        self.HelpBtn.place(x = 499, y = 610)

        self.ExitBtn = Button(self.NPWind, text="Exit", width=8, command=self._closeNotePad)
        self.ExitBtn.place(x = 591, y = 610)

        self.changeBtn = Button(self.NPWind, text="☀ Theme", width=9, command = self._changeThemeColor)
        self.changeBtn.place(x = 683, y = 610)

        chkCurrentYear = datetime.datetime.now().strftime("%Y")

        if int(chkCurrentYear) > 2023:
            cpyrightYear = "2023 - "+str(chkCurrentYear)
        else:
            cpyrightYear = "2023"

        self.authorLabel = Label(self.NPWind, text='PS Thamizhan - © '+str(cpyrightYear)+'. V1.0', font=("Segoe UI", 7))
        self.authorLabel.pack(side=BOTTOM, ipady=10)

        self.OutPutFolder = "Saved Files"

        if not os.path.exists(self.OutPutFolder):
            os.mkdir(self.OutPutFolder)

    def _saveFile(self):
        
        fileText = self.textEditor.get("1.0", END)
        fileName = self.fileNameEntry.get()

        if str(fileText.strip()) != "" and str(fileName.strip()) != "":

            actuaFile = str(self.OutPutFolder)+"/"+str(fileName)
            try:
                writeAct = "w"

                if not os.path.exists(actuaFile):
                    writeAct = "w"
                else:
                    writeAct = "w+"
                
                with open(str(actuaFile), writeAct, encoding="UTF-8") as tmp:
                    tmp.write(str(fileText))
                messagebox.showinfo("PS Notepad Alert", "File Saved Successfully.\nFilename :: "+str(actuaFile)+"                         ")
                
            except:
                messagebox.showerror("PS Notepad Alert", "Something wrong.                         ")
            
        else:
            messagebox.showerror("PS Notepad Alert", "Values are empty.                         ")

        return True

    def _clearEditor(self):
        try:
            self.textEditor.delete("1.0", END)
            self.fileNameEntry.delete("0", END)
        except:
            messagebox.showerror("PS Notepad Alert", "Something wrong.                         ")

        return True

    def _changeThemeColor(self):
        if not self.ThemeColor:
            self.textEditor.config(bg = self.CustomBg)
            self.textEditor.config(fg = self.CustomFg)
            self.textEditor.config(insertbackground = self.CustomFg)
            self.ThemeColor = True
        else:
            self.textEditor.config(bg = self.DefaultBg)
            self.textEditor.config(fg = self.DefaultFg)
            self.textEditor.config(insertbackground = self.DefaultFg)
            self.ThemeColor = False
        return True

    def _helpNotepad(self):

        helpContent = str(authorController.author)
        helpContent += "Follow steps to use Notepad\n-------------------------------------------------------"
        helpContent += "\nUse Editor for edit content.\nUse Filename field for give a name of the file.\nClick Save Button to save the file."
        helpContent += "\nUse Clear Button to clear both editor & filename field.\nUse Exit Button to close the Notepad.\n"
        helpContent += "\nUse Theme Button to change the Editor Background."
        messagebox.showinfo("PS Notepad Help", str(helpContent))

        return True

    def _closeNotePad(self):
        extBtn = messagebox.askquestion("PS Notepad Alert", "Are you sure to exit ?                                                  ")
        if(extBtn == 'yes'):

            fileText = self.textEditor.get("1.0", END)
            fileName = self.fileNameEntry.get()

            if str(fileText.strip()) != "" and str(fileName.strip()) != "":
                actualFile = str(self.OutPutFolder)+"/"+str(fileName)
                if os.path.exists(actualFile):
                    self.NPWind.destroy()
                else:
                    askQn = messagebox.askquestion("PS Notepad Alert", "File Not Saved.\nDo you want to save ?                                    ")
                    if str(askQn) == "no":
                        self.NPWind.destroy()
                    else:
                        self._saveFile()
                        self.NPWind.destroy()
            else:
                if str(fileText.strip()) != "":
                    askQn = messagebox.askquestion("PS Notepad Alert", "File Not Saved.\nDo you want to save ?                                    ")
                    if str(askQn) == "no":
                        self.NPWind.destroy()
                    else:
                        flNme = datetime.datetime.now().strftime("%Y%b%d_%I%M%S_%p")
                        flNme = str(flNme)+".txt"
                        self.fileVal.set(flNme)
                        self._saveFile()
                        self.NPWind.destroy()
                else:
                    self.NPWind.destroy()

        return True
    
    def runModule(self):
        self.NPWind.mainloop()

mod = NotePad()
mod.runModule()
