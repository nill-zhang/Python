#!/usr/bin/python
#-*-coding: GBK-*-
#---by sfzhang 2011.12.10---
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
def help():
    print('-----------------------------------------------------------------')
    print('使用方法：easyFile.exe sourceDir desDir fileName fileExName -m/-d/-c')
    print('easeFile.exe  :  工具的完整路径，若在当前目录下可以不指定路径')
    print('sourceDir   :  操作路径')
    print('desDir     :  目标目录，若不存在此路径则自动创建')
    print('fileName    :  文件名中包含此文字')
    print('fileExName   :  文件扩展名为这个格式')
    print('-m       :  即执行move操作移动到目标目录下')
    print('-d       :  执行删除操作，删除满足条件的文件')
    print('-c       :  复制到目标目录下')
    print('-----------------------------------------------------------------')
def handle(type,action,sourDir,desDir,fileName):
    if type == 'N':
        if action == 'copy':
            print('copyFile : from '+sourDir+'\\'+fileName+' to '+desDir+'\\'+re.sub('\\\\|:\\\\','_',sourDir)+'_'+fileName)
            shutil.copy2(sourDir+'\\'+fileName,desDir+'\\'+re.sub('\\\\|:\\\\','_',sourDir)+'_'+fileName)
        elif action == 'move':
            print('moveFile : from '+sourDir+'\\'+fileName+' to '+desDir+'\\'+re.sub('\\\\|:\\\\','_',sourDir)+'_'+fileName)
            shutil.move(sourDir+'\\'+fileName,desDir+'\\'+re.sub('\\\\|:\\\\','_',sourDir)+'_'+fileName)
        else:
            print('deleteFile : '+sourDir+'\\'+fileName)
            os.remove(sourDir+'\\'+fileName)
    else:
        if action == 'copy':
            print('copyFile : from '+sourDir+'\\'+fileName+' to '+desDir+'\\'+fileName)
            shutil.copy2(sourDir+'\\'+fileName,desDir+'\\'+fileName)
        elif action == 'move':
            print('moveFile : from '+sourDir+'\\'+fileName+' to '+desDir+'\\'+fileName)
            shutil.move(sourDir+'\\'+fileName,desDir+'\\'+fileName)
        else:
            print('deleteFile : '+sourDir+'\\'+fileName)
            os.remove(sourDir+'\\'+fileName)
    
def judgeActionType():
    actionType = input('若目标文件夹已存在相同的文件名，是否覆盖？Y/N')
    while actionType.strip() not in ('Y','N'):
        print('无效输入，请重新输入 Y or N!!')
        actionType = input('若目标文件夹已存在相同的文件名，是否覆盖？Y/N')
    return actionType.strip()
    
def judgeSearchType():
    type = input('是否精确查找 Y/N')
    while type.strip() not in ('Y','N'):
        print('无效输入，请重新输入 Y or N!!')
        type = input('无效输入，请输入 Y or N!!')
    return type.strip()
    
def copyFile(sDir,dDir,fName,fExName):
    if os.path.exists(sDir):
        if not '\\' in dDir:
            print('由于没有指定绝对路径，将在工具所在当前目录下，新建%s文件夹存放文件！'%(dDir))
            dDir = os.getcwd()+'\\'+dDir
        if fExName.startswith('.'):
            fExName = fExName.lstrip('.')
        if not os.path.exists(dDir):
            os.makedirs(dDir)
        print('copyFile : '+sDir)
        searchType = judgeSearchType()
        copyType = judgeActionType()
        for (root,dirs,files) in os.walk(sDir):
            for eachFile in files:
                currentfileName = os.path.splitext(eachFile)[0]
                fileExtenName = os.path.splitext(eachFile)[1].lstrip('.')
                if fName == '':
                    if searchType == 'N' and re.search(fExName,fileExtenName):
                        handle(copyType,'copy',root,dDir,eachFile)
                    elif searchType == 'Y' and fExName == fileExtenName:
                        handle(copyType,'copy',root,dDir,eachFile)
                elif fExName == '':
                    if searchType == 'N' and re.search(fName,currentfileName):
                        handle(copyType,'copy',root,dDir,eachFile)
                    elif searchType == 'Y' and fName == currentfileName:
                        handle(copyType,'copy',root,dDir,eachFile)
                else:
                    if searchType == 'N' and re.search(fName,currentfileName) and re.search(fExName,fileExtenName):
                        handle(copyType,'copy',root,dDir,eachFile)
                    elif searchType == 'Y' and fExName == fileExtenName and fName == currentfileName:
                        handle(copyType,'copy',root,dDir,eachFile)
    else:
        print('源路径设置错误，请重新设置运行！')
        sys.exit()
