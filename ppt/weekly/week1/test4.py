# Project: ZG3Doc
# File : test2.py
# Date : 2023/4/14 10:27
# Author: Younger Shen <申延刚>
# Web: https://github.com/youngershen
# Cell: 13811754531
# Wechat: 13811754531
# Email : shenyangang@163.com
"""
专高三 周考一 2023 年 1 月
"""
import numpy as np
import pandas as pd


def print_line(count=50):
    print("=" * count)


"""
一 使用 numpy 和 pandas 三方库等, 实现以下要求, 代码放在 week1.py 文件中:
"""

# 1. 使用["cat","dog","deer","fish","monkey"] 生成一个 numpy 数组

# 2. 生成一个元素值全为 5 长度为 20的一维数组

# 3. 对第 2 题中的一维数组增加一维，形成形状为 (20，1）的数组

# 4.生成一个形状为（3，3，3）、元素值依次为 1-27 的三维数组

# 5. 选取第 4 题中的数组的第 0-2 行, 1-2列, 打印筛选后的值

# 6. 使用 [["li",80,70,100],["yang",70,80,99],["zhang",60,70,100]]
# 数据初始化一个 pandas 的 dataframe 数据集
# 列名依次为 ["uid","en","cn","ma"]

# 7.使用 [["li",80,70,100],["yang",70,80,99],["zhang",60,70,100]]
# 数据初始化一个pandas的dataframe数据集，列名依次为["uid","en","cn","ma"]，
# 初始化方法不能与第 6 题使用的方法相同

# 8. 使用 {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
# 'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3]}
# 作为数据, 使用 ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# 作为索引初始化一个 dataframe 数据集

# 9. 对第 8 题中的数据集的 age 字段值按照均值进行空值填充处理


# 10. 对第 9 题中处理后的数据集按照 age 字段进行降序排序, 打印排序后结果


"""
二 使用适当的 python 库进行综合数据分析，代码保存为 week2.py
"""

# 11.读取 diamonds.csv 生成数据集 df, 对数据集的数据质量进行评价


# 12.对数据集中符合连续型数据的字段进行统计性描述

# 13. 根据 cut 字段计算每一个等级（clarity字段）钻石的数量

# 14.根据 color 字段进行分组, 统计 carat 字段最大值、最小值、均值

# 15. 先按字段color, 再按字段 cut 分组, 计算 carat 字段的总和

# 16. 筛选 carat 字段值大于 3.5 的数据, 生成新的数据集, 保存为 excel 文件

# 17. 根据 price 字段值进行处理
# 生成一个新列level
# price大于等于2000时
# level值设置为 1
# 否则设置为 0

# 18. 对第 17 题的数据
# 筛选 carat 字段值大于3.2
# level 字段值为 1 的数据，保存到 excel 文件

# 19. 对 df 数据集按照 carat, price 字段进行升序排序
# 保存到excel文件
