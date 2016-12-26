#!/usr/bin/python
#-*-coding: utf-8-*-
#2012.3.4 by sfzhang
import tkinter
import functools
import tkinter.messagebox
def showYes():
    showYesWin =tkinter.Toplevel()
    labelShowYes = tkinter.Label(showYesWin,test = 'yes,this is kernelTest!')
    labelShowYes.pack()
    showYesWin.mainloop()
    print('yes,this is kernelTest!')
def showNo():
    showNoWin =tkinter.Toplevel()
    labelShowNo = tkinter.Label(showNoWin,test = 'yes,this is kernelTest!')
    labelShowNo.pack()
    showNoWin.mainloop()
    print('no,this is not kernelTest!')
def setSize(ev=None):
    label.config(font = 'Helvetica -{0} bold'.format(scaleBar.get()))

warnCB = lambda : tkinter.messagebox.showwarning('Waring','警告！')
messageCB = lambda : tkinter.messagebox.showerror('message','消息！')
informationCB = lambda : tkinter.messagebox.showinfo('information','提示信息！')
root = tkinter.Tk()
root.geometry('800x600')
label = tkinter.Label(root,text ='内核测试组测试程序！',font = 'Helvetica -12 bold')
buttonYes = tkinter.Button(root,text = 'Yes',fg='blue',command = showYes)
buttonYes.bell()
buttonNo = tkinter.Button(root,text = 'No',fg = 'yellow',command = showNo)
buttonNo.pack(fill = tkinter.BOTH,side = tkinter.LEFT)
buttonYes.pack(fill = tkinter.BOTH,side = tkinter.RIGHT)
label.pack(side = tkinter.BOTTOM)
scaleBar = tkinter.Scale(root,from_ = 10,to = 40,fg = 'blue',command = setSize)
buttonTemplate = functools.partial(tkinter.Button,root,bg = 'green',fg = 'red',padx = 12,pady = 6)
canvasTemplate = functools.partial(tkinter.Canvas,root,bg ='white',height = 40,width = 20)
listBoxTemplate = functools.partial(tkinter.Listbox,root,bg = 'purple')
listBox1 = listBoxTemplate(takefocus = 'true')
listBox1.pack()
canvas1 = canvasTemplate(borderwidth = 2)
canvas1.pack()
radioButtonTemplate = functools.partial(tkinter.Radiobutton,root)
radioButton1 = radioButtonTemplate(text = '是否党员',)
radioButton1.pack()
buttonWarn = buttonTemplate(text = 'Warn',command = warnCB)
buttonMessage = buttonTemplate(text = 'Message',command = messageCB)
buttonInformation = buttonTemplate(text = 'Information',command = informationCB)
buttonInformation.pack()
buttonMessage.pack()
buttonWarn.pack()
scaleBar.set(12)
scaleBar.pack()
root.title = 'TK APPLICATION!'
root.mainloop()
str
