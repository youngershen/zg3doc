# Project: ZG3Doc
# File : test2.py
# Date : 2023/4/14 10:27
# Author: Younger Shen <申延刚>
# Web: https://github.com/youngershen
# Cell: 13811754531
# Wechat: 13811754531
# Email : shenyangang@163.com
"""
专高三 周考一 2023 年 1 月
"""
import numpy as np
import pandas as pd

"""
一 使用 numpy 和 pandas 三方库等, 实现以下要求, 代码放在 week1.py 文件中:
"""

# 1.使用["cat","dog","deer","fish","monkey"]生成一个numpy数组
a1 = np.array(["cat", "dog", "deer", "fish", "monkey"])
print(a1)

# 2.生成一个元素值全为5、长度为20的一维数组
# arr2 = np.zeros(20, dtype=int)
# arr2[arr2 == arr2] = 5
# print(arr2)
arr2 = np.array([5 for i in range(20)])
# print(arr2)
# 3.对第2题中的一维数组增加一维，形成形状为(20，1）的数组
arr3 = arr2.reshape(20, 1)
# 4.生成一个形状为（3，3，3）、元素值依次为1-27的三维数组
arr4 = np.arange(1, 28).reshape((3, 3, 3))
# 5.选取第4题中的数组的第0-2行、1-2列，打印筛选后的值
arr5 = arr4[:3, :, 1:]
# 6.使用[["li",80,70,100],["yang",70,80,99],["zhang",60,70,100]]
# 数据初始化一个pandas的dataframe数据集，列名依次为["uid","en","cn","ma"]
df = pd.DataFrame(columns=["uid", "en", "cn", "ma"],
                  data=[["li", 80, 70, 100], ["yang", 70, 80, 99],
                        ["zhang", 60, 70, 100]])
# 7.使用[["li",80,70,100],["yang",70,80,99],["zhang",60,70,100]]
# 数据初始化一个pandas的dataframe数据集，列名依次为["uid","en","cn","ma"]，
# 初始化方法不能与第6题使用的方法相同

# ## 差点代码  ####
dic = {'uid': ['li', 'yang', 'zhang'], 'en': [80, 70, 60], 'cn': [70, 80, 70],
       'ma': [100, 99, 100]}
df1 = pd.DataFrame(dic)
# 8.使用 {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake',
# 'cat', 'dog', 'dog'], 'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan,
# 7, 3]} 作为数据，使用 ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# 作为索引初始化一个dataframe数据集
df8 = pd.DataFrame(index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],
                   data={'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat',
                                    'snake', 'cat', 'dog', 'dog'],
                         'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3]})
# 9.对第8题中的数据集的age字段值按照均值进行空值填充处理
df8.fillna(value=df8['age'].mean(), axis=1, inplace=True)
# 10.对第9题中处理后的数据集按照age字段进行降序排序，打印排序后结果
df8.sort_values(by='age', ascending=False, inplace=True)
# （二）使用适当的python库进行综合数据分析，代码保存为week2.py：
# 11.读取diamonds.csv生成数据集df，对数据集的数据质量进行评价
df = pd.read_csv('./data/diamonds.csv')
# 12.对数据集中符合连续型数据的字段进行统计性描述
df12 = df.describe()
# 13.根据cut字段计算每一个等级（clarity字段）钻石的数量
df13 = df.groupby(by='cut')['clarity'].count()
# 14.根据color字段进行分组，统计carat字段最大值、最小值、均值
df14 = df.groupby(by='color').agg({'carat': ['max', 'min', 'mean']})
# 15.先按字段color、再按字段cut分组，计算carat字段的总和
df15 = df.groupby(by=['color', 'cut'])['carat'].sum()
# 16.筛选carat字段值大于3.5的数据，生成新的数据集，保存为excel文件
df[df['carat'] > 3.5].to_excel('./data/34.xlsx')
# 17.根据price字段值进行处理，生成一个新列level，price大于等于2000时，level值设置为1，否则设置为0
df['level'] = df.apply(lambda x: 1 if x['price'] >= 2000 else 0, axis=1)
# 18.对第17题的数据，筛选carat字段值大于3.2、level字段值为1的数据，保存到excel文件
df[(df['carat'] > 3.2) & (df['level'] == 1)].to_excel('./data/18.xlsx')
# 19.对df数据集按照carat、price字段进行升序排序，保存到excel文件
df.sort_values(by=['carat', 'price']).to_excel('./data/19.xlsx')
# 删除字段x,y,z，生成新的数据集，保存到excel文
df.drop(columns=['x', 'y', 'z']).to_excel('./data/20.xlsx')