# Project: ZG3Doc
# File : chapter1-1.py
# Date : 2023/4/14 9:36
# Author: Younger Shen <申延刚>
# Web: https://github.com/youngershen
# Cell: 13811754531
# Wechat: 13811754531
# Email : shenyangang@163.com

import numpy as np
from collections import Counter

# 使用numpy的相关方法完成以下需求
# 1．创建数字从 0 到 9 的 1 维数组arr
arr = np.arange(0, 10)
print(arr)
# 2．从 arr 中提取所有奇数
print(arr[arr % 2 != 0])
# 3．将 arr 中的所有奇数替换成 -1
arr[arr % 2 != 0] = -1
print(11111, arr)
# 4．将 arr  数组转换成 2 维数组arr2
arr2 = arr.reshape(5, 2)
print(arr2)
# 5．获取arr2的轴的数量
print(arr2.ndim)
# 6．获取arr2的第1行第2列
print(arr2[0, 1])
# 7．获取arr2的数组元素总个数
a7 = Counter(arr2.flatten())
print(a7)
# 8．获取arr2的元素类型
print(arr2.dtype)
