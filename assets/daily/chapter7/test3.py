# Project: ZG3Doc
# File : test3.py
# Date : 2023/4/14 9:44
# Author: Younger Shen <申延刚>
# Web: https://github.com/youngershen
# Cell: 13811754531
# Wechat: 13811754531
# Email : shenyangang@163.com

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# 1．请利用matplotlib编写一个程序，显示y=x*x+18这条抛物线
x = list(range(1, 20))
y = [i*i + 18 for i in x]
# plt.plot(x, y)
# plt.show()
# 2．用df表示以下航班乘客变化分析内容
data = {
    'year': [1949, 1949, 1949, 1949, 1949],
    'month': ['January', 'February', 'March', 'April', 'May'],
    'passengers': [112, 118, 132, 129, 121]
}
df = pd.DataFrame(data)
# 3．利用matplotlib分析年度乘客总量变化情况（折线图）
df3 = df.groupby(by='year')['passengers'].sum()
# plt.plot(df3.index.tolist(), df3.values.tolist(), marker='o')
# plt.show()
# 4．利用matplotlib分析年度乘客总量变化情况（柱状图）
# plt.bar(df3.index.tolist(), df3.values.tolist())
# plt.show()
# 5．利用matplotlib分析乘客在一年中各月份的分布（折线图）
df5 = df.groupby(by='month')['passengers'].sum()
# plt.plot(df5.index.tolist(), df5.values.tolist(), marker='o')
# plt.show()
# 6．利用matplotlib分析乘客在一年中各月份的分布（柱状图）
# plt.bar(df5.index.tolist(), df5.values.tolist())
# plt.show()
# 7．利用seaborn分析年度乘客总量变化情况（折线图）
# sns.lineplot(data=df, x='year', y='passengers')
# plt.show()
# 8．利用seaborn分析年度乘客总量变化情况（柱状图）
# sns.barplot(x=df3.index.tolist(), y=df3.values.tolist())
# plt.show()
# 9．利用seaborn分析乘客在一年中各月份的分布（折线图）
# sns.lineplot(data=df, x='month', y='passengers')
# plt.show()
# 10．利用seaborn分析乘客在一年中各月份的分布（柱状图）
# sns.barplot(x=df5.index.tolist(), y=df5.values.tolist())
# plt.show()
