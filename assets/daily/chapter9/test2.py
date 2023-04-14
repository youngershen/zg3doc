# Project: ZG3Doc
# File : test2.py
# Date : 2023/4/14 10:07
# Author: Younger Shen <申延刚>
# Web: https://github.com/youngershen
# Cell: 13811754531
# Wechat: 13811754531
# Email : shenyangang@163.com

import pandas as pd
import numpy as np
from pyecharts.charts import Bar, Line, Pie, WordCloud

# 1．读取附件，云南旅游数据.xlsx文件，pd查看数据集情况
# 2．pd查看数据值的分布
df = pd.read_excel('./云南旅游数据.xlsx')
def func(x):
    if str(x['价格']).isdigit():
        return x['价格']
    else:
        return np.nan
df['价格'] = df.apply(func, axis=1)
df.dropna(inplace=True)
# 3．简单进行数据统计，获取价格的平均数
print(df['价格'].mean())
# 4．简单进行数据统计，获取出游人数的总数
print(df['出游人数'].sum())
# 5．对数据中的供应商使用pyecharts生成词云图，期望效果如下：
df5 = df.groupby(by='供应商')['价格'].count()
word = WordCloud()
word.add('', list(zip(df5.index.tolist(), df5.values.tolist())))
# word.render('./5.html')
# 6．根据服务保障列，可视化生成饼图，期望效果如下：
df6 = df.groupby(by='服务保障')['价格'].count()
pie = Pie()
pie.add('', list(zip(df6.index.tolist(), df6.values.tolist())))
# pie.render('./6.html')
# 7．统计目的地人数，可视化生成柱状图，期望效果如下：
df7 = df.groupby(by='目的地')['出游人数'].count()
bar = Bar()
bar.add_xaxis(df7.index.tolist())
bar.add_yaxis('', df7.values.tolist())
# bar.render('./7.html')
# 8．根据出游人数，可视化生成折线图
line = Line()
line.add_xaxis(df7.index.tolist())
line.add_yaxis('', df7.values.tolist())
# line.render('./8.html')
# 9．根据点评数以及评分，可视化生成多柱状图
df9 = df[['点评数', '评分']]
bar9 = Bar()
bar9.add_xaxis(df9.index.tolist())
bar9.add_yaxis('', df9['点评数'].tolist())
bar9.add_yaxis('', df9['评分'].tolist())
# bar9.render('./9.html')
# 10．根据价格，出游人数，可视化生成多条折线图
df10 = df[['价格', '出游人数']]
line10 = Line()
line10.add_xaxis(df10.index.tolist())
line10.add_yaxis('', df10['价格'].tolist())
line10.add_yaxis('', df10['出游人数'].tolist())
# line10.render('./10.html')
