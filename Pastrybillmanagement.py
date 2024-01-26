import tkinter
from tkinter import *
from datetime import datetime
from tkinter import PhotoImage


root=tkinter.Tk()
root.geometry("1000x500")

image_path=PhotoImage(file=r"C:\Users\91979\Pictures\Python Images\pastery.png")
bg_image=tkinter.Label(root,image=image_path)
bg_image.place(relheight=0.5,relwidth=1)
text_label=tkinter.Label(root,text='Welcome to my shop',bg="green",fg="yellow",font=("constantia",33,"bold"),width="1150",height="2")
text_label.pack()
root.title("Bill Management")
root.resizable(False,False)

def Reset():
    entry_cheesecake.delete(0,END)
    entry_cookies.delete(0,END)
    entry_sandwitch.delete(0,END)
    entry_coffee.delete(0,END)
    entry_juice.delete(0,END)
    entry_pancakes.delete(0,END)
    entry_blackforestcake.delete(0,END)


def Total():
    try:a1=int(cheesecake.get())
    except: a1=0

    try:a2=int(cookies.get())
    except: a2=0

    try:a3=int(sandwitch.get())
    except: a3=0

    try:a4=int(coffee.get())
    except: a4=0

    try:a5=int(juice.get())
    except: a5=0

    try:a6=int(pancakes.get())
    except: a6=0
    
    try:a7=int(blackforestcake.get())
    except: a7=0



    #define cost of each item per quantity
    c1=40*a1
    c2=30*a2
    c3=50*a3
    c4=10*a4
    c5=20*a5
    c6=15*a6
    c7=60*a7

    lbl_total=Label(f2,font=('arial',20,'bold'),text="Total",width=16,fg="lightyellow",bg="black")
    lbl_total.place(x=0,y=50)


    entry_total=Entry(f2,font=("arial",20,'bold'),textvariable=Total_bill,bd=6,width=15,bg="green")
    entry_total.place(x=20,y=100)

    totalcost=c1+c2+c3+c4+c5+c6+c7
    string_bill="Rs. ",str(' %.2f'   %totalcost)
    Total_bill.set(string_bill)




    


Label(text="PASTRY SHOP MANAGEMENT",    ).pack()

#Menu card
f=Frame(root,bg="pink",highlightbackground="black",highlightthickness=1,width=300,height=370)
f.place(x=10,y=118)

Label(f,text="Menu",font=("Gabriola",40,"bold"),fg="red",bg="pink").place(x=80,y=0)

Label(f,font=("Lucida calligraphy",15,'bold'),text="Cheesecake.Rs.40/plate",fg="purple",bg="pink").place(x=10,y=80)
Label(f,font=("Lucida calligraphy",15,'bold'),text="Cookie......Rs.30/plate",fg="purple",bg="pink").place(x=10,y=110)
Label(f,font=("Lucida calligraphy",15,'bold'),text="Sandwitch...Rs.50/plate",fg="purple",bg="pink").place(x=10,y=140)
Label(f,font=("Lucida calligraphy",15,'bold'),text="Coffee......Rs.10/cup",fg="purple",bg="pink").place(x=10,y=170)
Label(f,font=("Lucida calligraphy",15,'bold'),text="Juice.......Rs.20/glass",fg="purple",bg="pink").place(x=10,y=200)
Label(f,font=("Lucida calligraphy",15,'bold'),text="pancakes....Rs.15/pack",fg="purple",bg="pink").place(x=10,y=230)
Label(f,font=("Lucida calligraphy",15,'bold'),text="Blackforest.Rs.60/piece",fg="purple",bg="pink").place(x=10,y=260)


#Bill
f2=Frame(root,bg="cyan",highlightbackground="black",highlightthickness=1,width=300,height=370)
f2.place(x=690,y=118)

Bill=Label(f2,text="BILL",font=('calibri',20,"italic"),bg="turquoise")
Bill.place(x=120,y=10)
#Entry Work
f1=Frame(root,bd=5,height=370,width=300,relief=RAISED)
f1.pack()

cheesecake=StringVar()
cookies=StringVar()
sandwitch=StringVar()
coffee=StringVar()
juice=StringVar()
pancakes=StringVar()
blackforest=StringVar()
Total_bill=StringVar()


#Label
lbl_cheesecake=Label(f1,font=("arial",20,'bold'),text="Cheesecake",width=12,fg="brown")
lbl_cookies=Label(f1,font=("arial",20,'bold'),text="Cookies",width=12,fg="brown")
lbl_sandwitch=Label(f1,font=("arial",20,'bold'),text="Sandwitch",width=12,fg="brown")
lbl_coffee=Label(f1,font=("arial",20,'bold'),text="Coffee",width=12,fg="brown")
lbl_juice=Label(f1,font=("arial",20,'bold'),text="Juice",width=12,fg="brown")
lbl_pancakes=Label(f1,font=("arial",20,'bold'),text="Pancakes",width=12,fg="brown")
lbl_blackforest=Label(f1,font=("arial",20,'bold'),text="BlackForest",width=12,fg="brown")
lbl_cheesecake.grid(row=1,column=0)
lbl_cookies.grid(row=2,column=0)
lbl_sandwitch.grid(row=3,column=0)
lbl_coffee.grid(row=4,column=0)
lbl_juice.grid(row=5,column=0)
lbl_pancakes.grid(row=6,column=0)
lbl_blackforest.grid(row=7,column=0)

#Entry
entry_cheesecake=Entry(f1,font=("arial",20,'bold'),textvariable=cheesecake,bd=6,width=8,bg="khaki")
entry_cookies=Entry(f1,font=("arial",20,'bold'),textvariable=cookies,bd=6,width=8,bg="khaki")
entry_sandwitch=Entry(f1,font=("arial",20,'bold'),textvariable=sandwitch,bd=6,width=8,bg="khaki")
entry_coffee=Entry(f1,font=("arial",20,'bold'),textvariable=coffee,bd=6,width=8,bg="khaki")
entry_juice=Entry(f1,font=("arial",20,'bold'),textvariable=juice,bd=6,width=8,bg="khaki")
entry_pancakes=Entry(f1,font=("arial",20,'bold'),textvariable=pancakes,bd=6,width=8,bg="khaki")
entry_blackforest=Entry(f1,font=("arial",20,'bold'),textvariable=blackforest,bd=6,width=8,bg="khaki")

entry_cheesecake.grid(row=1,column=1)
entry_cookies.grid(row=2,column=1)
entry_sandwitch.grid(row=3,column=1)
entry_coffee.grid(row=4,column=1)
entry_juice.grid(row=5,column=1)
entry_pancakes.grid(row=6,column=1)
entry_blackforest.grid(row=7,column=1)

#buttons

btn_reset=Button(f1,bd=5,fg="yellow",bg="navy",font=("arial",16,'bold'),width=10,text="Reset",command=Reset)
btn_reset.grid(row=8,column=0)

btn_total=Button(f1,bd=5,fg="magenta",bg="gold",font=("arial",16,'bold'),width=10,text="Total",command=Total)
btn_total.grid(row=8,column=1)






root.mainloop()
