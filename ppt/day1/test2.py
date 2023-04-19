# Project: ZG3Doc
# File : test2.py
# Date : 2023/4/19 13:58
# Author: Younger Shen <申延刚>
# Web: https://github.com/youngershen
# Cell: 13811754531
# Wechat: 13811754531
# Email : shenyangang@163.com
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
arr = np.arange(1, 21)
arr = arr[(arr % 3 == 0) & (arr % 5 != 0)]  # 重点
print(arr)

# 2．请将给定的数组 np.array([100,103,106,108,112,116,118,136,138,139]) 中的奇数批量替换为33
print("第二题")
arr = np.array([100, 103, 106, 108, 112, 116, 118, 136, 138, 139])
print(arr)
arr[arr % 2 != 0] = 33
print(arr)

# 3．请生成一个从201-300的一维数组，并将这个一维数组转化为10行10列的二维数组
print("第四题")
arr = np.arange(201, 301).reshape((10, 10))
print(arr)

# 4．有两个数组，x=np.array([436,556,607,899])
# y=np.array([556,559,607,936,966])
# 请使用合适的方法获取两个数组的公共项
print("第四题")
x = np.array([436, 556, 607, 899])
y = np.array([556, 559, 607, 936, 966])
arr4 = np.intersect1d(x, y)  # 寻找公共项的方法
print(arr4)

# 5．计算给定数组  np.array([33,35,60,70,85]) 和
# np.array([44,51,65,73,80]) 之间的欧氏距离
arr1 = np.array([33, 35, 60, 70, 85])
arr2 = np.array([44, 51, 65, 73, 80])
a5 = np.linalg.norm(arr1 - arr2)
print(a5)

# 6．输入数字n，创建数字从 1 到 n 的 1 维数组arr
# 将 arr 中的所有奇数替换成 -1
"""
难点:
1. 类型转换
2. 己得加 1
3. 布尔索引

"""

# print("第六题")
# n = input("输入")
# arr = np.arange(1, int(n) + 1)
# arr[arr % 2 != 0] = -1
# print(arr)

# 不改变原有数组
# 7．给定数组 [1, 2, 3, 4, 5]，获取到平均值，
# 将平均值插入到每个元素直接得到新的数组
print("第七题")
a1 = np.array([1, 2, 3, 4, 5])
print(a1.mean())
a3 = np.arange(1, len(a1))  # 1, 2, 3, 4
print(a3)

a5 = np.insert(a1, [0, 1, 2, 3, 4], a1.mean())
a6 = np.insert(a1, np.arange(0, len(a1)), a1.mean())

print(a5)
print(a6)

# 8．创建一个5*5的随机值数组，并找到最大值，并替换为 0
print("第八题:")
arr = np.random.randint(0, 100, (5, 5))
print(arr)

arr[arr == arr.max()] = 10000
print(arr)

# 1 创建一个 6 * 6 的随机数组
# 2 找到每一行的最大值
# 3 找到每一列的最大值
# 4 插入到原数组