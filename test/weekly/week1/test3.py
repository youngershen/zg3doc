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
print_line()
print("第 1 题:")
a1 = ['No', 'one', 'can', 'stand', 'it', 'if', 'they', 'are', 'always',
     'pressed'] # 创建 python 列表
arr1 = np.array(a1)  # 创建一维数组


# 2. 创建一个一维数组 ar1，该数组的元素值全为 100，长度为 10
print_line()
print("第 2 题:")
ar1 = 100 * np.ones(10)
print(ar1)

# 3.对 ar1 进行操作，改变其形状，变成形状为 (5,2) 的数组
print_line()
print("第 3 题:")
ar3 = ar1.reshape(5, 2)
print(ar3)

# 4.生成一个形状为(4,4), 元素值为随机值的二维数组 ar2
print_line()
print("第 4 题:")
ar2 = np.random.randint(0, 10, size=(4, 4))
print(ar2)

# 5.选取 ar2 中的元素, 打印前位于前两行同时位于前两列的元素的值
print_line()
print("第 5 题:")
ar5 = ar2[0:2, 0:2]  # 切片操作
print(ar5)

# 6.生成一个形状为(5, 5, 5), 元素值任意的三维数组
print_line()
print("第 6 题:")
ar6 = np.random.randint(0, 10, size=(5, 5, 5))
print(ar6)

# 7. 使用数据
# [["taxi",100,10000,100],
# ["car",1000,1000,1000],
# ["train",5000,5000,5000]]
# 创建一个 pandas 的 dataframe 数据集 df1
print_line()
print("第 7 题:")
df1 = pd.DataFrame(data=[["taxi", 100, 10000, 100],
                         ["car", 1000, 1000, 1000],
                         ["train", 5000, 5000, 5000]])

print(df1)

# 8.更改数据集 df1 的列名依次为, 交通工具, 指标1, 指标2, 指标3
print_line()
print("第 8 题:")
df1.columns = ['交通工具', '指标1', '指标2', '指标3']
print(df1)
# 方法二
# df1.rename(columns={0: '交通工具', 1: '指标1', 2: '指标2', 3: '指标3'}, inplace=True)

# 9. 设置数据集 df1 的行索引为 r1, r2, r3
print_line()
print("第 9 题:")
df1.index = ['r1', 'r2', 'r3']
# 方法二
# df1.rename(index={0: 'r1', 1: 'r2', 2: 'r3'}, inplace=True)
print(df1)

# 10.从 df1 中删除交通工具为 taxi 的记录
print_line()
print("第 10 题:")
df1.drop(df1[df1['交通工具'] == 'taxi'].index, inplace=True)
print(df1)


"""
二 使用适当的 python 库进行综合数据分析，代码保存为 week2.py
"""

# 11.读取数据文件 “汽车销量数据.xlsx”，形成 dataframe 数据集 df2
print_line()
print("第 11 题:")
df2 = pd.read_excel('./汽车销量数据.xlsx')
print(df2.head(3))

# 12. 对 df2 的空值字段数据进行合理的填充
print_line()
print("第 12 题:")
df2.fillna(value=0, inplace=True)  # inplace=True 原地替换
print(df2.head(3))

# 13.对数据集df2进行统计性基本信息描述
print_line()
print("第 13 题:")
print(df2.describe())
# describe 函数为统计函数
# 会默认得到 max, min, mean, std, 25%, 50% ,75%, count

# 14.按照 “市” 字段分组统计汽车销量情况
print_line()
print("第 14 题:")
# df2 = df.groupby(by=['市'])['制造商'].count()
df3 = df2.groupby(by=['市']).agg({'制造商': 'count'})  # 与上面的语法是等价的
print(df3)

# 15. 按照 “省” 进行分组, 分组统计每一年的汽车销量情况
print_line()
print("第 15 题:")
df15 = df2.groupby(by=['省', '年'])['制造商'].count()
print(df15)

# 16.从 df2 中选择 “所有权” 字段值为 “个人” 的数据, 形成新的数据集 df3
print_line()
print("第 16 题:")
df3 = df2[df2['所有权'] == '个人']
# 筛选  会使用 [[]]  最里面[] 是布尔表达式
print(df3.head(3))

# 17. 对 df3 数据集进行统计, 计算 “功率” 字段的最大值, 最小值, 平均值
print_line()
print("第 17 题:")
print(df3['功率'].max())
print(df3['功率'].min())
print(df3['功率'].mean())

# 18.筛选 df3 数据集中的字段 “燃料种类” 为
# “汽油” 且 “车长” 字段大于 6000 的记录,
# 作为新数据集df4, 保存到xlsx文件
print_line()
print("第 18 题:")
df4 = df3[(df3['燃料种类'] == '汽油') & (df3['车长'] > 6000)]
df4.to_excel('df4.xlsx')

# 19. 对 df4 中的数据按照 “省” 进行分组，计算 “车高” 字段的最大值, 最小值, 平均值
print_line()
print("第 19 题:")
df19 = df4.groupby(by=['市']).agg({'车高': ['max', 'min', 'mean']})
print(df19)