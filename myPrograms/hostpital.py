#!/usr/bin/python
#-*-coding: GBK-*-
#---by sfzhang 2012.7.7---
import os
import re
import os.path
import xml.dom.minidom
import sys
def yieldCombine(txt1Dir,txt2Dir):
		#�����ϸ��º�����µĻ�����Ϣ�б��ҽ��--�����ֵ��Ԫ��
    txt1Tuple = judgeExistLineEqual(txt1Dir)
    txt2Tuple = judgeExistLineEqual(txt2Dir)
		#���¶���Ϣ�ı���Ŀ¼�����ɺϲ���ı�
    fCombineTxt = open(os.path.dirname(txt1Dir)+'\\'+'combine.txt','w')
    txt1List = txt1Tuple[0]
    txt1DocPatiDic = txt1Tuple[1]
    txt2DocPatiDic = txt2Tuple[1]
    txt2List = txt2Tuple[0]
    combineList = []
    for eachList in txt1List:
				#�����ǰ��¼Ҳ�ں�һ���ļ�¼�б��У�������¼һ�������ںϲ�����б���ֻҪ�����߲�������ӾͿ�
        if eachList in txt2List:
            print('txt1Num: '+txt1DocPatiDic[eachList[5]]+'txt2Num: '+txt2DocPatiDic[eachList[5]])
            print('all:'+repr(int(txt1DocPatiDic[eachList[5]])+int(txt2DocPatiDic[eachList[5]])))
            combineList.append(eachList[0]+'\t'+eachList[1]+'\t'+eachList[2]+'\t'+\
            eachList[3]+'\t'+eachList[4]+'\t'+eachList[5]+'\t'+eachList[6]+'\t'+\
            repr(int(txt1DocPatiDic[eachList[5]])+int(txt2DocPatiDic[eachList[5]]))+'\n')
				#���򽫵�ǰ��¼д��ϲ�����б�
        else:
            print('txt1Num :'+repr(int(txt1DocPatiDic[eachList[5]])))
            combineList.append(eachList[0]+'\t'+eachList[1]+'\t'+eachList[2]+'\t'+\
            eachList[3]+'\t'+eachList[4]+'\t'+eachList[5]+'\t'+eachList[6]+'\t'+\
            repr(int(txt1DocPatiDic[eachList[5]]))+'\n')
		#ǰ���µ��б�д���ˣ�������ֻҪ����һ���µĲ���ǰ�����б��еļ�¼׷�ӵ��ϲ�����б���
    for eachOne in txt2List:
        if not eachOne in txt1List:
            print('txt2Num :'+repr(int(txt2DocPatiDic[eachOne[5]])))
            combineList.append(eachOne[0]+'\t'+eachOne[1]+'\t'+eachOne[2]+'\t'+\
            eachOne[3]+'\t'+eachOne[4]+'\t'+eachOne[5]+'\t'+eachOne[6]+'\t'+\
            repr(int(txt2DocPatiDic[eachOne[5]]))+'\n')
    for eachLine in combineList:
        fCombineTxt.write(eachLine)
    fCombineTxt.close()
    print('����ϲ���ɣ�')
