# Project: ZG3Doc
# File : test2.py
# Date : 2023/4/20 8:24
# Author: Younger Shen <申延刚>
# Web: https://github.com/youngershen
# Cell: 13811754531
# Wechat: 13811754531
# Email : shenyangang@163.com
import pandas as pd
from sqlalchemy import create_engine

# 按要求执行以下步骤
# 1．读取附件中的lagou.json文件到df中

# 2．增加一个平均薪资列，为薪资范围的平均值

# 3．增加一个经验类型列，如果经验为1-3年为初级开发，3-5年为中级开发，5年以上为高级开发

# 4．修改索引为4的数据，重新命名职位名称

# 5．删除经验范围列

# 6．删除经验在校，以及经验不限的数据

# 7．将df写入到本地数据库mysql中，表自定义

# 8．通过列表lt1 = ['python进阶', 'python数据分析', 'python基础', 'python数据采集']创建series结构数据se1

# 9．通过列表lt2 = [['python进阶', '专高一'],['python数据分析', '专高三'],
# ['python基础', '专业四'], ['python数据采集', '专高四']]
# 创建Dataframe结构数据df1

# 10．获取df1中专高三的课程名称
