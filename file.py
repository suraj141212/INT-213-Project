# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 21:53:54 2020

@author: Suraj
"""

from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

t = Tk()
t.geometry('500x300')

l1=Label(t,text='Enter captcha: ')
l1.grid(row=0,column=0,padx=10,pady=10)

e1=Entry(t,width=20,borderwidth=3) 
e1.grid(row=0,column=1,padx=10,pady=10)
# e1.pack()

def clicked(value):
    checkingz = e1.get()
    checkingz=checkingz.upper()
    if(value==0 and checkingz==captcha_ans[value]):
        popup_success()
        # print('hello there')
    elif(value==1 and checkingz==captcha_ans[value]):
        # print('bye there')
        popup_success()
    elif(value==2 and checkingz==captcha_ans[value]):
        # print('bye there')
        popup_success()
    elif(value==3 and checkingz==captcha_ans[value]):
        # print('bye there')
        popup_success()
    elif(value==4 and checkingz==captcha_ans[value]):
        # print('bye there')
        popup_success()
    elif(value==5 and checkingz==captcha_ans[value]):
        # print('bye there')
        popup_success()
    elif(value==6 and checkingz==captcha_ans[value]):
        # print('bye there')
        popup_success()
    elif(value==7 and checkingz==captcha_ans[value]):
        # print('bye there')
        popup_success()
    elif(value==8 and checkingz==captcha_ans[value]):
        # print('bye there')
        popup_success()
    elif(value==9 and checkingz==captcha_ans[value]):
        # print('bye there')
        popup_success()
    elif(value==10 and checkingz==captcha_ans[value]):
        # print('bye there')
        popup_success()
    elif(value==11 and checkingz==captcha_ans[value]):
        # print('bye there')
        popup_success()
    elif(value==12 and checkingz==captcha_ans[value]):
        # print('bye there')
        popup_success()
    elif(value==13 and checkingz==captcha_ans[value]):
        # print('bye there')
        popup_success()
    elif(value==14 and checkingz==captcha_ans[value]):
        # print('bye there')
        popup_success()
    elif(value==15 and checkingz==captcha_ans[value]):
        # print('bye there')
        popup_success()
    else:
        refresh_captcha(value)
        popup_error()
        #print('pls try again')


def refresh_captcha(num):
    global l
    global b2
    
    l.grid_forget()
    l = Label(image=captcha_list[num+1])
    l.grid(row=0,column=3,rowspan=2,pady=10)
    
    if (num<13):
        b2 = Button(t,image=refresh,borderwidth=0,command=lambda:refresh_captcha(num+1))
        b2.grid(row=0,column=4,rowspan=2)   
        b1 = Button(t,text='Check',command=lambda:clicked(num+1))
        b1.grid(row=1,column=0,columnspan=2,padx=10,pady=10)
    else:
        popup_finished()
        # print("Thats all we got!")


def popup_error():
    messagebox.showinfo('Info','Please enter correct captcha')

def popup_finished():
    messagebox.showinfo('Info','Thats all the captchas.. pls run the program again')

def popup_success():
    messagebox.showinfo('Info','You are successfully logged in.')

i1 = ImageTk.PhotoImage(Image.open("c1.jpg"))
i2 = ImageTk.PhotoImage(Image.open("c2.jpg"))
i3 = ImageTk.PhotoImage(Image.open("c3.jpg"))
i4 = ImageTk.PhotoImage(Image.open("c4.jpg"))
i5 = ImageTk.PhotoImage(Image.open("c5.jpg"))
i6 = ImageTk.PhotoImage(Image.open("c6.jpg"))
i7 = ImageTk.PhotoImage(Image.open("c7.jpg"))
i8 = ImageTk.PhotoImage(Image.open("c8.jpg"))
i9 = ImageTk.PhotoImage(Image.open("c9.jpg"))
i10 = ImageTk.PhotoImage(Image.open("c10.jpg"))
i11 = ImageTk.PhotoImage(Image.open("c11.jpg"))
i12 = ImageTk.PhotoImage(Image.open("c12.jpg"))
i13 = ImageTk.PhotoImage(Image.open("c13.jpg"))
i14 = ImageTk.PhotoImage(Image.open("c14.jpg"))
i15 = ImageTk.PhotoImage(Image.open("c15.jpg"))

captcha_list = [i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15]

captcha_ans = ['W4AB4','RJMY4','8UT6','HXDAJ3','3HC6K','TBYX','3V8MM','YTUT','6P4S','5UDEM','EA89M5','9SNRY9','DNRSH','PS4EE','BAXRAV']

l = Label(image=captcha_list[0])
l.grid(row=0,column=3,rowspan=2,pady=10)
# l.pack()


b1 = Button(t,text='Check',command=lambda:clicked(0))
b1.grid(row=1,column=0,columnspan=2,padx=10,pady=10)

refresh = ImageTk.PhotoImage(Image.open("refresh.jpg"))
ref = Label(image=refresh)
# ref.grid()

b2 = Button(t,image=refresh,borderwidth=0,command=lambda:refresh_captcha(0))
b2.grid(row=0,column=4,rowspan=2)   





t.mainloop()








    
