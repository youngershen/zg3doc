# Project: ZG3Doc
# File : chapter1.py
# Date : 2023/4/12 14:26
# Author: Younger Shen <申延刚>
# Web: https://github.com/youngershen
# Cell: 13811754531
# Wechat: 13811754531
# Email : shenyangang@163.com

import numpy as np
#
# # 数组的筛选
# # 通过 python 的筛选方式 进行 numpy 数组的筛选
#
# a1 = np.arange(10)
# # 选择第 0 个
# print(a1[0])
#
# # 选择 第 0 到 2 个
# print(a1[0:3])
#
# # 选择最后一个
# print(a1[-1])
#
# # 从第一个到倒数第四个
# print(a1[:-3])
#
# # 1. 选择第 1 行, 第 3 个数字
#
# # 2. 选择第 3 行
#
# # 3. 选择多行 0 - 2
#
# # 4. 选择第 1 列
#
# # 5. 使用神奇索引, 选择第 1, 3, 5 个元素

a1 = np.arange(9)
print(a1)

# 打印形状
print("第六题")
print(a1.shape)

# 通过 resize 进行改变数组形状
# np.resize(x, (2, 3))
print("第七题")
a2 = np.resize(a1, (3, 3))
print(a2)

# append 一维广播
print("第八题")
a2 = np.append(a2, 100)
print(a2)

#  1 随机生成一个 二维数组 (n * m)
print("===================")
a1 = np.arange(20).reshape((4, 5))
print(a1)
#  2 横向添加一个包含有 n 个 100 的一位数组
a2 = np.append(a1, [[100, 100, 100, 100, 100]], axis=0)
print(a2)
#  3 纵向添加一个包含有 m 个 200 的一维数组
a3 = np.append(a2, [[200], [200], [200], [200], [200], ], axis=1)
print(a3)


# append 二维广播
# print(a3)
# a4 = np.append(a3, [[100], [100], [100] ], axis=1)
# print(a4)


# 计算 python 中的 数组元素之和
print("计算数组和")
a1 = [1, 2, 3, 4, 5]
print(sum(a1))

s = 0
for i in a1:
    s += i
print(s)


# numpy 统计函数
a2 = np.arange(0, 101)
print(a2)
print(np.sum(a2))
print(sum(a2))

print(np.min(a2))
print(np.max(a2))

"""
1. 创建一个 a * b * c 的三维数组
2. 创建一个 a * b 随机数组, 并找到它的最大值和最小值
3. 用 10 到 100 构建一个一维数组, 步长是 3
"""
