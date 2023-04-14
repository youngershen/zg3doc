# Project: ZG3Doc
# File : test3.py
# Date : 2023/4/14 10:33
# Author: Younger Shen <申延刚>
# Web: https://github.com/youngershen
# Cell: 13811754531
# Wechat: 13811754531
# Email : shenyangang@163.com

"""
2022 年 11 月份

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pyecharts.charts import Line, Bar, Map
from pyecharts import options as opts

# （一）使用numpy和pandas三方库等，实现以下要求，代码放在week1.py文件中：
# 1.创建二维数组df1,形状为4行4列,其取值范围在0-10之间
df1 = np.random.randint(0, 10, size=4 * 4).reshape(4, 4)
# 2.设置df1行索引为(1,2,3,4),列索引为(“a”,”b”,”c”,”d”)
df1 = pd.DataFrame(df1, index=[1, 2, 3, 4], columns=['a', 'b', 'c', 'd'])
# 3.将df1进行降序排序
df1.sort_values(by='a', ascending=False, inplace=True)
# 4.将df1保存到csv文件中
df1.to_csv('./4.csv')
# 5.读取BJ_tianqi.csv文件创建df3数组, 给df3数组增加温差列
df3 = pd.read_csv('./BJ_tianqi.csv')
df3['最高温度'] = df3['最高温度'].str.replace('℃', '').astype(int)
df3['最低温度'] = df3['最低温度'].str.replace('℃', '').astype(int)
df3['温差'] = df3['最高温度'] - df3['最低温度']
# 6.取出最高温度小于30度并且最低温度>20的数据
df6 = df3[(df3['最高温度'] < 30) & (df3['最低温度'] > 20)]
# 7.对最高温度进行降序同时对温差进行升序
df3.sort_values(by=['最高温度', '温差'], ascending=[False, True], inplace=True)
# 8.将df3数组日期列设置为行索引
df3.rename(index=df3['日期'], inplace=True)
# 9.取出df3数组9月份所有数据
df3['月'] = pd.to_datetime(df3['日期']).dt.month
df9 = df3[df3['月'] == 9]
# 10.创建一个形状为6行4列的数组df8,设置索引为('ab','bc','a','c','bd','d'),进行索引排序
df8 = pd.DataFrame(np.random.randint(0, 10, size=6 * 4).reshape(6, 4),
                   index=['ab', 'bc', 'a', 'c', 'bd', 'd'])
df8.sort_index(inplace=True)
# 11.现有数据s1 = pd.Series(['a', 'b']), s2 = pd.Series(['c', 'd']) 进行索横向合并
s1 = pd.Series(['a', 'b'])
s2 = pd.Series(['c', 'd'])
s3 = pd.concat([s1, s2], axis=1)
# 12.现有数据   x = pd.DataFrame({'姓名': ['张三', '李四', '王五'], '班级': ['一班', '二班', '三班']})
# y = pd.DataFrame({'专业': ['统计学', '计算机', '绘画'], '班级': ['一班', '三班', '四班']}),基于指定列的横向拼接,以数据x为主
x = pd.DataFrame({'姓名': ['张三', '李四', '王五'], '班级': ['一班', '二班', '三班']})
y = pd.DataFrame({'专业': ['统计学', '计算机', '绘画'], '班级': ['一班', '三班', '四班']})
df12 = pd.merge(x, y, left_on='班级', right_on='班级', how='left')
# 13.读取数据./movie_metadata.csv'文件创建df11,处理df11缺失值
df11 = pd.read_csv('./movie_metadata.csv')
df11.dropna(inplace=True)
# 14.根据df11数据源不同纬度,分析导演和票房总收入关系.,并进行排序
df14 = df11.groupby('director_name').agg({'gross': 'sum'})
df14.sort_values(by='gross', inplace=True)
# 15.查看df11数据源各imdb电影评分的个数并进行简单可视化(折线图)
df15 = df11[['movie_imdb_link', 'imdb_score']]
line = Line()
line.add_xaxis(df15['movie_imdb_link'].tolist())
line.add_yaxis('', df15['imdb_score'].tolist())
# line.render('./15.html')
# 16.查看imdb平均分最高的前20导演,并进行可视化(条形图),保存图片
df16 = df11.groupby('director_name').agg({'imdb_score': 'mean'})
df16.sort_values(by='imdb_score', inplace=True)
df16 = df16[:20]
plt.bar(df16.index.tolist(), df16['imdb_score'].tolist())
plt.savefig('./16.png')
# 17.根据数据BJ = [50,55,53,60], Sh = [44,66,55,41]绘制以下效果:
data = pd.DataFrame({'BJ': [50, 55, 53, 60], 'Sh': [44, 66, 55, 41]})
stack_bar = (
    Bar()  # 设置图表画布宽度
        .add_xaxis(data.index.tolist())
        .add_yaxis("BJ", data["BJ"].tolist(), stack="stack")
        .add_yaxis("Sh", data["Sh"].tolist(), stack="stack")
)
# stack_bar.render('./17.html')
# 18.完成以下可视化图形
x = list(range(1, 8))
y = [17, 17, 18, 15, 11, 11, 13]
plt.plot(x, y, '-', linestyle='dashed')
plt.show()
# 19.现有数据POPULATION,使用Map制作全球人口分布地图
POPULATION = [["China", 1420062022], ["India", 1368737513],
              ["United States", 329093110], ["Indonesia", 269536482],
              ["Brazil", 212392717], ["Pakistan", 204596442],
              ["Nigeria", 200962417], ["Bangladesh", 168065920],
              ["Russia", 143895551], ["Mexico", 132328035],
              ["Japan", 126854745], ["Ethiopia", 110135635],
              ["Philippines", 108106310], ["Egypt", 101168745],
              ["Vietnam", 97429061], ["DR Congo", 86727573],
              ["Turkey", 82961805], ["Iran", 82820766], ["Germany", 82438639],
              ["Thailand", 69306160], ["Niue", 1628],
              ["United Kingdom", 66959016], ["France", 65480710],
              ["Tanzania", 60913557], ["Italy", 59216525],
              ["South Africa", 58065097], ["Myanmar", 54336138],
              ["Kenya", 52214791], ["South Korea", 51339238],
              ["Colombia", 49849818], ["Spain", 46441049], ["Uganda", 45711874],
              ["Argentina", 45101781],
              ["Ukraine", 43795220], ["Algeria", 42679018], ["Sudan", 42514094],
              ["Iraq", 40412299],
              ["Poland", 38028278], ["Canada", 37279811],
              ["Afghanistan", 37209007], ["Morocco", 36635156],
              ["Saudi Arabia", 34140662], ["Peru", 32933835],
              ["Uzbekistan", 32807368], ["Venezuela", 32779868],
              ["Malaysia", 32454455], ["Angola", 31787566],
              ["Mozambique", 31408823], ["Ghana", 30096970],
              ["Nepal", 29942018], ["Yemen", 29579986],
              ["Madagascar", 26969642], ["North Korea", 25727408],
              ["Côte d'Ivoire", 25531083], ["Cameroon", 25312993],
              ["Australia", 25088636], ["Tokelau", 1340], ["Holy See", 799]]
df19 = pd.DataFrame(POPULATION)
map = Map()
map.add("", [list(z) for z in zip(df19[0].tolist(), df19[1].tolist())], maptype="world")
map.render('./19.html')
# 20.使用pyechras绘制双Y轴图
x = list(range(1, 8))
y = [17, 17, 18, 15, 11, 11, 13]
y1 = [i + 2 for i in y]
bar1 = Bar()
bar2 = Bar()
bar1.add_xaxis(x)
bar2.add_xaxis(x)
bar1.add_yaxis('', y_axis=y)
bar1.extend_axis(yaxis=opts.AxisOpts())
bar2.add_yaxis('', y_axis=y1, yaxis_index=1)
bar1.overlap(bar2)
bar1.render('./20.html')
