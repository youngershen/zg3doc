# Project: ZG3Doc
# File : test2.py
# Date : 2023/4/14 10:20
# Author: Younger Shen <申延刚>
# Web: https://github.com/youngershen
# Cell: 13811754531
# Wechat: 13811754531
# Email : shenyangang@163.com
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