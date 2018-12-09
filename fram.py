# Frame 框架

import tkinter as tk
import time
from tkinter import ttk

window = tk.Tk()
window.title('XICE 1.0')
window.geometry('836x572')

lable = tk.Label(window, text="基于深度学习的课堂专注度行为识别系统", bd=10, font=("黑体", 20), height=3)
lable.pack()
# 定义一个大的frame，定义在window上
frm = tk.Frame(window)
frm.pack()

# 定义两个小的frame，放在大的frame上，分别放在左边和右边
frm_l = tk.Frame(frm)
frm_r = tk.Frame(frm)
frm_b = tk.Frame(frm)
frm_l.pack(side='left')
frm_r.pack(side='right')


def openVideo():
    print("button1")


def openCamera():
    print("button2")


def play_pause():
    print("button3")


# 左边
tk.Text(frm_l, width=70, height=25, bg="black").pack(side='top')
canvas = tk.Canvas(frm_l, width=500, height=20, bg="white")
canvas.pack()
tk.Button(frm_l, text='打开视频文件', width=23, command=openVideo).pack(side='left')
tk.Button(frm_l, text='打开摄像头', width=23, command=openCamera).pack(side='left')
tk.Button(frm_l, text='播放/暂停', width=23, command=play_pause).pack(side='left')


def progress():
    # 填充进度条
    fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
    x = 500  # 未知变量，可更改
    n = 465 / x  # 465是矩形填充满的次数
    for i in range(x):
        n = n + 465 / x
        canvas.coords(fill_line, (0, 0, n, 60))
        window.update()
        time.sleep(0.02)  # 控制进度条流动的速度

    # 清空进度条
    fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="white")
    x = 500  # 未知变量，可更改
    n = 465 / x  # 465是矩形填充满的次数

    for t in range(x):
        n = n + 465 / x
        # 以矩形的长度作为变量值更新
        canvas.coords(fill_line, (0, 0, n, 60))
        window.update()
        time.sleep(0)  # 时间为0，即飞速清空进度条


btn_download = tk.Button(window, text='启动进度条', command=progress)
btn_download.place()


def server_con():
    print("btn_server")


# 右边
tk.Label(frm_r, text='识别信息：', font=('宋体', 13), anchor="w", width=30, height=2).pack(side='top')
txt = tk.Text(frm_r, font=('宋体', 13), width=30, height=13)
txt.pack(side='top')
txt.insert(2.0, "\n总人数:")
txt.insert(tk.END, "XX")
txt.insert(5.0, "\n\n认真听讲（人数）:")
txt.insert(tk.END, "XX")
txt.insert(8.0, "\n\n开小差（人数）:")
txt.insert(tk.END, "XX")
txt.insert(11.0, "\n\n睡觉（人数）:")
txt.insert(tk.END, "XX")
tk.Label(frm_r, text='神经网络服务器：', font=('宋体', 13), anchor="w", width=30, height=2).pack(side='top')
server = tk.Entry(frm_r, font=('宋体', 13), width=30).pack(side='top')
tk.Label(frm_r, text='',width=30, height=1).pack(side='top')
tk.Button(frm_r, text='连接', width=23, command=server_con).pack(side='right')

window.mainloop()
