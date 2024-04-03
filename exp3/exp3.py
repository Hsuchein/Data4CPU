import matplotlib.pyplot as plt
import numpy as np

# 设置全局字体大小
plt.rcParams['font.size'] = 26

# 数据
mouse1 = [21,28,45,42]
mouse2 = [20,117,0,15]
mouse3 = [19,16,17,24]

# x轴的标签
x_labels = ['0min', '15min', '30min', '45min']

# 创建一个x的位置数组
x = np.arange(len(x_labels))

# 定义柱状图的宽度
bar_width = 0.25

# 创建柱状图
plt.bar(x - bar_width, mouse1, width = bar_width, color ='b', label ='Mouse1')
plt.bar(x, mouse2, width = bar_width, color ='g', label ='Mouse2')
plt.bar(x + bar_width, mouse3, width = bar_width, color ='r', label ='Mouse3')

# 添加x轴的标签
plt.xlabel('Drug injection time (min)')
plt.ylabel('Foot licking time (s)')
plt.title('Values at different times for each mouse')

# 添加图例
plt.legend()

# 在每个柱子上方添加数值
for i in range(len(mouse1)):
    plt.text(x = i-bar_width , y = mouse1[i]+0.5, s = mouse1[i], size = 26)
for i in range(len(mouse2)):
    plt.text(x = i , y = mouse2[i]+0.5, s = mouse2[i], size = 26)
for i in range(len(mouse3)):
    plt.text(x = i+bar_width , y = mouse3[i]+0.5, s = mouse3[i], size = 26)

# 添加x轴的标签
plt.xticks(x, x_labels)
plt.show()