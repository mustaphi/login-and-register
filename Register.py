from tkinter import *
from tkinter import ttk

from Users import Users

import tkinter.messagebox

class Register():
    def __init__(self):
        root = Tk()
        root.title("Register")
        style = ttk.Style()
        style.theme_use("alt")
        container = ttk.Frame(root, width=800, height=600)
        container.pack()
        ttk.Label(container, text="UserName: ").grid(row=0, column=0)
        UsernameField = Text(container, width=35, height=1)
        UsernameField.grid(row=0, column=1)
        ttk.Label(container, text="Password: ").grid(row=1, column=0)
        passwordField = Text(container, width=35, height=1)
        passwordField.grid(row=1, column=1)
        ttk.Label(container, text="Re-entrPassword: ").grid(row=2, column=0)
        reenterpasswordField = Text(container, width=35, height=1)
        reenterpasswordField.grid(row=2, column=1)
        def Submitbuttonfunction ():
            User=Users()
            if len(passwordField.get("1.0",END))>=8 and passwordField.get("1.0",END)==reenterpasswordField.get("1.0",END) and len(UsernameField.get("1.0",END))!=0:
                User.Username = str(UsernameField.get("1.0", END))
                User.Password=str(passwordField.get("1.0",END))
                try:
                    User.Register()
                    root.destroy()
                    root.quit()
                    from Dashboard import Dashboard
                    next=Dashboard(User)
                except :
                    tkinter.messagebox.showinfo("invalid Credentials","Do net leave any field empty and may be your user name used before")
            else:
                tkinter.messagebox.showinfo("weak password","Enter strong Password or password doesnot seem to be exactly")
        Submitbutton = ttk.Button(container, text="Submit",command=Submitbuttonfunction).grid(row=3, column=0)
        root.mainloop()


