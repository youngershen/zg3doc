# Project: ZG3Doc
# File : test2.py
# Date : 2023/4/14 9:44
# Author: Younger Shen <申延刚>
# Web: https://github.com/youngershen
# Cell: 13811754531
# Wechat: 13811754531
# Email : shenyangang@163.com
import pandas as pd
import numpy as np
from pyecharts.charts import Bar, Line, Pie

# 1．用df表示以下内容，字段从左往右依次是
# 幸存与否，仓位等级，性别，年龄，堂兄弟姐妹数，父母子女数，票价，上船港口缩写，仓位等级，
# 人员分类，是否成年男性，所在甲板，上船港口，是否幸存，是否单独乘船
data = {
    'survived': [0, 1, 1, 1, 0],  # 幸存与否
    'pclass': [3, 1, 3, 1, 3],  # 仓位等级
    'sex': ['male', 'female', 'female', 'female', 'male'],  # 性别
    'age': [22.0, 38.0, 26.0, 35.0, 25.0],  # 年龄
    'sibsp': [1, 1, 0, 1, 0],  # 堂兄弟姐妹数
    'parch': [0, 0, 0, 0, 0],  # 父母子女数
    'fare': [7.2500, 71.2833, 7.9250, 53.1000, 8.0500],  # 票价
    'embarked': ['S', 'C', 'S', 'S', 'S'],  # 上船港口缩写
    'class': ['Third', 'First', 'Third', 'First', 'Third'],  # 仓位等级
    'who': ['man', 'woman', 'woman', 'woman', 'man'],  # 人员分类
    'adult_male': [True, False, False, False, True],  # 是否成年男性
    'deck': [np.nan, 'C', np.nan, 'C', np.nan],  # 所在甲板
    'embark_town': ['Southampton', 'Cherbourg', 'Southampton', 'Southampton', 'Southampton'],  # 上船港口
    'alive': ['no', 'yes', 'yes', 'yes', 'no'],  # 是否幸存
    'alone': [False, False, True, False, True],  # 是否单独乘船
}
df = pd.DataFrame(data)
# 2．请分析 不同仓位等级中幸存和遇难的乘客比例，选择合适的组件可视化展示
df2 = df.groupby(by='pclass')['alive'].count()
pie = Pie()
pie.add('', list(zip(df2.index.tolist(), df2.values.tolist())))
# pie.render('./22.html')
# 3．请分析 不同性别的幸存比例，选择合适的组件可视化展示
df3 = df[df['alive'] == 'yes'].groupby(by='sex')['alive'].count()
pie1 = Pie()
pie1.add('', list(zip(df3.index.tolist(), df3.values.tolist())))
# pie1.render('./33.html')
# 4．请分析 幸存和遇难乘客的票价分布，选择合适的组件可视化展示
df4 = df.groupby(by='alive')['fare'].sum()
bar = Bar()
bar.add_xaxis(df4.index.tolist())
bar.add_yaxis('', df4.values.tolist())
# bar.render('./44.html')
# 5．请分析 幸存和遇难乘客的年龄分布，选择合适的组件可视化展示
df5 = df.groupby(by='alive')['age'].sum()
bar1 = Bar()
bar1.add_xaxis(df5.index.tolist())
bar1.add_yaxis('', df5.values.tolist())
# bar1.render('./55.html')
# 6．请分析 不同上船港口的乘客仓位等级分布，选择合适的组件可视化展示
df6 = df.groupby(by='embark_town')['pclass'].count()
bar2 = Bar()
bar2.add_xaxis(df6.index.tolist())
bar2.add_yaxis('', df6.values.tolist())
# bar2.render('./66.html')
# 7．请分析 幸存和遇难乘客堂兄弟姐妹的数量分布，选择合适的组件可视化展示
df7 = df.groupby(by='alive')['sibsp'].sum()
bar3 = Bar()
bar3.add_xaxis(df7.index.tolist())
bar3.add_yaxis('', df7.values.tolist())
# bar3.render('./77.html')
# 8．请分析 幸存和遇难乘客父母子女的数量分布，选择合适的组件可视化展示
df8 = df.groupby(by='alive')['parch'].sum()
bar4 = Bar()
bar4.add_xaxis(df8.index.tolist())
bar4.add_yaxis('', df8.values.tolist())
# bar4.render('./88.html')
# 9．请分析 单独乘船与否和幸存之间有没有联系，选择合适的组件可视化展示
df9 = df.groupby(by='alone')['alive'].count()
line = Line()
line.add_xaxis(df9.index.tolist())
line.add_yaxis('', df9.values.tolist())
# line.render('./99.html')