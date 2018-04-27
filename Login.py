import tkinter
from tkinter import *
from tkinter import ttk

from Admin import Admin
from Person import Person
from Register import Register
from Users import Users

root=Tk()
root.title("Login")
style=ttk.Style()
style.theme_use("alt")
container=ttk.Frame(root,width=800,height=600)
container.pack()
ttk.Label(container,text="Enter Your UserName: ").grid(row=0,column=0)
UsernameField=Text(container,width=35,height=1)
UsernameField.grid(row=0,column=1)
ttk.Label(container,text="Enter Your Password: ").grid(row=1,column=0)
passwordField=Text(container,width=35,height=1)
passwordField.grid(row=1,column=1)
def LoginButtonfunction():
        User=Person()
        User.Username=UsernameField.get("1.0",END)
        User.Password=passwordField.get("1.0",END)
        if  len(User.Username)-1!= 0 and  len(User.Password)-1!= 0:
                Data=User.Login(User.Username,User.Password)
                if Data[0] and Data[1].Authorize:
                        if not Data[1].Admin:
                                User=Users()
                        else:
                                User=Admin()
                        User.Username = Data[1].Username
                        User.Password = Data[1].Password
                        User.Folderpath = Data[1].Folderpath
                        User.Authorize = Data[1].Authorize
                        User.Admin = Data[1].Admin
                        if not User.Admin:
                                root.destroy()
                                root.quit()
                                from Dashboard import Dashboard
                                next=Dashboard(User)
                        else:
                                pass
                        # الى هيعمل ال admin

                else:
                        tkinter.messagebox.showinfo(" Invalid Credintial", "User Doesnot exist  thank you :)")
                        root.destroy()
                        root.quit()
        else:
                tkinter.messagebox.showinfo("Empty fields","Do net leave any field empty ")
LoginButton=ttk.Button(container,text="Login",command=LoginButtonfunction).grid(row=2,column=0)
def RegisterButtonfunction ():
        root.destroy()
        root.quit()
        next=Register()
RegisterButton=ttk.Button(container,text="Register!",command=RegisterButtonfunction).grid(row=2,column=1)
root.mainloop()
