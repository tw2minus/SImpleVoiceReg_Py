from logging import root
from tkinter import *
from tkinter import font
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

root = Tk()
root.geometry("600x300")
root.title("BaiKiemTraGiuaKy")

id = Label(root,text='Mã Sinh Viên',font=('bold',10))
id.place(x=20, y=30)
e_id = Entry()
e_id.place(x=150, y=30)

name = Label(root,text='Họ và tên',font=('bold',10))
name.place(x=20, y=60)
e_name = Entry()
e_name.place(x=150, y=60)

phone = Label(root,text='Số điện thoại',font=('bold',10))
phone.place(x=20, y=90)
e_phone = Entry()
e_phone.place(x=150, y=90)

email = Label(root,text='Email',font=('bold',10))
email.place(x=20, y=120)
e_email = Entry()
e_email.place(x=150, y=120)

gender = Label(root,text='Giới tính',font=('bold',10))
gender.place(x=20, y=150)
e_gender = Entry()
e_gender.place(x=150, y=150)

specialized = Label(root,text='Chuyên Ngành',font=('bold',10))
specialized.place(x=20, y=180)
e_specialized = Entry()
e_specialized.place(x=150, y=180)

classname = Label(root,text='Lớp',font=('bold',10))
classname.place(x=20, y=210)
e_classname = Entry()
e_classname.place(x=150, y=210)

def insert():
  id = e_id.get()
  name = e_name.get()
  phone =  e_phone.get()
  email = e_email.get()
  gender = e_gender.get()
  specialized = e_specialized.get()
  classname = e_classname.get()
  if (id == "" or name == "" or phone == "" or email == "" or gender == "" or specialized == "" or classname == ""):
    MessageBox.showinfo("Insert Status", "All Fields are required")
  else:
    con = mysql.connect(host='localhost', database='mysql', user='root', password='tuanan_1')
    cursor = con.cursor()


    cursor.execute(
      "INSERT INTO thongtin VALUES('" + id + "','" + name + "','" + phone + "','" + email + "','" + gender + "','" + specialized + "', '" + classname + "')")
    cursor.execute("commit")

    MessageBox.showinfo("Insert Status", "Insert Successfully")
    con.close()


insert = Button(root, text="Submit", font=("italic", 10), bg="white", command=insert)
insert.place(x=150, y=250)

root.mainloop()
