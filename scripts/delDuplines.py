#!/usr/bin/python
# -*- coding: GBK -*-
#2012.10.13 by  sfzhang
#���ű��������ǰ����ļ��б������ṩ���ļ�·��ȥѰ���ļ����������ھͽ���·��ɾ��
import os
import os.path
import shutil

def delEqualLine(FileDir):
	#ԭ�����ļ��б�
	sourceFileDir = FileDir
	#Ŀ���ļ��б�
	aimFileDir = os.path.dirname(sourceFileDir)+'/new.txt'
	#��ԭ�ļ��б�
	sourceFile= open(sourceFileDir,'r')
	#�������ļ��б�
	aimFile = open(aimFileDir,'w')
	#���ļ��б��е�ÿ����Ƶ·����Ϊ�б�Ԫ�ط���
	list1 = sourceFile.readlines()
	# list2 = sourceFile.readlines()
	list2 = []
	for eachOne in list1:
		if not eachOne in list2:
			list2.append(eachOne)
	#�ֱ�رմ򿪵��ļ�����
	for eachLine in list2:
		aimFile.write(eachLine)
	sourceFile.close()
	aimFile.close()
	#���µõ����ļ��б����ݿ�����ԭ�����ļ���ȥ
	shutil.copyfile(aimFileDir,sourceFileDir)
	os.remove(aimFileDir)
delEqualLine('E:\\cmd300.txt')