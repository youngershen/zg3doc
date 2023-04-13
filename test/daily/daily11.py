# Project: ZG3Doc
# File : daily1.py
# Date : 2023/4/12 14:33
# Author: Younger Shen <申延刚>
# Web: https://github.com/youngershen
# Cell: 13811754531
# Wechat: 13811754531
# Email : shenyangang@163.com
import numpy as np
from test.utils import print_line

"""
日考一 第一套习题

一定好好好练习哦 
知识点老师都讲过的 
不懂的随时问老师

练习的时候把题干
复制下来, 然后
不要看答案自己
敲, 每一套题至少
练习三遍以上
"""

"""
以下为日考题干: 

1．创建数字从 0 到 9 的 1 维数组arr
2．从 arr 中提取所有奇数
3．将 arr 中的所有奇数替换成 -1
4．将 arr  数组转换成 2 维数组arr2
5．获取arr2的轴的数量
6．获取arr2的第1行第2列
7．获取arr2的数组元素总个数
8．获取arr2的元素类型
"""

"""
1．创建数字从 0 到 9 的 1 维数组arr

分析: 使用 np.arange 函数直接创建,
做不出来是就去看 np.arange 函数的用法
"""
print_line()
arr = np.arange(0, 10, 1)
print("1．创建数字从 0 到 9 的 1 维数组arr: ")
print(arr)

"""
2．从 arr 中提取所有奇数

分析: 数组中数据的筛选这里使用到了布尔筛选
方法是在方括号里放入一个返回值为
布尔类型的表达式, 奇数的筛选方法为
任意数模 2 结果如果是 1 , 那么久判定它为奇数
不理解的话就去看关于布尔检索的内容
"""
print_line()
print("从 arr 中提取所有奇数: ")
print(arr[arr % 2 == 1])

"""
3．将 arr 中的所有奇数替换成 -1

分析: 与第二问类似, 只是赋值直接把筛选出的
奇数换成了 -1
"""
print_line()
arr[arr % 2 == 1] = -1
print("3．将 arr 中的所有奇数替换成 -1: ")
print(arr)

"""
4．将 arr  数组转换成 2 维数组arr2

分析: 使用 reshape 改变数组形状
不会做就去查 reshape 的文档
"""
print_line()
arr2 = arr.reshape((2, 5))
print("将 arr 变形为 (2,5) 的二维数组")
print(arr2)

"""
5．获取arr2的轴的数量

分析: 使用 ndim 参数即可直接得到 arr2
的轴的数量
"""
print_line()
d = arr2.ndim
print("5．获取arr2的轴的数量:")
print(d)

"""
6．获取arr2的第1行第2列

分析: 使用下标索引即可
"""
print_line()
print("6．获取arr2的第1行第2列:")
print(arr2[1, 2])
print(arr2[1][2])
print(arr2[(1,), (2,)])

"""
7．获取arr2的数组元素总个数

分析: 使用数组元素的 array.size 属性
即可直接得到数组中元素的个数,
即为形状元组中的两个数的乘积
"""
print_line()
print("7．获取arr2的数组元素总个数:")
count = arr2.size
print(count)

"""
8．获取arr2的元素类型

分析: 使用数组元素中的 dtype 即
可直接得到数组元素的类型
"""
print_line()
print("8．获取arr2的元素类型:")
print(arr2.dtype)
