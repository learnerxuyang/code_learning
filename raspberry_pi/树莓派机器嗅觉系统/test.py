# import matplotlib.pyplot as plt
# import numpy as np

# # 读取文本文件
# file_name = 'sampling_data_202311251732_1.txt'
# data = np.loadtxt(file_name)

# # 获取数据的形状（行数和列数）
# num_rows, num_columns = data.shape

# # 创建图形和轴
# plt.figure(figsize=(10, 6))
# ax = plt.subplot()

# # 绘制每一列的曲线
# for i in range(num_columns):
#     sensor_values = data[:, i]
#     ax.plot(sensor_values, label=f'Sensor{i + 1}')

# # 添加图例和标签
# ax.legend()
# ax.set_xlabel('Time (s)')
# ax.set_ylabel('Sensor Values')

# # 显示图形
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# # 读取文本文件
# file_name = 'sampling_data_202311251732_1.txt'
# data = np.loadtxt(file_name)

# fig = plt.figure()
# ax1 = fig.add_subplot(441)
# ax2 = fig.add_subplot(442)
# ax3 = fig.add_subplot(443)
# ax4 = fig.add_subplot(444)
# ax5 = fig.add_subplot(445)
# ax6 = fig.add_subplot(446)
# ax7 = fig.add_subplot(447)
# ax8 = fig.add_subplot(448)
# ax9 = fig.add_subplot(449)
# ax10 = fig.add_subplot(4, 4, 10)
# ax11 = fig.add_subplot(4, 4, 11)
# ax12 = fig.add_subplot(4, 4, 12)
# ax13 = fig.add_subplot(4, 4, 13)
# ax14 = fig.add_subplot(4, 4, 14)
# ax15 = fig.add_subplot(4, 4, 15)
# ax16 = fig.add_subplot(4, 4, 16)

# t_list = []
# for i in range(0, 419):
#     t_list.append(i)


# ax1.plot(t_list, data[:, 0], color='blue', label='Sensor1', linewidth=1)
# ax2.plot(t_list, data[:, 1], color='black', label='Sensor2', linewidth=1)
# ax3.plot(t_list, data[:, 2], color='red', label='Sensor3', linewidth=1)
# ax4.plot(t_list, data[:, 3], color='blue', label='Sensor4', linewidth=1)
# ax5.plot(t_list, data[:, 4], color='magenta', label='Sensor5', linewidth=1)
# ax6.plot(t_list, data[:, 5], color='green', label='Sensor6', linewidth=1)
# ax7.plot(t_list, data[:, 6], color='cyan', label='Sensor7', linewidth=1)
# ax8.plot(t_list, data[:, 7], color='green', label='Sensor8', linewidth=1)
# ax9.plot(t_list, data[:, 8], color='yellow', label='Sensor9', linewidth=1)
# ax10.plot(t_list, data[:, 9], color='cyan', label='Sensor10', linewidth=1)
# ax11.plot(t_list, data[:, 10], color='green', label='Sensor11', linewidth=1)
# ax12.plot(t_list, data[:, 11], color='black', label='Sensor12', linewidth=1)
# ax13.plot(t_list, data[:, 12], color='cyan', label='Sensor13', linewidth=1)
# ax14.plot(t_list, data[:, 13], color='blue', label='Sensor14', linewidth=1)
# ax15.plot(t_list, data[:, 14], color='red', label='Sensor15', linewidth=1)
# ax16.plot(t_list, data[:, 15], color='magenta', label='Sensor16', linewidth=1)
# ax1.set_ylabel('Voltage (mv)')
# ax1.set_xlabel('Time (s)')

# # 添加图例和标签

# ax1.set_ylabel('Voltage (mv)')
# ax1.set_xlabel('Time (s)')
# plt.tight_layout()
# # 显示图形
# plt.show()




import matplotlib.pyplot as plt
import numpy as np

# 读取文本文件
file_name = 'sampling_data_202311251732_1.txt'
data = np.loadtxt(file_name)

# 获取数据的形状（行数和列数）
num_rows, num_columns = data.shape

# 创建图形和轴
plt.figure(figsize=(10, 6))
ax = plt.subplot()

# 绘制每一列的曲线
# for i in range(num_columns):
#     sensor_values = data[:, i]
#     ax.plot(sensor_values, label=f'Sensor{i + 1}')
i = 15
sensor_values = data[:, i]
ax.plot(sensor_values, label=f'Sensor{i + 1}')

# 添加图例和标签
ax.legend()
ax.set_xlabel('Time (s)')
ax.set_ylabel('Sensor Values')

# 显示图形
plt.show()