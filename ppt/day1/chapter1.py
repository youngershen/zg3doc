# Project: ZG3Doc
# File : chapter1.py
# Date : 2023/4/12 14:26
# Author: Younger Shen <申延刚>
# Web: https://github.com/youngershen
# Cell: 13811754531
# Wechat: 13811754531
# Email : shenyangang@163.com

import numpy as np

# 数组的筛选
# 通过 python 的筛选方式 进行 numpy 数组的筛选

a1 = np.arange(10)
# 选择第 0 个
print(a1[0])

# 选择 第 0 到 2 个
print(a1[0:3])

# 选择最后一个
print(a1[-1])

# 从第一个到倒数第四个
print(a1[:-3])

# 1. 选择第 1 行, 第 3 个数字

# 2. 选择第 3 行

# 3. 选择多行 0 - 2

# 4. 选择第 1 列

# 5. 使用神奇索引, 选择第 1, 3, 5 个元素