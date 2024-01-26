from tkinter import *
from tkinter import messagebox
import os

def  login():
    user=username.get()
    code=password.get()

    
    if user=="Joana" and code=="1999":
        root=Toplevel(screen)
        root.title("Bill")
        root.geometry("1280x720+150+80")
        root.configure(bg="#0000ff")
        root.resizable(False,False)

    elif  user=="" and code=="":
            messagebox.showerror("Invalid","Please enter username and password")
    elif user=="":
            messagebox.showerror("Invalid"," username is required")
    elif  code=="":
            messagebox.showerror("Invalid","The Password field is required")

    elif user!="Joana" and code!="1999":
            messagebox.showerror("Invalid username and password")
    elif user!="Joana":
            messagebox.showerror("Invalid username,Please enter a valid username ")
    elif code!="1999":
        messagebox.showerror("Invalid password,Please enter a valid password ")


        
def main_screen():


      global screen
      global username
      global password

      screen=Tk()
      screen.geometry("1280x720+150+100")
      screen.configure(bg="#0000ff")

      #icon
      image_icon=PhotoImage(file="admin.png")
      screen.iconphoto(False,image_icon)
      screen.title("Login System")
    
      lblTitle=Label(text="LOGIN",font=("constantia",50,'bold'),fg="white",bg="#0000ff")
      lblTitle.pack(pady=50)

      bordercolor=Frame(screen,bg="black",width=800,height=400)
      bordercolor.pack()

      mainframe=Frame(bordercolor,bg="#FF1493",width=800,height=400)
      mainframe.pack(padx=20,pady=20)

      Label(mainframe,text="Username",font=("arial",30,"bold"),bg="#FFD700").place(x=100,y=50)
      Label(mainframe,text="Password",font=("arial",30,"bold"),bg="#FFD700").place(x=100,y=150)


      username=StringVar()
      password=StringVar()

      entry_username=Entry(mainframe,textvariable=username,width=12,bd=2,font=("arial",30))
      entry_username.place(x=400,y=50)
      entry_password=Entry(mainframe,textvariable=password,width=12,bd=2,font=("arial",30),show="*")
      entry_password.place(x=400,y=150)

      def reset():
          entry_username.delete(0,END)
          entry_password.delete(0,END)



      Button(mainframe,text="Login",height="2",width=23,bg="#4B0082",fg="white",bd=0,command=login).place(x=100,y=250)
      Button(mainframe,text="Reset",height="2",width=23,bg="#7FFF00",fg="white",bd=0,command=reset).place(x=300,y=250)
      Button(mainframe,text="Exit",height="2",width=23,bg="#FF4500",fg="white",bd=0,command=screen.destroy).place(x=500,y=250)

      screen.mainloop()

    
main_screen()
