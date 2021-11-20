import numpy as np	
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import style

fig, axes = plt.subplots()
a = np.linspace(0,240,240)
b = np.linspace(160,161,240)
a1 = np.linspace(0,240,240)
b1 = np.linspace(200,201,240)
x = np.linspace(0,240,240)
y1 = [0]
target = 160
t_error = 0
d_error = 0
y = 0

Kp = 0.07
Ki = 0.003 #设置PID参数
Kd = 0.5


def draw_PID():
    global fig,axes, a, b, a1, b1, x, y1, target, d_error, y, Kp, Ki, Kd, t_error
    for i in range(len(x)-1):
        error = target - y
        y = y + error*Kp
        
        t_error = t_error + error
        y = y + t_error*Ki

        if i != 0:
            y = y + (error-d_error)*Kd

        #y = y - 3
        y1.append(y)
        d_error = error
    axes.plot(a1, b1, color='gray', label='top')
    axes.plot(a, b, color='skyblue', label='Target')
    axes.plot(x, y1, color='lightcoral', label='Output')
    axes.set(ylabel='Y Ax', xlabel='X Ax', title='PID_control (P I D)',
            ylim=[-2,320], xlim=[-2,240])
    axes.legend()

    plt.show()

    fig, axes = plt.subplots()
    y1 = [0]
    y = 0      #初始化

if __name__ =="__main__":       #__main__为主程序脚本文件名，__name__为该程序文件名
    draw_PID()                  #当主程序为当前程序文件时，执行该段代码
