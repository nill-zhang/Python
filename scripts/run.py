#!/usr/bin/python

import os

#os.system("offline_eva2_16K.exe -t score_paper.txt -l score_list.txt -r result/AiET30_16K_result.txt --pcm_rate=16 --code=0 --responstime=20 --speech-time=10 ")
#os.system("offline_eva2_8K.exe -t score_paper.txt -l score_list.txt -r result/AiET30_8K_result.txt --pcm_rate=16 --code=0 --responstime=20 --speech-time=10 ")

os.system("offline_eva2_8K.exe -t ./3.0与原型对比/hard.txt -l ./3.0与原型对比/hardlist.txt -r ./3.0与原型对比/AiET30_8K_result.txt --pcm_rate=16 --code=0 --responstime=20 --speech-time=10")
os.system("offline_eva2_16K.exe -t ./3.0与原型对比/hard.txt -l ./3.0与原型对比/hardlist.txt -r ./3.0与原型对比/AiET30_16K_result.txt --pcm_rate=16 --code=0 --responstime=20 --speech-time=10")
