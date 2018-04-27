import sqlite3
class Person:
    Username=""
    Password=""
    Folderpath=""
    Authorize=1
    Admin=0
    def __init__(self):
        Username = ""
        Password = ""
        Folderpath = ""
        Authorize = 1
        Admin = 0
    def Login (self,Username,Password):
        found=False
        User = Person()
        connection=sqlite3.connect("SecurebackupSystemdatabase")
        connection.row_factory=sqlite3.Row
        Allusers=connection.execute("select * from Users")
        for row in Allusers:
            if row["Username"]==Username and row["Password"]==Password:
                User.Username=row["Username"]
                User.Password=row["Password"]
                User.Folderpath=row["Folderpath"]
                User.Authorize=row["Authorize"]
                User.Admin=row["Admin"]
                found=True
                return (found,User,)
        if not found:
            return (found,)
