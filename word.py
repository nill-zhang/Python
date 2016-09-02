#!/usr/bin/python
# -*- coding: GBK -*-
#2011.9.1 by  sfzhang
import os
import re
def wordCompute(result,mark):
	bothWrong = 0
	machWrong = 0
	humanWrong = 0
	wordResult = open(result,'r')
	humanMark = open(mark,'r')
	wordResultList = wordResult.readlines()
	#humanScoreLine = humanMark.readline()
	for eachLine in wordResultList:
		humanScoreLine = humanMark.readline()
		if (eachLine.strip() != '') & (humanScoreLine !=''):
			wordScoreItem = re.split(',',eachLine)
			if len(wordScoreItem) == 4:
				if wordScoreItem[2].strip() =='{SUCCESS}':
					#wordScoreList = re.split(',',wordScoreItem[3])
					wordScore = int(re.sub('{|}','',wordScoreItem[3]))
					if wordScore in (0,1,2,3,4,5,6,7):
						if wordScore !=0 :
							machWrong = machWrong+1
						humanScoreItem = re.split('\t',humanScoreLine)
						if int(humanScoreItem[1].strip()) in (1,3):
							humanScore = int(humanScoreItem[1].strip())
							if humanScore == 1:
								humanWrong = humanWrong+1
							qu = re.sub('{|}','',wordScoreItem[1])
							t = os.path.basename(qu)
							audio = re.sub('\.pcm|\.wav','',t)
							if audio.strip() == humanScoreItem[0].strip():
								if (wordScore !=0) & (humanScore == 1):
									bothWrong = bothWrong+1
	print('机器检出错的个数 ： '+repr(machWrong))
	print('人工检出错的个数 ： '+repr(humanWrong))
	print('机器和人工都检出错的个数 ： '+repr(bothWrong))
	print('单词检错的正确率即错误一致率为 ： '+repr(bothWrong/machWrong))
	print('单词检错的召回率为 ： '+repr(bothWrong/humanWrong))
	return[bothWrong/machWrong,bothWrong/humanWrong]

def wordRate(t):
	A1=wordCompute('D:/AiET/test/func/ReadWordExpert1Active.log','D:/AiET/test/func/effectResult/expert1.txt')
	A2=wordCompute('D:/AiET/test/func/ReadWordExpert2Active.log','D:/AiET/test/func/effectResult/expert2.txt')
	P1=wordCompute('D:/AiET/test/func/ReadWordExpert1Precise.log','D:/AiET/test/func/effectResult/expert1.txt')
	P2=wordCompute('D:/AiET/test/func/ReadWordExpert2Precise.log','D:/AiET/test/func/effectResult/expert2.txt')
	S1=wordCompute('D:/AiET/test/func/ReadWordExpert1Strict.log','D:/AiET/test/func/effectResult/expert1.txt')
	S2=wordCompute('D:/AiET/test/func/ReadWordExpert2Strict.log','D:/AiET/test/func/effectResult/expert2.txt')
	t.write('单词检错**松门限**的专家1正确率为 ： '+repr(A1[0])+'\n')
	t.write('单词检错**松门限**的专家1召回率为 ： '+repr(A1[1])+'\n')
	t.write('单词检错**松门限**的专家2正确率为 ： '+repr(A2[0])+'\n')
	t.write('单词检错**松门限**的专家2召回率为 ： '+repr(A2[1])+'\n')
	t.write('单词检错--较松门限--的专家1正确率为 ： '+repr(P1[0])+'\n')
	t.write('单词检错--较松门限--的专家1召回率为 ： '+repr(P1[1])+'\n')
	t.write('单词检错--较松门限--的专家2正确率为 ： '+repr(P2[0])+'\n')
	t.write('单词检错--较松门限--的专家2召回率为 ： '+repr(P2[1])+'\n')
	t.write('单词检错~~严门限~~的专家1正确率为 ： '+repr(S1[0])+'\n')
	t.write('单词检错~~严门限~~的专家1召回率为 ： '+repr(S1[1])+'\n')
	t.write('单词检错~~严门限~~的专家2正确率为 ： '+repr(S2[0])+'\n')
	t.write('单词检错~~严门限~~的专家2召回率为 ： '+repr(S2[1])+'\n')

