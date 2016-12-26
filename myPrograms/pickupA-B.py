#!/usr/bin/python
# -*- coding: GBK -*-
#2011.7.13 by  sfzhang
import os
import os.path
import shutil
import re
baseFileDir = 'D:/AiTalkSmall效果评估命令词集-中文（建议）.txt'
aimFileDir = 'D:/cmd.txt'
FileDir = open('D:/notEquel.txt','w')
sourceFile= open(baseFileDir,'r')
aimFile = open(aimFileDir,'r')
sourceFileList = sourceFile.readlines()
aimFileList = aimFile.readlines()
print(aimFileList)
for eachlist in sourceFileList:
	if eachlist not in aimFileList:
		print('       everyline: '+eachlist)
		FileDir.write(eachlist)
sourceFile.close()
aimFile.close()
FileDir.close()