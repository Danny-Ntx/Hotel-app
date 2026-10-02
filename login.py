# from tkinter import *
# from tkinter import ttk

# root=Tk()
# root.title("Introduction to GUI")
# root.geometry('400x400+600+0')
# root.configure(background="#f91aa7")
# root.resizable(0,0)

# lblhead=Label(root, text="Login Page", font=("verdana",20,"bold"), bg="#f91aa7", fg="white")
# lblhead.pack(pady=20)

# fr=Frame(root, width=400,height=250,bg="#f91aa7")

# # Name
# lbln=Label(fr, text="Name:", font=("verdana", 14), bg="#f91aa7", fg="white")
# lbln.grid(row=0,column=0, pady=15)
# entn=Entry(fr,width=40,relief="flat")
# entn.grid(row=0, column=1, pady=15)

# # Email
# lble=Label(fr, text="Email:", font=("verdana", 14), bg="#f91aa7", fg="white")
# lble.grid(row=1,column=0, pady=15)
# ente=Entry(fr,width=40,relief="flat")
# ente.grid(row=1, column=1, pady=15)

# # Password
# lblp=Label(fr, text="Password:", font=("verdana", 14), bg="#f91aa7", fg="white")
# lblp.grid(row=2,column=0, pady=15)
# entp=Entry(fr,width=40,relief="flat", show="*")
# entp.grid(row=2, column=1, pady=15)

# # def login():
# #     print("Name:", entn.get())
# #     print("Email:", ente.get())
# #     print("Password:", entp.get())

# btn=Button(fr, text="Login", font=("verdana",14,"bold"), bg="white", fg="#f91aa7", width=20, relief="flat",)
# btn.grid(row=3, column=1, pady=15)
# # btn.pack(pady=30)


# fr.pack()
# root.mainloop()

from tkinter import *
from tkinter import ttk
import connect
from tkinter import messagebox as msg
import os

def manager():
    os.system('python manager.py')

def recept():
    os.system('python rec.py')

def login():
    root.destroy()
    os.system('python intro.py')
def log():
    username=entn.get()
    password=entp.get()
    role=user_role.get()

    if username=="" and password=="" and role=="":
        msg.showinfo("Alert", "Empty record not allowed, please fill the form")
        return
    connect.con
    connect.cur
    connect.cur.execute(''' select * from users where username=? and password=? and role=?''', (username,password,role))
    result=connect.cur.fetchone()
    if result:
        msg.showinfo("Success", "Record found!!!")
        root.destroy()
        if role.lower()=="hotel manager":
            manager()
        elif role.lower()=="receptionist":
            recept()
            return
    else:
        msg.showinfo("Alert", "UnAuthorized Login")    
      
            

root=Tk()
root.title("Introduction to GUI")
root.geometry('400x400+600+0')
root.configure(background="#f91aa7")
root.resizable(0,0)

lblhead=Label(root, text="Login Page", font=("verdana",20,"bold"), bg="#f91aa7", fg="white")
lblhead.pack(pady=(60,20))

fr=Frame(root, width=400,height=250,bg="#f91aa7")

# Name
lbln=Label(fr, text="username:", font=("verdana", 14), bg="#f91aa7", fg="white")
lbln.grid(row=0,column=0, pady=15)
entn=Entry(fr,width=40,relief="flat")
entn.grid(row=0, column=1, pady=15)

# # Email
# lble=Label(fr, text="Email:", font=("verdana", 14), bg="#f91aa7", fg="white")
# lble.grid(row=1,column=0, pady=15)
# ente=Entry(fr,width=40,relief="flat")
# ente.grid(row=1, column=1, pady=15)

# Password
lblp=Label(fr, text="Password:", font=("verdana", 14), bg="#f91aa7", fg="white")
lblp.grid(row=2,column=0, pady=15)
entp=Entry(fr,width=40,relief="flat", show="*")
entp.grid(row=2, column=1, pady=15)

# user role
lblr=Label(fr,text='Role:', font=("verdana", 14), bg="#f91aa7", fg="white")
lblr.grid(row=3, column=0)
role=["hotel manager", "receptionist"]
user_role=ttk.Combobox(fr, width=38, values=role )
user_role.grid(row=3, column=1)




# def login():
#     email = ente.get()
#     if "@" not in email:
#         msg.showerror("Invalid Email", "Email must contain '@'. Please enter a valid email address.")
#         return
#     print("Name:", entn.get())
#     print("Email:", email)
#     print("Password:", entp.get())

btn=Button(fr, text="Login", font=("verdana",14,"bold"), bg="black", fg="white", width=10, relief="flat", command=log)
btn.grid(row=4, column=1, pady=15)

already=Button(fr,width=40, bg="#f91aa7", fg="white", text="Don't have an account? Sign up!", command= login ,relief="flat")
already.grid(row=5 ,column=1)




fr.pack()
root.mainloop()