# Project: ZG3Doc
# File : test4.py
# Date : 2023/4/14 11:31
# Author: Younger Shen <申延刚>
# Web: https://github.com/youngershen
# Cell: 13811754531
# Wechat: 13811754531
# Email : shenyangang@163.com

"""
2022 年 12 月
"""

# （一）创建名为my_line.py的文件，完成相关多元线性回归的操作（30分,每题5分)
# 1）读取附件美国某地区房价.csv
# 2）获取数据，对美国某地区的房价，建立多元线性回归模型
# 3）拟合数据
# 4）获取回归模型的斜率,截距
# 5）回归模型评估
# 6）预测街区为B的，面积为110平的，卧室为3个，房屋样式为ranch的房屋的价格为多少

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import KMeans

df = pd.read_csv('/Users/wenjie/Documents/八维/pythonProject/美国某地区房价.csv')
x = df[['所属街区', '面积', '卧室', '房屋样式']]
y = df['价格']
line = LinearRegression()
le = LabelEncoder()
x['所属街区'] = le.fit_transform(x['所属街区'])
x['房屋样式'] = le.fit_transform(x['房屋样式'])

x_train, x_test, y_train, y_test = train_test_split(x, y)
line.fit(x_train, y_train)
print(line.coef_)
print(line.intercept_)
print(line.predict(np.array([1, 110, 3, 0]).reshape(1, -1)))
#
# （二）创建名为my_sklearn.py的文件，完成相关聚类算法的操作（40分,每题5分)
# 7）读取附件中的car_price.csv到df中
df = pd.read_csv('/Users/wenjie/Documents/八维/pythonProject/car_price.csv')
# 8）预处理数据，
df.fillna(value=0, inplace=True)
# 9）建立训练集
train_x = df[df.columns.tolist()]
# 10）将每个要素缩放到给定范围，拟合数据，然后对其进行转换
le = LabelEncoder()
columns = ['CarName', 'fueltype', 'aspiration', 'doornumber', 'carbody',
           'drivewheel', 'enginelocation', 'enginetype', 'cylindernumber',
           'fuelsystem']
for column in columns:
    # LabelEncoder().transform将标签转换为归一化的编码。fit_transform安装标签编码器
    # 并返回编码的标签。
    train_x[column] = le.fit_transform(train_x[column])
# 11）选择聚类组数
kmeans = KMeans(n_clusters=5)
# 12）计算聚类中心并预测每个样本的聚类索引
kmeans.fit(train_x)  # 也可以直接fit+predict
predict_y = kmeans.predict(train_x)
# 13）合并聚类结果，插入到原数据中,axis： 需要合并链接的轴，0是行，1是列
result = pd.concat((df, pd.DataFrame(predict_y)), axis=1)
# 14）找出vokswagen汽车的聚类结果
label = result[result['CarName'].str.contains('vokswagen')][0]
#
# （三）创建名为my_sklearn_2.py的文件，完成相关聚类算法的操作（30分,每题5分)
# 15）训练集x_train为 '关键词是能够表达文档中心内容的词语，常用于计算机系统标引论文内容特征、
# 信息检索、系统汇集以供读者检阅。关键词提取是文本挖掘领域的一个分支，是文本检索、文档比较、
# 摘要生成、文档分类和聚类等文本挖掘研究的基础性工作',
# 测试集x_test为 '关键词、检索、文本、文档'
# 16）将文本中的词语转换为词频矩阵
# 17）统计每个词语的tf-idf权值
# 18）将文本转为词频矩阵并计算tf-idf
# 19）对测试集进行tf-idf权重计算
# 20）输出训练集的文本向量，测试集的文本向量
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

x_train = ['关键词是能够表达文档中心内容的词语，常用于计算机系统标引论文内容特征、',
           '信息检索、系统汇集以供读者检阅。关键词提取是文本挖掘领域的一个分支，',
           '是文本检索、文档比较、摘要生成、文档分类和聚类等文本挖掘研究的基础性工作']
x_test = ['关键词', '检索', '文本', '文档']

# 该类会将文本中的词语转换为词频矩阵，矩阵元素a[i][j] 表示j词在i类文本下的词频
vectorizer = CountVectorizer(max_features=10)
# 该类会统计每个词语的tf-idf权值
tf_idf_transformer = TfidfTransformer()
# 将文本转为词频矩阵并计算tf-idf
tf_idf = tf_idf_transformer.fit_transform(vectorizer.fit_transform(x_train))
# 将tf-idf矩阵抽取出来，元素a[i][j]表示j词在i类文本中的tf-idf权重
x_train_weight = tf_idf.toarray()

# 对测试集进行tf-idf权重计算
tf_idf = tf_idf_transformer.transform(vectorizer.transform(x_test))
x_test_weight = tf_idf.toarray()  # 测试集TF-IDF权重矩阵

print('输出x_train文本向量：')
print(x_train_weight)
print('输出x_test文本向量：')
print(x_test_weight)