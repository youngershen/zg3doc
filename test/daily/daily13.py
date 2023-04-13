# Project: ZG3Doc
# File : daily13.py
# Date : 2023/4/13 14:59
# Author: Younger Shen <申延刚>
# Web: https://github.com/youngershen
# Cell: 13811754531
# Wechat: 13811754531
# Email : shenyangang@163.com
import numpy as np
from test.utils import print_line

"""
日考一 第三套习题

1．创建一个10*10的ndarray对象，且矩阵边界全为1，里面全为0
2．创建所有 False的 2×2 NumPy 数组
3．使用numpy获得2022年1月对应的所有日期
4．创建一个形态为 3x5 的 2 维数组，包含 1 和 10 之间的随机小数
5．创建全是1的3X3数组
6．如何从数组np.array([1, 2, 0, 0, 4, 0])中找出非0元素的位置索引
7．创建一个5*3随机矩阵和一个3*2随机矩阵，求矩阵积
8．使用numpy获取昨天、今天、明天的日期
"""

"""
   1．创建一个10*10的ndarray对象，且矩阵边界全为1，里面全为0

   分析:
   先建立认为数组, 可以使用 np.zeros 进行建立,
   然后使用切片赋值的操作, 把边界赋值为 1

   也可以使用 np.one 建立二维数组, 把除边界以外的
   值替换为 0

   两种算法自己至少会一个
   """

# 方法 一
print_line()
arr = np.zeros((10, 10))
print("1．创建一个10*10的ndarray对象，且矩阵边界全为1，里面全为0")
print("原二维数组为:")
print(arr)
arr[0, :] = arr[-1, :] = arr[:, 0] = arr[:, -1] = 1
print("边界为 1 的数组为:")
print(arr)
# 方法 二
arr = np.ones((10, 10))
arr[1:-1, 1:-1] = 0
# print(arr)

"""
2．创建所有 False的 2×2 NumPy 数组

分析:

核心原理是使用了布尔数组, 然后取反

方法一
arr = np.zeros((2, 2), dtype=bool)
arr[:] = False
print(arr)

方法 二
arr = np.full((2, 2), False, dtype=bool)
print(arr)

方法三
arr = np.zeros((2, 2), dtype=bool)
arr = ~arr

"""
print_line()
arr = np.zeros((2, 2), dtype=bool)
arr = ~arr
print("2．创建所有 False的 2×2 NumPy 数组")
print("数组为")
print(arr)

"""
3．使用numpy获得2022年1月对应的所有日期

分析:
可以使用NumPy的arange函数生成2022年1月份的所有日期。
首先，我们需要确定1月份的天数，
可以使用Python的标准库datetime来获取。
然后，我们可以使用arange函数生成从1号到月末的所有整数，
再将其转换为日期格式。

不理解的同学去翻一下关于 numpy 处理相关的文档
"""
print_line()
from datetime import date

# 获取 2022 年 1 月份的天数
days_in_january = (date(2022, 2, 1) - date(2022, 1, 1)).days
# 使用arange函数生成从1号到月末的所有整数
dates = np.arange(1, days_in_january + 1)
# 将整数转换为日期格式
dates = np.array([date(2022, 1, d) for d in dates])
print("3. 使用numpy获得2022年1月对应的所有日期: ")
print(dates)

"""
4．创建一个形态为 3x5 的 2 维数组，包含 1 和 10 之间的随机小数

分析:
重点是 np.random.uniform 这个
函数的用法, 不会的去看文档, 注意
每一个参数的用法
"""
print_line()
arr = np.random.uniform(low=1, high=10, size=(3, 5))
print("4．创建一个形态为 3x5 的 2 维数组，包含 1 和 10 之间的随机小数")
print(arr)

"""
5．创建全是1的3X3数组

分析:

思路就是使用 numpy.ones 进行数组的创建
"""
print_line()
print("5．创建全是1的3X3数组")
arr = np.ones((3, 3))
print(arr)

"""
6．如何从数组np.array([1, 2, 0, 0, 4, 0])中找出非0元素的位置索引

分析:
在这里，返回值是一个元组，
其中包含了非零元素的位置索引。
在这个例子中，元组中只有一个数组，
这个数组包含了索引值为 0、1 和 4 的元素
，也就是说，这些位置上的元素不为零（0）。
"""
print_line()
arr = np.array([1, 2, 0, 0, 4, 0])
indices = np.nonzero(arr)
print("6．如何从数组np.array([1, 2, 0, 0, 4, 0])中找出非0元素的位置索:")
print(indices)


"""
7．创建一个5*3随机矩阵和一个3*2随机矩阵，求矩阵积

分析:

主要是 np.random.rand 的用法以及
np.dot 求矩阵积这个方法的应用
"""
print_line()
# 创建5x3和3x2的随机矩阵
A = np.random.rand(5, 3)
B = np.random.rand(3, 2)
# 计算矩阵积
C = np.dot(A, B)

print("7．创建一个5*3随机矩阵和一个3*2随机矩阵，求矩阵积")
print("矩阵 A:\n", A)
print("\n矩阵 B:\n", B)
print("\n矩阵积 C:\n", C)

"""
8．使用numpy获取昨天、今天、明天的日期

分析
"""