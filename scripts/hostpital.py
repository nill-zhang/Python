#!/usr/bin/python
#-*-coding: GBK-*-
#---by sfzhang 2012.7.7---
import os
import re
import os.path
import xml.dom.minidom
import sys
def yieldCombine(txt1Dir,txt2Dir):
		#返回上个月和这个月的基础信息列表和医生--病人字典二元组
    txt1Tuple = judgeExistLineEqual(txt1Dir)
    txt2Tuple = judgeExistLineEqual(txt2Dir)
		#在月度信息文本的目录下生成合并后的表
    fCombineTxt = open(os.path.dirname(txt1Dir)+'\\'+'combine.txt','w')
    txt1List = txt1Tuple[0]
    txt1DocPatiDic = txt1Tuple[1]
    txt2DocPatiDic = txt2Tuple[1]
    txt2List = txt2Tuple[0]
    combineList = []
    for eachList in txt1List:
				#如果当前记录也在后一个的记录列表中，两条记录一样，则在合并后的列表中只要将二者病人数相加就可
        if eachList in txt2List:
            print('txt1Num: '+txt1DocPatiDic[eachList[5]]+'txt2Num: '+txt2DocPatiDic[eachList[5]])
            print('all:'+repr(int(txt1DocPatiDic[eachList[5]])+int(txt2DocPatiDic[eachList[5]])))
            combineList.append(eachList[0]+'\t'+eachList[1]+'\t'+eachList[2]+'\t'+\
            eachList[3]+'\t'+eachList[4]+'\t'+eachList[5]+'\t'+eachList[6]+'\t'+\
            repr(int(txt1DocPatiDic[eachList[5]])+int(txt2DocPatiDic[eachList[5]]))+'\n')
				#否则将当前记录写入合并后的列表
        else:
            print('txt1Num :'+repr(int(txt1DocPatiDic[eachList[5]])))
            combineList.append(eachList[0]+'\t'+eachList[1]+'\t'+eachList[2]+'\t'+\
            eachList[3]+'\t'+eachList[4]+'\t'+eachList[5]+'\t'+eachList[6]+'\t'+\
            repr(int(txt1DocPatiDic[eachList[5]]))+'\n')
		#前个月的列表写完了，接下来只要将后一个月的不在前个月列表中的记录追加到合并后的列表中
    for eachOne in txt2List:
        if not eachOne in txt1List:
            print('txt2Num :'+repr(int(txt2DocPatiDic[eachOne[5]])))
            combineList.append(eachOne[0]+'\t'+eachOne[1]+'\t'+eachOne[2]+'\t'+\
            eachOne[3]+'\t'+eachOne[4]+'\t'+eachOne[5]+'\t'+eachOne[6]+'\t'+\
            repr(int(txt2DocPatiDic[eachOne[5]]))+'\n')
    for eachLine in combineList:
        fCombineTxt.write(eachLine)
    fCombineTxt.close()
    print('两表合并完成！')
