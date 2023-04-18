# Project: ZG3Doc
# File : chapter1-1.py
# Date : 2023/4/14 9:36
# Author: Younger Shen <申延刚>
# Web: https://github.com/youngershen
# Cell: 13811754531
# Wechat: 13811754531
# Email : shenyangang@163.com
""""
第一单元 - 日考一 - 文档
"""


import numpy as np

"""
1．创建数字从 0 到 9 的 1 维数组arr

解析:

使用 np.arange 函数生成连续数字序列的
数组是最简单的

这道题的核心是 np.arange 函数的用法要
熟悉

a = np.arrange(a1, a2 ,a3)

a1 参数代表的是生成的数组的起始值, 是包含在生成的数组以内的
a2 参数是生成序列的结束值, 需要注意的是这个值是不包含在
生成的数组里的
a3 是步长

详细参见: https://numpy.org/devdocs/reference/generated/numpy.arange.html#numpy.arange

"""
arr = np.arange(0, 10)
print(arr)

"""
2．从 arr 中提取所有奇数

解析:
这道题的解法是使用布尔索引
布尔索引通过布尔运算（如：比较运算符）
来获取符合指定条件的元素的数组。

语法需要注意，需要在方括号里写入一个
合适的布尔运算值才可以

arr[arr % 2 != 0] 

的含义是从数组中筛选出 模 2 不等于
0 的选项, 奇数的特点要熟悉，要明白
不能被 2 整除的数是奇数

"""
print(arr[arr % 2 != 0])

"""
3．将 arr 中的所有奇数替换成 -1

这道题需要两步操作 首先是筛选出
所有的奇数的选项 使用布尔索引
其次是直接给筛选出的结果赋值
就可以了
"""

arr[arr % 2 != 0] = -1
print(arr)

"""
4．将 arr  数组转换成 2 维数组 arr2

解析:

这道题使用 np.reshape 函数进行对
一维数组进行变形 核心是 np.reshape
函数的用法 需要牢记

a = np.arange(6).reshape(a1)

reshape 的参数是一个元组 
a1 是一个想要把当前数组变形
成的新的形状的参数
类型是元组

比如 a.reshape((2, 2))
会把数组 a 变成两行， 两列的一个二维数组

a.reshape((3, 3))
会把数组 a 变成三行，三列的一个二维数组

"""
arr2 = arr.reshape(5, 2)
print(arr2)

"""
5．获取arr2的轴的数量

解析:
numpy 中的数组之中的一个非常核心的参数就是
ndim 代表的是数组中的轴的数量
参考：
https://numpy.org/devdocs/reference/generated/numpy.ndarray.ndim.html
"""

print(arr2.ndim)

"""
6．获取arr2的第1行第2列
解析:

这个问题涉及到 numpy 数组的一般索引
可以使用两种方法进行解答
a1 = x[0, 2]
a2 = x[0][2]

这两种方法都可以， 区别是 a1 方法性能较高
"""

print(arr2[0, 1])

"""
7．获取arr2的数组元素总个数

ndarray 中的 size 属性就是
表示的是数组中的元素的个数
参见
https://numpy.org/devdocs/reference/generated/numpy.ndarray.size.html
"""

print(arr2.size)

"""
8．获取arr2的元素类型
ndarray 中的 dtype 属性
表示的就是
"""
print(arr2.dtype)
