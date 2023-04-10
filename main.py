import numpy as np
# 直接创建数组
a1 = [1, 2, 3, 4, 5]
a2 = np.array(a1)

# 创建二维数组
a3 = np.array([[1,3], [3, 4]])

# 创建随机数组
a4 = np.random.randint(0, 10, size=(3, 3))
print(a4)
