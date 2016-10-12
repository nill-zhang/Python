#!/usr/bin/python
# -*- coding: GBK -*-
#2012.5.13 by  sfzhang
import os
import os.path
import shutil
import win32com.client
app = win32com.client.Dispatch('excel.application')
workbk = app.workbooks.open('E:/t.xls')
print('workbk sheetcount = '+repr(workbk.sheets.count))
sheet = workbk.sheets('sheet1')
sheet.cells(2,1).value = 'app'
sheet.cells(2,2).value = 0.25
print('sheet1 rows = '+repr(sheet.usedrange.rows.count))
print('sheet1 columns = '+repr(sheet.usedrange.columns.count))
workbk.save()
workbk.close()
app.quit()
