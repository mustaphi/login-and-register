import tkinter
from tkinter import ttk, END, Text

from Users import Users


class Changepassword():
    def __init__(self,User=Users()):
        root = tkinter.Tk()
        root.title("Change Account Password")
        style = ttk.Style()
        style.theme_use("alt")
        container = ttk.Frame(root, width=800, height=600)
        container.pack()
        ttk.Label(container, text="Current Password: ").grid(row=0, column=0)
        passwordField = Text(container, width=35, height=1)
        passwordField.grid(row=0, column=1)
        ttk.Label(container, text="New-Password: ").grid(row=1, column=0)
        NewpasswordField = Text(container, width=35, height=1)
        NewpasswordField.grid(row=1, column=1)
        ttk.Label(container, text="Re-entr-New-Password: ").grid(row=2, column=0)
        reenternewpasswordField = Text(container, width=35, height=1)
        reenternewpasswordField.grid(row=2, column=1)

        def LoginButtonfunction():
            if passwordField.get("1.0", END) == User.Password and len(NewpasswordField.get("1.0", END)) >= 9 and NewpasswordField.get("1.0",END) == reenternewpasswordField.get("1.0", END):
                 try:
                        User.Changepassword(NewpasswordField.get("1.0", END))
                        root.destroy()
                        root.quit()
                        from Dashboard import Dashboard
                        next = Dashboard(User)
                 except:
                        tkinter.messagebox.showinfo("Error", "Operation failed try later")
                        root.destroy()
                        root.quit()
            else:
                tkinter.messagebox.showinfo("Invalid Passwords", "Passwords are Invalid")
                root.destroy()
                root.quit()

        LoginButton = ttk.Button(container, text="Submit", command=LoginButtonfunction).grid(row=3, column=0)

        def CancelButtonfunction():
            root.destroy()
            root.quit()
            from Dashboard import Dashboard
            next = Dashboard(User)

        CancelButton = ttk.Button(container, text="Cancel", command=CancelButtonfunction).grid(row=3, column=1)
        root.mainloop()