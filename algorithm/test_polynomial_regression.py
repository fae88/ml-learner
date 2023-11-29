# 导入 numpy 库
import numpy
# 导入 matplotlib.pyplot 库
import matplotlib.pyplot as plt

# 定义 x 轴和 y 轴的值
x = [1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 21, 22]
y = [100, 90, 80, 60, 60, 55, 60, 65, 70, 70, 75, 76, 78, 79, 90, 99, 99, 100]

# 使用 numpy.polyfit() 函数拟合三次多项式
mymodel = numpy.poly1d(numpy.polyfit(x, y, 1))

# 使用 numpy.linspace() 函数生成 100 个点
myline = numpy.linspace(1, 22, 1000)

# 使用 plt.scatter() 函数绘制散点图
plt.scatter(x, y)

# 使用 plt.plot() 函数绘制拟合曲线
plt.plot(myline, mymodel(myline))

# 使用 plt.show() 函数显示图像
plt.show()
