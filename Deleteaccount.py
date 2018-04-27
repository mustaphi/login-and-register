import tkinter
from tkinter import Tk, ttk, Text,messagebox

from Dashboard import Dashboard
from Users import Users


class Deleteaccount():
    def __init__(self,User=Users()):
        root=Tk()
        root.title("Delete account")
        ttk.Label(root,text="Enter your password").pack()
        Passwordfield=Text(root,width=35,height=2)
        Passwordfield.pack()
        def Deletebuttonfunction():
            if Passwordfield.get("1.0", tkinter.END)==User.Password:
                User.Deleteaccount()
            else:
                tkinter.messagebox.showinfo("Error","Failed Try later")
            root.destroy()
            root.quit()
        Deletebutton=ttk.Button(root,text="Delete!",command=Deletebuttonfunction).pack()
        def Cancelbuttonfunction():
            root.destroy()
            root.quit()
            next=Dashboard(User)
        Cancelbutton=ttk.Button(root,text="Cancel",command=Cancelbuttonfunction).pack()
        root.mainloop()