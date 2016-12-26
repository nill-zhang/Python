#!/usr/bin/python
# -*- coding: UTF-8 -*-
#2012.10.1 by  sfzhang
import os
import re
import os.path
import random
#判断存放paper.txt和wave.txt以及评测结果result.txt的目录是否存在，若不存在，新建目录
desDir = ('D:/work/python/toolTest')
if os.path.exists(desDir):
        os.chdir(desDir)
else:
       os.makedirs(desDir)
#新建paper和wave
waveList = open('D:/work/python/toolTest/wave.txt','w')
paperList = open('D:/work/python/toolTest/paper.txt','w')
#分别打开放置各个评测参数文本路径的文本
paramWaveSetTxt = open('D:/work/python/paramTXT/ParamWaveSetTxtList.txt','r')
paramWaveTxtList = paramWaveSetTxt.readlines()
paramPaperSetTxt = open('D:/work/python/paramTXT/ParamPaperSetTxtList.txt','r')
paramPaperTxtList = paramPaperSetTxt.readlines()
#进行wave.txt的自动生成
for j in range(1,9155,1):
    #生成wave.txt的一行
    for i in range(0,14,1):
         #获得要生成的wave.txt第i列的参数文本位置
         currentWaveTxtDir = paramWaveTxtList[i]
         #去除位置字符串首尾的格式字符串，根据位置打开参数文本
         currentWaveParamTxtFile = open(currentWaveTxtDir.strip(),'r')
         #获取所有这个参数的可取值
         currentWaveTxtList = currentWaveParamTxtFile.readlines()
         #随机取一个参数值，写入到wave.txt的第i列
         itemWave = random.choice(currentWaveTxtList)
         if (i+1)%14 == 0:
             #一行14个参数生成完，换行
             waveList.write(itemWave.strip()+'\n')
         else:
             #一行未写完，一个参数一个参数的写，中间制表符分割
             waveList.write(itemWave.strip()+'\t')
    #waveList.write('\n')
#进行paper.txt的自动生成
for l in range(1,9155,1):
    #生成paper.txt的一行
    for k in range(0,2,1):
        #获得要生成的paper.txt的第k列的参数文本位置
        currentPaperTxtDir = paramPaperTxtList[k]
        #去除位置字符串首尾的空格等，并根据位置打开参数文本
        currentPaperParamTxtFile = open(currentPaperTxtDir.strip(),'r')
        #获得这个参数的所有可取的值
        currentPaperTxtList = currentPaperParamTxtFile.readlines()
        #随机取一个值，写入到paper.txt的第K列
        itemPaper= random.choice(currentPaperTxtList)
        if (k+1)%2 == 0:
             #一行两个参数写完，换行
             paperList.write(itemPaper.strip()+'\n')
        else:
             #一行未写完，一个参数一个参数写，中间制表符分割
             paperList.write(itemPaper.strip()+'\t')
    #paperList.write('\n')
#paper.txt和wave.txt生成后，关闭文件
paperList.close()
waveList.close()
#设置当前目录
os.chdir('D:/work/python/toolTest')
#设置工具位置
tool='D:/work/aiet/OfflineBatchTest.exe '
#设置离线测试工具需要的三个参数的位置
paperList = './paper.txt '
waveList =  './wave.txt '
resultDir = './result.txt'
cmd = (tool+paperList+waveList+resultDir)
#调用离线测试工具，传入参数随机生成的文本信息和语音信息文本进行评测
os.system(cmd)
