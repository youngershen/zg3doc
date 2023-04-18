# Project: ZG3Doc
# File : chapter1.py
# Date : 2023/4/12 14:26
# Author: Younger Shen <申延刚>
# Web: https://github.com/youngershen
# Cell: 13811754531
# Wechat: 13811754531
# Email : shenyangang@163.com
"""
第一单元 - 数据分析基础概念与 numpy 入门
该单元主要涉及 numpy 的概念以及常规操作,
需要实践的部分比较多, 比较好的方法就是
多动手去实践案例
"""

import numpy as np  # 引入相应的包


def print_line(count=40):
    print("=" * count)


def case1():
    """
    案例一 : Numpy 的安装
    pip install numpy -i https://pypi.tuna.tsinghua.edu.cn/simple
    """
    pass


def case2():
    """
    案例二 - Numpy 的简单介绍:

    NumPy是Python中科学计算的基础包。它是一个Python库，
    提供多维数组对象，各种派生对象（如掩码数组和矩阵），
    以及用于数组快速操作的各种API，
    有包括数学、逻辑、形状操作、排序、选择、输入输出、离散傅立叶变换、
    基本线性代数，基本统计运算和随机模拟等等。

    NumPy包的核心是 ndarray 对象。
    它封装了python原生的同数据类型的 n 维数组，
    为了保证其性能优良，
    其中有许多操作都是代码在本地进行编译后执行的。
    """
    pass


def case3():
    """
    案例三 - Numpy 的参考文档

    https://numpy.org/ (Numpy 的官方网站, 有很多重要的文档, 学习和工作都可以从这个网站开始)
    https://www.numpy.org.cn/ (Numpy 的中文网站, 英文不好的可以参考, 但是有滞后)
    https://www.runoob.com/numpy/numpy-tutorial.html (另一个 Numpy 的参考文档)
    """
    pass


def case4():
    """
    案例四 - 多维数组的概念

    NumPy 最重要的一个特点是其 N 维数组对象 ndarray，
    它是一系列同类型数据的集合，以 0 下标为开始进行集合中元素的索引。
    ndarray 对象是用于存放同类型元素的多维数组。
    ndarray 中的每个元素在内存中都有相同存储大小的区域。
    """

    a1 = [1, 2, 3, 4, 5]
    print("Python 一维数组:")
    print(a1)

    a2 = np.array([6, 7, 8, 8, 10])
    print("Numpy 中的一维数组:")
    print(a2)

    a3 = [[1, 2, 3], [4, 5, 6]]
    print("Python 的二维数组:")
    print(a3)

    a4 = np.array([1, 2, 3, 4, 5, 6]).reshape(2, 3)
    print("Numpy 中的二维数组:")
    print(a4)


def case5():
    """
    案例五 - 多维数组的数据类型

    numpy 支持的数据类型比 Python 内置的类型要多很多，
    基本上可以和 C 语言的数据类型对应上，
    其中部分类型对应为 Python 内置的类型。
    下表列举了常用 NumPy 基本类型。
    """

    # int32 类型
    dt = np.dtype(np.int32)
    print("Numpy 中的 int32 类型:")
    print(dt)

    # int64 类型
    dt = np.dtype(np.int64)
    print("Numpy 中的 int64 类型:")
    print(dt)

    # float32 类型
    dt = np.dtype(np.float32)
    print("Numpy 中的 float32 类型:")
    print(dt)

    # bool 类型
    dt = np.dtype(np.bool_)
    print("Numpy 中的 bool 类型")
    print(dt)

    pass


def case6():
    """
    案例六 - 多维数组的创建
    """

    # 使用 python 数组创建 numpy 数组
    a0 = [1, 2, 3, 4, 5]
    a1 = np.array(a0, dtype=np.int32)
    print("创建 int32 类型 numpy 数组:")
    print(a1)

    a2 = np.array(a0, dtype=np.int64)
    print("创建 int64 类型 numpy 数组:")
    print(a2)

    # 创建布尔数组
    a3 = np.array(a0, dtype=np.bool_)
    print("创建 bool 类型 numpy 数组:")
    print(a3)


def case7():
    """
    案例七 - 多维数组的属性

    np.ndim 维度:

    即轴的数量或维度的数量
    """
    a1 = np.array([1, 2, 3])
    print("输出一维数组的维度:")
    print(a1)
    print(a1.ndim)

    a2 = np.array([[1, 2, 3], [4, 5, 6]])
    print("输出二维数组的维度:")
    print(a2)
    print(a2.ndim)

    # 自己动手创建一个 3维数组, 然后输出它的维度

    """
    ndarray.shape 数组的形状，对于矩阵，n 行 m 列
    """
    print_line()
    a3 = np.arange(24)
    print("输出 a3 数组:")
    print(a3)

    print("输出 a3 的维度")
    print(a3.ndim)
    # 现在调整其大小
    print("调整 a3 的形状")
    a4 = a3.reshape((2, 3, 4))  # b 现在拥有三个维度
    print(a4.shape)
    print(a4.ndim)

    """
    ndarray.size 数组元素的总个数，相当于 .shape 中 n*m 的值
    """
    print_line()
    a5 = np.array([[1, 2, 3], [4, 5, 6]])
    print("输出数组 a5:")
    print(a5)
    print("输出数组 a5 的元素个数, 2  * 3 = ?")
    print(a5.size)


def case8():
    """
    案例八 - 多维数组的创建

    数组的创建是 numpy 中非常重要的内容, numpy 中的数组拥有
    多种不同的创建方法
    """

    """
    1. 使用 python 数组创建 numpy 数组
    """
    print_line()
    a1 = np.array([1, 2, 3, 4])
    print("一维数组的创建:")
    print(a1)

    """
    2. 二维数组的创建
    """
    print_line()
    a2 = np.array([[1, 2, 3], [4, 5, 6]])
    print("二维数组的创建:")
    print(a2)


def case9():
    """
    案例九 - 多维数组的普通索引
    """
    pass


def case10():
    """
    案例十 - 多维数组的高级索引
    """
    pass


def case11():
    """
    案例 11 - 多维数组的相关操作
    """


def case12():
    """
    案例 12 - 多维数组的广播
    """
    pass


def case13():
    """
    案例 13 - Numpy 中的常用函数
    """
    pass


def main():
    # case4()
    # case5()
    # case6()
    # case7()
    case8()
    # case9()
    # case10()
    # case11()
    # case12()
    # case13()
    pass


if __name__ == '__main__':
    main()
