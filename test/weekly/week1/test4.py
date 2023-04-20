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


def print_line(count=50):
    print("=" * count)


"""
一 使用 numpy 和 pandas 三方库等, 实现以下要求, 代码放在 week1.py 文件中:
"""

# 1. 使用["cat","dog","deer","fish","monkey"] 生成一个 numpy 数组
print_line()
a1 = np.array(["cat", "dog", "deer", "fish", "monkey"])
print("第 1 题:")
print(a1)

# 2. 生成一个元素值全为 5 长度为 20的一维数组
print_line()
print("第 2 题:")
a2 = np.array(['5'] * 20)
print(a2)

# 3. 对第 2 题中的一维数组增加一维，形成形状为 (20，1）的数组
print_line()
print("第 3 题:")
a2 = a2.reshape((20, 1))
print(a2)

# 4.生成一个形状为（3，3，3）、元素值依次为1-27的三维数组
print_line()
print("第 4 题:")
a4 = np.arange(1, 28).reshape((3, 3, 3))
print(a4)

# 5. 选取第 4 题中的数组的第 0-2 行, 1-2列, 打印筛选后的值
print_line()
print("第 5 题")
a5 = a4[0:3, 1:3, :]
print(a5)

# 6. 使用 [["li",80,70,100],["yang",70,80,99],["zhang",60,70,100]]
# 数据初始化一个 pandas 的 dataframe 数据集
# 列名依次为 ["uid","en","cn","ma"]
print_line()
print("第 6 题")
df6 = pd.DataFrame(columns=["uid", "en", "cn", "ma"],
                   data=[["li", 80, 70, 100], ["yang", 70, 80, 99],
                         ["zhang", 60, 70, 100]])
print(df6)

# 7.使用 [["li",80,70,100],["yang",70,80,99],["zhang",60,70,100]]
# 数据初始化一个pandas的dataframe数据集，列名依次为["uid","en","cn","ma"]，
# 初始化方法不能与第 6 题使用的方法相同
print_line()
print("第 7 题")

#  第一种方法
print("第一种方法")
d7 = [["li", 80, 70, 100], ["yang", 70, 80, 99], ["zhang", 60, 70, 100]]
c7 = ["uid", "en", "cn", "ma"]

df7 = pd.DataFrame(data=d7, columns=c7)
print(df7)

# 第二种方法
print("第二种方法")
d8 = {"uid": ["li", "yang", "zhang"],
      "en": [80, 70, 60],
      "cn": [70, 80, 70],
      "ma": [100, 99, 100]}

df8 = pd.DataFrame(d8)
print(df8)

# 第三种方法
print("第三种方法")
df = pd.DataFrame(columns=["uid", "en", "cn", "ma"])

df.loc[0] = ["li", 80, 70, 100]
df.loc[1] = ["yang", 70, 80, 99]
df.loc[2] = ["zhang", 60, 70, 100]

print(df)

# 8. 使用 {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
# 'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3]}
# 作为数据, 使用 ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# 作为索引初始化一个 dataframe 数据集
print_line()
print("第 8 题")
df8 = pd.DataFrame(
    index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],
    data={'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
          'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3]})

print(df8)

# 9. 对第 8 题中的数据集的 age 字段值按照均值进行空值填充处理
print_line()
print("第 9 题")
df8.fillna(value=df8['age'].mean(), axis=1, inplace=True)
print(df8)

# 10. 对第 9 题中处理后的数据集按照 age 字段进行降序排序, 打印排序后结果
print_line()
print("第 10 题")
df8.sort_values(by='age', ascending=False, inplace=True)
print(df8)

"""
二 使用适当的 python 库进行综合数据分析，代码保存为 week2.py
"""

# 11.读取 diamonds.csv 生成数据集 df, 对数据集的数据质量进行评价
print_line()
print("第 11 题:")
df11 = pd.read_csv('./diamonds.csv')
print("生成数据集:")
print(df11.head(3))
print("评价")
print("空置数量:")
print(df.isnull().sum())
print("重复值数量")
print(df.duplicated().sum())
print("非法值数量:")
print(df.isna().sum())

# 12.对数据集中符合连续型数据的字段进行统计性描述
print_line()
print("第 12 题:")
df12 = df11.describe()
print(df12)

# 13. 根据 cut 字段计算每一个等级（clarity字段）钻石的数量
print_line()
print("第 13 题:")
df13 = df11.groupby(by='cut')['clarity'].count()
print(df13)

# 14.根据 color 字段进行分组, 统计 carat 字段最大值、最小值、均值
print_line()
print("第 14 题:")
df14 = df11.groupby(by='color').agg({'carat': ['max', 'min', 'mean']})
print(df14)

# 15. 先按字段color, 再按字段 cut 分组, 计算 carat 字段的总和
print_line()
print("第 15 题:")
df15 = df11.groupby(by=['color', 'cut'])['carat'].sum()
print(df15)

# 16. 筛选 carat 字段值大于 3.5 的数据, 生成新的数据集, 保存为 excel 文件
print_line()
print("第 16 题:")
print("生成 34.xlsx")
df11[df11['carat'] > 3.5].to_excel('./34.xlsx')

# 17. 根据 price 字段值进行处理
# 生成一个新列level
# price大于等于2000时
# level值设置为 1
# 否则设置为 0
print_line()
print("第 17 题:")
df11['level'] = df11.apply(lambda x: 1 if x['price'] >= 2000 else 0, axis=1)
print(df11.head(3))

# 18. 对第 17 题的数据
# 筛选 carat 字段值大于3.2
# level 字段值为 1 的数据，保存到 excel 文件
print_line()
print("第 18 题:")
df11[(df11['carat'] > 3.2) & (df11['level'] == 1)].to_excel('./18.xlsx')
print("生成 18.xlsx")

# 19. 对 df 数据集按照 carat, price 字段进行升序排序
# 保存到excel文件
print_line()
print("第 19 题:")
df11.sort_values(by=['carat', 'price'], ascending=True).to_excel('./19.xlsx')
