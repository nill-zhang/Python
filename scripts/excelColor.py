#!/usr/bin/python
# -*- coding: GBK -*-
#2012.11.13 by  sfzhang
from tkinter import Tk
from time import sleep
from tkinter.messagebox import showwarning
import win32com.client as win32
warn = lambda app:showwarning(app,'Exit?')
row = range(3,9)
queue = range(3,9)

def excel():
    excl = win32.Dispatch('Excel.Application')
    workbook =excl.Workbooks.Add()
    sh1 = workbook.activesheet
    excl.visible = 1
    sleep(1)
    #sh1.cells(1,1).value = 'python'
    sleep(1)
    for i in row:
        for j in queue:
                sh1.cells(i,j).value ='行 '+repr(i)+'列'+repr(j)
                sh1.Cells(i,j).Interior.ColorIndex =  i
                sleep(1)
                #sh1.cells(i+2,1).value = 'that\'s all folks'
    warn('Excel')
    workbook.close(false)
    excl.application.quit()
if __name__ =='__main__':
    Tk().withdraw()
    excel()
    