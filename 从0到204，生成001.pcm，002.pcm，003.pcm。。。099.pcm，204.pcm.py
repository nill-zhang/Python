#!/usr/bin/python
#-*-coding: GBK-*-
#---by sfzhang  2011.8.3---
import os
import re
import os.path
import shutil
import sys
import code
import random
b = []
c = open('D:\\python\\204.txt','w')
for i in range(1,205,1):
		if i>99:
				c.write(repr(i)+'.pcm'+'\n')
		elif 9 <i< 100:
				c.write('0'+repr(i)+'.pcm'+'\n')
		else:
				c.write('00'+repr(i)+'.pcm'+'\n')
c.close()