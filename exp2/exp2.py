import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 创建数据框
data = {
    'Group': ['A: background', 'B: control group', 'C: experimental group'],
    'Saline 1': [0, 0.372, 0.143],
    'Neostigmine 1': [0, 0.329, 0.172],
    'Saline 2': [0, 0.52, 0.11],
    'Neostigmine 2': [0, 0.368, 0.243]
}
df = pd.DataFrame(data)

# 设置图形大小
plt.figure(figsize=(16, 8))

# 创建柱状图
barWidth = 0.15
bars1 = df['Saline 1']
bars2 = df['Neostigmine 1']
bars3 = df['Saline 2']
bars4 = df['Neostigmine 2']

r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
r4 = [x + barWidth for x in r3]

def create_bar_and_labels(r, bars, color, label):
    plt.bar(r, bars, color=color, width=barWidth, edgecolor='grey', label=label)
    for i in range(len(r)):
        plt.text(r[i], bars[i] + 0.01, round(bars[i], 2), ha = 'center')

# Subplot 1
plt.subplot(1, 2, 1)
create_bar_and_labels(r1, bars1, '#1f77b4', 'Saline 1')
create_bar_and_labels(r2, bars2, '#ff7f0e', 'Neostigmine 1')
create_bar_and_labels(r3, bars3, '#2ca02c', 'Saline 2')
create_bar_and_labels(r4, bars4, '#d62728', 'Neostigmine 2')
plt.xlabel('Group', fontweight='bold')
plt.xticks([r + barWidth for r in range(len(bars1))], ['A: Background Group', 'B: Control Group', 'C: Experimental Group'])
plt.legend()

# 创建颜色列表
plt.subplot(1, 2, 2)
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

# 创建数据
bars5 = [61.56, 47.72, 78.845, 33.965]
labels = ['Saline 1', 'Neostigmine 1', 'Saline 2', 'Neostigmine 2']

# 创建柱状图
r = np.arange(len(bars5))
for i in range(len(bars5)):
    create_bar_and_labels([r[i]], [bars5[i]], colors[i], labels[i])

# 添加标签
plt.xlabel('Group', fontweight='bold')
plt.xticks([r for r in range(len(bars5))], labels)

plt.legend()
plt.show()