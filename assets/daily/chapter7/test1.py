# Project: ZG3Doc
# File : test1.py
# Date : 2023/4/14 9:44
# Author: Younger Shen <申延刚>
# Web: https://github.com/youngershen
# Cell: 13811754531
# Wechat: 13811754531
# Email : shenyangang@163.com

from pyecharts.charts import Bar, Line, Pie
import pandas as pd

# 1．读取附件tips.csv，用df表示以下内容，字段从左往右依次是总消费，小费，性别，
# 吸烟与否，就餐星期，就餐时间，就餐人数
df = pd.read_csv('./tips.csv')
print(df)
# 2．请分析 小费和总消费之间的关系，选择合适的组件可视化展示
x = df['tip'].tolist()
y = df['total_bill'].tolist()
bar = Bar()
bar.add_xaxis(x)
bar.add_yaxis('小费和总消费之间的关系', y)
# bar.render('./小费和总消费之间的关系.html')
# 3．请分析 男性顾客和女性顾客，谁更慷慨，选择合适的组件可视化展示
df3 = df.groupby(by='sex')['tip'].sum()
line = Line()
x3 = df3.index.tolist()
y3 = df3.values.tolist()
line.add_xaxis(x3)
line.add_yaxis('慷慨', y3)
# line.render('./慷慨.html')
# 4．请分析 抽烟与否是否会对小费金额产生影响，选择合适的组件可视化展示
df4 = df.groupby(by='smoker')['tip'].count()
pie = Pie()
x4 = df4.index.tolist()
y4 = df4.values.tolist()
pie.add('抽烟', list(zip(x4, y4)))
# pie.render('./抽烟.html')
# 5．请分析 工作日，什么时候顾客给的小费更慷慨，选择合适的组件可视化展示
df5 = df[(df['day'] != 'Sun') & (df['day'] != 'Sat')]
df5_1 = df5.groupby(by=['day', 'time'])['tip'].max()
bar1 = Bar()
bar1.add_xaxis(df5_1.index.tolist())
bar1.add_yaxis('', df5_1.values.tolist())
# bar1.render('5.html')
# 6．请分析 午饭和晚饭，哪一顿顾客更愿意给小费，选择合适的组件可视化展示
df6 = df.groupby(by='time')['tip'].max()
line1 = Line()
line1.add_xaxis(df6.index.tolist())
line1.add_yaxis('', df6.values.tolist())
# line1.render('./6.html')
# 7．请分析 就餐人数是否会对慷慨度产生影响，选择合适的组件可视化展示
df7 = df.groupby(by='size')['tip'].max()
line2 = Line()
line2.add_xaxis(df7.index.tolist())
line2.add_yaxis('', df7.values.tolist())
# line2.render('./7.html')
# 8．请分析 性别+抽烟的组合因素对慷慨度的影响，选择合适的组件可视化展示
df8 = df.groupby(by=['sex', 'smoker'])['tip'].max()
pie1 = Pie()
x8 = df8.index.tolist()
y8 = df8.values.tolist()
pie1.add('', list(zip(x8, y8)))
pie1.render('./8.html')
# 9．请分析 周末，什么时候顾客给的小费更慷慨，选择合适的组件可视化展示
df9 = df[(df['day'] == 'Sun') | (df['day'] == 'Sat')]
df9_1 = df5.groupby(by=['day', 'time'])['tip'].max()
bar2 = Bar()
bar2.add_xaxis(df9_1.index.tolist())
bar2.add_yaxis('', df9_1.values.tolist())
bar2.render('9.html')
