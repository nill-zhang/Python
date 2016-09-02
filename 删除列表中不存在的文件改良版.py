#!/usr/bin/python
# -*- coding: GBK -*-
#2011.10.13 by  sfzhang
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
	for eachOne in fileList:
		if not os.path.exists(eachOne.strip()):
			print(eachOne.strip())
			del eachOne
	# #分别关闭打开的文件对象
	sourceFile.close()
	aimFile.close()
	#将新得到的文件列表内容拷贝到原来的文件中去
	shutil.copyfile(aimFileDir,sourceFileDir)
	os.remove(aimFileDir)
#delNotExistFile('W:/test_work/AiET/3.1/teat/steady/blurRec/paramTxt/FuzzyWave.txt')
#delNotExistFile('D:/Wave.txt')
delNotExistFile('D:\work\python\参数列表\WaveList.txt')
