#!/usr/bin/python
# -*- coding: UTF-8 -*-
#2012.10.1 by  sfzhang
import os
import re
import os.path
import random
#�жϴ��paper.txt��wave.txt�Լ�������result.txt��Ŀ¼�Ƿ���ڣ��������ڣ��½�Ŀ¼
desDir = ('D:/work/python/toolTest')
if os.path.exists(desDir):
        os.chdir(desDir)
else:
       os.makedirs(desDir)
#�½�paper��wave
waveList = open('D:/work/python/toolTest/wave.txt','w')
paperList = open('D:/work/python/toolTest/paper.txt','w')
#�ֱ�򿪷��ø�����������ı�·�����ı�
paramWaveSetTxt = open('D:/work/python/paramTXT/ParamWaveSetTxtList.txt','r')
paramWaveTxtList = paramWaveSetTxt.readlines()
paramPaperSetTxt = open('D:/work/python/paramTXT/ParamPaperSetTxtList.txt','r')
paramPaperTxtList = paramPaperSetTxt.readlines()
#����wave.txt���Զ�����
for j in range(1,9155,1):
    #����wave.txt��һ��
    for i in range(0,14,1):
         #���Ҫ���ɵ�wave.txt��i�еĲ����ı�λ��
         currentWaveTxtDir = paramWaveTxtList[i]
         #ȥ��λ���ַ�����β�ĸ�ʽ�ַ���������λ�ô򿪲����ı�
         currentWaveParamTxtFile = open(currentWaveTxtDir.strip(),'r')
         #��ȡ������������Ŀ�ȡֵ
         currentWaveTxtList = currentWaveParamTxtFile.readlines()
         #���ȡһ������ֵ��д�뵽wave.txt�ĵ�i��
         itemWave = random.choice(currentWaveTxtList)
         if (i+1)%14 == 0:
             #һ��14�����������꣬����
             waveList.write(itemWave.strip()+'\n')
         else:
             #һ��δд�꣬һ������һ��������д���м��Ʊ���ָ�
             waveList.write(itemWave.strip()+'\t')
    #waveList.write('\n')
#����paper.txt���Զ�����
for l in range(1,9155,1):
    #����paper.txt��һ��
    for k in range(0,2,1):
        #���Ҫ���ɵ�paper.txt�ĵ�k�еĲ����ı�λ��
        currentPaperTxtDir = paramPaperTxtList[k]
        #ȥ��λ���ַ�����β�Ŀո�ȣ�������λ�ô򿪲����ı�
        currentPaperParamTxtFile = open(currentPaperTxtDir.strip(),'r')
        #���������������п�ȡ��ֵ
        currentPaperTxtList = currentPaperParamTxtFile.readlines()
        #���ȡһ��ֵ��д�뵽paper.txt�ĵ�K��
        itemPaper= random.choice(currentPaperTxtList)
        if (k+1)%2 == 0:
             #һ����������д�꣬����
             paperList.write(itemPaper.strip()+'\n')
        else:
             #һ��δд�꣬һ������һ������д���м��Ʊ���ָ�
             paperList.write(itemPaper.strip()+'\t')
    #paperList.write('\n')
#paper.txt��wave.txt���ɺ󣬹ر��ļ�
paperList.close()
waveList.close()
#���õ�ǰĿ¼
os.chdir('D:/work/python/toolTest')
#���ù���λ��
tool='D:/work/aiet/OfflineBatchTest.exe '
#�������߲��Թ�����Ҫ������������λ��
paperList = './paper.txt '
waveList =  './wave.txt '
resultDir = './result.txt'
cmd = (tool+paperList+waveList+resultDir)
#�������߲��Թ��ߣ��������������ɵ��ı���Ϣ��������Ϣ�ı���������
os.system(cmd)
