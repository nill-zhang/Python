#!/usr/bin/python
# -*- coding: UTF-8 -*-
#2011.2.31 by sfzhang
import os
import re
import os.path
#����effect�ļ����������ļ��б�
fileList = os.listdir('D:/work/python/effect')
desDir= 'D:/work/python/EffectResult'
os.chdir('D:/work/aiet')
for everyline in fileList:
    print(everyline)
	#����������ʽ������ƥ��ÿ���ļ�
    patternTxt = '.+\.txt'
    txtFile = re.match(patternTxt,everyline)
    if not txtFile:
	            #��ǰ�ļ�����txt�ļ�����ƥ��ʧ����Ϣ
                print('txtFile pattern match failed')
    else:       
	            #ƥ���ı��ļ��ɹ�������������ʽ
                patternPaper = '(.+?_)paper.txt'
				#ƥ��txt�ļ����Ƿ���paper��β
                rePaper = re.match(patternPaper,everyline)
                if not rePaper:
				        #ƥ��ʧ�ܣ�txt�ļ�������paper��β
                        print('paperTxt pattern match failed')
                else:   
				        #ƥ��ɹ�������paper��β���ı��ļ�
						#�ж�EffectResult�ļ����Ƿ���ڣ������ھ��½����ļ���
                        if os.path.exists(desDir):
                                os.chdir(desDir)
                        else:
                                os.makedirs(desDir)
						#�����ļ��б�
                        for eachline in fileList:
						        #����������ʽ��ƥ������͵������ı����Ӧ����Ƶ��Ϣ�ı�
                                patternWave = rePaper.group(1)+'wave.txt'
								#�Ե�ǰ�ļ�����ƥ��
                                reWave = re.match(patternWave,eachline)
                                if not reWave:
								        #�����ı�����Ӧ
                                        print('waveTxt pattern match failed')
                                else:   
								        #��ǰ�ļ��Ǻ������ı���Ӧ����Ƶ��Ϣ�ı�
										#�������߲��Թ���Ŀ¼
                                        tool='D:/work/aiet/OfflineBatchTest.exe'
										#��Ŀ¼�������ı��ļ����������ᣬ��Ϊpaper.txt��·��
                                        paperList = ' D:/work/python/effect/'+rePaper.group()
										#��Ŀ¼����Ƶ��Ϣ�ļ����������ᣬ��Ϊwave.txt��·��
                                        waveList =  ' D:/work/python/effect/'+reWave.group()
										#���ú������ı��Լ���Ƶ��Ϣ�ı���һ�µ��������ļ���
                                        resultDir = desDir+'/'+rePaper.group(1)+'result.txt'
										#�������߲��Թ��߽�������
                                        cmd = (tool+paperList+waveList+' '+resultDir)
                                        os.system(cmd)
  