# Project: ZG3Doc
# File : test3.py
# Date : 2023/4/19 16:12
# Author: Younger Shen <申延刚>
# Web: https://github.com/youngershen
# Cell: 13811754531
# Wechat: 13811754531
# Email : shenyangang@163.com
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

# 1．创建一个 10*10 的ndarray对象，且矩阵边界全为1，里面全为 0
print("第一题:")
a1 = np.ones(100).reshape((10, 10))
print(a1)
a1[1:-1, 1:-1] = 0
print("===================")
print(a1)

# 用第二种方法实现需求

# 2．创建所有 False的 2×2 NumPy 数组
print("第二题")
a2 = np.array([False, False, False, False]).reshape((2, 2))
print(a2)

# 用第二种方法实现功能

# 3．使用numpy获得2022年1月对应的所有日期
print("第三题:")
a3 = np.arange('2022-01-01', '2022-02-01', dtype=np.datetime64)
print(a3)

# 4．创建一个形态为 3x5 的 2 维数组，
# 包含 1 和 10 之间的随机小数
# randint 整数
# uniform 为小数

a4 = np.random.uniform(1, 11, (3, 5))
print(a4)

# 5．创建全是1的3X3数组
print('第五题')
a5 = np.ones(9).reshape((3, 3))
print(a5)

# 6．如何从数组np.array([1, 2, 0, 0, 4, 0])
# 中找出非0元素的位置索引
print("第六题")
a6 = np.array([1, 2, 0, 0, 4, 0])
i = np.where(a6 != 0)
print(a6)
print(i)

# 7．创建一个5*3随机矩阵和一个3*2随机矩阵，求矩阵积
print("第七题")
a71 = np.random.randint(0, 100, 15).reshape(5, 3)
print(a71)
a72 = np.random.randint(0, 100, 6).reshape(3, 2)
print(a72)

a73 = np.dot(a71, a72)
print(a73)

# 8．使用numpy获取昨天、今天、明天的日期
print("第八题")
a81 = np.datetime64('today', 'D') - 1  # 昨天
a82 = np.datetime64('today', 'D') # 今天
a83 = np.datetime64('today', 'D') + 1 #  明天
print(a81)
print(a82)
print(a83)