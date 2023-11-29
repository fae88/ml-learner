from matplotlib import pyplot as plt
import matplotlib
from matplotlib.pyplot import*
import numpy as np
import math
#title
plt.title("私有汽车拥有量")
#设置中文
plt.rcParams['font.sans-serif']=['SimHei']
years=['2012年', '2013年', '2014年', '2015年', '2016年', '2017年', '2018年', '2019年', '2020年', '2021年']
num=[8838.60,10501.68,12339.36,14099.10,16330.22,18515.11,20574.93,22508.99,24291.19,26152.02]
#标签
plt.xlabel("年份")
plt.ylabel("拥有量")
from scipy.optimize import minimize
from numpy import ones
def obj(ans):
    a,b=ans
    sum=0.0
    for i in range(len(num)):
       sum+=(a*i+b-num[i])**2
    return sum
res=minimize(obj,ones(2))
print(res.x)
a,b=res.x
def F(x):
    return a*x+b
x1=[i/100 for i in range(1001)]
y1=[F(i/100) for i in range(1001)]
plt.plot(years,num)
plt.plot(x1,y1)
plt.show()