import pandas as pd
import numpy as np

# pandas 中的分组聚合

d1 = {
    'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar'],
    'B': ['one', 'one', 'two', 'two', 'three', 'three'],
    'C': [1, 2, 3, 4, 5, 6],
    'D': [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
}

df1 = pd.DataFrame(d1)
print(df1)

# 按 A 列分组, 计算平均值
print("=============")
print(df1.groupby('A').mean(numeric_only=True))

# 按 B 列分组, 统计 D 列的总和
print("=============")
print(df1.groupby('B')['D'].mean(numeric_only=True))

# 先按 A 列分组, 再按 B 列分组, 统计所有列均值
print("===========")
print(df1.groupby(['A', 'B']).mean(numeric_only=True))

# 对某一列应用多个聚合函数
print("=============")
print(df1.groupby('A').agg(['max', 'min', 'mean']))

# 为列应用不同的聚合函数
print("===================")
print(df1.groupby('A').agg({'C': ['mean', 'sum'], 'D': 'median'}))

# 使用 rename 为聚合之后的列重命名
print("============")
print(df1.groupby('A').agg({'C': ['mean', 'sum'], 'D': 'median'}).rename(
    columns={'mean': '均值', 'sum': '总和', 'median': '中位数'}
))

