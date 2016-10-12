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

def copyFile(sDir,fFile):
    if os.path.exists(sDir):
        for (root,dirs,files) in os.walk(sDir):
            for eachFile in files:
                fFile.write(root+'\\'+eachFile+'\n')
    else:
        print('Ŀ¼�����ڣ�')
if __name__ == '__main__':
    fListFile = open(convertToWindowsPath(sys.argv[1].strip())+'fileList.txt','w')
    print(sys.argv[1])
    print(sys.argv[1].strip())
    print(convertToWindowsPath(sys.argv[1].strip()))
    copyFile(convertToWindowsPath(sys.argv[1].strip()),fListFile)
    fListFile.close()
