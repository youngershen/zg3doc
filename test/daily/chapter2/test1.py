# Project: ZG3Doc
# File : test1.py
# Date : 2023/4/14 9:39
# Author: Younger Shen <申延刚>
# Web: https://github.com/youngershen
# Cell: 13811754531
# Wechat: 13811754531
# Email : shenyangang@163.com

import pandas as pd


def print_line(count=50):
    print('=' * 50)


"""
1．读取附件中的天津天气2020年10月.csv文件到df中

解析:

1. 使用 pd.read_csv 这个方法读入 csv 文件, 不要用错方法
不同类型的文件用不同的方法

2. 因为文件的第一行数据不标准, 所以直接删除使用 df.drop, 
直接修改读入的 df, 注意参数, index 与 inplace 的用法

3. 最后不要忘记输出 df

"""
print_line()
print("第一题:")
df = pd.read_csv('./data/天津天气2020年10月.csv')
df.columns = df.loc[0]
print(df.columns)  # df.columns 获取字段名
df.drop(index=0, inplace=True)  # drop删除 index是行索引  inplace=True叫原地修改
print(df)

"""
2．增加一个气温差值列，气温最大值和最小值的差值

解析:

1. 首席是要明确如何求温差, 即用每一行的
温度最大值减去温度最小值即可

2 因为数据不标准, 需要进行简单的数据处理, 这里
使用字符串操作, 先去掉 ℃, 然后通过 '/'
作为分隔符, 切分字符串, 前者为最大值, 后者为
最大值

3. 最后是 df.apply 这个方法的应用,
它会再每一行或列上应用它第一个参数指定的函数,

axis 用来指定行或者列
0 为操作列
1 为操作行
"""
print_line()
print("第二题:")


def func1(x):
    max_x = x['气温'].replace('℃', '').split('/')[0]
    min_x = x['气温'].replace('℃', '').split('/')[1]
    return f'{int(max_x) - int(min_x)}℃'


df['气温差值'] = df.apply(func1, axis=1)

"""
3．增加一个气温类型列，如果最大值大于20，代表高温，小于等于20代表低温

解析:


"""
def func1(x):
    max_x = x['气温'].replace('℃', '').split('/')[0]
    return '高温' if int(max_x) > 20 else '低温'


df['气温类型'] = df.apply(func1, axis=1)


# 4．修改2020年10月31日的数据，天气改为晴
def func2(x):
    if x['日期'] == '2020年10月31日':
        x['天气状况'] = '晴'
    return x['天气状况']


df['天气状况'] = df.apply(func2, axis=1)
print(df)
df.loc[df['日期'] == '2020年10月31日', '天气状况'] = '晴'
print(df)

# 5．将原有的列名，日期修改为date
df.rename(columns={'日期': 'date'}, inplace=True)

# 6．删除2020年10月1日的数据
df.drop(index=df[df['date'] == '2020年10月1日'].index, inplace=True, axis=0)

# 7．将df写入到天津天气2020年10月.html文件中
df.to_html('./data/天津天气2020年10月.html')

# 8．通过列表lt1 = ['西游记', '水浒传', '三国演义', '红楼梦'] 创建series 结构数据se1
lt1 = ['西游记', '水浒传', '三国演义', '红楼梦']
s1 = pd.Series(lt1)

# 9．通过列表lt2 = [['西游记', '吴承恩'],['水浒传', '施耐庵'],
# ['三国演义', '罗贯中'], ['红楼梦', '曹雪芹']]创建 Dataframe 结构数据df1
lt2 = [['西游记', '吴承恩'], ['水浒传', '施耐庵'],
       ['三国演义', '罗贯中'], ['红楼梦', '曹雪芹']]
df1 = pd.DataFrame(lt2)
print(df1)

# 10．获取df1中第1行第2列数据
print(df1[1][0])
