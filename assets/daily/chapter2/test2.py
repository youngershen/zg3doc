# Project: ZG3Doc
# File : test2.py
# Date : 2023/4/14 9:39
# Author: Younger Shen <申延刚>
# Web: https://github.com/youngershen
# Cell: 13811754531
# Wechat: 13811754531
# Email : shenyangang@163.com
# 按要求执行以下步骤
# 1．读取附件中的lagou.json文件到df中
df = pd.read_json('./lagou.json')
# 2．增加一个平均薪资列，为薪资范围的平均值
def func(x):
    min_x = x['薪资'].replace('k', '').split('-')[0]
    max_x = x['薪资'].replace('k', '').split('-')[1]
    return f'{(int(max_x) + int(min_x)) / 2}k'


df['平均薪资'] = df.apply(func, axis=1)
# 3．增加一个经验类型列，如果经验为1-3年为初级开发，3-5年为中级开发，5年以上为高级开发
def func1(x):
    if x['经验范围'] == '经验1-3年': return '初级开发'
    elif x['经验范围'] == '经验3-5年': return '中级开发'
    elif x['经验范围'] == '经验5-10年': return '高级开发'
    else: return ''


df['经验类型'] = df.apply(func1, axis=1)
# 4．修改索引为4的数据，重新命名职位名称
df.loc[4, '职位名称'] = 'React开发'
# 5．删除经验范围列
# df.drop('经验范围', axis=1, inplace=True)
# print(df)
# 6．删除经验在校，以及经验不限的数据
df.drop(df[df['经验范围'].isin(['经验在校', '经验不限'])].index, axis=0, inplace=True)
# 7．将df写入到本地数据库mysql中，表自定义
user = 'root'
pwd = 'root'
db = '2009a'
host = 'localhost'
port = 3306
con = create_engine(f'mysql+pymysql://{user}:{pwd}@{host}:{port}/{db}')
df.to_sql('lagou', con=con, if_exists='replace')
# 8．通过列表lt1 = ['python进阶', 'python数据分析', 'python基础', 'python数据采集']创建series结构数据se1
lt1 = ['python进阶', 'python数据分析', 'python基础', 'python数据采集']
se1 = pd.Series(lt1)
# 9．通过列表lt2 = [['python进阶', '专高一'],['python数据分析', '专高三'], ['python基础', '专业四'], ['python数据采集', '专高四']]创建Dataframe结构数据df1
lt2 = [['python进阶', '专高一'],['python数据分析', '专高三'], ['python基础', '专业四'], ['python数据采集', '专高四']]
df1 = pd.DataFrame(lt2)
print(df1)
# 10．获取df1中专高三的课程名称
df1.rename(columns={0: '课程名称', 1: '阶段'}, inplace=True)
print(df1[df1['阶段'] == '专高三']['课程名称'])
