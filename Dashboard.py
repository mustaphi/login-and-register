import tkinter
from tkinter import *
from tkinter import ttk,messagebox,simpledialog

from Changepassword import  Changepassword
from Users import Users
class Dashboard():
    def __init__(self,User=Users()):
        root = Tk()
        root.title("Dash board")
        style = ttk.Style()
        style.theme_use("alt")
        image = PhotoImage(file="userimage.png")
        imageframe = ttk.Frame(root, width=10, height=10).grid(row=0, column=0)
        ttk.Label(imageframe, image=image).grid(row=0, column=0)
        container = ttk.Frame(root, width=800, height=600)
        container.grid(row=0, column=1)
        def DeleteaccountButtonfunction():
                root.destroy()
                root.quit()
                from Deleteaccount import Deleteaccount
                next=Deleteaccount(User)
        DeleteaccountButton = ttk.Button(container, text="  Delete account ",command=DeleteaccountButtonfunction).pack()
        def ChangepasswordButtonfunction ():
            root.destroy()
            root.quit()
            after=Changepassword(User)
        ChangepasswordButton = ttk.Button(container, text="Change password",command=ChangepasswordButtonfunction).pack()
        root.mainloop()
