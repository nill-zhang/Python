#!/usr/bin/python
# -*- coding: GBK -*-
#2011.10.13 by  sfzhang
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
	for eachOne in fileList:
		if not os.path.exists(eachOne.strip()):
			print(eachOne.strip())
			del eachOne
	# #�ֱ�رմ򿪵��ļ�����
	sourceFile.close()
	aimFile.close()
	#���µõ����ļ��б����ݿ�����ԭ�����ļ���ȥ
	shutil.copyfile(aimFileDir,sourceFileDir)
	os.remove(aimFileDir)
#delNotExistFile('W:/test_work/AiET/3.1/teat/steady/blurRec/paramTxt/FuzzyWave.txt')
#delNotExistFile('D:/Wave.txt')
delNotExistFile('D:\work\python\�����б�\WaveList.txt')
