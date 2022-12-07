import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import pdfConverterMain

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("434x291+732+293")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1,  1)
        top.title("Image to Pdf")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.top = top

        self.path = tk.Label(self.top)
        self.path.place(relx=0.046, rely=0.172, height=31, width=394)
        self.path.configure(activebackground="#f9f9f9")
        self.path.configure(activeforeground="black")
        self.path.configure(background="#d9d9d9")
        self.path.configure(compound='left')
        self.path.configure(disabledforeground="#a3a3a3")
        self.path.configure(foreground="#000000")
        self.path.configure(highlightbackground="#d9d9d9")
        self.path.configure(highlightcolor="black")
        self.path.configure(text='''File Path''')

        self.Button1 = tk.Button(self.top)
        self.Button1.place(relx=0.415, rely=0.344, height=44, width=87)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(compound='left')
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Choose Path''')
        self.Button1.configure(command=pdfConverterMain.choosePath)

        self.Button1_1 = tk.Button(self.top)
        self.Button1_1.place(relx=0.415, rely=0.584, height=44, width=87)
        self.Button1_1.configure(activebackground="#ececec")
        self.Button1_1.configure(activeforeground="#000000")
        self.Button1_1.configure(background="#66ccfd")
        self.Button1_1.configure(compound='left')
        self.Button1_1.configure(disabledforeground="#a3a3a3")
        self.Button1_1.configure(foreground="#000000")
        self.Button1_1.configure(highlightbackground="#d9d9d9")
        self.Button1_1.configure(highlightcolor="black")
        self.Button1_1.configure(pady="0")
        self.Button1_1.configure(text='''Create PDF''')
        self.Button1_1.configure(command=pdfConverterMain.createPdf)

        self.error = tk.Label(self.top)
        self.error.place(relx=0.023, rely=0.859, height=31, width=414)
        self.error.configure(activebackground="#f9f9f9")
        self.error.configure(activeforeground="black")
        self.error.configure(background="#d9d9d9")
        self.error.configure(compound='left')
        self.error.configure(disabledforeground="#a3a3a3")
        self.error.configure(foreground="#000000")
        self.error.configure(highlightbackground="#d9d9d9")
        self.error.configure(highlightcolor="black")

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

def start_up():
    pdfConverterMain.main()

if __name__ == '__main__':
    pdfConverterMain.main()




