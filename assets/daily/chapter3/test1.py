# Project: ZG3Doc
# File : test1.py
# Date : 2023/4/14 9:40
# Author: Younger Shen <申延刚>
# Web: https://github.com/youngershen
# Cell: 13811754531
# Wechat: 13811754531
# Email : shenyangang@163.com
import pandas as pd

# 按要求执行以下步骤
# 1．读取附件中的北京空气质量指数.csv文件到df中
df = pd.read_csv('./北京空气质量指数.csv')
# 2．判断文件中是否有缺失值
# 3．过滤掉全为缺失值的那一行
# print(df.isnull().count())  # 计算每一列的数据的个数,并不会对缺失值进行判断
# print(df.isnull().sum())  # 返回每一列的缺失值的个数
# print(df.isnull().any())  # 返回每一列是不是有缺失值,如果有的话返回True,没有返回False
# print(df.isnull().all())  # 每一列都为缺失值的话返回True,否则返回False
df.drop(df[df.isnull().all(axis=1) == True].index, inplace=True)
# 4．进行数据清洗动作
#  缺失值进行删除  缺失值进行填充
df.fillna(value=0, inplace=True)
# 5．分别按PM10，PM2.5两列进行排序
df.sort_values(by=['PM10', 'PM2.5'], inplace=True, ascending=[True, False])
# 6．将排序后的df，原有的列名Co，No2，So2，O3修改为一氧化碳，二氧化氮，二氧化硫，臭氧
df.rename(columns={'Co': '一氧化碳', 'No2': '二氧化氮', 'So2': '二氧化硫',
                   'O3': '臭氧'}, inplace=True)
# 7．将上面整理后df，重新写入到北京空气质量指数.json文件中
df.to_json('./北京空气质量指数.json')
# 8．将上述的df写入到本地的html文件，通过浏览器展示
df.to_html('./北京空气质量指数.html')
