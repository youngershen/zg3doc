# Project: ZG3Doc
# File : test1.py
# Date : 2023/4/14 10:33
# Author: Younger Shen <申延刚>
# Web: https://github.com/youngershen
# Cell: 13811754531
# Wechat: 13811754531
# Email : shenyangang@163.com
"""
2022 年 9 月
"""

"""
（一）创建名为my_pandas.py的文件，完成相关pandas的操作（每题5分)
1）读取附件文件信用卡客户.xlsx
2）请在原有数据上增加一列征信记录,如果违约记录大于1次即为失信人员,否则为正常用户
3）写一个函数，实现对年龄的分箱操作。条件为 年龄小于30，返回“年轻群体”；年龄大于等于30，同时小于50，返回“中年群体”；其余条件返回“中老年群体”。可新建一列“年龄群体”，接收返回值（不能使用cut函数，函数要自己定义）
4）针对用户类型列的缺失值做合理的预处理
5）按信用卡余额的降序，年龄的升序进行排序
6）对信用卡客户进行数据透视，index使用上一题生成的“年龄群体”列，columns使用“职业”列，分析的values使用“信用卡余额”值
7）为了观察不同类型的客户群体的使用习惯，我们需要通过RFM分析法实现客户分群。请从学历这个维度，分析不同学历层次的客户的M值(累计信用卡余额)、F值(最后使用天数的最近值)、R值（月使用频率的均值），并将结果生成一个dataframe，写入rfm.html网页
8）对最近使用日期做日期转换,提取到周,月
9）请按最近使用日期的自然月, 统计信用卡余额的最大值
10）请按最近使用日期的自然周，统计信用卡余额的平均值
11）将上述9, 10的数据,分别使用pyecharts的折线图可视化展示
12）请统计婚姻状况每个组员下，失信人员的总数
13）请统计每个学历下，月使用频率的中位数
14）请统计每个学历下, 月使用频率的平均值
15）将上述13,14的数据,使用matplotlib的多维柱状图可视化展示
16）婚姻状况是否对信用卡余额有影响？请从婚姻状况的角度，探索信用卡余额的状态，分析指标为中位数
17）对第16题的分析结果，使用交互化绘图工具pyecharts的饼图进行绘图，并将结果生成到网页
18）请分析是否买房列下的月使用频率的最大值,以及信用卡余额的总和
19）将上述18的数据,使用pyecharts的多维柱状图可视化展示
20）根据职业列的数据,生成对应的pyecharts的词云图

"""

import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from pyecharts.charts import Bar, Line, Pie, WordCloud

# （一）创建名为my_pandas.py的文件，完成相关pandas的操作（每题5分)
# 1）读取附件文件信用卡客户.xlsx
df = pd.read_excel('./信用卡客户.xlsx')
# 2）请在原有数据上增加一列征信记录,如果违约记录大于1次即为失信人员,否则为正常用户
df['征信记录'] = df.apply(lambda x: '失信人员' if x['违约记录'] > 1 else '正常用户', axis=1)
# 3）写一个函数，实现对年龄的分箱操作。条件为 年龄小于30，返回“年轻群体”；年龄大于等于30，同时小于50，返回“中年群体”；
# 其余条件返回“中老年群体”。可新建一列“年龄群体”，接收返回值（不能使用cut函数，函数要自己定义）
def func(x):
    if x['年龄'] < 30: return '年轻群体'
    elif 30 <= x['年龄'] < 50: return '中年群体'
    else: return '中老年群体'
