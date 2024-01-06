from tkinter import *
import datetime
from tkinter import ttk 
import openpyxl
from openpyxl import Workbook

root = Tk()
root.geometry('950x552+150+150')
root.iconbitmap('img/store-64.ico')
root.title('Market tools for Building')
# ============ FRAMES ===============
# ============ frame 1 ==============
f1 = Frame(root,bg='silver')
f1.place(x=1, y=1, width=600, height=550)
# ============ frame 2 ==============
f2 = Frame(root,bg='gray')
f2.place(x=610, y=1, width=343, height=550)

trv = ttk.Treeview(f2,selectmod='browse')

trv.place(x=0, y=0, width=340, height=550)

# ============ LABEL ================
title = Label(f1,text='Building equipment sale project',font=('Perpetua',16),fg='white',bg='#5f7161')# Lucida Calligraphy italic
title.pack(fill=X)
# ============ IMAGES ===============
image_menu1 =  image=PhotoImage(file='img/icons8-hammer-60.png')
image_menu2 =  image=PhotoImage(file='img/icons8-saw-32.png')
image_menu3 =  image=PhotoImage(file='img/icons8-wagon-32.png')
image_menu4 =  image=PhotoImage(file='img/icons8-broom-64.png')
image_menu5 =  image=PhotoImage(file='img/icons8-hammer-60.png') 
image_menu6 =  image=PhotoImage(file='img/icons8-saw-32.png')
image_menu7 =  image=PhotoImage(file='img/icons8-wagon-32.png')
image_menu8 =  image=PhotoImage(file='img/icons8-broom-64.png')
image_menu9 =  image=PhotoImage(file='img/icons8-hammer-60.png')
image_menu10 =  image=PhotoImage(file='img/icons8-saw-32.png')
image_menu11 =  image=PhotoImage(file='img/icons8-wagon-32.png') 
image_menu12 =  image=PhotoImage(file='img/icons8-broom-64.png')
#========== BUTONNS =================
button_menu1 = Button(f1,bg='#efead8',bd=1,relief=SOLID,cursor='hand2',width=88,height=85,image=image_menu1,text='Hammer',compound=TOP)
button_menu2 = Button(f1,bg='#efead8',bd=1,relief=SOLID,cursor='hand2',width=88,height=85,image=image_menu2,text='Saw',compound=TOP)
button_menu3 = Button(f1,bg='#efead8',bd=1,relief=SOLID,cursor='hand2',width=88,height=85,image=image_menu3,text='Wagon',compound=TOP)
button_menu4 = Button(f1,bg='#efead8',bd=1,relief=SOLID,cursor='hand2',width=88,height=85,image=image_menu4,text='Broom',compound=TOP)
button_menu5 = Button(f1,bg='#efead8',bd=1,relief=SOLID,cursor='hand2',width=88,height=85,image=image_menu5,text='Hammer',compound=TOP)
button_menu6 = Button(f1,bg='#efead8',bd=1,relief=SOLID,cursor='hand2',width=88,height=85,image=image_menu6,text='Saw',compound=TOP)
button_menu7 = Button(f1,bg='#efead8',bd=1,relief=SOLID,cursor='hand2',width=88,height=85,image=image_menu7,text='Wagon',compound=TOP)
button_menu8 = Button(f1,bg='#efead8',bd=1,relief=SOLID,cursor='hand2',width=88,height=85,image=image_menu8,text='Broom',compound=TOP)
button_menu9 = Button(f1,bg='#efead8',bd=1,relief=SOLID,cursor='hand2',width=88,height=85,image=image_menu9,text='Hammer',compound=TOP)
button_menu10 = Button(f1,bg='#efead8',bd=1,relief=SOLID,cursor='hand2',width=88,height=85,image=image_menu10,text='Saw',compound=TOP)
button_menu11 = Button(f1,bg='#efead8',bd=1,relief=SOLID,cursor='hand2',width=88,height=85,image=image_menu11,text='Wagon',compound=TOP)
button_menu12 = Button(f1,bg='#efead8',bd=1,relief=SOLID,cursor='hand2',width=88,height=85,image=image_menu12,text='Broom',compound=TOP)
button_menu1.place(x=30,y=45)
button_menu2.place(x=170,y=45)
button_menu3.place(x=310,y=45)
button_menu4.place(x=450,y=45)
button_menu5.place(x=30,y=180)
button_menu6.place(x=170,y=180)
button_menu7.place(x=310,y=180)
button_menu8.place(x=450,y=180)
button_menu9.place(x=30,y=315)
button_menu10.place(x=170,y=315)
button_menu11.place(x=310,y=315)
button_menu12.place(x=450,y=315)
# ========= Varible + count ==============
sb = []
font1 =('Lucida Calligraphy italic',12,'normal')
sv1 =IntVar()
sv2 =IntVar()
sv3 =IntVar()
sv4 =IntVar()
sv5 =IntVar()
sv6 =IntVar()
sv7 =IntVar()
sv8 =IntVar()
sv9 =IntVar()
sv10 =IntVar()
sv11 =IntVar()
sv12 =IntVar()

sb1 = Spinbox(f1,from_=0,to_=5,font=font1,width=7,textvariable=sv1)
sb2 = Spinbox(f1,from_=0,to_=5,font=font1,width=7,textvariable=sv2)
sb3 = Spinbox(f1,from_=0,to_=5,font=font1,width=7,textvariable=sv3)
sb4 = Spinbox(f1,from_=0,to_=5,font=font1,width=7,textvariable=sv4)
sb5 = Spinbox(f1,from_=0,to_=5,font=font1,width=7,textvariable=sv5)
sb6 = Spinbox(f1,from_=0,to_=5,font=font1,width=7,textvariable=sv6)
sb7 = Spinbox(f1,from_=0,to_=5,font=font1,width=7,textvariable=sv7)
sb8 = Spinbox(f1,from_=0,to_=5,font=font1,width=7,textvariable=sv8)
sb9 = Spinbox(f1,from_=0,to_=5,font=font1,width=7,textvariable=sv9)
sb10 = Spinbox(f1,from_=0,to_=5,font=font1,width=7,textvariable=sv10)
sb11 = Spinbox(f1,from_=0,to_=5,font=font1,width=7,textvariable=sv11)
sb12 = Spinbox(f1,from_=0,to_=5,font=font1,width=7,textvariable=sv12)

sb1.place(x=30,y=140)
sb2.place(x=170,y=140)
sb3.place(x=310,y=140)
sb4.place(x=450,y=140)
sb5.place(x=30,y=275)
sb6.place(x=170,y=275)
sb7.place(x=310,y=275)
sb8.place(x=450,y=275)
sb9.place(x=30,y=410)
sb10.place(x=170,y=410)
sb11.place(x=310,y=410)
sb12.place(x=450,y=410)

sb.append(sb1)
sb.append(sb2)
sb.append(sb3)
sb.append(sb4)
sb.append(sb5)
sb.append(sb6)
sb.append(sb7)
sb.append(sb8)
sb.append(sb9)
sb.append(sb10)
sb.append(sb11)
sb.append(sb12)

B1 = Button(f1,text="buying",font=font1,bd=1,bg='#6d8b74')
B2 = Button(f1,text="New bill",font=font1,bd=1,bg='#6d8b74')
B3 = Button(f1,text="Rent materials",font=font1,bd=1,bg='#6d8b74')
B4 = Button(f1,text="Close the program",font=font1,bd=1,bg='#6d8b74')

B1.place(x=0,y=480)
B2.place(x=110,y=480)
B3.place(x=250,y=480)
B4.place(x=420,y=480)







root.mainloop()