# Project: ZG3Doc
# File : test2.py
# Date : 2023/4/14 9:40
# Author: Younger Shen <申延刚>
# Web: https://github.com/youngershen
# Cell: 13811754531
# Wechat: 13811754531
# Email : shenyangang@163.com
import pandas as pd

from sqlalchemy import create_engine

# 按要求执行以下步骤
# 读取附件中电子病历.xlsx文件
df = pd.read_excel('./电子病历.xlsx')
# 判断文件是否有缺失值并过滤掉该记录即可
# print(df.isnull())
df.drop(df[df.isnull().all(axis=1) == True].index, inplace=True)
# 按”等级要求“的降序，和”分值“的升序，对电子病历进行排序
df.sort_values(by=['等级要求', '分值'], ascending=[False, True], inplace=True)
# 将上面整理后df，重新写入到电子病历.json文件中
df.to_json('./电子病历.json')
# 将上面整理后df，写入到本地的mysql数据库中
con = create_engine('mysql+pymysql://root:root@localhost:3306/2009a')
df.to_sql('电子病历', con=con, if_exists='replace')