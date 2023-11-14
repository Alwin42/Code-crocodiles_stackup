from tkinter import *
from tkinter import messagebox
import mysql.connector as sql
from PIL import ImageTk,Image
con=sql.connect(host="localhost",user="root",passwd="password")
cur=con.cursor()
cur.execute("create database if not exists TM")
cur.execute("use TM")
#cur.execute("drop table user")
cur.execute("create table if not exists user(username varchar(50),password varchar(20),email varchar(30))")
#cur.execute("insert into user values('s','s','s')")
con.commit()

def quitmain1():
    global base
    base.destroy()

def reload():
    mainscreen()

def loginfun(uname,upassword):
    global tname
    cur.execute("select username,password from user")
    l=cur.fetchall()
    print(l)
    tname=uname
    c=0
    for i in l:
        if uname and upassword in i:
        #if uname in i[0]:
            #if upassword in i[1]:
            messagebox.showinfo("Done","Login Successfull!")#editlater
            mainscreen()
            c=c+1
            break
            #else:
                #messagebox.showerror("Error!","INVALID CREDITIONALS!")
                #loginpage()
    if c==0:
        messagebox.showerror("Error!","INVALID CREDITIONALS!")
        loginpage()

def loginpage():
    global base
    try:
        base.destroy()
    except:
        pass
    base=Tk()
    base.geometry("1423x800")
    img=Image.open("Task.png")
    myimg=ImageTk.PhotoImage(img)
    imglabel=Label(image=myimg)
    imglabel.place(x=0,y=0)
    
    text1=Label(base,text="LOGIN",font=("Arial",21),fg="black").place(x=670,y=320)
    text2=Label(base,text="Username:",font=("Arial",17),fg="black").place(x=510,y=410)
    box1=Entry(base,font=('Arial 15'))
    box1.place(x=655,y=412)
    text3=Label(base,text="Password:",font=("Arial",17),fg="black").place(x=510,y=460)
    box2=Entry(base,font=('Arial 15'))
    box2.place(x=655,y=462)
    
    button1=Button(base,text="Enter",font=("Arial",13),fg="black",command=lambda:loginfun(box1.get(),box2.get())).place(x=680,y=520)
    text4=Label(base,text="New to Zentask Sphere?",font=("Arial",13),fg="black").place(x=628,y=600)
    button2=Button(base,text="Signup",font=("Arial",11),fg="blue",command=lambda:signuppage()).place(x=680,y=630)
    button4=Button(base,text="QUIT",font=("Arial",13),command=lambda:quitmain1()).place(x=1350,y=750)
    
    base.mainloop()

def signupfun(newuname,newpassword,umail):
    global tname
    try:
        tname=newuname
        cur.execute("insert into user values('{}','{}','{}')".format(newuname,newpassword,umail))
        cur.execute("create table {} (todolist varchar(200))".format(newuname))
        con.commit()
        messagebox.showinfo("Done","Sign Up Successfull!")
        mainscreen()
    except:
        messagebox.showerror("Error!","User Already Exists!")
        signuppage()

def signuppage():
    global base,base
    try:
        base.destroy()
    except:
        pass
    base=Tk()
    base.geometry("1423x800")
    img=Image.open("Task.png")
    myimg=ImageTk.PhotoImage(img)
    imglabel=Label(image=myimg)
    imglabel.place(x=0,y=0)
    
    text1=Label(base,text="SIGNUP",font=("Arial",21),fg="black").place(x=670,y=320)
    text2=Label(base,text="Username:",font=("Arial",17),fg="black").place(x=510,y=410)
    box1=Entry(base,font=('Arial 15'))
    box1.place(x=655,y=412)
    text3=Label(base,text="Password:",font=("Arial",17),fg="black").place(x=510,y=460)
    box2=Entry(base,font=('Arial 15'))
    box2.place(x=655,y=462)
    text4=Label(base,text="Email:",font=("Arial",17),fg="black").place(x=510,y=510)
    box3=Entry(base,font=('Arial 15'))
    box3.place(x=655,y=512)
    
    button1=Button(base,text="Enter",font=("Arial",13),fg="black",command=lambda:signupfun(box1.get(),box2.get(),box3.get())).place(x=680,y=580)
    text5=Label(base,text="Already a Member of Zentask Sphere?",font=("Arial",13),fg="black").place(x=578,y=650)
    button2=Button(base,text="Login",font=("Arial",11),fg="blue",command=lambda:loginpage()).place(x=680,y=680)
    button4=Button(base,text="QUIT",font=("Arial",13),fg="red",command=lambda:quitmain1()).place(x=1350,y=750)
    
    base.mainloop()

def newtaskfun(task01):
    if task01=="":
        messagebox.showerror("Error!","Please Enter Something!")
        reload()
    else:
        cur.execute("insert into {} values('{}')".format(tname,task01))
        con.commit()
        cur.execute("select*from {}".format(tname))
        g=cur.fetchall()
        print(g)
        messagebox.showinfo("Done","Task Added Successfully")
        reload()
            

