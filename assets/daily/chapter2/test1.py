# Project: ZG3Doc
# File : test1.py
# Date : 2023/4/14 9:39
# Author: Younger Shen <申延刚>
# Web: https://github.com/youngershen
# Cell: 13811754531
# Wechat: 13811754531
# Email : shenyangang@163.com

import pandas as pd

# 1．读取附件中的天津天气2020年10月.csv文件到df中
df = pd.read_csv('./天津天气2020年10月.csv')
df.columns = df.loc[0]
print(df.columns)  # df.columns 获取字段名
df.drop(index=0, inplace=True)  # drop删除 index是行索引  inplace=True叫原地修改


# 2．增加一个气温差值列，气温最大值和最小值的差值
def func(x):
    max_x = x['气温'].replace('℃', '').split('/')[0]
    min_x = x['气温'].replace('℃', '').split('/')[1]
    return f'{int(max_x) - int(min_x)}℃'


df['气温差值'] = df.apply(func, axis=1)


# 3．增加一个气温类型列，如果最大值大于20，代表高温，小于等于20代表低温
def func1(x):
    max_x = x['气温'].replace('℃', '').split('/')[0]
    return '高温' if int(max_x) > 20 else '低温'


df['气温类型'] = df.apply(func1, axis=1)
# 4．修改2020年10月31日的数据，天气改为晴
# def func2(x):
#     if x['日期'] == '2020年10月31日':
#         x['天气状况'] = '晴'
#     return x['天气状况']
# df['天气状况'] = df.apply(func2, axis=1)
# print(df)
df.loc[df['日期'] == '2020年10月31日', '天气状况'] = '晴'
# print(df)
# 5．将原有的列名，日期修改为date
df.rename(columns={'日期': 'date'}, inplace=True)
# 6．删除2020年10月1日的数据
df.drop(index=df[df['date'] == '2020年10月1日'].index, inplace=True, axis=0)
# 7．将df写入到天津天气2020年10月.html文件中
df.to_html('./天津天气2020年10月.html')
# 8．通过列表lt1 = ['西游记', '水浒传', '三国演义', '红楼梦']创建series结构数据se1
# 如图：
lt1 = ['西游记', '水浒传', '三国演义', '红楼梦']
s1 = pd.Series(lt1)
# 9．通过列表lt2 = [['西游记', '吴承恩'],['水浒传', '施耐庵'], ['三国演义', '罗贯中'], ['红楼梦', '曹雪芹']]创建Dataframe结构数据df1
# 如图：
lt2 = [['西游记', '吴承恩'], ['水浒传', '施耐庵'],
       ['三国演义', '罗贯中'], ['红楼梦', '曹雪芹']]
df1 = pd.DataFrame(lt2)
print(df1)
# 10．获取df1中第1行第2列数据
print(df1[1][0])
