#Login
import mysql.connector as sql
con=sql.connect(host="localhost",user="root",password="password")
cur=con.cursor()
cur.execute("create database if not exists TM")
cur.execute("use TM")
cur.execute("create table if not exists user(username varchar(50),password varchar(20),email varchar(30))")
con.commit()


def todofunctions():
     global tname
     tname=uname
     print("-------------------------------------FUNCTIONS------------------------------------")
     while True:
          print("WHAT TO YOU WANT TO DO?")
          print("ENTER A NEW TASK (N)")
          print("UPDATE AN EXISTING TASK (U)")
          print("DELETE AN EXISTING TASK (D)")
          print("EXIT (E)")
          function=input("CHOOSE YOUR DESIRED OPERATION: ")
          if function.upper()=="N":
               newtask()
          elif function.upper()=="U":
               edittodo()
          elif function.upper()=="D":
               deletetodo()
          elif function.upper()=="E":
               exit()
          else:
               print("PLEASE ENTER A VALID OPERATION!!")


def newtask():
     print("------------------------------------NEW TASK --------------------------------------")
     while True:
          task01=input("Enter Your Task: ")
          if task01=="":
               print("PLEASE ENTER SOMETHING!")
          else:
               cur.execute("insert into {} values('{}')".format(tname,task01))
               con.commit()
               cur.execute("select*from {}".format(tname))
               g=cur.fetchall()
               print(g)
               while True:
                    en=input("DO YOU WANT TO ENTER ANOTHER TASK? (Y/N): ")
                    if en.upper()=="N":
                         print("")
                         todofunctions()
                    elif en.upper()=="Y":
                         break
                    else:
                         print("ENTER A VALID OPERATION!")




def edittodo():
     print("------------------------------------EDIT TASK-----------------------------------------")
     while True:
          cur.execute("select*from {}".format(tname))
          list=cur.fetchall()
          print("HERE ARE YOUR TO DO LISTS: ")
          print(list)
          ind=int(input("PLEASE ENTER THE INDEX OF THE TASK YOU WANT TO UPDATE: "))
          index=ind-1
          che=len(list)
          check=che-1
          if index>check:
               print("ENTER A VALID INDEX!")
          else:
               ol=list[index]
               for i in ol:
                    old=i
               print("HERE IS YOUR CURRENT TASK: ",old)
               new=input("ENTER YOUR UPDATED TASK: ")
               cur.execute("update {} set todolist='{}' where todolist='{}'".format(tname,new,old))
               print("LIST EDITED SUCCESSFULLY")
               cur.execute("select*from {}".format(tname))
               newlist=cur.fetchall()
               print("HERE IS YOUR UPDATED TO-DO LIST: ",newlist)
               print("")
               todofunctions()
     



def deletetodo():
     print("--------------------------------------DELETE TASK------------------------------------")
     while True:
          cur.execute("select*from {}".format(tname))
          list=cur.fetchall()
          print("HERE ARE YOUR TO DO LISTS: ")
          print(list)
          ind=int(input("PLEASE ENTER THE INDEX OF THE TASK YOU WANT TO DELETE: "))
          index=ind-1
          che=len(list)
          check=che-1
          if index>check:
               print("ENTER A VALID INDEX!")
          else:
               ol=list[index]
               for i in ol:
                    old=i
               print("IS THIS THE TASK YOU WANT TO DELETE?",old)
               confirm=input("YES (Y) OR NO (N): ")
               if confirm.upper()=="Y":
                    cur.execute("delete from {} where todolist='{}'".format(tname,old))
                    print("TASK DELETED SUCCESSFULLY!!")
                    cur.execute("select*from {}".format(tname))
                    newlist=cur.fetchall()
                    print("THIS IS YOUR UPDATED LIST:",newlist)
                    print("")
                    todofunctions()
               elif confirm.upper()=="N":
                    while True:
                         wexit=input("DO YOU WANT TO EXIT TO MAIN MENU? (Y/N) : ")
                         if wexit.upper()=="Y":
                              print("")
                              todofunctions()
                         elif wexit.upper()=="N":
                              break
                         else:
                              print("PLEASE ENTER A VALID OPERATION!")



def login():
     global uname
     print("-------------------------------LOGIN----------------------------------")
     cur.execute("select username,password from user")
     l=cur.fetchall()
     print(l)
     uname=input("Enter Username: ")
     upassword=input("Enter Password: ")
     for i in l:
          if uname in i[0]:
               if upassword in i[1]:
                    print("")
                    todofunctions()
               else:
                    print("INVALID CREDENTIALS")
                    user()
               



def signup():
     print("-----------------------------------SIGN UP-------------------------------------")
     newuname=input("Enter New Username: ")
     newpassword=input("Enter New Password: ")
     umail=input("Enter Email id: ")
     cur.execute("insert into user values('{}','{}','{}')".format(newuname,newpassword,umail))
     cur.execute("create table {} (todolist varchar(200))".format(newuname))
     print("PLEASE LOGIN TO CONTINUE :)")
     login()
     con.commit()



'''def admin():
     print("--------------------ADMIN------------------------")
     cur.execute("select admin,password from admin")
     m=cur.fetchall()
     aname=input("Enter Username: ")
     apassword=input("Enter Password: ")
     c2=0
     for i in m:
          if aname in i[0]:
               print("Admin id Verified")
               c2=c2+1
          if apassword in  i[1]:
               print("Admin Password Verified")
               c2=c2+1
          if c2<2:
               print("Invalid Creditionals")'''

def user():
     print("--------------------------------------USER----------------------------------")
     while True:
          LS=input("DO YOU WANT TO LOGIN(L) OR SIGNUP(S): ")
          if LS.upper()=="L":
               login()
               break
          elif LS.upper()=="S":
               signup()
               break
          else:
               print("Invalid Operation! TRY AGAIN")
                    
'''def mainscreen():
     while True:
          Type=input("ARE YOU A USER(U) OR ADMIN(A): ")
          if Type.upper()=="U":
               user()
               break
          elif Type.upper()=="A":
               break
          else:
               print("Invalid Operation! TRY AGAIN"

mainscreen()'''
user()
con.close()

'''def nextfunctions():
     while True:
          wish=input("DO YOU WANT TO EDIT YOUR TO DO'S?(Y/N): ")
          if wish.upper()=="Y":
               print("WHAT DO YOU WANT TP D0?")
               fun=input("UPDATE YOUR TODOS (E) OR DELETE (D): ")
               if fun.upper()=="E":
                    edittodo()
                    break
               elif fun.upper()=="D":
                    deletetodo()
                    break
               else:
                    continue
          elif wish.upper()=="N":
               break
          else:
               print("PLEASE ENTER A VALID OPERATION!")
               continue'''