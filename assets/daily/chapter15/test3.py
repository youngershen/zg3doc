# Project: ZG3Doc
# File : test3.py
# Date : 2023/4/14 10:20
# Author: Younger Shen <申延刚>
# Web: https://github.com/youngershen
# Cell: 13811754531
# Wechat: 13811754531
# Email : shenyangang@163.com
import jieba
import math
s1 = '我喜欢看电视，不喜欢看电影。'
s1_cut = [i for i in jieba.cut(s1, cut_all=True) if i != '']
s2 = '我不喜欢看电视，也不喜欢看电影。'
s2_cut = [i for i in jieba.cut(s2, cut_all=True) if i != '']
s3 = '我不喜欢看电视，喜欢看电影。'
s3_cut = [i for i in jieba.cut(s3, cut_all=True) if i != '']
s4 = '我喜欢看电视，也喜欢看电影。'
s4_cut = [i for i in jieba.cut(s4, cut_all=True) if i != '']
word_set = set(s1_cut).union(set(s2_cut)).union(set(s3_cut)).union(set(s4_cut))
print(word_set)

word_dict = dict()
i = 0
for word in word_set:
    word_dict[word] = i
    i += 1
print(word_dict)

s1_cut_code = [word_dict[word] for word in s1_cut]
print(s1_cut_code)
s1_cut_code = [0]*len(word_dict)

for word in s1_cut:
    s1_cut_code[word_dict[word]]+=1
print(s1_cut_code)

s2_cut_code = [word_dict[word] for word in s2_cut]
print(s2_cut_code)
s2_cut_code = [0]*len(word_dict)
for word in s2_cut:
    s2_cut_code[word_dict[word]]+=1
print(s2_cut_code)

s3_cut_code = [word_dict[word] for word in s3_cut]
print(s3_cut_code)
s3_cut_code = [0]*len(word_dict)
for word in s3_cut:
    s3_cut_code[word_dict[word]]+=1
print(s3_cut_code)

s4_cut_code = [word_dict[word] for word in s4_cut]
print(s4_cut_code)
s4_cut_code = [0]*len(word_dict)
for word in s4_cut:
    s4_cut_code[word_dict[word]]+=1
print(s4_cut_code)

# 计算余弦相似度
sum1 = 0
sq1 = 0
sq2 = 0
sq3 = 0
sq4 = 0
for i in range(len(s1_cut_code)):
    sum1 += s1_cut_code[i] * s2_cut_code[i] * s3_cut_code[i] * s4_cut_code[i]
    sq1 += pow(s1_cut_code[i], 2)
    sq2 += pow(s2_cut_code[i], 2)
    sq3 += pow(s3_cut_code[i], 2)
    sq4 += pow(s4_cut_code[i], 2)

try:
    result = round(float(sum1) /
                   (math.sqrt(sq1) * math.sqrt(sq2) * math.sqrt(sq3) * math.sqrt(sq3)), 2)
except ZeroDivisionError:
    result = 0.0
print(result)
