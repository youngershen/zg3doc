# Project: ZG3Doc
# File : daily1.py
# Date : 2023/4/12 14:33
# Author: Younger Shen <申延刚>
# Web: https://github.com/youngershen
# Cell: 13811754531
# Wechat: 13811754531
# Email : shenyangang@163.com
import numpy as np
from test.utils import print_line


"""
日考一 第一套习题

一定好好好练习哦 
知识点老师都讲过的 
不懂的随时问老师 
"""


def case1():
    """
    1．创建数字从 0 到 9 的 1 维数组arr

    分析: 使用 np.arange 函数直接创建,
    做不出来是就去看 np.arange 函数的用法
    """
    arr = np.arange(0, 10, 1)
    print("输出创建的包含 0 - 9 的数组:")
    print(arr)

    """
    2．从 arr 中提取所有奇数
    
    分析: 数组中数据的筛选这里使用到了布尔筛选
    方法是在方括号里放入一个返回值为
    布尔类型的表达式, 奇数的筛选方法为
    任意数模 2 结果如果是 1 , 那么久判定它为奇数
    不理解的话就去看关于布尔检索的内容
    """
    print_line()
    print("arr 输出奇数:")
    print(arr[arr % 2 == 1])

    """
    3．将 arr 中的所有奇数替换成 -1
    
    分析: 与第二问类似, 只是赋值直接把筛选出的
    奇数换成了 -1
    """
    print_line()
    arr[arr % 2 == 1] = -1
    print("输出将 arr 中的奇数替换为 -1 之后的数组:")
    print(arr)

    """
    4．将 arr  数组转换成 2 维数组arr2
    
    分析: 使用 reshape 改变数组形状
    不会做就去查 reshape 的文档
    """
    print_line()
    arr2 = arr.reshape((2, 5))
    print("将 arr 变形为 (2,5) 的二维数组")
    print(arr2)

    """
    5．获取arr2的轴的数量
    
    分析: 使用 ndim 参数即可直接得到 arr2
    的轴的数量
    """
    print_line()
    d = arr2.ndim
    print("arr2 的轴的数量为:")
    print(d)

    """
    6．获取arr2的第1行第2列
    
    分析: 使用下标索引即可
    """
    print_line()
    print("获取 arr2 的第 1 行, 第 2 列")
    print(arr2[1, 2])
    print(arr2[1][2])
    print(arr2[(1, ), (2, )])

    """
    7．获取arr2的数组元素总个数
    
    分析: 使用数组元素的 array.size 属性
    即可直接得到数组中元素的个数,
    即为形状元组中的两个数的乘积
    """
    print_line()
    print("arra2 元素总个数:")
    count = arr2.size
    print(count)

    """
    8．获取arr2的元素类型
    
    分析: 使用数组元素中的 dtype 即
    可直接得到数组元素的类型
    """
    print_line()
    print("arr2 中元素的类型为:")
    print(arr2.dtype)


    pass


"""
日考一 第二套习题
"""


def case2():
    pass


"""
日考一 第三套习题
"""


def case3():
    pass


def case11():
    """
    日习题 1.1
    创建数字从 0 到 9 的 1 维数组arr
    """
    # 方法 1, 直接使用 python 数组生成 numpy 数组
    print_line()
    print("方法 1, 直接使用 python 数组生成 numpy 数组")
    a1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(a1)

    # 方法 2, 使用 python 的生成器生成 numpy 数组
    print_line()
    print("方法 2, 使用 python 的生成器生成 numpy 数组")
    a2 = np.array([i for i in range(0, 10)])
    print(a2)

    # 方法 3, 使用 np.narange 生成数组
    print_line()
    print("方法 3, 使用 np.narange 生成数组")
    a3 = np.arange(0, 10)
    print(a3)


def case12():
    """
    日习题 1.2
    从 arr 中提取所有奇数
    """
    # 生成一个数组
    print_line()
    a1 = np.arange(0, 10, 1)
    # 方法1 使用布尔索引来取出奇数
    a2 = a1[a1 % 2 == 1]
    print("方法1 使用布尔索引来取出奇数")
    print(a2)

    # 方法2 对数组进行遍历挨个输出
    print_line()
    print("方法2 对数组进行遍历挨个输出")
    for i in a1:
        print(i) if i % 2 == 1 else None


def case13():
    """
    日习题 1.3
    将 arr 中的所有奇数替换成 -1
    """
    # 创建一个数组
    a1 = np.arange(0, 10)
    print_line()
    print("创建一个数组")
    print(a1)

    # 方法 1. 使用布尔索引选择然后替换
    print_line()
    print("方法 1. 使用布尔索引选择然后替换")
    a1[a1 % 2 == 1] = -1
    print(a1)


def case14():
    """
    日习题 1.4 将 arr  数组转换成 2 维数组arr2
    """
    # 创建数组
    arr = np.arange(0, 10)
    print("原数组为:")
    print(arr)

    print_line()
    print("reshape 之后的数组为:")
    # 直使用 reshape 改编数组的形状
    arr2 = arr.reshape((2, 5))
    print(arr2)

    """
    日习题 1.5 获取arr2的轴的数量
    """
    print_line()
    # 获取 arr2 轴的数量
    n = arr2.ndim
    print("arr2 轴的数量为: ")
    print(n)

    """
    日习题 1.6 获取arr2的第1行第2列
    """


def main():
    case1()
    pass


if __name__ == '__main__':
    main()
