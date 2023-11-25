from tkinter import Tk, Label, Button, Entry, IntVar, StringVar, Radiobutton
import matplotlib.pyplot as plt
import time
import warnings
import random
import datetime
import numpy as np
from threading import Thread
import RPi.GPIO as GPIO


warnings.filterwarnings('ignore')
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)         


def pattern_selection():
    GPIO.output(11, False)                                  # 关闭三通阀和气泵
    GPIO.output(13, False)
    window_pattern_selection = Tk()
    window_pattern_selection.geometry('500x300')            # 改变窗体大小（‘宽x高’），注意是x不是*
    window_pattern_selection.resizable(0, 0)                # 将窗口大小设置为不可变
    #root1.config(bg='blanched almond')                     # 设置背景色
    window_pattern_selection.title('台式实验分析型机器嗅觉设备')                      # 修改框体的名字
    Label(window_pattern_selection, text='选择模式',font='arial 20 normal').pack()    # 用来显示文字或图片

    def draw_sampling(a, b, c, repeat_counts):
        GPIO.output(11, True)                               # 打开气泵，关闭三通阀          
        GPIO.output(13, False)
        address = [0x48, 0x49, 0x4a, 0x4c]
        ain_address = [0x40, 0x41, 0x42, 0x43]

        bus = smbus.SMBus(1)

        sampling_data = [] #采样阶段数据
        sensors_data = []  #全局数据
        t_list = []

        sensor1 = []
        sensor2 = []
        sensor3 = []
        sensor4 = []
        sensor5 = []
        sensor6 = []
        sensor7 = []
        sensor8 = []
        sensor9 = []
        sensor10 = []
        sensor11 = []
        sensor12 = []
        sensor13 = []
        sensor14 = []
        sensor15 = []
        sensor16 = []

        plt.ion()
        times = 0
        count = 1
        plt.style.use('seaborn')
        save_data_txt  = False    # 只保存采样阶段的数据到txt文档
        # 获取当前系统时间
        current_time = datetime.datetime.now().strftime("%Y%m%d%H%M")
        while count <= repeat_counts:
            # print(f"重复次数为: {count}") 
            plt.clf()
            ax = plt.subplot()

            #读取传感器数据
            sensor_data = []
            for i in range(0, 4):
                for j in range(0, 4):
                    bus.write_byte(address[i], ain_address[j])
                    time.sleep(0.1)   # 等待一段时间以确保转换完成
                    value = bus.read_byte(address[i]) * 5000 / 255
                    value = round(value, 2)
                    sensor_data.append(value)
                
            sensors_data.append(sensor_data)
            if save_data_txt:
                sampling_data.append(sensor_data)
            
            t_list.append(times)
            sensor1.append(sensors_data[times][0])
            sensor2.append(sensors_data[times][1])
            sensor3.append(sensors_data[times][2])
            sensor4.append(sensors_data[times][3])
            sensor5.append(sensors_data[times][4])
            sensor6.append(sensors_data[times][5])
            sensor7.append(sensors_data[times][6])
            sensor8.append(sensors_data[times][7])
            sensor9.append(sensors_data[times][8])
            sensor10.append(sensors_data[times][9])
            sensor11.append(sensors_data[times][10])
            sensor12.append(sensors_data[times][11])
            sensor13.append(sensors_data[times][12])
            sensor14.append(sensors_data[times][13])
            sensor15.append(sensors_data[times][14])
            sensor16.append(sensors_data[times][15])

            ax.plot(t_list, sensor1, color='blue', label='Sensor1')
            ax.plot(t_list, sensor2, color='black', label='Sensor2')
            ax.plot(t_list, sensor3, color='red', label='Sensor3')
            ax.plot(t_list, sensor4, color='blue', label='Sensor4')
            ax.plot(t_list, sensor5, color='magenta', label='Sensor5')
            ax.plot(t_list, sensor6, color='green', label='Sensor6')
            ax.plot(t_list, sensor7, color='cyan', label='Sensor7')
            ax.plot(t_list, sensor8, color='green', label='Sensor8', linewidth=3)
            ax.plot(t_list, sensor9, color='yellow', label='Sensor9', linewidth=3)
            ax.plot(t_list, sensor10, color='cyan', label='Sensor10', linewidth=3)
            ax.plot(t_list, sensor11, color='green', label='Sensor11', linewidth=3)
            ax.plot(t_list, sensor12, color='black', label='Sensor12', linewidth=4)
            ax.plot(t_list, sensor13, color='cyan', label='Sensor13', linewidth=4)
            ax.plot(t_list, sensor14, color='blue', label='Sensor14', linewidth=4)
            ax.plot(t_list, sensor15, color='red', label='Sensor15', linewidth=4)
            ax.plot(t_list, sensor16, color='magenta', label='Sensor16', linewidth=4)
            ax.legend(bbox_to_anchor=(1.02, 0), loc=3, borderaxespad=0, title='Sensors')
            ax.set_ylabel('Voltage (mv)')
            ax.set_xlabel('Time (s)')
            
            plt.tight_layout()
            # plt.pause(0.0001)
            plt.pause(0.001)
            plt.show()
            time_sum = a + b + c
            
            if times >= (a + (count - 1) * time_sum) and times < (a + b + (count - 1) * time_sum):
                # 采样阶段
                GPIO.output(13, True)     # 采样阶段三通阀打开
                save_data_txt = True      # 只保存采样阶段的数据到txt文档
            else:
                GPIO.output(13, False)
                save_data_txt = False     # 基线和吹扫阶段不保存数据到txt
            times += 1
            time.sleep(1)
            if times == (count * time_sum):
                # 构建文档名
                file_name = f"sampling_data_{current_time}_{count}.txt"
                sensor_array = np.array(sampling_data)
                # 使用numpy的savetxt函数将数组保存到txt文档
                np.savetxt(file_name, sensor_array, fmt='%d', delimiter=' ')
                sampling_data.clear()
                count += 1

    def sampling():                                                                 # 采样  
        def return_pattern_selection():                                              # 定义函数返回模式选择，关掉采样窗口
            print("End: %s" % time.ctime())
            window_sampling.destroy()
            pattern_selection()
        
        window_pattern_selection.destroy()
        window_sampling = Tk()
        window_sampling.geometry('500x300')                                         # 改变窗体大小（‘宽x高’），注意是x不是*
        window_sampling.resizable(0, 0)                                             # 将窗口大小设置为不可变
        #root1.config(bg='blanched almond')                                         # 设置背景色
        window_sampling.title('台式实验分析型机器嗅觉设备')                              # 标题
        Label(window_sampling, text='采样',font='arial 12 normal').pack()            # 显示文字或图片       
        Label(window_sampling, text='s',font='arial 12 normal').place(x=370, y=130)
        
        Button(window_sampling, text='结束',width =3, height=1, bd='3',              # 创建NEXT按钮
               command=return_pattern_selection, font='arial 10 bold').place(x=230, y=260)
        
        time_a = IntVar()
        Entry(window_sampling, textvariable=time_a, width=2,
              bd='5', font='arial 30').place(x=170, y=90)
        time_a.set(1)
        Label(window_sampling, text='基线阶段',font='arial 8 normal').place(x=175, y=70)               # 设置文字标签提示
        
        time_b = IntVar()
        Entry(window_sampling, textvariable=time_b, width=2,
              bd='5', font='arial 30').place(x=240, y=90)
        time_b.set(1)
        Label(window_sampling, text='样气接触反应',font='arial 8 normal').place(x=236, y=70)
        
        time_c = IntVar()
        Entry(window_sampling, textvariable=time_c, width=2,
              bd='5', font='arial 30').place(x=310, y=90)
        time_c.set(1)
        Label(window_sampling, text='吹扫阶段',font='arial 8 normal').place(x=315, y=70)
        
        counts = IntVar()
        Entry(window_sampling, textvariable=counts, width=3,
              bd='5', font='arial 30').place(x=60, y=90)
        counts.set(1)
        Label(window_sampling, text='实验重复次数',font='arial 8 normal').place(x=68, y=70)
        
        def draw():
            print("Start: %s" % time.ctime())
            a = int(time_a.get())
            b = int(time_b.get())
            c = int(time_c.get())
            repeat_counts = int(counts.get())
            thread = Thread(target=draw_sampling(a,b,c,repeat_counts))
            thread.start()
            thread.join()
            
            
        Button(window_sampling, text='开始',width =3, height=1, bd='3',              # 创建START按钮
               command=draw, font='arial 10 bold').place(x=230, y=180)
        window_sampling.mainloop()
    
    def testing():
        def return_pattern_selection():                                              # 定义函数返回模式选择，关掉采样窗口
            window_testing.destroy()
            pattern_selection()
        window_pattern_selection.destroy()
        window_testing = Tk()
        window_testing.geometry('500x300')                                              # 改变窗体大小（‘宽x高’），注意是x不是*
        window_testing.resizable(0, 0)                                                  # 将窗口大小设置为不可变
        #root1.config(bg='blanched almond')                                          # 设置背景色
        window_testing.title('台式实验分析型机器嗅觉设备')                                   # 标题
        Label(window_testing, text='测试',font='arial 12 normal').pack()                 # 显示文字或图片
        Label(window_testing, text='min',font='arial 12 normal').place(x=370, y=130)
        testing_result = StringVar()                                                 # IntVar
        #Entry(window_test, textvariable=testing_result, width=5,
        #         bd='5', font='arial 20', state='readonly').place(x=200, y=90)
        Label(window_testing, textvariable=testing_result, bg='blue',
              fg='white', font='arial 12 normal', width=6, height=2).pack()
        testing_result.set('')
        
        def draw_testing(a,b,c):                                                              # 动态显示
            GPIO.output(11, True)                               # 打开气泵，关闭三通阀          
            GPIO.output(13, False)
            address = [0x48, 0x49, 0x4a, 0x4c]
            ain_address = [0x40, 0x41, 0x42, 0x43]

            bus = smbus.SMBus(1)

            sensors_data = []
            sensor_data = []
            t_list = []

            sensor1 = []
            sensor2 = []
            sensor3 = []
            sensor4 = []
            sensor5 = []
            sensor6 = []
            sensor7 = []
            sensor8 = []
            sensor9 = []
            sensor10 = []
            sensor11 = []
            sensor12 = []
            sensor13 = []
            sensor14 = []
            sensor15 = []
            sensor16 = []

            def getdata(i, j, times):
                bus.write_byte(address[i], ain_address[j])
                bus.read_byte(address[i])
                value = bus.read_byte(address[i]) *5000 / 256
                value = round(value, 2)
                sensor_data.append(value)

                with open('data_testing.txt', mode='a') as f:
                    value = str(value)
                    if i == 0 and j == 0:
                        f.write(str(times) + ' ' +value + ' ')
                    elif i == 3 and j == 3:
                        f.write(value + '\n')
                    else:
                        f.write(value + ' ')
                
            plt.ion()
            times = 0
            count = 1
            plt.style.use('seaborn')
            fig = plt.figure()
            #print(f"重复次数为: {repeat_counts}") 
            while True:
                plt.clf()
                ax1 = fig.add_subplot(441)
                ax2 = fig.add_subplot(442)
                ax3 = fig.add_subplot(443)
                ax4 = fig.add_subplot(444)
                ax5 = fig.add_subplot(445)
                ax6 = fig.add_subplot(446)
                ax7 = fig.add_subplot(447)
                ax8 = fig.add_subplot(448)
                ax9 = fig.add_subplot(449)
                ax10 = fig.add_subplot(4, 4, 10)
                ax11 = fig.add_subplot(4, 4, 11)
                ax12 = fig.add_subplot(4, 4, 12)
                ax13 = fig.add_subplot(4, 4, 13)
                ax14 = fig.add_subplot(4, 4, 14)
                ax15 = fig.add_subplot(4, 4, 15)
                ax16 = fig.add_subplot(4, 4, 16)

                sensor_data.clear()
                for i in range(0, 4):
                    for j in range(0, 4):
                        getdata(i, j, times)
                sensors_data.append(sensor_data)
                sum_sensors = 0
                for i in range(0, 16):
                    sum_sensors += sensors_data[times][i]
                if sum_sensors >= 3240:
                    testing_result.set('花露水')
                else:
                    testing_result.set('空气')
                    
                t_list.append(times)
                sensor1.append(sensors_data[times][0])
                sensor2.append(sensors_data[times][1])
                sensor3.append(sensors_data[times][2])
                sensor4.append(sensors_data[times][3])
                sensor5.append(sensors_data[times][4])
                sensor6.append(sensors_data[times][5])
                sensor7.append(sensors_data[times][6])
                sensor8.append(sensors_data[times][7])
                sensor9.append(sensors_data[times][8])
                sensor10.append(sensors_data[times][9])
                sensor11.append(sensors_data[times][10])
                sensor12.append(sensors_data[times][11])
                sensor13.append(sensors_data[times][12])
                sensor14.append(sensors_data[times][13])
                sensor15.append(sensors_data[times][14])
                sensor16.append(sensors_data[times][15])
                
                ax1.plot(t_list, sensor1, color='blue', label='Sensor1', linewidth=1)
                ax2.plot(t_list, sensor2, color='black', label='Sensor2', linewidth=1)
                ax3.plot(t_list, sensor3, color='red', label='Sensor3', linewidth=1)
                ax4.plot(t_list, sensor4, color='blue', label='Sensor4', linewidth=1)
                ax5.plot(t_list, sensor5, color='magenta', label='Sensor5', linewidth=1)
                ax6.plot(t_list, sensor6, color='green', label='Sensor6', linewidth=1)
                ax7.plot(t_list, sensor7, color='cyan', label='Sensor7', linewidth=1)
                ax8.plot(t_list, sensor8, color='green', label='Sensor8', linewidth=1)
                ax9.plot(t_list, sensor9, color='yellow', label='Sensor9', linewidth=1)
                ax10.plot(t_list, sensor10, color='cyan', label='Sensor10', linewidth=1)
                ax11.plot(t_list, sensor11, color='green', label='Sensor11', linewidth=1)
                ax12.plot(t_list, sensor12, color='black', label='Sensor12', linewidth=1)
                ax13.plot(t_list, sensor13, color='cyan', label='Sensor13', linewidth=1)
                ax14.plot(t_list, sensor14, color='blue', label='Sensor14', linewidth=1)
                ax15.plot(t_list, sensor15, color='red', label='Sensor15', linewidth=1)
                ax16.plot(t_list, sensor16, color='magenta', label='Sensor16', linewidth=1)
                #ax1.legend(bbox_to_anchor=(1.02, 0), loc=3, borderaxespad=0, title='Sensors')
                ax1.set_ylabel('Voltage (mV)')
                ax1.set_xlabel('Time (s)')
                
                ax1.set_title('TGS2620')
                ax2.set_title('TGS2603')
                ax3.set_title('TGS2602')
                ax4.set_title('TGS2600')
                ax5.set_title('TGS2610')
                ax6.set_title('MQ2')
                ax7.set_title('MQ4')
                ax8.set_title('MQ5')
                ax9.set_title('MQ8')
                ax10.set_title('MQ9')
                ax11.set_title('MQ135')
                ax12.set_title('MQ138')
                ax13.set_title('MQ131')
                ax14.set_title('MQ3')
                ax15.set_title('MQ7')
                # ax15.title.set_text('MQ7')
                # fig.suptitle("RES") # fig.suptitle("广西电力装备智能控制与运维重点实验室")
                # plt.suptitle('dddd',fontsize=10,x=0.5,y=0.98)

                plt.tight_layout()
                plt.pause(0.0001)
                time_sum = a + b + c
                
                if times >= (a + (count - 1) * time_sum) * 60 and times < (a + b + (count - 1) * time_sum) * 60 :
                    GPIO.output(13, True)                                 # 11气泵，13三通阀
                else:
                    GPIO.output(13, False)
                times += 1
                time.sleep(0.05)
                if times == (count * time_sum) * 60:
                    count += 1
        
        Button(window_testing, text='结束',width =3, height=1, bd='3',              # 创建NEXT按钮
               command=return_pattern_selection, font='arial 10 bold').place(x=230, y=260)
        
        time_a = IntVar()
        Entry(window_testing, textvariable=time_a, width=2,
              bd='5', font='arial 30').place(x=170, y=90)
        time_a.set(1)
        Label(window_testing, text='基线阶段',font='arial 8 normal').place(x=175, y=70)               # 设置文字标签提示
        
        time_b = IntVar()
        Entry(window_testing, textvariable=time_b, width=2,
              bd='5', font='arial 30').place(x=240, y=90)
        time_b.set(1)
        Label(window_testing, text='样气接触反应',font='arial 8 normal').place(x=236, y=70)
        
        time_c = IntVar()
        Entry(window_testing, textvariable=time_c, width=2,
              bd='5', font='arial 30').place(x=310, y=90)
        time_c.set(1)
        Label(window_testing, text='吹扫阶段',font='arial 8 normal').place(x=315, y=70)
        
        counts = IntVar()
        Entry(window_testing, textvariable=counts, width=3,
              bd='5', font='arial 30').place(x=60, y=90)
        counts.set(1)
        Label(window_testing, text='实验重复次数',font='arial 8 normal').place(x=68, y=70)
        
        def draw():
            print("Start: %s" % time.ctime())
            a = int(time_a.get())
            b = int(time_b.get())
            c = int(time_c.get())
            #repeat_counts = int(counts.get())
            draw_testing(a,b,c)
            
        Button(window_testing, text='开始',width =3, height=1, bd='3',              # 创建START按钮
               command=draw, font='arial 10 bold').place(x=230, y=180)
        
        window_testing.mainloop()                                                       # 窗口循环  
    


    var = StringVar()                                                                # 定义一个var用来将radiobutton的值和Label的值联系在一起. 
    # 创建三个radiobutton选项，其中variable=var, value='A'的意思就是，当我们鼠标选中了其中一个选项，把value的值A放到变量var中，然后赋值给variable
    
    Radiobutton(window_pattern_selection, text='采样', variable=var,
                        value='A', command=sampling, font='arial 12 normal').pack()
    Radiobutton(window_pattern_selection, text='测试', variable=var,
                        value='B', command=testing, font='arial 12 normal').pack()
    window_pattern_selection.mainloop()


