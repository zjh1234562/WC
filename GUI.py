from tkinter import *
import tkinter
from tkinter import filedialog
from Count import *
import sys
import re


class Windows():
    def __init__(self):
        self.top = tkinter.Tk()
        self.file_path=None
        self.text=None

    def openfile(self):
        self.file_path = tkinter.filedialog.askopenfilename(title=u'选择文件')

    def countfile(self):
        c=Count()
        self.text.insert(INSERT, c.get_other(self.file_path))
        self.text.insert(INSERT,'\n')
        self.text.insert(INSERT, c.get_line(self.file_path))
        self.text.insert(INSERT, '\n')
        self.text.insert(INSERT, c.get_word(self.file_path))
        self.text.insert(INSERT, '\n')
        self.text.insert(INSERT, c.get_char(self.file_path))
        self.text.insert(INSERT, '\n')



    def gui(self):
        self.top.geometry("700x400")
        button=tkinter.Button(self.top,text="打开文件",width=10, height=5,command=self.openfile)
        button2=tkinter.Button(self.top,text="统计",width=10, height=5,command=self.countfile)
        label=tkinter.Label(self.top,text="显示")
        self.text=tkinter.Text(self.top,font=("Helvetica",16),width = 40, height=10)


        button.grid(row=0,column=50)
        button2.grid(row=1,column=50)
        label.grid(row=0, column=0)
        self.text.grid(row=1, column=0)

        self.top.mainloop()