def judgeExistLineEqual(txtDir):
		#判断给的路径是否是文件
    if not os.path.isfile(txtDir):
        print('妞，你输入的文本路径'+txtDir+'不对吧，查看一下重新输入(⊙o⊙)…')
        sys.exit()
    fTxtFile = open(txtDir,'r')
    txtList = fTxtFile.readlines()
    txtDocList = []
    txtDocPatiDic = {}
    txtDocLevelDic = {}
    txtHospDocLevelDic = {}
    txtBaseInfor = []
    for o in range(0,len(txtList),1):
				#获得\t分割后的每一行的每个属性列表
        txtOneList = re.split('\t',txtList[o].strip())
        if len(txtOneList) == 8:
						#判断医生列表里是否已有这个医生
            if not txtOneList[5] in txtDocList:
								#往医生列表添加元素
                txtDocList.append(txtOneList[5])
								#往医生--病人字典添加元素
                txtDocPatiDic[txtOneList[5]] = txtOneList[7]
								#往医生--客户等级字典添加元素
                txtDocLevelDic[txtOneList[5]] = txtOneList[6]
								#往某个医院的医生--客户等级字典添加元素
                txtHospDocLevelDic[txtOneList[4]+'|'+txtOneList[5]] = txtOneList[6]
								#生成基础信息列表，列表中每个元素分别是一条记录
                txtBaseInfor.append(txtOneList[0:7])
            else:
								#已经有了这个医生了，查看这个医院的这个医生是否在医院医生--客户等级字典中
                if txtOneList[4]+'|'+txtOneList[5] in txtHospDocLevelDic.keys():
										#如果在的话，查看已经存档的这个医院的这个医生的客户等级是否与这条记录的相同
                    if txtHospDocLevelDic[txtOneList[4]+'|'+txtOneList[5]] == txtOneList[6]:
												#相同，则输出这个医院的这个医生存在相同的客户等级两条记录
                        print(os.path.basename(txtDir)+'中'+txtOneList[4]+'的'+txtOneList[5]+' 有相同的客户等级')
                    else:  
												#不同，则输出这个医院的这个医生存在不同的客户等级两条记录
                        print(os.path.basename(txtDir)+'中'+txtOneList[4]+'的'+txtOneList[5]+' 有不同的客户等级')
                #若，有这个医生，但是这个医院的这个医生还不在医院医生--客户等级字典中，说明有两家来自不同医院的相同名字的两个医生
								else:
                    print(os.path.basename(txtDir)+'中名字是：'+txtOneList[5]+' 的医生来自两家不同的医院，请确认！')
    #返回没有相同医生名字的基础信息列表和医生--病人字典
		return (txtBaseInfor,txtDocPatiDic)
