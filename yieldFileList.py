#!/usr/bin/python
#-*-coding: GBK-*-
#---by sfzhang 2011.6.8---
import os
import re
import os.path
import shutil
import sys
import code
def convertToWindowsPath(pathString):
    '''对路径字符串进行规整，将各种路径转化成windows标准路径，即正斜杠\形式路径'''
    #判断是否有windows双斜杠路径
    if '\\\\' in pathString:
        #判断是不是网络共享路径
        if not pathString.startswith('\\\\'):
            pathString = re.sub('\\\\\\\\','\\\\',pathString)
        else:
            #若是网络共享路径，则保留协议\\,将后面的双斜杠路径整理成标准路径
            pathString = '\\\\'+re.sub('\\\\\\\\','\\\\',pathString.lstrip('\\\\'))
    #判断是否有unix路径分隔符，若有就转换
    if '/' in pathString:
        pathString = re.sub('/','\\\\',pathString)
    return pathString.strip()

def copyFile(sDir,fFile):
    if os.path.exists(sDir):
        for (root,dirs,files) in os.walk(sDir):
            for eachFile in files:
                fFile.write(root+'\\'+eachFile+'\n')
    else:
        print('目录不存在！')
if __name__ == '__main__':
    fListFile = open(convertToWindowsPath(sys.argv[1].strip())+'fileList.txt','w')
    print(sys.argv[1])
    print(sys.argv[1].strip())
    print(convertToWindowsPath(sys.argv[1].strip()))
    copyFile(convertToWindowsPath(sys.argv[1].strip()),fListFile)
    fListFile.close()
