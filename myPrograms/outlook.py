#!/usr/bin/python
# -*- coding: GBK -*-
#2011.8.25 by  sfzhang
from tkinter import Tk
from time import sleep
from tkinter.messagebox import showwarning
import win32com.client as win32
warn = lambda app:showwarning(app,'Exit?')
RANGE = range(3,8)

def outlook():
    otlook = win32.Dispatch('Outlook.Application')
    ns = otlook.GetNamespace('MAPI')
    mail = otlook.CreateItem(win32.constants.olMailItem)
    receivePerson = mail.recipients.add('sfzhang@iflytek.com')
    subj = mail.subject ='Python Test '
    body = ['line'+repr(i) for i in RANGE]
    body.insert(0,subj+'\r\n')
    body.append('\r\n that\'s all folks!')
    mail.body ='\r\n'.join(body)
    mail.send()
    
    obox = ns.GetDefaultFolder(win32.constants.olFolderOutbox)
    obox.Display()
    obox.Items.Item(1).Display()
    warn(app)
    otlook.quit()
if __name__ =='__main__':
    Tk().withdraw()
    outlook()
    