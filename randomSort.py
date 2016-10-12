#!/usr/bin/python
#-*-coding: GBK-*-
#---by sfzhang  2011.6.10---
import os
import re
import os.path
import shutil
import sys
import code
import random
'''将一个文件的所以行打乱，重新生成一个目标文件'''
#将脚本所在目录设置为当前目录
print(sys.argv[0])
os.chdir(os.path.dirname(sys.argv[0]))
source = open('E:\\source.txt','r')
sourceList = source.readlines()
print(sourceList)
aimText = open('E:\\aim.txt','w')
while(len(sourceList) != 0):
		#在列表长度范围内，随机选择一个整数
		tickLineNum = random.randint(0,len(sourceList)-1)
		#找到这个索引对应的元素，写进目标文件
		randomLine = sourceList[tickLineNum].strip()
		print(randomLine)
		aimText.write(randomLine+'\n')
		#把这个元素从列表中剔除
		sourceList.pop(tickLineNum)
aimText.close()
