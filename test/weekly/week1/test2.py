# Project: ZG3Doc
# File : test2.py
# Date : 2023/4/14 10:27
# Author: Younger Shen <申延刚>
# Web: https://github.com/youngershen
# Cell: 13811754531
# Wechat: 13811754531
# Email : shenyangang@163.com
"""
专高三 周考一 2022 年 11 月
"""
import numpy as np
import pandas as pd


def print_line(count=50):
    print("=" * count)


# 1. 创建一个长度为 10 的一维数组, 元素值为整数
print_line()
print("第 1 题:")
a1 = np.arange(0, 10)
print(a1)

# 2.创建一个形状为 (4,5) 的二维数组, 元素值为小数
print_line()
print("第 2 题:")
a2 = np.random.rand(4, 5)
print(a2)


# 3.创建一个形状为 (1,5) 的数组, 元素值为字符串
print_line()
print("第 3 题:")
a3 = np.array(['a', 'b', 'c', 'd', 'e'])
print(a3)

# 4. 使用 np.arang e生成一个长度为 10 的数组 a
print_line()
print("第 4 题:")
a = np.arange(10)
print(a)

# 5. 基于上题中的数组 a 使用 full_like 创建元素值为全 1 的一维数组 b
print_line()
print("第 5 题:")
a = np.arange(10)
b = np.full_like(a, 1)
print(b)

# 6. 选择数组 a 中序号为奇数的元素, 组成新的数组, 并打印
print_line()
print("第 6 题:")
a = np.arange(10)
b = a[1::2]  # a[开始:结束:步长]
print(b)

# 7. 创建一个形状为 (10, 2, 5) 的随机数组，变形为 (10，10)，形成数组 c
print_line()
print("第 7 题:")
a7 = np.random.rand(10, 2, 5)
c = a7.reshape(10, 10)
print(c)

# 8. 选取数组 c 最后一列, 并打印
print_line()
print("第 8 题:")
print(c[:, -1])

# 9. 使用列表 [1,2,3,4,5,6] 初始化为一个形状为 (2,3) 的数组 d, 新增一列，元素值为 7,8
print_line()
print("第 9 题:")
d = np.arange(1, 7).reshape((2, 3))
c = np.array([[7], [8]])
d = np.hstack((d, c))
print(d)

# 10. 使用列表 [1,2,3,4,5,6] 初始化为一个形状为 (2,3)
# 的数组f, 使用 insert 函数在第 0 行后面新增一行,
# 元素值为 7,8,9
print_line()
print("第 10 题:")
f = np.array([1, 2, 3, 4, 5, 6]).reshape(2, 3)
new_row = np.array([[7, 8, 9]])
f = np.insert(f, 1, new_row, axis=0)
print(f)

# 11. 用 1-20 之间的数字,
# 创建一个形状为（4,5) 的数组 g,
# 按行求和, 按行累加, 打印结果
print_line()
print("第 11 题:")
g = np.arange(1, 21).reshape(4, 5)
print(g)
sum_by_row = np.sum(g, axis=1)  # 按行求和
cum_sum_by_row = np.cumsum(g, axis=1)  # 按行累加
print("按行求和：")
print(sum_by_row)
print("按行累加：")
print(cum_sum_by_row)

# 12. 按列对数组 g 计算中位数, 均值, 最大值和最小值
print_line()
print("第 12 题:")
median_col = np.median(g, axis=0)
mean_col = np.mean(g, axis=0)
max_col = np.max(g, axis=0)
min_col = np.min(g, axis=0)
print("中位数:")
print(median_col)
print("均值:")
print(mean_col)
print("最大值:")
print(max_col)
print("最小值:")
print(min_col)

# 13. 两个列表 ls1 = [1,2,3],
# ls2 = [4,5,6],
# 使用 numpy 的 hstack 合并为一个数组 h1
# 使用 vstack 合并为一个数组 h2
print_line()
print("第 13 题:")
ls1 = [1, 2, 3]
ls2 = [4, 5, 6]
# 水平合并
print("水平合并:")
h1 = np.hstack((ls1, ls2))
print(h1)
# 垂直合并
print("垂直合并:")
h2 = np.vstack((ls1, ls2))
print(h2)

# 14. 使用 numpy 对数组 h1 进行操作, 形状为 (1,6) 使用 squeeze 函数压缩为一维数组
"""
这将使用 NumPy 中的 reshape() 
函数将数组 h1 从形状 (1, 6) 转换为一维数组，
并用 -1 表示让 NumPy 根据原始数组大小自动计算新形状中的缺失维度。
然后，使用 squeeze() 函数去除多余的维度
得到了形状为 (6,) 的一维数组。
"""
print_line()
print("第 14 题:")
ls1 = [1, 2, 3]
ls2 = [4, 5, 6]
# 水平合并
h1 = np.hstack((ls1, ls2))
# 压缩为一维数组
h1 = np.squeeze(h1.reshape(1, -1))
print(h1)

# 15. 读取数据文件 car_crashes.csv，形成数据集 df
print_line()
print("第 15 题:")

df = pd.read_csv("car_crashes.csv")
print(df.head(3))

# 16. 获取 df 数据集的第二列数据, 请说明返回的是什么对象类型
print_line()
print("第 16 题:")
f = df.iloc[:, 1]
print(type(f))

# 17. 选取 df 数据集的第 4-5 行，第 2-4 列, 并打印
print_line()
print("第 17 题:")
df17 = df.iloc[3:5, 1:4]
print(df17)


# 18. 选取 df 数据集最后一列以字符 ’A’ 开头的记录, 并打印
"""
要选取 df 数据集中最后一列以字符 ’A’ 
开头的记录, 可以使用 DataFrame 的布尔索引功能.
先获取数据集最后一列的列名, 
然后对该列进行字符串匹配并返回一个布尔数组.
最后将该布尔数组用作行索引, 
即可选取符合条件的记录.
"""
print_line()
print("第 18 题:")
# 获取最后一列的列名
last_col_name = df.columns[-1]
# 选取最后一列以字符 ’A’ 开头的记录
selected_df = df[df[last_col_name].str.startswith('A')]
# 打印结果
print(selected_df)

# 19. 对 df 数据集按照字段 speeding 进行降序排序, 并打印
print_line()
print("第 19 题:")
# 按字段 speeding 进行降序排序
sorted_df = df.sort_values(by=['speeding'], ascending=False)
# 打印结果
print(sorted_df)


# 20. 对 df 数据集的字段 ins_losses 进行操作,
# 值大于100为1, 否则为0, 形成一个新列 flag
"""
可以使用 Pandas 的 apply() 
方法对 DataFrame 的某一列进行操作
并根据条件生成新的一列
在本题中，我们需要对 ins_losses 列进行操作
如果该列的值大于 100，则将对应位置的 flag 置为 1，否则置为 0。
"""
print_line()
print("第 20 题:")
df = pd.read_csv('car_crashes.csv')

# 对 ins_losses 列进行操作，生成新的 flag 列
df['flag'] = df['ins_losses'].apply(lambda x: 1 if x > 100 else 0)
# 打印结果
print(df.head())
