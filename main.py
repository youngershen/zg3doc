import numpy as np

"""
4．有两个数组，x=np.array([436,556,607,899]),
y=np.array([556,559,607,936,966]),
请使用合适的方法获取两个数组的公共项

"""
x = np.array([436, 556, 607, 899])
y = np.array([556, 559, 607, 936, 966])
arr4 = np.intersect1d(x, y)
print(arr4)