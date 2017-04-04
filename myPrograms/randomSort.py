# !/usr/bin/python
# -*-coding: GBK-*-
# ---by sfzhang  2011.6.10---
import os
import os.path
import sys
import random


def main():
    # ���ű�����Ŀ¼����Ϊ��ǰĿ¼
    print(sys.argv[0])
    os.chdir(os.path.dirname(sys.argv[0]))
    source = open('E:\\source.txt', 'r')
    sourceList = source.readlines()
    print(sourceList)
    aimText = open('E:\\aim.txt', 'w')
    while (len(sourceList) != 0):
        # ���б��ȷ�Χ�ڣ����ѡ��һ������
        tickLineNum = random.randint(0, len(sourceList) - 1)
        # �ҵ����������Ӧ��Ԫ�أ�д��Ŀ���ļ�
        randomLine = sourceList[tickLineNum].strip()
        print(randomLine)
        aimText.write(randomLine + '\n')
        # �����Ԫ�ش��б����޳�
        sourceList.pop(tickLineNum)
    aimText.close()


if __name__ == "__main__":
    main()