#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pattern_selection import pattern_selection
from tkinter import Tk, Label, Button, Entry, IntVar
import time
## ************************************************************************************************************************
## 显示倒计时预热窗口
root_window = Tk()                               # 生成窗口
root_window.geometry('400x400')                  # 改变窗体大小（‘宽x高’），注意是x不是*
root_window.resizable(0, 0)                      # 将窗口大小设置为不可变
#root.config(bg='blanched almond')               # 设置背景色
root_window.title('欢迎使用机器嗅觉设备')          # 修改框体的名字
Label(root_window, text='传感器正在预热，请您等待',
           font='arial 20 normal').pack()        # 用来显示文字或图片

values = IntVar()
Entry(root_window, textvariable=values, width=3,
      bd='5', font='arial 30').place(x=160, y=90)
values.set(0)
## ************************************************************************************************************************
## define countdown function
def countdown():                                 # 设置倒计时函数
    value = int(values.get())                    # 得到当前框里面的值
    while value != 0:     
        while value > -1:
            values.set(value)
            root_window.update()                 # 更新窗口
            time.sleep(1)                        # 1 sencond
            value -= 1
        value = int(values.get())
    root_window.destroy()
    pattern_selection()
  
Button(root_window, text='START',width =3, height=1, bd='3',
       command=countdown, font='arial 10 bold').place(x=174, y=200)
root_window.mainloop()



