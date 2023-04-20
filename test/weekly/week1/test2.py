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

"""
（一）使用numpy和pandas三方库等，实现以下要求，代码放在week1.py文件中： 
1.	创建一个长度为10的一维数组，元素值为整数
2.	创建一个形状为(4,5)的二维数组，元素值为小数
3.	创建一个形状为(1,5)的数组，元素值为字符串
4.	使用np.arange生成一个长度为10的数组a
5.	基于上题中的数组a使用full_like创建元素值为全1的一维数组b
6.	选择数组a中序号为奇数的元素，组成新的数组，并打印
7.	创建一个形状为(10，2，5)的随机数组，变形为(10，10)，形成数组c
8.	选取数组c最后一列，并打印
9.	使用列表[1,2,3,4,5,6]初始化为一个形状为(2,3)的数组d，新增一列，元素值为7,8
10.	使用列表[1,2,3,4,5,6]初始化为一个形状为(2,3)的数组f，使用insert函数在第0行后面新增一行，元素值为7,8,9
11.	使用1-20之间的数字，创建一个形状为（4,5)的数组g，按行求和、按行累加，打印结果
12.	按列对数组g计算中位数，均值，最大值和最小值
13.	两个列表ls1 = [1,2,3]，  ls2 = [4,5,6]，使用numpy的hstack合并为一个数组h1；使用vstack合并为一个数组h2
14.	使用numpy对数组h1进行操作，形状为(1,6)，使用squeeze函数压缩为一维数组
15.	读取数据文件car_crashes.csv，形成数据集df
16.	获取df数据集的第二列数据，请说明返回的是什么对象类型
17.	选取df数据集的第4-5行，第2-4列，并打印
18.	选取df数据集最后一列以字符’A’开头的记录，并打印
19.	对df数据集按照字段speeding进行降序排序，并打印
20.	对df数据集的字段ins_losses进行操作，值大于100为1，否则为0，形成一个新列flag
"""