def judgeExistLineEqual(txtDir):
		#�жϸ���·���Ƿ����ļ�
    if not os.path.isfile(txtDir):
        print('椣���������ı�·��'+txtDir+'���԰ɣ��鿴һ����������(��o��)��')
        sys.exit()
    fTxtFile = open(txtDir,'r')
    txtList = fTxtFile.readlines()
    txtDocList = []
    txtDocPatiDic = {}
    txtDocLevelDic = {}
    txtHospDocLevelDic = {}
    txtBaseInfor = []
    for o in range(0,len(txtList),1):
				#���\t�ָ���ÿһ�е�ÿ�������б�
        txtOneList = re.split('\t',txtList[o].strip())
        if len(txtOneList) == 8:
						#�ж�ҽ���б����Ƿ��������ҽ��
            if not txtOneList[5] in txtDocList:
								#��ҽ���б����Ԫ��
                txtDocList.append(txtOneList[5])
								#��ҽ��--�����ֵ����Ԫ��
                txtDocPatiDic[txtOneList[5]] = txtOneList[7]
								#��ҽ��--�ͻ��ȼ��ֵ����Ԫ��
                txtDocLevelDic[txtOneList[5]] = txtOneList[6]
								#��ĳ��ҽԺ��ҽ��--�ͻ��ȼ��ֵ����Ԫ��
                txtHospDocLevelDic[txtOneList[4]+'|'+txtOneList[5]] = txtOneList[6]
								#���ɻ�����Ϣ�б��б���ÿ��Ԫ�طֱ���һ����¼
                txtBaseInfor.append(txtOneList[0:7])
            else:
								#�Ѿ��������ҽ���ˣ��鿴���ҽԺ�����ҽ���Ƿ���ҽԺҽ��--�ͻ��ȼ��ֵ���
                if txtOneList[4]+'|'+txtOneList[5] in txtHospDocLevelDic.keys():
										#����ڵĻ����鿴�Ѿ��浵�����ҽԺ�����ҽ���Ŀͻ��ȼ��Ƿ���������¼����ͬ
                    if txtHospDocLevelDic[txtOneList[4]+'|'+txtOneList[5]] == txtOneList[6]:
												#��ͬ����������ҽԺ�����ҽ��������ͬ�Ŀͻ��ȼ�������¼
                        print(os.path.basename(txtDir)+'��'+txtOneList[4]+'��'+txtOneList[5]+' ����ͬ�Ŀͻ��ȼ�')
                    else:  
												#��ͬ����������ҽԺ�����ҽ�����ڲ�ͬ�Ŀͻ��ȼ�������¼
                        print(os.path.basename(txtDir)+'��'+txtOneList[4]+'��'+txtOneList[5]+' �в�ͬ�Ŀͻ��ȼ�')
                #���������ҽ�����������ҽԺ�����ҽ��������ҽԺҽ��--�ͻ��ȼ��ֵ��У�˵�����������Բ�ͬҽԺ����ͬ���ֵ�����ҽ��
								else:
                    print(os.path.basename(txtDir)+'�������ǣ�'+txtOneList[5]+' ��ҽ���������Ҳ�ͬ��ҽԺ����ȷ�ϣ�')
    #����û����ͬҽ�����ֵĻ�����Ϣ�б��ҽ��--�����ֵ�
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
		#�½���ԭ���ļ����Ӧ���µ�txt�ļ�����Ҫos.path.splitext��ʹ��
    fPreHaveNextNot = open(os.path.dirname(firstTxtDir)+'\\'+os.path.splitext(os.path.basename(firstTxtDir))[0]+'have.txt','w')
    fNextHavePreNot = open(os.path.dirname(firstTxtDir)+'\\'+os.path.splitext(os.path.basename(secondTxtDir))[0]+'have.txt','w')
    fLevelChange = open(os.path.dirname(firstTxtDir)+'\\'+'levelChange.txt','w')
    fLevelNotChange = open(os.path.dirname(firstTxtDir)+'\\'+'levelNotChange.txt','w')
		#�Լ�¼���д�����ÿ����¼���ҽ���������ҽ���б��������ĸ�ҽԺ���ĸ�ҽ�������ҽԺҽ��--�ͻ��ȼ��ֵ�
    for i in range(0,len(preMonthList),1):
        preOneList = re.split('\t',preMonthList[i].strip())
        if len(preOneList) == 8:
            preDoctorList.append(preOneList[5])
            if (preOneList[4]+'|'+preOneList[5]) in preDoctorDic.keys():
                print('ǰһ���·�����ͬһ��ҽԺ��ͬһ��ҽ�����ǣ�'+preOneList[4]+'��'+preOneList[5])
            else:
                preDoctorDic[preOneList[4]+'|'+preOneList[5]] = preOneList[6]
    for j in range(0,len(nextMonthList),1):
        nextOneList = re.split('\t',nextMonthList[j].strip())
        if len(nextOneList) == 8:
            nextDoctorList.append(nextOneList[5])
            if (nextOneList[4]+'|'+nextOneList[5]) in nextDoctorDic.keys():
                print('��һ���·�����ͬһ��ҽԺ��ͬһ��ҽ�����ǣ�'+nextOneList[4]+'��'+nextOneList[5])
            else:
                nextDoctorDic[nextOneList[4]+'|'+nextOneList[5]] = nextOneList[6]
            # if nextOneList[5] in nextDoctorDic.keys():
                # print('7�·�����ҽ��������ͬ�����֣�ֻ������һ���������ǣ�'+nextOneList[5])
            # else:
                # nextDoctorDic[nextOneList[5]] = nextOneList[6]
		#���ǰһ���·ݵ�ҽԺҽ�����ж����Ƿ��ں�һ���µ�ҽԺҽ���ֵ��������ڣ���ôǰ�����У�����һ����û�еļ�¼�б�Ҳ������
    for l in range(0,len(preMonthList),1):
        preOneLineList = re.split('\t',preMonthList[l].strip())
        if len(preOneLineList) == 8:
            if not (preOneLineList[4]+'|'+preOneLineList[5]) in nextDoctorDic.keys():
                fPreHaveNextNot.write(preMonthList[l])
    fPreHaveNextNot.close()
    print('ǰһ���·��У�����һ���·�û�е�ҽ���б��Ѿ����� '+os.path.splitext(os.path.basename(firstTxtDir))[0]+'have.txt!')
    #
		for m in range(0,len(nextMonthList),1):
        
				nextOneLineList = re.split('\t',nextMonthList[m].strip())
        if len(nextOneLineList) == 8:
						#�жϺ�һ���µ�XҽԺXҽ���Ƿ���ǰһ���µ�ҽԺҽ��--�ͻ��ȼ��ֵ���
            if not (nextOneLineList[4]+'|'+nextOneLineList[5]) in preDoctorDic.keys():
                fNextHavePreNot.write(nextMonthList[m])
						#����ڣ��ж�XҽԺXҽ���Ŀͻ��ȼ��Ƿ���ȣ�������ȣ�˵���ͻ��ȼ������˱仯
            elif preDoctorDic[nextOneLineList[4]+'|'+nextOneLineList[5]]!= nextOneLineList[6] :
                fLevelChange.write(nextOneLineList[0]+'\t'+nextOneLineList[1]+'\t'+\
                nextOneLineList[2]+'\t'+nextOneLineList[3]+'\t'+nextOneLineList[4]+'\t'+nextOneLineList[5]+'\t'+\
                preDoctorDic[nextOneLineList[4]+'|'+nextOneLineList[5]]+'\t'+nextOneLineList[6]+'\t'+nextOneLineList[7]+'\n')
            #����ڣ����ҿͻ��ȼ���ȵĻ����ͻ��ȼ�û�б仯�б�����
						else:
                fLevelNotChange.write(nextOneLineList[0]+'\t'+nextOneLineList[1]+'\t'+\
                nextOneLineList[2]+'\t'+nextOneLineList[3]+'\t'+nextOneLineList[4]+'\t'+nextOneLineList[5]+'\t'+\
                preDoctorDic[nextOneLineList[4]+'|'+nextOneLineList[5]]+'\t'+nextOneLineList[6]+'\t'+nextOneLineList[7]+'\n')
    print('��һ���·��У���ǰһ���·�û�е�ҽ���б��Ѿ����� '+os.path.splitext(os.path.basename(secondTxtDir))[0]+'have.txt!')
    fNextHavePreNot.close()
    print('�����·ݶ��У�ҽ���Ŀͻ��ȼ� û�� �����仯�б��Ѿ����ɣ�levelNotchange.txt!')
    fLevelNotChange.close()
    print('�����·ݶ��У�ҽ���Ŀͻ��ȼ� �Ѿ� �����仯�б��Ѿ����ɣ�levelchange.txt!')
    fLevelChange.close()
