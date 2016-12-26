#!/usr/bin/python
# -*- coding: GBK -*-
#2011.9.13 by  sfzhang
'''将一个list文件中的空和非空文件拉出来单独存放'''
import os
t =open('E:/POI0510.scp','r')
empty = open('E:/empty.txt','w')
notEmpty = open('E:/notEmpty.txt','w')
for eachline in t.readlines():
	s = eachline.strip()
	if s != '':
		if os.path.isfile(s):
			size = os.path.getsize(s)
			if size ==0:
				empty.write(s+'\n')
			else:
				notEmpty.write(s+'\n')
t.close()
empty.close()
notEmpty.close()