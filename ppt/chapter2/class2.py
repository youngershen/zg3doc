# Project: ZG3Doc
# File : class2.py
# Date : 2023/4/20 10:13
# Author: Younger Shen <申延刚>
# Web: https://github.com/youngershen
# Cell: 13811754531
# Wechat: 13811754531
# Email : shenyangang@163.com
import numpy as np
import pandas as pd
"""
1. dataframe 的 loc 检索方式

生成一个 5*5 的 ndarray,
使用 abcde 作为 index
使用 a1, b1, c1, d1, e1 作为 columns

最后使用 loc 方式, 检索出第 a - d 行
"""

a1 = np.random.randint(0, 100, 5*5).reshape((5, 5))
print(a1)
d1 = pd.DataFrame(a1, index=list('abcde'), columns=['a1',
                                                    'b1',
                                                    'c1',
                                                    'd1',
                                                    'e1'])
print(d1)
print(d1.loc['a', 'b1'])


"""
2. dataframe 的 iloc 的检索方式
随机生成一个 二维 ndarray
使用 iloc 检索出它的第 3 - 5 行

"""


"""
3. at 检索方式, 检索某一格的值

1) 建立一个 5 * 5 的随机二维整数数组
2) 检索出, 它的第 (0, 1) (1, 3) (2, 4) 个数字并输出
"""

print("第三题")
a3 = np.random.randint(0, 100,  5 * 5).reshape((5, 5))
print(a3)
d3 = pd.DataFrame(a3)
print(d3)

i1 = d3.at[0, 1]
print(i1)

i2 = d3.at[[[0, 1], [1, 3]]]
print(i2)




"""
4. iat 使用整数, 检索某一格的值
"""


"""
5. 直接索引, 使用 df[] 的方式进行索引

1). df 里即可以是数字, 也可以是列名, 或者索引名
2). 花式索引 和 切片的应用
"""