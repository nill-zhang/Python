#!/usr/bin/python
# -*- coding: GBK -*-
#2012.4.13 by  sfzhang ����Ƶ�ļ��б���ںͲ����ڵ���Ƶ�ֿ�
import os
import shutil
t =open('F:/wave.txt','r')
exist = open('F:/exist.txt','w')
notExist = open('F:/notExist.txt','w')
for eachline in t.readlines():
	s = eachline.strip()
	if s != '':
		if os.path.exists(s):
			exist.write(s+'\n')
		else:
			notExist.write(s+'\n')
t.close()
exist.close()
notExist.close()
shutil.copyfile('F:/exist.txt','F:/wave.txt')
os.remove('F:/Exist.txt')
