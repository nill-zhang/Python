#!/usr/bin/python
# -*- coding: GBK -*-
#2012.10.13 by  sfzhang
#本脚本的作用是按照文件列表里面提供的文件路径去寻找文件，若不存在就将其路径删除
import os
import os.path
import shutil

def delEqualLine(FileDir):
	#原来的文件列表
	sourceFileDir = FileDir
	#目标文件列表
	aimFileDir = os.path.dirname(sourceFileDir)+'/new.txt'
	#打开原文件列表
	sourceFile= open(sourceFileDir,'r')
	#创建新文件列表
	aimFile = open(aimFileDir,'w')
	#将文件列表中的每个音频路径作为列表元素返回
	list1 = sourceFile.readlines()
	# list2 = sourceFile.readlines()
	list2 = []
	for eachOne in list1:
		if not eachOne in list2:
			list2.append(eachOne)
	#分别关闭打开的文件对象
	for eachLine in list2:
		aimFile.write(eachLine)
	sourceFile.close()
	aimFile.close()
	#将新得到的文件列表内容拷贝到原来的文件中去
	shutil.copyfile(aimFileDir,sourceFileDir)
	os.remove(aimFileDir)
delEqualLine('E:\\cmd300.txt')