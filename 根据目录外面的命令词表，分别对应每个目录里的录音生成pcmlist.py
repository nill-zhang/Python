#!/usr/bin/python
#-*-coding: GBK-*-
#---by sfzhang  2012.9.5---
import os
import re
import os.path
import shutil
import sys
import code
'''���ű��������Ǹ��ݲ�ͬƽ̨¼���ļ�Ŀ¼�����������б��Ŀ¼�ڵ���Ƶ����pcmlist'''
dir = 'E:\\project\\SE_AitalkSmall\\07.test\\������Դ\\ƽ̨¼��'
genList = os.listdir(dir)
fNo3 = open('E:\\project\\SE_AitalkSmall\\07.test\\������Դ'+'\\NO3[16K]_PcmList.txt','w')
fNo4 = open('E:\\project\\SE_AitalkSmall\\07.test\\������Դ'+'\\NO4[16K]_PcmList.txt','w')
fPc = open('E:\\project\\SE_AitalkSmall\\07.test\\������Դ'+'\\PC[16K]_PcmList.txt','w')
for i in range(0,len(genList),1):
  subGenList = os.listdir(dir+'\\'+genList[i])
  for j in range(0,len(subGenList),1):
    fuckList = os.listdir(dir+'\\'+genList[i]+'\\'+subGenList[j])
    for l in range(0,len(fuckList),1):
      cmdDirList = os.listdir(dir+'\\'+genList[i]+'\\'+subGenList[j]+'\\'+fuckList[l])
      for eachElement in cmdDirList:
        if os.path.isfile(dir+'\\'+genList[i]+'\\'+subGenList[j]+'\\'+fuckList[l]+'\\'+eachElement):
          file = open(dir+'\\'+genList[i]+'\\'+subGenList[j]+'\\'+fuckList[l]+'\\'+eachElement,'r')
          fileList = file.readlines()
          break 
      for eachFile in cmdDirList:
        if os.path.isdir(dir+'\\'+genList[i]+'\\'+subGenList[j]+'\\'+fuckList[l]+'\\'+eachFile):
          wavList = os.listdir(dir+'\\'+genList[i]+'\\'+subGenList[j]+'\\'+fuckList[l]+'\\'+eachFile)
          for k in range(0,len(wavList),1):
            if eachFile.strip() == 'No3[16K]':
              fNo3.write(dir+'\\'+genList[i]+'\\'+subGenList[j]+'\\'+fuckList[l]+'\\'+eachFile+'\\'+wavList[k]+' '+fileList[k])
            elif eachFile.strip() == 'No4[16K]':
              fNo4.write(dir+'\\'+genList[i]+'\\'+subGenList[j]+'\\'+fuckList[l]+'\\'+eachFile+'\\'+wavList[k]+' '+fileList[k])
            else:
              fPc.write(dir+'\\'+genList[i]+'\\'+subGenList[j]+'\\'+fuckList[l]+'\\'+eachFile+'\\'+wavList[k]+' '+fileList[k])
      file.close()
fNo3.close()
fNo4.close()
fPc.close()