df['年龄群体'] = df.apply(func, axis=1)
# 4）针对用户类型列的缺失值做合理的预处理
df['用户类型'].fillna(value='unknown', inplace=True)
# 5）按信用卡余额的降序，年龄的升序进行排序
df.sort_values(ascending=[False, True], inplace=True, by=['信用卡余额', '年龄'])
# 6）对信用卡客户进行数据透视，index使用上一题生成的“年龄群体”列，columns使用“职业”列，分析的values使用“信用卡余额”值
df6 = df.pivot_table(index=['年龄群体'], columns=['职业'], values=['信用卡余额'])
# 7）为了观察不同类型的客户群体的使用习惯，我们需要通过RFM分析法实现客户分群。请从学历这个维度，
# 分析不同学历层次的客户的M值(累计信用卡余额)、F值(最后使用天数的最近值)、R值（月使用频率的均值），并将结果生成一个dataframe，写入rfm.html网页
M = df.groupby('学历').agg({'信用卡余额': 'sum'}).reset_index()
R = df.groupby('学历').agg({'月使用频率': 'mean'}).reset_index()
f = df.groupby('学历').agg({'最近使用日期': 'max'}).reset_index()
f['F'] = (pd.to_datetime(datetime.now()) -
            pd.to_datetime(df['最近使用日期'], unit='s')).dt.days
F = f[['学历', 'F']]
RF = pd.merge(R, F, left_on='学历', right_on='学历', how='inner')
RFM = pd.merge(RF, M, left_on='学历', right_on='学历', how='inner')
RFM.rename(columns={'月使用频率': 'R', '信用卡余额': 'M'}, inplace=True)
print(RFM)
# 8）对最近使用日期做日期转换,提取到周,月
df['周'] = pd.to_datetime(df['最近使用日期']).dt.week
df['月'] = pd.to_datetime(df['最近使用日期']).dt.month
# 9）请按最近使用日期的自然月, 统计信用卡余额的最大值
df9 = df.groupby('月')['信用卡余额'].max()
# 10）请按最近使用日期的自然周，统计信用卡余额的平均值
df10 = df.groupby('周')['信用卡余额'].mean()
# 11）将上述9, 10的数据,分别使用pyecharts的折线图可视化展示
line = Line()
line.add_xaxis([str(i) for i in df9.index.tolist()])
line.add_yaxis('信用卡余额的最大值', df9.values.tolist())
# line.render('./9.html')
line1 = Line()
line1.add_xaxis([str(i) for i in df10.index.tolist()])
line1.add_yaxis('信用卡余额的最大值', df10.values.tolist())
# line1.render('./10.html')
# 12）请统计婚姻状况每个组员下，失信人员的总数
df12 = df[df['征信记录'] == '失信人员'].groupby(by='婚姻状况')['征信记录'].count()
# 13）请统计每个学历下，月使用频率的中位数
print(df.columns)
df13 = df.groupby('学历')['月使用频率'].median()
# 14）请统计每个学历下, 月使用频率的平均值
df14 = df.groupby('学历')['月使用频率'].mean()
# 15）将上述13,14的数据,使用matplotlib的多维柱状图可视化展示
x = df13.index.tolist()
y1 = df13.values.tolist()
y2 = df14.values.tolist()
plt.bar(x, y1, y2)
# plt.show()
# 16）婚姻状况是否对信用卡余额有影响？请从婚姻状况的角度，探索信用卡余额的状态，分析指标为中位数
df16 = df.groupby('婚姻状况')['信用卡余额'].median()
# 17）对第16题的分析结果，使用交互化绘图工具pyecharts的饼图进行绘图，并将结果生成到网页
pie = Pie()
pie.add('中位数', list(zip(df16.index.tolist(), df16.values.tolist())))  # [(), (), ()]  列表嵌套元组的数据
# pie.render('./16.html')
# 18）请分析是否买房列下的月使用频率的最大值,以及信用卡余额的总和
df18 = df.groupby(by='是否买房').agg({'月使用频率': 'max', '信用卡余额': 'sum'})
# 19）将上述18的数据,使用pyecharts的多维柱状图可视化展示
bar = Bar()
bar.add_xaxis(df18.index.tolist())
bar.add_yaxis('月使用频率', df18['月使用频率'].tolist())
bar.add_yaxis('信用卡余额', df18['信用卡余额'].tolist())
# bar.render('./19.html')
# 20）根据职业列的数据,生成对应的pyecharts的词云图
df20 = df.groupby(by='职业')['ID'].count()
word = WordCloud()
word.add('', list(zip(df20.index.tolist(), df20.values.tolist())))  # [(), (), ()]  列表嵌套元组的数据
word.render('./20.html')