def yieldDiffer(firstTxtDir,secondTxtDir):
    txt3Tuple = judgeExistLineEqual(firstTxtDir)
    txt4Tuple = judgeExistLineEqual(secondTxtDir)
    fPreTxt = open(firstTxtDir,'r')
    preMonthList = fPreTxt.readlines()
    fNextTxt = open(secondTxtDir,'r')
    nextMonthList = fNextTxt.readlines()
    nextDoctorList = []
    preDoctorList = []
    preDoctorDic = {}
    nextDoctorDic = {}
		#新建跟原来文件相对应的新的txt文件，主要os.path.splitext的使用
    fPreHaveNextNot = open(os.path.dirname(firstTxtDir)+'\\'+os.path.splitext(os.path.basename(firstTxtDir))[0]+'have.txt','w')
    fNextHavePreNot = open(os.path.dirname(firstTxtDir)+'\\'+os.path.splitext(os.path.basename(secondTxtDir))[0]+'have.txt','w')
    fLevelChange = open(os.path.dirname(firstTxtDir)+'\\'+'levelChange.txt','w')
    fLevelNotChange = open(os.path.dirname(firstTxtDir)+'\\'+'levelNotChange.txt','w')
		#对记录进行处理，把每条记录里的医生都保存成医生列表，把来自哪个医院的哪个医生保存成医院医生--客户等级字典
    for i in range(0,len(preMonthList),1):
        preOneList = re.split('\t',preMonthList[i].strip())
        if len(preOneList) == 8:
            preDoctorList.append(preOneList[5])
            if (preOneList[4]+'|'+preOneList[5]) in preDoctorDic.keys():
                print('前一个月份中有同一家医院的同一个医生，是：'+preOneList[4]+'的'+preOneList[5])
            else:
                preDoctorDic[preOneList[4]+'|'+preOneList[5]] = preOneList[6]
    for j in range(0,len(nextMonthList),1):
        nextOneList = re.split('\t',nextMonthList[j].strip())
        if len(nextOneList) == 8:
            nextDoctorList.append(nextOneList[5])
            if (nextOneList[4]+'|'+nextOneList[5]) in nextDoctorDic.keys():
                print('后一个月份中有同一家医院的同一个医生，是：'+nextOneList[4]+'的'+nextOneList[5])
            else:
                nextDoctorDic[nextOneList[4]+'|'+nextOneList[5]] = nextOneList[6]
            # if nextOneList[5] in nextDoctorDic.keys():
                # print('7月份中有医生的有相同的名字，只处理了一个，名字是：'+nextOneList[5])
            # else:
                # nextDoctorDic[nextOneList[5]] = nextOneList[6]
		#针对前一个月份的医院医生，判断他是否在后一个月的医院医生字典里，如果不在，那么前个月有，后面一个月没有的记录列表也会生成
    for l in range(0,len(preMonthList),1):
        preOneLineList = re.split('\t',preMonthList[l].strip())
        if len(preOneLineList) == 8:
            if not (preOneLineList[4]+'|'+preOneLineList[5]) in nextDoctorDic.keys():
                fPreHaveNextNot.write(preMonthList[l])
    fPreHaveNextNot.close()
    print('前一个月份有，而后一个月份没有的医生列表已经生成 '+os.path.splitext(os.path.basename(firstTxtDir))[0]+'have.txt!')
    #
		for m in range(0,len(nextMonthList),1):
        
				nextOneLineList = re.split('\t',nextMonthList[m].strip())
        if len(nextOneLineList) == 8:
						#判断后一个月的X医院X医生是否在前一个月的医院医生--客户等级字典里
            if not (nextOneLineList[4]+'|'+nextOneLineList[5]) in preDoctorDic.keys():
                fNextHavePreNot.write(nextMonthList[m])
						#如果在，判断X医院X医生的客户等级是否相等，如果不等，说明客户等级发生了变化
            elif preDoctorDic[nextOneLineList[4]+'|'+nextOneLineList[5]]!= nextOneLineList[6] :
                fLevelChange.write(nextOneLineList[0]+'\t'+nextOneLineList[1]+'\t'+\
                nextOneLineList[2]+'\t'+nextOneLineList[3]+'\t'+nextOneLineList[4]+'\t'+nextOneLineList[5]+'\t'+\
                preDoctorDic[nextOneLineList[4]+'|'+nextOneLineList[5]]+'\t'+nextOneLineList[6]+'\t'+nextOneLineList[7]+'\n')
            #如果在，并且客户等级相等的话，客户等级没有变化列表生成
						else:
                fLevelNotChange.write(nextOneLineList[0]+'\t'+nextOneLineList[1]+'\t'+\
                nextOneLineList[2]+'\t'+nextOneLineList[3]+'\t'+nextOneLineList[4]+'\t'+nextOneLineList[5]+'\t'+\
                preDoctorDic[nextOneLineList[4]+'|'+nextOneLineList[5]]+'\t'+nextOneLineList[6]+'\t'+nextOneLineList[7]+'\n')
    print('后一个月份有，而前一个月份没有的医生列表已经生成 '+os.path.splitext(os.path.basename(secondTxtDir))[0]+'have.txt!')
    fNextHavePreNot.close()
    print('两个月份都有，医生的客户等级 没有 发生变化列表已经生成，levelNotchange.txt!')
    fLevelNotChange.close()
    print('两个月份都有，医生的客户等级 已经 发生变化列表已经生成，levelchange.txt!')
    fLevelChange.close()
def help():
    print('*********************************工具使用方法***********************************')
    print('*---------- yxl.exe firstMonthTxtDirectory secondMonthTxtDiretory -------------*')
    print('* firstMonthTxtDirectory  :前一个月excel数据的Txt文件路径，如 E:\羊雪莲\\6.txt*')
    print('* secondMonthTxtDirectory :后一个月excel数据的Txt文件路径，如 E:\羊雪莲\\7.txt*')
    print('********************************************************************************')
if __name__ == '__main__':
    sys.argv = ['a','E:\\8.txt','E:\\9.txt']
    if len(sys.argv) != 3:
        print('输入参数个数有误，工具需要两个参数，请按照工具使用方法使用！')
        help()
        sys.exit()
    tag = input('你是想将两个不同月份的表进行合并吗？Y\n你是想生成两个表的医生客户等级发生变化的表吗 N')
    while not tag in ('Y','N'):
        print('输入错误，请重新输入！！')
        tag = input('将两个不同月份的表合并请输入 Y 并回车 \n想筛选出两个表中的医生客户等级发生变化的数据请输入 N 并回车')
    if tag == 'Y':
        yieldCombine(sys.argv[1].strip(),sys.argv[2].strip())
    else :
        yieldDiffer(sys.argv[1].strip(),sys.argv[2].strip())
