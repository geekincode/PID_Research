#from Draw_PID import draw_PID
import Draw_PID

import tkinter as tk  


def function():
    #print(e1.get(),e2.get())
    Draw_PID.Kp = eval(e1.get())
    Draw_PID.Ki = eval(e2.get())
    Draw_PID.Kd = eval(e3.get())
    Draw_PID.draw_PID()

def e1press1(self):
    e1.config(bg='skyblue')
def e1press2(self):
    e1.config(bg='white')
def e2press1(self):
    e2.config(bg='skyblue')
def e2press2(self):
    e2.config(bg='white')
def e3press1(self):
    e3.config(bg='skyblue')
def e3press2(self):
    e3.config(bg='white')


window = tk.Tk()

window.title('PID_control')
 
window.geometry('500x300')  # 这里的乘是小x

# 第4步，在图形界面上设定标签
var = tk.StringVar()    # 将label标签的内容设置为字符类型，用var来接收hit_me函数的传出内容用以显示在标签上
var.set('white')
bgcolor = 'white'
l1 = tk.Label(window, text='Kp:', 
                font=('Arial Black',12),
                width=3, height=1)
l1.place(relx=0.25, rely=0.03)

l2 = tk.Label(window, text='Ki:', 
                font=('Arial Black',12),
                width=3, height=1)
l2.place(relx=0.25, rely=0.13)

l3 = tk.Label(window, text='Kd:', 
                font=('Arial Black',12),
                width=3, height=1)
l3.place(relx=0.25, rely=0.23)

e1 = tk.Entry(window, show = None, bg='white',font=('Arial',10))#显示成明文形式
e1.place(relx=0.35,rely=0.05)
e1.bind('<Enter>',e1press1)
e1.bind('<Leave>',e1press2)


e2 = tk.Entry(window, show = None, bg='white', font=('Arial',10))#显示成明文形式
e2.place(relx=0.35, rely=0.15)
e2.bind('<Enter>',e2press1)
e2.bind('<Leave>',e2press2)

e3 = tk.Entry(window, show = None, bg='white', font=('Arial',10))#显示成明文形式
e3.place(relx=0.35, rely=0.25)
e3.bind('<Enter>',e3press1)
e3.bind('<Leave>',e3press2)

# 第5步，在窗口界面设置放置Button按键Draw_PID.Kp
b = tk.Button(window,
                 text='Show PID', 
                 font=('Arial', 12), 
                 width=10, height=1, 
                 bg='lightcoral',
                 command=function)
b.place(relx=0.4, rely=0.75)

# 第6步，主窗口循环显示
window.mainloop()
