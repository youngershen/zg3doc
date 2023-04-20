# Project: ZG3Doc
# File : class3.py
# Date : 2023/4/20 10:13
# Author: Younger Shen <申延刚>
# Web: https://github.com/youngershen
# Cell: 13811754531
# Wechat: 13811754531
# Email : shenyangang@163.com
import pandas as pd
"""
1. apply 方法的简单应用

给每一行, 添加一列, 列名是 总分, 通过 apply

"""

# 姓名, 数学分数, 语文分数, 英语分数
a1 = [
    ['jack', 1, 2, 3],
    ['jack2', 4, 5, 6],
    ['jack3', 7, 8, 9],
    ['jack4', 10, 11, 12],
]


def score_sum(col):
    s = col['数学'] + col['语文'] + col['英语']
    return s


df1 = pd.DataFrame(a1, columns=['姓名', '数学', '语文', '英语'])
print(df1)
df1['总分'] = df1.apply(score_sum, axis=1)
print(df1)

"""
1. 生成一个包含 姓名, 语文分数, 数学分数, 英语分数 的二位数组

a1 = [['name', 'yuwen', 'shuxue', 'yingyu'] ....... ]

2. 使用 for in 循环的方式, 统计每一个学生的总分

3. 把总分插入到相应的行里

"""
