 #!/usr/bin/python
# -*- coding: GBK -*-
#2011.4.13 by  sfzhang
#本脚本的作用是按照文件列表里面提供的文件路径去寻找文件，若不存在就将其路径删除
import os
import os.path
import shutil

def delNotExistFile(FileDir):
    #原来的文件列表
    sourceFileDir = FileDir
    #目标文件列表
    aimFileDir = os.path.dirname(sourceFileDir)+'/new.txt'
    #打开原文件列表
    sourceFile= open(sourceFileDir,'r')
    #创建新文件列表
    aimFile = open(aimFileDir,'w')
    #将文件列表中的每个音频路径作为列表元素返回
    fileList = sourceFile.readlines()
    #获取列表长度
    length = len(fileList)
    #从列表头一直找到列表尾
    tokenId = 0
    for i in range(0,length,1):
        #print('eachlist:'+'i:'+repr(i)+fileList[i])
        print(fileList)
        #从列表首个元素开始，找第一个路径不正确的文件，将其删除
        for j in range(tokenId,len(fileList),1):
            print('     everyline: '+'j:'+repr(j)+fileList[j])
            #根据路径判断是否存在此文件
            if not os.path.exists(fileList[j].strip()):
                #若此路径上没有这个文件，则从列表中删除
                next = fileList[j+1]
                del fileList[j]
                tokenId = fileList.index(next)
                #找到了一个，退出循环
                break
    #将重新整理好的文件列表写入到目标文件中
    for eachline in fileList:
        aimFile.write(eachline.strip()+'\n')
    #分别关闭打开的文件对象
    sourceFile.close()
    aimFile.close()
    #将新得到的文件列表内容拷贝到原来的文件中去
    shutil.copyfile(aimFileDir,sourceFileDir)
    os.remove(aimFileDir)
#delNotExistFile('W:/test_work/AiET/3.1/teat/steady/blurRec/paramTxt/FuzzyWave.txt')
#delNotExistFile('D:/Wave.txt')
delNotExistFile('F:/wav.txt')
