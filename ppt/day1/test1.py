# Project: ZG3Doc
# File : test1.py
# Date : 2023/4/19 13:36
# Author: Younger Shen <申延刚>
# Web: https://github.com/youngershen
# Cell: 13811754531
# Wechat: 13811754531
# Email : shenyangang@163.com


import numpy as np
"""
第一单元 - 第一套题

使用numpy的相关方法完成以下需求
"""


# 1．创建数字从 0 到 9 的 1 维数组arr

arr = np.arange(0, 10)
print("第一题:")
print(arr)

# 2．从 arr 中提取所有奇数
print("第二题:")
print(arr[arr % 2 != 0])
print(arr[arr % 2 == 1])

# 3．将 arr 中的所有奇数替换成 -1
print("第三题")
arr[arr % 2 != 0] = -1
print(arr)

# 4．将 arr  数组转换成 2 维数组 arr2
print("第四题")
arr2 = arr.reshape((2, 5))
print(arr2)


# 5．获取 arr2 的轴的数量
print("第五题")
print(arr2.ndim)

# 6．获取 arr2 的第1行第2列
print("第六题")
print(arr2[0, 1])
print(arr2[0][1])

# 7．获取 arr2 的数组元素总个数
print("第七题")
print(arr2.size)

# 8．获取 arr2 的元素类型
print("第八题")
print(arr2.dtype)
