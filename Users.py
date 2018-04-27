from Person import Person
import os
import  sqlite3
class Users(Person):
    def Register(self):
        self.Folderpath = os.getcwd() + "/" + self.Username
        connection=sqlite3.connect("SecurebackupSystemdatabase")
        connection.execute("insert into Users (Username,Password,Folderpath,Authorize,Admin) values ('{}','{}','{}',{},{})".format(self.Username,self.Password,self.Folderpath,self.Authorize,self.Admin))
        connection.commit()
        os.mkdir(str(self.Folderpath))
    def Uploadfile(self):
        pass
    def Downloadfile(self):
        pass
    def Deleteaccount(self):
        os.rmdir(self.Folderpath)
        connection=sqlite3.connect("SecurebackupSystemdatabase")
        connection.execute("delete from Users where Username='{}'".format(self.Username))
        connection.commit()
    def Changepassword(self,password):
        self.Password=password
        connection=sqlite3.connect("SecurebackupSystemdatabase")
        connection.execute("update  Users set Password='{}' where Username ='{}'".format(self.Password,self.Username))
        connection.commit()
    def Viewfiles(self):
        pass
    def Openfile(self):
        pass
    def Removefile(self):
        pass
