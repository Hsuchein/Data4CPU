import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from scipy import stats

df = pd.read_csv(r"C:\Users\wayne\Desktop\2.csv")
from scipy.stats import mannwhitneyu

# 进行Mann-Whitney U检验
u_statistic, p_value = mannwhitneyu(df['value1'], df['value2'])

print("U statistic:", u_statistic)
print("p value:", p_value)

# 创建颜色列表
colors1 = ['blue' if line1 == 4 else 'red' if line1 == 5 else 'gray' for line1 in df['line1']]
colors2 = ['blue' if line2 == 4 else 'red' if line2 == 5 else 'gray' for line2 in df['line2']]

plt.figure(figsize=(20, 6))  # 创建一个新的图形，设置图形的大小

# 创建颜色标识
legend_elements = [Patch(facecolor='blue', label='Intensity 4'),
                   Patch(facecolor='red', label='Intensity 5')]

# 创建第一个子图
plt.subplot(1, 2, 1)  # 1行2列的第1个子图
plt.bar(range(1, len(df['value1']) + 1), df['value1'], color=colors1)  # 创建柱状图，x轴是1到'value1'列的长度，y轴是'value1'列的值，颜色由colors1列表决定
plt.xlabel('Group Number')  # 设置x轴的标签
plt.ylabel('Latent Period (s)')  # 设置y轴的标签
plt.title('Sodium Valproate Group')  # 设置图形的标题
plt.xticks(range(1, len(df['value1']) + 1))  # 设置x轴的刻度为1到'value1'列的长度
plt.ylim(0, 650)  # 设置y轴的范围为0-650
plt.legend(handles=legend_elements, loc='upper right')  # 添加图例

# 创建第二个子图
plt.subplot(1, 2, 2)  # 1行2列的第2个子图
plt.bar(range(1, len(df['value2']) + 1), df['value2'], color=colors2)  # 创建柱状图，x轴是1到'value2'列的长度，y轴是'value2'列的值，颜色由colors2列表决定
plt.xlabel('Group Number')  # 设置x轴的标签
plt.ylabel('Latent Period (s)')  # 设置y轴的标签
plt.title('Positive Saline (PC)')  # 设置图形的标题
plt.xticks(range(1, len(df['value2']) + 1))  # 设置x轴的刻度为1到'value2'列的长度
plt.ylim(0, 650)  # 设置y轴的范围为0-650
plt.legend(handles=legend_elements, loc='upper right')  # 添加图例

plt.tight_layout()  # 自动调整子图参数，使之填充整个图像区域
plt.show()  # 显示图形
