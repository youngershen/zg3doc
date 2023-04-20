# Project: ZG3Doc
# File : test2.py
# Date : 2023/4/14 10:27
# Author: Younger Shen <申延刚>
# Web: https://github.com/youngershen
# Cell: 13811754531
# Wechat: 13811754531
# Email : shenyangang@163.com

"""
专高三 周考一 2022 年 12 月
"""

import pandas as pd
import numpy as np


def print_line(count=50):
    print("=" * count)

"""
一 使用 numpy 和 pandas 三方库等，实现以下要求，代码放在 week1.py 文件中
"""

# 1.使用列表创建一个 numpy 数组内容为
# ['No', 'one', 'can', 'stand', 'it', 'if', 'they', 'are', 'always', 'pressed']

# 2. 创建一个一维数组 ar1，该数组的元素值全为 100，长度为 10

# 3.对 ar1 进行操作，改变其形状，变成形状为 (5,2) 的数组

# 4.生成一个形状为(4,4), 元素值为随机值的二维数组 ar2

# 5.选取 ar2 中的元素, 打印前位于前两行同时位于前两列的元素的值

# 6.生成一个形状为(5, 5, 5), 元素值任意的三维数组

# 7. 使用数据
# [["taxi",100,10000,100],
# ["car",1000,1000,1000],
# ["train",5000,5000,5000]]
# 创建一个 pandas 的 dataframe 数据集 df1

# 8.更改数据集 df1 的列名依次为, 交通工具, 指标1, 指标2, 指标3


# 9. 设置数据集 df1 的行索引为 r1, r2, r3

# 10.从 df1 中删除交通工具为 taxi 的记录

"""
二 使用适当的 python 库进行综合数据分析，代码保存为 week2.py
"""

# 11.读取数据文件 “汽车销量数据.xlsx”，形成 dataframe 数据集 df2

# 12. 对 df2 的空值字段数据进行合理的填充

# 13.对数据集df2进行统计性基本信息描述

# 14.按照 “市” 字段分组统计汽车销量情况

# 15. 按照 “省” 进行分组, 分组统计每一年的汽车销量情况

# 16.从 df2 中选择 “所有权” 字段值为 “个人” 的数据, 形成新的数据集 df3

# 17. 对 df3 数据集进行统计, 计算 “功率” 字段的最大值, 最小值, 平均值

# 18.筛选 df3 数据集中的字段 “燃料种类” 为
# “汽油” 且 “车长” 字段大于 6000 的记录,
# 作为新数据集df4, 保存到xlsx文件

# 19. 对 df4 中的数据按照 “省” 进行分组，计算 “车高” 字段的最大值, 最小值, 平均值