def newtaskmenu():
    text1=Label(base,text="Enter New Task:",font=("Arial",13),fg="black").place(x=250,y=630)
    box1=Entry(base,font=('Arial 15'))
    box1.place(x=380,y=630)
    button1=Button(base,text="Enter",font=("Arial",13),fg="black",command=lambda:newtaskfun(box1.get())).place(x=450,y=659)

def edittaskfun(ind,new):
    if new=="":
        messagebox.showerror("Error!","Please Enter Something!")
        reload()
    else:
        cur.execute("select*from {}".format(tname))
        list=cur.fetchall()
        indnum=int(ind)
        index=indnum-1
        che=len(list)
        check=che-1
        if index>check:
            messagebox.showerror("Error!","Please Enter a Valid Index!")
            reload()
        else:
            ol=list[index]
            for i in ol:
                old=i
            print("HERE IS YOUR CURRENT TASK: ",old)
            cur.execute("update {} set todolist='{}' where todolist='{}'".format(tname,new,old))
            con.commit()
            cur.execute("select*from {}".format(tname))
            newlist=cur.fetchall()
            messagebox.showinfo("Done","Task Edited Successfully")
            reload()
            
    

def edittaskmenu():
    text1=Label(base,text="Enter Index Number:",font=("Arial",13),fg="black").place(x=450,y=630)
    box1=Entry(base,font=('Arial 15'))
    box1.place(x=610,y=630)
    text2=Label(base,text="Enter Updated Task:",font=("Arial",13),fg="black").place(x=450,y=665)
    box2=Entry(base,font=('Arial 15'))
    box2.place(x=610,y=665)
    button1=Button(base,text="Enter",font=("Arial",13),fg="black",command=lambda:edittaskfun(box1.get(),box2.get())).place(x=850,y=645)

def deletetaskfun(ind):
    cur.execute("select*from {}".format(tname))
    list=cur.fetchall()
    print(list)
    indnum=int(ind)
    index=indnum-1
    che=len(list)
    check=che-1
    if index>check:
        messagebox.showerror("Error!","Please Enter a Valid Index!")
        reload()
    else:
        ol=list[index]
        for i in ol:
            confirm=messagebox.askyesno("Confirmation","Press Yes to confirm deletion!")
            if confirm:
                cur.execute("delete from {} where todolist='{}'".format(tname,i))
                con.commit()
                reload()
            else:
                reload()

def deletetaskmenu():
    text1=Label(base,text="Enter Index Number:",font=("Arial",13),fg="black").place(x=800,y=630)
    box1=Entry(base,font=('Arial 15'))
    box1.place(x=960,y=630)
    button1=Button(base,text="Enter",font=("Arial",13),fg="black",command=lambda:deletetaskfun(box1.get())).place(x=1000,y=665)

def mainscreen():
    print(tname)
    global base,base
    try:
        base.destroy()
    except:
        pass
    base=Tk()
    base.geometry("1423x800")
    img=Image.open("MainScreen.png")
    myimg=ImageTk.PhotoImage(img)
    imglabel=Label(image=myimg)
    imglabel.place(x=0,y=0)
    
    text1=Label(base,text="Your Current To Do List",font=("Arial",21),fg="red").place(x=560,y=190)
    cur.execute("select*from {}".format(tname))
    g=cur.fetchall()
    count=len(g)
    print(count)
    l=[]
    
    for i in g:
        for u in i:
            l.append(u)
    print(l)
    try:
        for i in range(count):
            text2=Label(base,text=l[0],font=("Arial",15),fg="black").place(x=645,y=250)
            text3=Label(base,text=l[1],font=("Arial",15),fg="black").place(x=645,y=290)
            text4=Label(base,text=l[2],font=("Arial",15),fg="black").place(x=645,y=330)
            text5=Label(base,text=l[3],font=("Arial",15),fg="black").place(x=645,y=370)
            text6=Label(base,text=l[4],font=("Arial",15),fg="black").place(x=645,y=410)
            text7=Label(base,text=l[5],font=("Arial",21),fg="black").place(x=645,y=450)
            text8=Label(base,text=l[6],font=("Arial",21),fg="black").place(x=645,y=490)
            text9=Label(base,text=l[7],font=("Arial",21),fg="black").place(x=645,y=530)
            text10=Label(base,text=l[8],font=("Arial",21),fg="black").place(x=645,y=570)
            text11=Label(base,text=l[9],font=("Arial",21),fg="black").place(x=560,y=610)
            text12=Label(base,text=l[10],font=("Arial",21),fg="black").place(x=560,y=650)
    except:
        pass
    
    button1=Button(base,text="New Task",font=("Arial",13),fg="black",command=lambda:newtaskmenu()).place(x=320,y=580)
    button2=Button(base,text="Edit Task",font=("Arial",13),fg="black",command=lambda:edittaskmenu()).place(x=640,y=580)
    button3=Button(base,text="Delete Task",font=("Arial",13),fg="black",command=lambda:deletetaskmenu()).place(x=970,y=580)
    button4=Button(base,text="BACK",font=("Arial",13),command=lambda:loginpage()).place(x=1345,y=700)
    button5=Button(base,text="QUIT",font=("Arial",13),fg="red",command=lambda:quitmain1()).place(x=1350,y=750)
    base.mainloop()
loginpage()

con.close()