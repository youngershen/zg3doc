# Project: ZG3Doc
# File : chapter1-1.py
# Date : 2023/4/14 9:36
# Author: Younger Shen <申延刚>
# Web: https://github.com/youngershen
# Cell: 13811754531
# Wechat: 13811754531
# Email : shenyangang@163.com
"""
第一单元 - 日考二 - 文档
"""

import numpy as np


"""
1．创建数字从 1 到 20 的 1 维数组arr，需要满足能被3整除不能被5整除

解析:
首席使用 a1 生成一个 1 到 20 的数组
注意 np.arange 的参数是 21 不是 20
其次是用布尔索引筛选出满足条件的数组元素

(a1 % 3 == 0) & (a1 % 5 != 0)
左边括号表示能被三整除的条件
右边括号表示能被 5 整除的条件
中间的 & 符号表示同时满足这个条件

"""
a1 = np.arange(21)
print(a1)
a2 = a1[(a1 % 3 == 0) & (a1 % 5 != 0)]
print(a2)

"""
2．请将给定的数组np.array([100,103,106,108,112,116,118,136,138,139])
中的奇数批量替换为33

解析:

1. 建立数组, 使用 np.arange 注意步长这个参数
2. 其次使用布尔索引 筛选出奇数
3. 然后进行替换旧就可以了
"""
a1 = np.arange(100, 140, 3)
print(a1)
a1[a1 % 2 == 1] = 33
print(a1)

"""
3．请生成一个从201-300的一维数组，并将这个一维数组转化为10行10列的二维数组

解析:

1. 使用 np.arange 建立一维数组
2. 使用 np.reshape 改变数组的形状

"""
a1 = np.arange(201, 301).reshape(10, 10)
print(a1)

"""
4．有两个数组，x=np.array([436,556,607,899]),
y=np.array([556,559,607,936,966]),
请使用合适的方法获取两个数组的公共项

解析：
1. 建立两个数组
2. 使用 np.intersect1d 这个函数进行公共项的计算
3. 核心是 np.intersect1d 的用法, 两个参数分别是数组
4. 该函数的返回是一个包含公功元素的新数组

参见 https://numpy.org/doc/stable/reference/generated/numpy.intersect1d.html

"""
x = np.array([436, 556, 607, 899])
y = np.array([556, 559, 607, 936, 966])
arr4 = np.intersect1d(x, y)
print(arr4)

"""
5．计算给定数组np.array([33,35,60,70,85])
和np.array([44,51,65,73,80])之间的欧氏距离

解析:
1. 首席建立数组
2. 其次私用

"""
arr1 = np.array([33, 35, 60, 70, 85])
arr2 = np.array([44, 51, 65, 73, 80])

# 计算两个数组之间的欧氏距离
distance = np.linalg.norm(arr1 - arr2)  # 使用 np.linalg.norm() 函数计算两个数组之间的欧氏距离

print(distance)

"""
6．输入数字n，创建数字从 1 到 n 的 1 维数组arr
将 arr 中的所有奇数替换成 -1


解析:
1. 使用 input 数组数字, 注意使用 int 强转否则不能计算
2. 使用 np.arange 生成数组, 注意第二个参数需要 + 1
3. 使用 np.where 函数或者布尔索引进行筛选出所有奇数
4. 将筛选出的奇数项, 赋值为 -1
"""
num = input('输入数字n:')
arr = np.arange(1, int(num) + 1)
out = np.where(arr % 2 == 1, -1, arr)  # 不改变原有数组
arr[arr % 2 == 1] = -1  # 改变原有的数组

"""
7．给定数组[1, 2, 3, 4, 5]，获取到平均值，
将平均值插入到每个元素直接得到新的数组

1 

"""
arr = np.array([1, 2, 3, 4, 5])
np.insert(arr, np.arange(1, len(arr)), arr.mean())

# 8．创建一个5*5的随机值数组，并找到最大值，并替换为0
arr = np.random.random(25).reshape(5, 5)
arr[arr == arr.max()] = 0
