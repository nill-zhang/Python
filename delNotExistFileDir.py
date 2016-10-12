#!/usr/bin/python
# -*- coding: GBK -*-
#2011.8.2 by  sfzhang
import os
import os.path
import shutil
import re
baseFileDir = 'D:/t.txt'
aimFileDir = 'D:/a.txt'
sourceFile= open(baseFileDir,'r')
aimFile = open(aimFileDir,'w')
fileList = sourceFile.readlines()
for eachlist in fileList:
    print('eachlist:'+eachlist)
    print(fileList)
    for eachline in fileList:
        print('       everyline: '+eachline)
        if not os.path.exists(eachline.strip()):
            fileList.remove(eachline)
            break
for eachline in fileList:
    aimFile.write(eachline.strip()+'\n')
sourceFile.close()
aimFile.close()
#if os.path.exists(baseFileDir):
    #temFileDir = baseFileDir
    #os.remove(baseFileDir)
    #os.rename(os.path.basename(aimFileDir),temFileDir)
shutil.copyfile(aimFileDir,baseFileDir)
