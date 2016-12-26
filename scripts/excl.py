#!/usr/bin/python
# -*- coding: GBK -*-
#2012.6.23 by  sfzhang
from tkinter import Tk
from time import sleep
from tkinter.messagebox import showwarning
import win32com.client as win32
warn = lambda app:showwarning(app,'Exit?')
RANGE = range(3,8)

def excel():
    excl = win32.Dispatch('Excel.Application')
    workbook =excl.Workbooks.Add()
    sh1 = workbook.activesheet
    excl.visible = 1
    sleep(1)
    sh1.cells(1,1).value = 'python'
    sleep(1)
    for i in RANGE:
        sh1.cells(i,1).value ='line '+repr(i)
        sleep(1)
        sh1.cells(i+2,1).value = 'that\'s all folks'
    warn('Excel')
    workbook.close(false)
    excl.application.quit()
if __name__ =='__main__':
    Tk().withdraw()
    excel()
    
