 #!/usr/bin/python
# -*- coding: GBK -*-
#2011.4.13 by  sfzhang
#���ű��������ǰ����ļ��б������ṩ���ļ�·��ȥѰ���ļ����������ھͽ���·��ɾ��
import os
import os.path
import shutil

def delNotExistFile(FileDir):
    #ԭ�����ļ��б�
    sourceFileDir = FileDir
    #Ŀ���ļ��б�
    aimFileDir = os.path.dirname(sourceFileDir)+'/new.txt'
    #��ԭ�ļ��б�
    sourceFile= open(sourceFileDir,'r')
    #�������ļ��б�
    aimFile = open(aimFileDir,'w')
    #���ļ��б��е�ÿ����Ƶ·����Ϊ�б�Ԫ�ط���
    fileList = sourceFile.readlines()
    #��ȡ�б���
    length = len(fileList)
    #���б�ͷһֱ�ҵ��б�β
    tokenId = 0
    for i in range(0,length,1):
        #print('eachlist:'+'i:'+repr(i)+fileList[i])
        print(fileList)
        #���б��׸�Ԫ�ؿ�ʼ���ҵ�һ��·������ȷ���ļ�������ɾ��
        for j in range(tokenId,len(fileList),1):
            print('     everyline: '+'j:'+repr(j)+fileList[j])
            #����·���ж��Ƿ���ڴ��ļ�
            if not os.path.exists(fileList[j].strip()):
                #����·����û������ļ�������б���ɾ��
                next = fileList[j+1]
                del fileList[j]
                tokenId = fileList.index(next)
                #�ҵ���һ�����˳�ѭ��
                break
    #����������õ��ļ��б�д�뵽Ŀ���ļ���
    for eachline in fileList:
        aimFile.write(eachline.strip()+'\n')
    #�ֱ�رմ򿪵��ļ�����
    sourceFile.close()
    aimFile.close()
    #���µõ����ļ��б����ݿ�����ԭ�����ļ���ȥ
    shutil.copyfile(aimFileDir,sourceFileDir)
    os.remove(aimFileDir)
#delNotExistFile('W:/test_work/AiET/3.1/teat/steady/blurRec/paramTxt/FuzzyWave.txt')
#delNotExistFile('D:/Wave.txt')
delNotExistFile('F:/wav.txt')
