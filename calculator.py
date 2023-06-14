from turtle import *
from tkinter import *
from unittest import result

from matplotlib.pyplot import title
 
mw=Tk()
mw.title('Calculator')
display_screen=Entry(mw,width=28,font=('airal',35),justify=RIGHT,bg='#99e6ff')


first_num=0
math=''
def calculate(calc_type):
    global first_num,math
    math=calc_type
    first_num=display_screen.get()
    clear()

def equal():
    second_num=display_screen.get()
    clear()
    if math=='add':
        result=int(first_num)+int(second_num)
    elif math=='sub':
        result=int(first_num)-int(second_num)
    elif math=='mul':
        result=int(first_num)*int(second_num)
    elif math=='div':
        result=int(first_num)/int(second_num)
    display_screen.insert(0,result)






def clear():
    display_screen.delete(0,END)

def btn_click(num):
    cur_value=display_screen.get()
    clear()
    final_value=cur_value+num
    display_screen.insert(0,final_value)

btn_0=Button(mw,text='0',padx=86,pady=10,font=('arial',14),bg='#ffb3b3',command=lambda:btn_click('0'))
btn_1=Button(mw,text='1',padx=86,pady=10,font=('arial',14),bg='#ffb3b3',command=lambda:btn_click('1'))
btn_2=Button(mw,text='2',padx=86,pady=10,font=('arial',14),bg='#ffb3b3',command=lambda:btn_click('2'))
btn_3=Button(mw,text='3',padx=86,pady=10,font=('arial',14),bg='#ffb3b3',command=lambda:btn_click('3'))
btn_4=Button(mw,text='4',padx=86,pady=10,font=('arial',14),bg='#ffb3b3',command=lambda:btn_click('4'))
btn_5=Button(mw,text='5',padx=86,pady=10,font=('arial',14),bg='#ffb3b3',command=lambda:btn_click('5'))
btn_6=Button(mw,text='6',padx=86,pady=10,font=('arial',14),bg='#ffb3b3',command=lambda:btn_click('6'))
btn_7=Button(mw,text='7',padx=86,pady=10,font=('arial',14),bg='#ffb3b3',command=lambda:btn_click('7'))
btn_8=Button(mw,text='8',padx=86,pady=10,font=('arial',14),bg='#ffb3b3',command=lambda:btn_click('8'))
btn_9=Button(mw,text='9',padx=86,pady=10,font=('arial',14),bg='#ffb3b3',command=lambda:btn_click('9'))

btn_clear=Button(mw,text='clear',font=('arial',14),padx=196,pady=10,bg='#d5ff80',command=clear)
btn_div=Button(mw,text='/',font=('arial',14),padx=88,pady=10,bg='#c2c2a3',command=lambda:calculate('div'))
btn_mul=Button(mw,text='*',font=('arial',14),padx=86,pady=10,bg='#c2c2a3',command=lambda:calculate('mul'))
btn_add=Button(mw,text='+',font=('arial',14),padx=86,pady=10,bg='#c2c2a3',command=lambda:calculate('add'))
btn_sub=Button(mw,text='-',font=('arial',14),padx=86,pady=10,bg='#c2c2a3',command=lambda:calculate('sub'))
btn_equal=Button(mw,text='=',font=('arial',14),padx=86,pady=40,bg='#ff99ff',command=equal)


#showinng widgits
display_screen.grid(padx=10,pady=10,columnspan=3)
btn_clear.grid(row=4,column=1,columnspan=2,padx=2,pady=2)
btn_div.grid(row=5,column=0,padx=2,pady=2)
btn_mul.grid(row=5,column=1,padx=2,pady=2)
btn_add.grid(row=6,column=0,padx=2,pady=2)
btn_sub.grid(row=6,column=1,padx=2,pady=2)
btn_equal.grid(row=5,column=2,padx=2,pady=4,rowspan=2)

btn_0.grid(row=4,column=0,padx=2,pady=2)

btn_1.grid(row=3,column=0,padx=2,pady=2)
btn_2.grid(row=3,column=1,padx=2,pady=2)
btn_3.grid(row=3,column=2,padx=2,pady=2)

btn_4.grid(row=2,column=0,padx=2,pady=2)
btn_5.grid(row=2,column=1,padx=2,pady=2)
btn_6.grid(row=2,column=2,padx=2,pady=2)

btn_7.grid(row=1,column=0,padx=2,pady=2)
btn_8.grid(row=1,column=1,padx=2,pady=2)
btn_9.grid(row=1,column=2,padx=2,pady=2)
mw.mainloop()