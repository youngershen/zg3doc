# Project: ZG3Doc
# File : test10.py
# Date : 2023/4/18 9:55
# Author: Younger Shen <申延刚>
# Web: https://github.com/youngershen
# Cell: 13811754531
# Wechat: 13811754531
# Email : shenyangang@163.com
"""
读取titanic.csv数据文件, 生成dataframe。数据集中字段survived 为标签，其他字段为特征数据候选字段
对数据集age、fare字段的缺失值进行处理，采用适当的数据填充方法
使用相关性分析方法，选取合适字段作为特征字段，对数据集进行特征处理，例如数据类型转换等
将数据集按8:2比例划分为训练集和测试集，输出训练集样本数，测试集样本数
使用逻辑回归函数建立模型，并开始训练，对模型性能进行评估，对结果评估结果进行恰当的描述
基于模型预测结果，分析影响生存的主要因素，分析各个特征与生成率之间的关系，使用图表进行展示，并以注释形式解释结果
"""

import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('D:\\bw\上课资料\\3\\titanic.csv')

#11对数据集age、fare字段的缺失值进行处理，采用适当的数据填充方法
df['age'].fillna(df['age'].mean(), inplace=True)
df['fare'].fillna(df['fare'].mean(), inplace=True)

# 根据相关性，挑选 pclass, fare, adult_male, alone 做为特征
df = df[['pclass', 'fare', 'adult_male', 'alone', 'survived']]


#12 使用相关性分析方法，选取合适字段作为特征字段，对数据集进行特征处理，例如数据类型转换等
#print(df.corr())
df['adult_male'] = df['adult_male'].apply(lambda x: 1 if x else 0)
df['alone'] = df['alone'].apply(lambda x: 1 if x else 0)

#
x = df[['pclass', 'fare', 'adult_male', 'alone']]
y = df['survived']

#13将数据集按8:2比例划分为训练集和测试集，输出训练集样本数，测试集样本数
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8)
#print(df.head())

#14 使用逻辑回归函数建立模型，并开始训练，对模型性能进行评估，对结果评估结果进行恰当的描述
from sklearn.linear_model._logistic import LogisticRegression
model = LogisticRegression()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
from sklearn.metrics import accuracy_score
score = accuracy_score(y_test, y_pred)
#print('score', score)
#15基于模型预测结果，分析影响生存的主要因素，分析各个特征与生存率之间的关系，使用图表进行展示，并以注释形式解释结果
from pyecharts.charts import Bar

# bar.render('../templates/14.html')
x_test['predict_s'] = y_pred
gender = x_test.groupby('adult_male')['predict_s'].sum()
bar = Bar()
bar.add_xaxis(gender.index.tolist())
bar.add_yaxis('', gender.values.tolist())
print('aaa', gender.values.tolist())
bar.render('D:\\bw\上课资料\\3\\gender.html')

