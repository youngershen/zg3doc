# Project: ZG3Doc
# File : daily1.py
# Date : 2023/4/12 14:33
# Author: Younger Shen <申延刚>
# Web: https://github.com/youngershen
# Cell: 13811754531
# Wechat: 13811754531
# Email : shenyangang@163.com
import numpy as np


def print_line(count=50):
    line = '=' * count
    print(line)


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

    # 方法 2.
    print_line()
    print("方法2")
    print(a1)


def main():
    case13()
    # case12()
    # case11()
    pass


if __name__ == '__main__':
    main()
