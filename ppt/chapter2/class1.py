# Project: ZG3Doc
# File : class1.py
# Date : 2023/4/20 10:13
# Author: Younger Shen <申延刚>
# Web: https://github.com/youngershen
# Cell: 13811754531
# Wechat: 13811754531
# Email : shenyangang@163.com
import pandas as pd
import numpy as np

"""
1. 安装 pandas
pip install pandas -i https://pypi.tuna.tsinghua.edu.cn/simple
"""

"""
2. 使用 numpy 创建一个随机一维数组, 使用这个一维数组创建 pd.Series
"""
print("第三题:")
a1 = np.random
print(a1)
s1 = pd.Series(a1)
print(s1)

"""
3. 创建一个包含有, 姓名, 年龄, 分数的, 二维数组, 
然后通过这个数组, 船舰一个 pd.DataFrame 对象

创建一个成绩单, 包含有, 姓名, 语文, 数学, 英语, 分数,
创建成 pd.DataFrame

"""
print("第三题:")
a1 = [['jack', '18', '100'], ['mary', '20', '95']]
d1 = pd.DataFrame(a1, columns=['姓名', '年龄', '分数'])
print(d1.loc[1])


"""
4. 读取北京天气2009文件, 输出前 8 行
"""
print("第四题")
a4 = pd.read_json('data/beijing_tianqi_2019.json')
print(a4.head(8))
