#!/usr/bin/python
#-*-coding: GBK-*-
#---by sfzhang  2011.6.10---
'''将一行音标一行标注的scp文件分割成pcmlist.txt和answer.txt'''
import os
import re
import os.path
import shutil
import sys
import code
print(sys.argv[0])
os.chdir(os.path.dirname(sys.argv[0]))
f = open('StudentTestPcmListOriginal.scp','r')
l = open('pcmlist.txt','w')
r = open('answer.txt','w')
t= f.readlines()
for i in range(0,len(t),2):
        l.write(t[i].strip()+'\n')
        r.write(t[i+1].strip()+'\n')
f.close()
l.close()
r.close()