def help():
    print('*********************************����ʹ�÷���***********************************')
    print('*---------- yxl.exe firstMonthTxtDirectory secondMonthTxtDiretory -------------*')
    print('* firstMonthTxtDirectory  :ǰһ����excel���ݵ�Txt�ļ�·������ E:\��ѩ��\\6.txt*')
    print('* secondMonthTxtDirectory :��һ����excel���ݵ�Txt�ļ�·������ E:\��ѩ��\\7.txt*')
    print('********************************************************************************')
if __name__ == '__main__':
    sys.argv = ['a','E:\\8.txt','E:\\9.txt']
    if len(sys.argv) != 3:
        print('��������������󣬹�����Ҫ�����������밴�չ���ʹ�÷���ʹ�ã�')
        help()
        sys.exit()
    tag = input('�����뽫������ͬ�·ݵı���кϲ���Y\n�����������������ҽ���ͻ��ȼ������仯�ı��� N')
    while not tag in ('Y','N'):
        print('����������������룡��')
        tag = input('��������ͬ�·ݵı�ϲ������� Y ���س� \n��ɸѡ���������е�ҽ���ͻ��ȼ������仯������������ N ���س�')
    if tag == 'Y':
        yieldCombine(sys.argv[1].strip(),sys.argv[2].strip())
    else :
        yieldDiffer(sys.argv[1].strip(),sys.argv[2].strip())
