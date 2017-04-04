# !/usr/bin/python
# -*-coding: GBK-*-
# ---by sfzhang 2011.12.10---
import os
import re
import os.path
import shutil
import sys

def convertToWindowsPath(pathString):
    '''��·���ַ������й�����������·��ת����windows��׼·��������б��\��ʽ·��'''
    #�ж��Ƿ���windows˫б��·��
    if '\\\\' in pathString:
        #�ж��ǲ������繲��·��
        if not pathString.startswith('\\\\'):
            pathString = re.sub('\\\\\\\\','\\\\',pathString)
        else:
            #�������繲��·��������Э��\\,�������˫б��·������ɱ�׼·��
            pathString = '\\\\'+re.sub('\\\\\\\\','\\\\',pathString.lstrip('\\\\'))
    #�ж��Ƿ���unix·���ָ��������о�ת��
    if '/' in pathString:
        pathString = re.sub('/','\\\\',pathString)
    return pathString.strip()


def help():
    print('-'*80)
    print('ʹ�÷�����easyFile.exe sourceDir desDir fileName fileExName -m/-d/-c')
    print('easeFile.exe  :  ���ߵ�����·�������ڵ�ǰĿ¼�¿��Բ�ָ��·��')
    print('sourceDir   :  ����·��')
    print('desDir     :  Ŀ��Ŀ¼���������ڴ�·�����Զ�����')
    print('fileName    :  �ļ����а���������')
    print('fileExName   :  �ļ���չ��Ϊ�����ʽ')
    print('-m       :  ��ִ��move�����ƶ���Ŀ��Ŀ¼��')
    print('-d       :  ִ��ɾ��������ɾ�������������ļ�')
    print('-c       :  ���Ƶ�Ŀ��Ŀ¼��')
    print('-'*80)


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
    actionType = input('��Ŀ���ļ����Ѵ�����ͬ���ļ������Ƿ񸲸ǣ�Y/N')
    while actionType.strip() not in ('Y','N'):
        print('��Ч���룬���������� Y or N!!')
        actionType = input('��Ŀ���ļ����Ѵ�����ͬ���ļ������Ƿ񸲸ǣ�Y/N')
    return actionType.strip()


def judgeSearchType():
    type = input('�Ƿ�ȷ���� Y/N')
    while type.strip() not in ('Y','N'):
        print('��Ч���룬���������� Y or N!!')
        type = input('��Ч���룬������ Y or N!!')
    return type.strip()


def copyFile(sDir,dDir,fName,fExName
    if os.path.exists(sDir):
        if not '\\' in dDir:
            print('����û��ָ������·�������ڹ������ڵ�ǰĿ¼�£��½�%s�ļ��д���ļ���'%(dDir))
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
        print('Դ·�����ô����������������У�')
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
        print('Դ·�����ô����������������У�')
        sys.exit()


def moveFile(sDir,dDir,fName,fExName):
    if os.path.exists(sDir):
        if not '\\' in dDir:
            print('����û��ָ������·�������ڹ������ڵ�ǰĿ¼�£��½�%s�ļ��д���ļ���'%(dDir))
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
        print('Դ·�����ô����������������У�')
        sys.exit()



if __name__ == '__main__':
    #paramList = ['easyFile.py','D:/work','F:/test','','c','-c']
    if len(sys.argv) < 6:
        print('�˹�������ʱ��Ҫ5�����������������ã�')
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
                print('�û�ȡ��ɾ��������')
                sys.exit
        else:
            print('�����������ô�����ָ�� -m|-d|-c')
            help()
            sys.exit
    else:
        print('���ò������࣬�������ֻ��Ҫ5������')
        help()
        sys.exit
