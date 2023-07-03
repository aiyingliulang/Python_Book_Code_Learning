# coding=utf-8
import matplotlib.pyplot as plt

x_values = range(1,5001)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn')
fig,ax = plt.subplots()
ax.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Reds,s=10)

# 设置图表标题并给坐标轴加上标签。
ax.set_title("立方数",fontsize=24,fontproperties="SimHei")
ax.set_xlabel("值",fontsize=14,fontproperties="SimSun")
ax.set_ylabel("值的立方",fontsize=14,fontproperties="SimSun")

# 设置刻度标记的大小。
ax.tick_params(axis='both',which='major',labelsize=14)

# 设置每个坐标轴的取值范围。
ax.axis([0,5100,0,126000000000])

plt.show()