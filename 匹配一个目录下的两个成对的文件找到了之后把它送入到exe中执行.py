#!/usr/bin/python
# -*- coding: UTF-8 -*-
#2011.2.31 by sfzhang
import os
import re
import os.path
#返回effect文件夹下所有文件列表
fileList = os.listdir('D:/work/python/effect')
desDir= 'D:/work/python/EffectResult'
os.chdir('D:/work/aiet')
for everyline in fileList:
    print(everyline)
	#定义正则表达式，依次匹配每个文件
    patternTxt = '.+\.txt'
    txtFile = re.match(patternTxt,everyline)
    if not txtFile:
	            #当前文件不是txt文件返回匹配失败信息
                print('txtFile pattern match failed')
    else:       
	            #匹配文本文件成功，定义正则表达式
                patternPaper = '(.+?_)paper.txt'
				#匹配txt文件名是否以paper结尾
                rePaper = re.match(patternPaper,everyline)
                if not rePaper:
				        #匹配失败，txt文件不是以paper结尾
                        print('paperTxt pattern match failed')
                else:   
				        #匹配成功，是以paper结尾的文本文件
						#判断EffectResult文件夹是否存在，不存在就新建此文件夹
                        if os.path.exists(desDir):
                                os.chdir(desDir)
                        else:
                                os.makedirs(desDir)
						#遍历文件列表
                        for eachline in fileList:
						        #设置正则表达式，匹配和题型的评测文本相对应的音频信息文本
                                patternWave = rePaper.group(1)+'wave.txt'
								#对当前文件进行匹配
                                reWave = re.match(patternWave,eachline)
                                if not reWave:
								        #评测文本不对应
                                        print('waveTxt pattern match failed')
                                else:   
								        #当前文件是和评测文本对应的音频信息文本
										#设置离线测试工具目录
                                        tool='D:/work/aiet/OfflineBatchTest.exe'
										#将目录和评测文本文件名进行连结，作为paper.txt的路径
                                        paperList = ' D:/work/python/effect/'+rePaper.group()
										#将目录和音频信息文件名进行连结，作为wave.txt的路径
                                        waveList =  ' D:/work/python/effect/'+reWave.group()
										#设置和评测文本以及音频信息文本相一致的评测结果文件名
                                        resultDir = desDir+'/'+rePaper.group(1)+'result.txt'
										#调用离线测试工具进行评测
                                        cmd = (tool+paperList+waveList+' '+resultDir)
                                        os.system(cmd)
  