# Project: ZG3Doc
# File : test3.py
# Date : 2023/4/14 9:40
# Author: Younger Shen <申延刚>
# Web: https://github.com/youngershen
# Cell: 13811754531
# Wechat: 13811754531
# Email : shenyangang@163.com
import pandas as pd

from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:root@127.0.0.1:3306/2009a')


# 读取hotel.xlsx文件，文件包含全国各城市酒店及价格数据
df = pd.read_excel('./hotel.xlsx')
# 按beds的降序，和originalPrice的升序，对酒店数据进行排序操作
df.sort_values(by=['beds', 'originalPrice'], ascending=[False, True], inplace=True)
# 将cityName等于”北京“，tuanType列的数据修改为”四星级“
df.loc[df[df['cityName'] == '北京'].index, 'tuanType'] = '四星级'
# 筛选出所有cityName为”澳门“的数据,保留cityName，originalPrice这两列
df1 = df[df['cityName'] == '澳门']['cityName']
df2 = df[df['cityName'] == '澳门']['originalPrice']
df3 = pd.merge(df1, df2, left_index=True, right_index=True, how='inner')
# 将上面的筛选结果写入html文件
df3.to_json('./hotel.html')
# 将上面的结果写入到本地的mysql中
df3.to_sql('hotel', con=engine)