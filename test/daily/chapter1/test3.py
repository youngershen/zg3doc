# Project: ZG3Doc
# File : dailytest13.py
# Date : 2023/4/14 9:36
# Author: Younger Shen <申延刚>
# Web: https://github.com/youngershen
# Cell: 13811754531
# Wechat: 13811754531
# Email : shenyangang@163.com

import numpy as np

# 使用numpy完成以下需求
# 1．创建一个10*10的ndarray对象，且矩阵边界全为1，里面全为0
arr = np.ones(100, dtype=int).reshape(10, 10)
arr[1:-1, 1:-1] = 0
print(arr)

# 2．创建所有 False的 2×2 NumPy 数组
arr2 = np.array([False, False, False, False]).reshape(2, 2)
print(arr2)

# 3．使用numpy获得2022年1月对应的所有日期
arr3 = np.arange('2022-01-01', '2022-02-01', dtype=np.datetime64)
print(arr3)

# 4．创建一个形态为 3x5 的 2 维数组，包含 1 和 10 之间的随机小数
arr4 = np.random.uniform(1, 10, size=15).reshape(3, 5)
print(arr4)

# 5．创建全是1的3X3数组
arr5 = np.ones(9).reshape(3, 3)
print(arr5)

# 6．如何从数组np.array([1, 2, 0, 0, 4, 0])中找出非0元素的位置索引
arr6 = np.array([1, 2, 0, 0, 4, 0])
index = np.where(arr6 != 0)
print(index)

# 7．创建一个5*3随机矩阵和一个3*2随机矩阵，求矩阵积
arr = np.random.random(15).reshape(5, 3)
arr1 = np.random.random(6).reshape(3, 2)
np.dot(arr, arr1)

# 8．使用numpy获取昨天、今天、明天的日期
arr = np.datetime64('today', 'D') - 1
arr1 = np.datetime64('today', 'D')
arr2 = np.datetime64('today', 'D') + 1
print(arr, arr1, arr2)
