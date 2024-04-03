import matplotlib.pyplot as plt

plt.rcParams['font.size'] = 26
# 定义时间间隔（分钟）
time_intervals = [5, 10, 15, 25]

# 定义每只老鼠的活动和静止状态的累计行为次数
mouse1_active = [55, 232, 411, 1200]
mouse1_stand = [4, 6, 7, 8]
mouse2_activity = [45, 64, 90, 130]
mouse2_stand = [1, 1, 1, 1]

# 绘制折线图
plt.figure(figsize=(10, 6))  # 设置图形的大小

plt.plot(time_intervals, mouse1_active, label='Mouse 1 Activity', marker='o')
plt.plot(time_intervals, mouse1_stand, label='Mouse 1 Stand', marker='o')
plt.plot(time_intervals, mouse2_activity, label='Mouse 2 Activity', marker='o')
plt.plot(time_intervals, mouse2_stand, label='Mouse 2 Stand', marker='o')

# 添加图例
plt.legend()

# 设置x轴和y轴的标签
plt.xlabel('Time (min)')
plt.ylabel('Cumulative Actions')

# 设置图形的标题
plt.title('Cumulative Actions vs. Time')

# 显示图形
plt.show()
