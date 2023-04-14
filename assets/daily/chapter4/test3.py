# Project: ZG3Doc
# File : test3.py
# Date : 2023/4/14 9:41
# Author: Younger Shen <申延刚>
# Web: https://github.com/youngershen
# Cell: 13811754531
# Wechat: 13811754531
# Email : shenyangang@163.com
import pandas as pd

# 1．读取附件航空公司会员.xlsx文件，形成一个dataframe
df = pd.read_excel('航空公司会员.xlsx')
# 2．按会员卡级别的降序，年龄的升序，对数据进行排序
df.sort_values(by=['会员卡级别', '年龄'], ascending=[False, True], inplace=True)
# 3．增加一列，列名为"普通积分"，为总积分与精英积分的差值
df['普通积分'] = df.apply(lambda x: x['总积分'] - x['精英积分'], axis=1)
# 4．增加一列，列名为“会员特征”，条件为：会员卡级别大于5，同时年龄小于40，为“明日之星”；否则为“普通会员”
df['会员特征'] = df.apply(lambda x: '明日之星' if x['会员卡级别'] > 5 and x['年龄'] < 40 else '普通会员', axis=1)
# 5．通过会员级别分组，统计每组年龄的平均值
df1 = df.groupby(by='会员级别')['年龄'].mean()
# 6．先通过性别，再通过会员级别分组，获取飞行次数的最大值，平均值
df2 = df.groupby(by=['性别', '会员级别']).agg({'飞行次数': ['max', 'mean']})
# 7．统计明日之星下的总积分的平均值
df3 = df[df['会员特征'] == '明日之星']['总积分'].mean()
# 8．获取每个国家的普通积分的情况
df4 = df.groupby(by='国家')['普通积分'].max()