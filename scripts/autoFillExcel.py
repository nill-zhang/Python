#!/usr/bin/python
# -*- coding: GBK -*-
#2011.8.13 by  sfzhang

''' excel operation sample '''
import os
import os.path
import shutil
import win32com.client
app = win32com.client.Dispatch('excel.application')
workbk = app.workbooks.open('E:/t.xlsx')
print('workbk sheetcount = '+repr(workbk.sheets.count))
sheet = workbk.sheets('sheet1')
sheet.cells(2,1).value = 'fuck'
sheet.cells(2,2).value = 0.25
print('sheet1 rows = '+repr(sheet.usedrange.rows.count))
print('sheet1 columns = '+repr(sheet.usedrange.columns.count))
workbk.save()
workbk.close()
app.quit()
