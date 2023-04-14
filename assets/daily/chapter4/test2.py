# Project: ZG3Doc
# File : test2.py
# Date : 2023/4/14 9:41
# Author: Younger Shen <申延刚>
# Web: https://github.com/youngershen
# Cell: 13811754531
# Wechat: 13811754531
# Email : shenyangang@163.com
import pandas as pd

# 1．按要求创建Dataframe df（如下图），并通过分组得到以下结果

data = [
    {'A': 'one', 'B': 'h', 'C': 10, 'D': -0.866738, 'E': 0.015762},
    {'A': 'two', 'B': 'h', 'C': 12, 'D': -0.951518, 'E': 0.970876},
    {'A': 'three', 'B': 'h', 'C': 14, 'D': -0.631149, 'E': 0.210083},
    {'A': 'one', 'B': 'h', 'C': 16, 'D': -0.052842, 'E': 0.700343},
    {'A': 'two', 'B': 'f', 'C': 18, 'D': -0.540053, 'E': 0.782866},
    {'A': 'three', 'B': 'f', 'C': 20, 'D': -0.504618, 'E': 0.366960},
    {'A': 'one', 'B': 'f', 'C': 22, 'D': -0.390521, 'E': 0.423688},
    {'A': 'two', 'B': 'f', 'C': 24, 'D': -2.747241, 'E': 0.088761}
]

df = pd.DataFrame(data=data)
# 2．以A分组，求出每组的中位数
df1 = df.groupby(by='A')['C'].median()
# 3．以A分组，求出C,D的分组平均值
df2 = df.groupby(by='A').agg({'C': 'mean', 'D': 'mean'})
# 4．以A,B分组，求出D,E的分组求和
df3 = df.groupby(by=['A', 'B']).agg({'D': 'sum', 'E': 'sum'})
# 5．以A分组，得到所有分组，以字典显示
df4 = df.groupby(by='A').groups
# 6．按照数值类型分组，求和
for group, result in df.groupby(by=df.dtypes, axis=1):
    print(group)
    print(result.sum())
# 7．将C,D作为一组分出来，并计算求和
df7 = df.groupby({'C': 'r', 'D': 'r'}, axis=1).sum()
# 8．以B分组，求出每组的均值，求和
df8 = df.groupby(by='B').agg({'C': ['mean', 'sum']})
# 9．以B分组，求出f组的最大值，最小值
df9 = df[df['B'] == 'f'].max()
df99 = df[df['B'] == 'f'].min()
# 以B分组，求出D，E的分组平均值
df3 = df.groupby(by=['B']).agg({'D': 'mean', 'E': 'mean'})