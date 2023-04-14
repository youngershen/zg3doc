# Project: ZG3Doc
# File : chapter1-1.py
# Date : 2023/4/14 9:36
# Author: Younger Shen <申延刚>
# Web: https://github.com/youngershen
# Cell: 13811754531
# Wechat: 13811754531
# Email : shenyangang@163.com
import numpy as np

# 使用numpy完成以下需求
# 1．创建数字从 1 到 20 的 1 维数组arr，需要满足能被3整除不能被5整除
lt = [i for i in range(1, 21) if i % 3 == 0 and i % 5 != 0]
arr1 = np.array(lt)
print(arr1)
# 2．请将给定的数组np.array([100,103,106,108,112,116,118,136,138,139])中的奇数批量替换为33
arr2 = np.array([100, 103, 106, 108, 112, 116, 118, 136, 138, 139])
arr2[arr2 % 2 == 1] = 33
print(arr2)
# 3．请生成一个从201-300的一维数组，并将这个一维数组转化为10行10列的二维数组
arr3 = np.arange(201, 301).reshape(10, 10)
print(arr3)
# 4．有两个数组，x=np.array([436,556,607,899]),y=np.array([556,559,607,936,966]),请使用合适的方法获取两个数组的公共项
x = np.array([436, 556, 607, 899])
y = np.array([556, 559, 607, 936, 966])
arr4 = np.intersect1d(x, y)
print(arr4)
# 5．计算给定数组np.array([33,35,60,70,85])和np.array([44,51,65,73,80])之间的欧氏距离
a5 = np.linalg.norm(arr1-arr2)
print(a5)
# 6．输入数字n，创建数字从 1 到 n 的 1 维数组arr，将 arr 中的所有奇数替换成 -1
num = input('输入数字n:')
arr = np.arange(1, int(num))
out = np.where(arr % 2 == 1, -1, arr)  # 不改变原有数组
# arr[arr % 2 == 1] = -1  # 改变原有的数组
# 7．给定数组[1, 2, 3, 4, 5]，获取到平均值，将平均值插入到每个元素直接得到新的数组
arr = np.array([1, 2, 3, 4, 5])
np.insert(arr, np.arange(1, len(arr)), arr.mean())
# 8．创建一个5*5的随机值数组，并找到最大值，并替换为0
arr = np.random.random(25).reshape(5, 5)
arr[arr == arr.max()] = 0