# Project: ZG3Doc
# File : daily2.py
# Date : 2023/4/12 14:33
# Author: Younger Shen <申延刚>
# Web: https://github.com/youngershen
# Cell: 13811754531
# Wechat: 13811754531
# Email : shenyangang@163.com
import pandas as pd
from test.utils import print_line
"""
日考二 第一套题

要求执行以下步骤
1．读取附件中的天津天气2020年10月.csv文件到df中
2．增加一个气温差值列，气温最大值和最小值的差值
3．增加一个气温类型列，如果最大值大于20，代表高温，小于等于20代表低温
4．修改2020年10月31日的数据，天气改为晴
5．将原有的列名，日期修改为date
6．删除2020年10月1日的数据
7．将df写入到天津天气2020年10月.html文件中
8．通过列表lt1 = ['西游记', '水浒传', '三国演义', '红楼梦']创建series结构数据se1
如图： 
9．通过列表lt2 = [['西游记', '吴承恩'],['水浒传', '施耐庵'], 
['三国演义', '罗贯中'], ['红楼梦', '曹雪芹']]
创建Dataframe结构数据df1
如图： 
10．获取df1中第1行第2列数据
"""

"""
1．读取附件中的天津天气2020年10月.csv文件到df中

分析:

知识点涉及到 pd.read_csv 的用法
重新设置列明, 以及使用 df.drop 
删除行的用法
"""
print_line()
df = pd.read_csv('./data/天津天气2020年10月.csv')
df.columns = df.loc[0]
df.drop(index=0, inplace=True)  # drop删除 index 是行索引  inplace=True 叫原地修改
print("1．读取附件中的天津天气2020年10月.csv文件到df中:")
print(df.head())

"""
2．增加一个气温差值列，气温最大值和最小值的差值

分析: 
1. 首先时是给 df 增加列的知识点
2. 其次是 df.apply 的使用,
3. 重点是 df.apply 中的回调函数的写法, 
以及子串的处理方法

注意在进行减法的时候, 要把 str 准换为 int
"""
print_line()


def get_temp_diff(row):
    high, low = row['气温'].split('/')
    high = int(high.replace('℃', ''))
    low = int(low.replace('℃', ''))
    return f'{high - low}℃'


df['温差'] = df.apply(get_temp_diff, axis=1)
print("2．增加一个气温差值列，气温最大值和最小值的差值")
print(df.head(3))

"""
3．增加一个气温类型列，如果最大值大于20，代表高温，小于等于20代表低温

分析:
还是使用 df.apply 进行计算
然后就是列的增加
"""
print_line()


def show_temp(row):
    t = int(row['温差'].replace('℃', ''))
    return "高温" if t > 20 else "低温"


df['气温类型'] = df.apply(show_temp, axis=1)
print("3．增加一个气温类型列，如果最大值大于20，代表高温，小于等于20代表低温")
print(df.head(3))

"""
修改2020年10月31日的数据，天气改为晴
"""