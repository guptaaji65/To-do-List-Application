from tkinter import *
import mysql.connector
from addTask import*
 
window=Tk()
window.title("ProjectGurukul To-Do List")
db = mysql.connector.connect(host ="localhost",user = "root",password = 'password',database='db')
cursor = db.cursor()
 
greet = Label(window, font = ('arial', 20,'bold'), text = "To Do List")
greet.grid(row = 0,columnspan = 3)
 
L = Label(window, font = ('arial', 15), text = "Add a task")
L.grid(row = 2,column =1)
 
btn=Button(window,text="Add",command=add,padx=10,pady=5,bg="DodgerBlue2",fg="white",font = ('arial', 15))
btn.grid(row=2,column=3)
 
def delete(*args, **kwargs):
    tid=args[0]
 
    sqlquery= "Delete from ToDoList  where id='" + tid +"';"
    print(sqlquery)
 
    try:
        cursor.execute(sqlquery)
        db.commit()
        messagebox.showinfo('Success',"Task Deleted Successfully")
    except:
        messagebox.showinfo("Error","Cannot access Database")
 
def update(*args, **kwargs):
    tid=args[0]
    print("called")
    sqlquery= "Update ToDoList set status='YES' where id='" + tid +"';"
    print(sqlquery)
 
    try:
        cursor.execute(sqlquery)
        db.commit()
        messagebox.showinfo('Success',"Task Updated Successfully")
    except:
        messagebox.showinfo("Error","Cannot access Database")
 
sqlquery= "select * from toDoList;"
 
try:
    cursor.execute(sqlquery)
    print(sqlquery)
    L = Label(window, font = ('arial', 15), text = "%-10s%-50s%-10s"%('Tid','Task','Completed'))
    L.grid(row = 3,columnspan = 4)
 
    x=4
    for i in cursor:
        L = Label(window, font = ('arial', 15), text = "%-10s%-50s%-10s"%(i[0],i[1],i[2]))
        L.grid(row = x,column = 1)
 
        btn=Button(window,text="Delete",command=lambda arg=i[0], kw="delete" : delete(arg, o1=kw),padx=10,pady=5,bg="DodgerBlue2",fg="white",font = ('arial', 15))
        btn.grid(row=x,column=4)
 
        btn=Button(window,text="Done",command=lambda arg=i[0], kw="update" : update(arg, o1=kw),padx=10,pady=5,bg="DodgerBlue2",fg="white",font = ('arial', 15))
        btn.grid(row=x,column=5)
 
        x+=1   
 
except:
    messagebox.showinfo("Error","Cannot access Database")
 
mainloop()
