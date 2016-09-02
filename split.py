#!/usr/bin/python
# -*- coding: UTF-8 -*-
#2011.11.8 sfzhang
import os
import re
import os.path
sourceDirList =['W:/test_work/AiET/3.1/test/effect/tosplit','W:/test_work/AiET/3.1/test/effect/900english']
for i in range(0,2,1):
	fileList = os.listdir(sourceDirList[i])
	desDir = 'W:/test_work/AiET/3.1/test/effect/input'
	if not os.path.exists(desDir):
		os.makedirs(desDir)
	for everyline in fileList:
		patternTxt = '(\w+)\.txt'
		txtFile = re.match(patternTxt,everyline)
		print(everyline)
		if not txtFile :
			print('pattern match failed')
		else:
			all = sourceDirList[i]+'/'+txtFile.group()
			f = open(all,'r')
			paper = open(desDir+'/'+txtFile.group(1)+'_paper.txt','w')
			wave = open(desDir+'/'+txtFile.group(1)+'_wave.txt','w')
			for eachline in f.readlines():
				pattern = '(.+?0\t)(.+\n)'
				m = re.match(pattern,eachline)
				paper.write(m.group(1).strip()+'\n')
				wave.write(m.group(2))
			paper.close()
			wave.close()
