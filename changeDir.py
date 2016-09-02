#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import os.path
import shutil
#获取音频文件存放路径列表
waveList = open('W:/test_work/AiET/3.1/test/effect/for_word_1047/列表/wav.txt','r')
#获取评测文本存放路径列表
paperList = open('W:/test_work/AiET/3.1/test/effect/for_word_1047/列表/paper.txt','r')
#重新生成的评测文本列表
desList = open('W:/test_work/AiET/3.1/test/effect/for_word_1047/列表/paperlist.txt','w')
allLines = waveList.readlines()
paperDir = paperList.readline()
waveList.close()
for eachline in allLines:
    #获取音频文件全称
    wavName = os.path.basename(eachline)
	#切分出想要的文件名
    str = wavName[24:30]
    #str = eachline[86:92]
    print(str)
	#将文件名和评测文本存放目录进行联结
    pathName = os.path.dirname(paperDir)+'\\'+str+'txt'
    #pathName = '\\\\192.168.77.158\data\esee25\defect_detect\word\data\paper'+'\\'+str+'txt'
    desList.write(pathName+'\n')
print('Dir has been changed OK!')