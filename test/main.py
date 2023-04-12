import pandas as pd
import numpy as np

df1 = pd.read_csv('./data/beijing_tianqi_2019.csv')
df1.loc[:, 'bWendu'] = df1['bWendu'].str.replace('℃', '').astype('int32')
df1.loc[:, 'yWendu'] = df1['yWendu'].str.replace('℃', '').astype('int32')
print(df1)

# 需要把 字符串的日期, 转换成 pandas 中的 datetime 对象
print("==============")
print(type(df1.loc[0, 'ymd']))
df1.set_index(pd.to_datetime(df1['ymd']), inplace=True)
print(type(df1.index[0]))

# 需要统计每周的最高温
print("===========")
print(df1.index)
print(df1.groupby(df1.index.week)['bWendu'].max())

# 使用日期方便的查询数据
print("===============")
print(df1.loc['2019-03-06'])
print(df1.loc['2019-03-16': '2019-03-20'])

# datetime 的 resample
print("============")
print(df1.resample('3D').sum())