import pymysql
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Python & Database")
empno = Entry(root,width = 7)
empname = Entry(root,width = 7)
deptno = Entry(root,width = 7)
job = Entry(root,width = 7)
salary = Entry(root,width = 7)

empno.grid(row = 2, column = 4)
empname.grid(row = 3, column = 4)
deptno.grid(row = 4, column = 4)
job.grid(row = 5, column = 4)
salary.grid(row = 6, column = 4)

def create():
    con = pymysql.connect(user = 'root', password = '', host = 'localhost')
    cur = con.cursor()
    cur.execute("CREATE DATABASE Employeenew")
    cur.execute("USE Employeenew")
    cur.execute("CREATE TABLE DETAILS(empno VARCHAR(20),empname VARCHAR(20),deptno VARCHAR(20),job VARCHAR(10),salary VARCHAR(20))")

def select():
    con = pymysql.connect(user = 'root', password = '', host = 'localhost', database = 'Employeenew')
    cur = con.cursor()
    s = "SELECT * FROM DETAILS WHERE empno = '" + empno.get() + "'"
    cur.execute(s)
    result = cur.fetchall()
    root_show = Tk()
    root_show.title("Python & Database")
    ci=0
    for i in result[0]:
            Label(root_show,text = result[0][ci]).grid(row = 1, column = ci+1)
            ci=ci+1
    
    

def insert():
    con = pymysql.connect(user = 'root', password = '', host = 'localhost', database = 'Employeenew')
    cur = con.cursor()
    s = "INSERT INTO DETAILS VALUES ('" + empno.get() + "', '" + empname.get() + "', '" + deptno.get() + "', '" + job.get() + "', '" + salary.get() + "') " 
    cur.execute(s)
    result = cur.fetchall()
    row = cur.fetchone()
    messagebox.showinfo("info msg", "Record Inserted")
    con.commit()
    con.close()

def update():
    con = pymysql.connect(user = 'root', password = '', host = 'localhost', database = 'Employeenew')
    cur = con.cursor()
    s = "UPDATE DETAILS SET NAME= '" + empname.get() +"', deptno = '" + deptno.get() + "', job = '" + job.get() +"',salary = '" +salary.get() + "' WHERE empno='"+ empno.get()+ "'"
    cur.execute(s)
    con.commit()
    messagebox.showinfo("info msg", "Record Deleted")
    con.close()

def delete():
    con = pymysql.connect(user = 'root', password = '', host = 'localhost', database = 'Employeenew')
    cur = con.cursor()
    str = "DELETE FROM Employeenew WHERE empno='" + empno.get()+"'"
    cur.execute(str)
    messagebox.showinfo("info msg", "Record Deleted")
    con.commit()
    con.close()
    
def show():
    con = pymysql.connect(user = 'root', password = '', host = 'localhost', database = 'Employeenew')
    cur = con.cursor()
    s = "SELECT * FROM Employeenew"
    cur.execute(s)
    result = cur.fetchall()
    root_show = Tk()
    root_show.title("Python & Database")
    ri=0
    ci=0
    for i in result:
        print(result[ri])
        
        for i in result[ri]:
            Label(root_show,text = result[ri][ci]).grid(row = ri+1, column = ci+1)
            ci=ci+1
        ri=ri+1
        ci=0
        

Label(root,text = 'empno:').grid(row = 2, column = 2)
Label(root,text = 'empname').grid(row = 3, column = 2)
Label(root,text = 'deptno').grid(row = 4, column = 2)
Label(root,text = 'job').grid(row = 5, column = 2)
Label(root,text = 'salary').grid(row = 6, column = 2)

Button(root,text = 'Create',command = create).grid(row = 8, column = 1)
Button(root,text = 'Insert',command = insert).grid(row = 8, column = 2)
Button(root,text = 'Select',command = select).grid(row = 8, column = 3)
Button(root,text = 'Update',command = update).grid(row = 8, column = 4)
Button(root,text = 'Delete',command = delete).grid(row = 8, column = 5)
Button(root,text = 'Show',command = show).grid(row = 8, column = 6)

root.mainloop()
