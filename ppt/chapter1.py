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

"""
numpy 的安装, 执行 pip install numpy
指定源安装 (如果上面的方法安装比较慢, 可以使用下面的方法用于加速安装)
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple
"""
import numpy as np  # 引入相应的包


def case1():
    """
    数组的定义
    该案例涉及到了 numpy 中创建数组的主要方法
    需要熟练应用, 多加练习
    """

    # 使用 python 数组创建 numpy 的数组
    a1 = np.array([1, 2, 3, 4, 5])
    print(a1)

    print("=========================")
    # 使用 np.empty 创建 numpy 数组
    a2 = np.empty([3, 3], dtype=np.int32)
    print(a2)


def case2():
    """
    numpy

    :return:
    """
    pass


def case3():
    pass


def main():
    pass


if __name__ == '__main__':
    main()