import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
from tkinter.filedialog import askdirectory
import pdfConverterGui
import os
import fpdf


filePATH = ""

def main(*args):
    '''Main entry point for the application.'''
    global root
    root = tk.Tk()
    root.protocol('WM_DELETE_WINDOW', root.destroy)
    global _top1, _w1
    _top1 = root
    _w1 = pdfConverterGui.Toplevel1(_top1)
    root.mainloop()


if __name__ == '__main__':
    pdfConverterGui.start_up()


def choosePath():
    global filePATH
    filePATH = askdirectory()
    _w1.path["text"] = filePATH

def createPdf():
    if(filePATH == ""):
        _w1.error["text"] = "Please choose a path"
        return
    pdf = fpdf.FPDF()
    fileSize = 0
    for i in range(1, len(os.listdir(filePATH))+1):
        if(os.path.exists(filePATH + "/" + str(i) + ".png")):
            im = filePATH + "/" + str(i) + ".png"
            pdf.add_page()
            pdf.image(im, 0, 0, 210, 297)
            fileSize += 1
        elif(os.path.exists(filePATH + "/" + str(i) + ".jpg")):
            im = filePATH + "/" + str(i) + ".jpg"
            pdf.add_page()
            pdf.image(im, 0, 0, 210, 297)
            fileSize += 1
        elif(os.path.exists(filePATH + "/" + str(i) + ".jpeg")):
            im = filePATH + "/" + str(i) + ".jpg"
            pdf.add_page()
            pdf.image(im, 0, 0, 210, 297)
            fileSize += 1
        else:
            print("File is not a image")
            break
    if(fileSize == 0):
        _w1.error["text"] = "No files found"
        pdf = None
    else:
        pdf.output(filePATH + "/output.pdf", "F")
        _w1.error["text"] = "File created with " + str(fileSize) + " pages"
