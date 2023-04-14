# Project: ZG3Doc
# File : test3.py
# Date : 2023/4/14 10:18
# Author: Younger Shen <申延刚>
# Web: https://github.com/youngershen
# Cell: 13811754531
# Wechat: 13811754531
# Email : shenyangang@163.com
from math import log
import operator


def score_ent(data):
    """
    计算数据的熵
    :param data: 数据集
    :return:
    """
    all_num = len(data)  # 获取数据集的条数
    label_counts = {}  # 每一个性别出现的次数
    for i in data:
        current_label = i[-1]  # 获取每行数据的最后一列  --- 性别
        if current_label not in label_counts.keys():
            label_counts[current_label] = 0
        label_counts[current_label] += 1
    ent_num = 0
    for i in label_counts:
        prob = float(label_counts[i]) / all_num  # 计算每个类别的熵值
        ent_num -= prob * log(prob, 2)  # 累计每个类别的熵值
    return ent_num


def split_data(data, axis, value):
    """
    按照某个特征分类得到最后的数据
    :param data:
    :param axis:
    :param value:
    :return:
    """
    result = []
    for i in data:
        if i[axis] == value:
            # 过滤掉匹配到的那一项,获取剩下的部分
            reduced = i[:axis]
            reduced.extend(i[axis + 1:])
            result.append(reduced)
    return result


def choose_best_data(data):
    """
    选择到最优的分类特征数据
    :param data:
    :return:
    """
    num_features = len(data[0]) - 1
    # 获取最开始的熵值
    base_ent = score_ent(data)
    base_gain = 0
    best_feature = -1
    for i in range(num_features):
        feat_list = set([j[i] for j in data])
        new_ent = 0
        for z in feat_list:
            sub_data_set = split_data(data, i, z)
            prob = len(sub_data_set) / float(len(data))
            new_ent += prob * score_ent(sub_data_set)
        info_gain = base_ent - new_ent  # 原始的熵与按照特征分类后的熵的差值
        if info_gain > base_gain:  # 如果分类完毕后,熵值减少最大的那个分类,称之为最优的分类
            base_gain = info_gain
            best_feature = i
    return best_feature


def majority_cnt(class_list):
    """
    按照分类后类别数量进行排序
    :param class_list:
    :return:
    """
    class_count = {}
    for i in class_list:
        if i not in class_count.keys():
            class_count[i] = 0
        class_count[i] += 1
    sorted_class_count = sorted(class_count.items(),
                                key=operator.itemgetter(1), reverse=True)
    return sorted_class_count[0][0]


def create_data():
    # 根据上述的数据 进行创建数据集
    # 武器类型  子弹  血量  行为类别
    # 步枪  少  少  逃跑
    # 机枪  多  多  战斗
    # 步枪  多  少  逃跑
    # 机枪  少  多  战斗
    # 步枪  少  多  战斗
    # 机枪  多  少  逃跑
    # 步枪  多  多  战斗
    # 机枪  少  少  逃跑
    data = [
        ['步枪', '少', '少', '逃跑'],
        ['机枪', '多', '多', '战斗'],
        ['步枪', '多', '少', '逃跑'],
        ['机枪', '少', '多', '战斗'],
        ['步枪', '少', '多', '战斗'],
        ['机枪', '多', '少', '逃跑'],
        ['步枪', '多', '多', '战斗'],
        ['机枪', '少', '少', '逃跑'],
    ]
    labels = ['武器类型', '子弹', '血量']
    return data, labels


def creat_tree(data, labels):
    """创建决策树模型"""
    class_list = [i[-1] for i in data]  # 获取类别  : 男或女
    if class_list.count(class_list[0]) == len(class_list):
        return class_list[0]
    if len(data[0]) == 1:
        return majority_cnt(class_list)
    best_feat = choose_best_data(data)  # 获取最优特征
    best_feat_label = labels[best_feat]
    # 分类后的结果以字典的形式进行保存返回
    my_tree = {best_feat_label: {}}
    del(labels[best_feat])
    feat_values = set([i[best_feat] for i in data])
    for i in feat_values:
        sub_labels = labels[:]
        my_tree[best_feat_label][i] = creat_tree(split_data(data, best_feat, i),
                                                 sub_labels)
    return my_tree


if __name__ == '__main__':
    data, labels = create_data()
    result = creat_tree(data, labels)
    print(result)