def deleteFile(sDir,dDir,fName,fExName):
    if os.path.exists(sDir):
        if fExName.startswith('.'):
            fExName = fExName.lstrip('.')
        print('deleteFile : '+sDir)
        searchType = judgeSearchType()
        for (root,dirs,files) in os.walk(sDir):
            for eachFile in files:
                currentfileName = os.path.splitext(eachFile)[0]
                fileExtenName = os.path.splitext(eachFile)[1].lstrip('.')
                if fName == '':
                    if searchType == 'N' and re.search(fExName,fileExtenName):
                        handle('Y','delete',root,dDir,eachFile)
                    elif searchType == 'Y' and fExName == fileExtenName:
                        handle('Y','delete',root,dDir,eachFile)
                elif fExName == '':
                    if searchType == 'N' and re.search(fName,currentfileName):
                        handle('Y','delete',root,dDir,eachFile)
                    elif searchType == 'Y' and fName == currentfileName:
                        handle('Y','delete',root,dDir,eachFile)
                else:
                    if searchType == 'N' and re.search(fName,currentfileName) and re.search(fExName,fileExtenName):
                        handle('Y','delete',root,dDir,eachFile)
                    elif searchType == 'Y' and fExName == fileExtenName and fName == currentfileName:
                        handle('Y','delete',root,dDir,eachFile)
        for (root,dirs,files) in os.walk(sDir):
            if len(os.listdir(root)) == 0:
                print('deleteEmptyDiretory : '+root)
                os.rmdir(root)
    else:
        print('源路径设置错误，请重新设置运行！')
        sys.exit()
def moveFile(sDir,dDir,fName,fExName):
    if os.path.exists(sDir):
        if not '\\' in dDir:
            print('由于没有指定绝对路径，将在工具所在当前目录下，新建%s文件夹存放文件！'%(dDir))
            dDir = os.getcwd()+'\\'+dDir
        if fExName.startswith('.'):
            fExName = fExName.lstrip('.')
        if not os.path.exists(dDir):
            os.makedirs(dDir)
        print('moveFile : '+sDir)
        searchType = judgeSearchType()
        moveType = judgeActionType()
        for (root,dirs,files) in os.walk(sDir):
            for eachFile in files:
                currentfileName = os.path.splitext(eachFile)[0]
                fileExtenName = os.path.splitext(eachFile)[1].lstrip('.')
                if fName == '':
                    if searchType == 'N' and re.search(fExName,fileExtenName):
                        handle(moveType,'move',root,dDir,eachFile)
                    elif searchType == 'Y' and fExName == fileExtenName:
                        handle(moveType,'move',root,dDir,eachFile)
                elif fExName == '':
                    if searchType == 'N' and re.search(fName,currentfileName):
                        handle(moveType,'move',root,dDir,eachFile)
                    elif searchType == 'Y' and fName == currentfileName:
                        handle(moveType,'move',root,dDir,eachFile)
                else:
                    if searchType == 'N' and re.search(fName,currentfileName) and re.search(fExName,fileExtenName):
                        handle(moveType,'move',root,dDir,eachFile)
                    elif searchType == 'Y' and fExName == fileExtenName and fName == currentfileName:
                        handle(moveType,'move',root,dDir,eachFile)
        for (root,dirs,files) in os.walk(sDir):
            if len(os.listdir(root)) == 0:
                print('deleteEmptyDiretory : '+root)
                os.rmdir(root)
    else:
        print('源路径设置错误，请重新设置运行！')
        sys.exit()
if __name__ == '__main__':
    #paramList = ['easyFile.py','D:/work','F:/test','','c','-c']
    if len(sys.argv) < 6:
        print('此工具运行时需要5个参数，请重新设置！')
        help()
        sys.exit
    elif len(sys.argv) == 6:
        sys.argv[1] = convertToWindowsPath(sys.argv[1])
        sys.argv[2] = convertToWindowsPath(sys.argv[2])
        if sys.argv[-1].strip() == '-m':
            moveFile(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
        elif sys.argv[-1].strip() == '-c':
            copyFile(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
        elif sys.argv[-1].strip() == '-d':
            delInfo = input('Do you really want to delete file Y/N?')
            if delInfo == 'Y':
                deleteFile(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
            else:
                print('用户取消删除操作！')
                sys.exit
        else:
            print('操作参数设置错误，请指定 -m|-d|-c')
            help()
            sys.exit
    else:
        print('设置参数过多，工具最多只需要5个参数')
        help()
        sys.exit
