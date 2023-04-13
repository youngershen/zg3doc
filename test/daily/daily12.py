# Project: ZG3Doc
# File : day12.py
# Date : 2023/4/13 14:59
# Author: Younger Shen <申延刚>
# Web: https://github.com/youngershen
# Cell: 13811754531
# Wechat: 13811754531
# Email : shenyangang@163.com
import numpy as np
from test.utils import print_line
"""
日考一 第二套习题

题干:

1．创建数字从 1 到 20 的 1 维数组arr，需要满足能被3整除不能被5整除
2．请将给定的数组np.array([100,103,106,108,112,116,118,136,138,139])中的奇数批量替换为33
3．请生成一个从201-300的一维数组，并将这个一维数组转化为10行10列的二维数组
4．有两个数组，x=np.array([436,556,607,899]),y=np.array([556,559,607,936,966]),请使用合适的方法获取两个数组的公共项
5．计算给定数组np.array([33,35,60,70,85])和np.array([44,51,65,73,80])之间的欧氏距离
6．输入数字n，创建数字从 1 到 n 的 1 维数组arr，将 arr 中的所有奇数替换成 -1
7．给定数组[1, 2, 3, 4, 5]，获取到平均值，将平均值插入到每个元素直接得到新的数组
8．创建一个5*5的随机值数组，并找到最大值，并替换为0

"""


"""
   1．创建数字从 1 到 20 的 1 维数组arr，需要满足能被3整除不能被5整除

   分析: 先使用 arange 创建 1 到 20 的数组
   然后使用布尔索引直接过滤
   注意条件不要写错
   """
print_line()
arr = np.arange(1, 21)
condition = (arr % 3 == 0) & (arr % 5 != 0)
arr2 = arr[condition]
print("1．创建数字从 1 到 20 的 1 维数组arr，需要满足能被3整除不能被5整除:")
print(arr2)

"""
2．请将给定的数组np.array([100,103,106,108,112,116,118,136,138,139])中的奇数批量替换为 33

分析: 收件创建数组, 然后使用布尔索引, 最后赋值
需要注意的是条件不能写错
"""
print_line()
arr = np.array([100, 103, 106, 108, 112, 116, 118, 136, 138, 139])
arr[arr % 2 == 1] = 33
print("2．请将给定的数组np.array([100,103,106,108,112,116,118,136,138,139])中的奇数批量替换为 33")
print(arr)

"""
3．请生成一个从201-300的一维数组，
并将这个一维数组转化为10行10列的二维数组

分析: 
首先生成一位数组, 注意第二个下标
然后通过 reshape 改编数组的形状
"""
print_line()
arr = np.arange(201, 301)
arr2 = arr.reshape((10, 10))
print("3. 请生成一个从201-300的一维数组，并将这个一维数组转化为10行10列的二维数组")
print("原数组:")
print(arr)
print("新数组:")
print(arr2)

"""
4．有两个数组，x=np.array([436,556,607,899]),
y=np.array([556,559,607,936,966]),
请使用合适的方法获取两个数组的公共项

分析:
直接使用 np.intersect1d 方法进行
公共项的查找
"""
print_line()
x = np.array([436, 556, 607, 899])
y = np.array([556, 559, 607, 936, 966])
common_items = np.intersect1d(x, y)

print(
    "4．有两个数组，x=np.array([436,556,607,899]),y=np.array([556,559,607,936,966]),请使用合适的方法获取两个数组的公共项")
print("公共项为:")
print(common_items)

"""
5．计算给定数组np.array([33,35,60,70,85])
和np.array([44,51,65,73,80])之间的欧氏距离

分析:

直接调用 np.linalg.norm() 函数即可得到结果,
欧氏距离简单的说就是 n 维空间中点的距离, 
n 维不好立即的话可想象成笛卡尔坐标系
中的两个点, 只不过 n 维空间有 n 个坐标
实质还是两个点之间的距离

欧氏距离的概念:
https://baike.baidu.com/item/欧几里得度量
"""
print_line()
x = np.array([33, 35, 60, 70, 85])
y = np.array([44, 51, 65, 73, 80])
distance = np.linalg.norm(x - y)
print("5．计算给定数组np.array([33,35,60,70,85]) 和 np.array([44,51,65,73,80])之间的欧氏距离")
print("结果为:")
print(distance)

"""
6．输入数字n，创建数字从 1 到 n 
的 1 维数组arr，将 arr
中的所有奇数替换成 -1

分析:
使用 input 输入数字, 要注意
类型非法, 其次就是使用布尔索引
筛选和更改奇数的值
"""
while True:
    print_line()
    n = input("请输入一个数字:")
    try:
        n = int(n)
    except ValueError:
        print("输入错误请重试")
    else:
        arr = np.arange(1, n)
        arr[arr % 2 == 1] = -1
        print("结果为:")
        print(arr)
        break

"""
7．给定数组[1, 2, 3, 4, 5]，
获取到平均值，
将平均值插入到每个元素直接得到新的数组

分析:
首先生成数组, 不需多言
其次就是调用 mean 求数组平均
最后调用 np.insert 往
原数组中插入, 注意 insert
的参数的用法, 第二个参数为数组时
会将 mean 值直接插入到所有的位置中
"""
print_line()
# 定义数组
arr = np.array([1, 2, 3, 4, 5])
# 计算平均值
mean = np.mean(arr)
# 插入操作
new_arr = np.insert(arr, range(len(arr)), mean)
print(" 7．给定数组[1, 2, 3, 4, 5], 获取到平均值, 将平均值插入到每个元素直接得到新的数组")
print("原数组为:")
print(arr)
print("新数组为:")
print(new_arr)

"""
8．创建一个5*5的随机值数组，并找到最大值，并替换为0

分析:
首先创建随机数组使用 random 相关方法,注意维度
寻找最大值私用 np.max方法
插入值使用布尔索引随后赋值
"""
print_line()
arr = np.random.randint(0, 100, size=(5, 5))
m = np.max(arr)
print("8．创建一个5*5的随机值数组，并找到最大值，并替换为0")
print("原数组为:")
print(arr)
print("最大值为:")
print(m)
print("替换之后的数组为:")
arr[arr == m] = 0
print(arr)
