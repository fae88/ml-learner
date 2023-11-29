# 导入 matplotlib.pyplot 库
import matplotlib.pyplot as plt
 # 导入 scipy.stats 库
from scipy import stats
 # 定义 x 轴和 y 轴的值
x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]
 # 使用 stats.linregress() 函数计算回归直线的斜率、截距、相关系数、p 值和标准误差
slope, intercept, r, p, std_err = stats.linregress(x, y)
 # 定义回归直线的函数
def myfunc(x):
  return slope * x + intercept
 # 使用 map() 函数将 x 轴的值映射到回归直线的函数上，得到回归直线的值
mymodel = list(map(myfunc, x))
 # 使用 plt.scatter() 函数绘制散点图
plt.scatter(x, y)
 # 使用 plt.plot() 函数绘制回归直线
plt.plot(x, mymodel)
 # 使用 plt.show() 函数显示图像
plt.show()