from tkinter import *
import sqlite3,sys

def connection():
    try:
        conn=sqlite3.connect("student.db")
    except:
        print("cannot connect to the database")
    return conn   

def verifier():
    a=b=c=d=e=f=0
    if not student_name.get():
        t1.insert(END,"<>Student name is required<>\n")
        a=1
    if not roll_no.get():
        t1.insert(END,"<>Roll no is required<>\n")
        b=1
    if not branch.get():
        t1.insert(END,"<>Branch is required<>\n")
        c=1
    if not phone.get():
        t1.insert(END,"<>Phone number is requrired<>\n")
        d=1
    if not father.get():
        t1.insert(END,"<>Father name is required<>\n")
        e=1
    if not address.get():
        t1.insert(END,"<>Address is Required<>\n")
        f=1
    if a==1 or b==1 or c==1 or d==1 or e==1 or f==1:
        return 1
    else:
        return 0


def add_student():
            ret=verifier()
            if ret==0:
                conn=connection()
                cur=conn.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS STUDENTS(NAME TEXT,ROLL_NO INTEGER,BRANCH TEXT,PHONE_NO INTEGER,FATHER TEXT,ADDRESS TEXT)")
                cur.execute("insert into STUDENTS values(?,?,?,?,?,?)",(student_name.get(),int(roll_no.get()),branch.get(),int(phone.get()),father.get(),address.get()))
                conn.commit()
                conn.close()
                t1.insert(END,"ADDED SUCCESSFULLY\n")


def view_student():
    conn=connection()
    cur=conn.cursor()
    cur.execute("select * from STUDENTS")
    data=cur.fetchall()
    conn.close()
    for i in data:
        t1.insert(END,str(i)+"\n")


def delete_student():
    ret=verifier()
    if r==0:
        conn=connection()
        cur=conn.cursor()
        cur.execute("DELETE FROM STUDENTS WHERE ROLL_NO=?",(int(roll_no.get()),))
        conn.commit()
        conn.close()
        t1.insert(END,"SUCCESSFULLY DELETED THE USER\n")

def update_student():
    ret=verifier()
    if ret==0:
        conn=connection()
        cur=conn.cursor()
        cur.execute("UPDATE STUDENTS SET NAME=?,ROLL_NO=?,BRANCH=?,PHONE_NO=?,FATHER=?,ADDRESS=? where ROLL_NO=?",(student_name.get(),int(roll_no.get()),branch.get(),int(phone.get()),father.get(),address.get(),int(roll_no.get())))
        conn.commit()
        conn.close()
        t1.insert(END,"UPDATED SUCCESSFULLY\n")


def close():
    root.destroy() 

def reset():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    


if __name__=="__main__":
    root=Tk()
    root.geometry("950x600+0+0")
    root.title("Student Management System")
    
    appLabel = Label(root, text="Student Management System", fg="#06a099", width=35)
    appLabel.config(font=("Sylfaen", 30))
    appLabel.grid(row=0, columnspan=2, padx=(10,10), pady=(30, 0))
     
    student_name=StringVar()
    roll_no=StringVar()
    branch=StringVar()
    phone=StringVar()
    father=StringVar()
    address=StringVar()
    
    label1=Label(root,text="Student name:")
    label1.place(x=50,y=150)

    label2=Label(root,text="Roll no:")
    label2.place(x=50,y=180)

    label3=Label(root,text="Branch:")
    label3.place(x=50,y=210)

    label4=Label(root,text="Phone Number:")
    label4.place(x=50,y=240)

    label5=Label(root,text="Father Name:")
    label5.place(x=50,y=270)

    label6=Label(root,text="Address:")
    label6.place(x=50,y=300)

    e1=Entry(root,textvariable=student_name)
    e1.place(x=150,y=150)

    e2=Entry(root,textvariable=roll_no)
    e2.place(x=150,y=180)

    e3=Entry(root,textvariable=branch)
    e3.place(x=150,y=210)

    e4=Entry(root,textvariable=phone)
    e4.place(x=150,y=240)
    
    e5=Entry(root,textvariable=father)
    e5.place(x=150,y=270)

    e6=Entry(root,textvariable=address)
    e6.place(x=150,y=300)
    
    t1=Text(root,width=80,height=20)
    t1.grid(row=10,column=1)
   


    b1=Button(root,text="ADD STUDENT",command=add_student,width=40)
    b1.grid(row=11,column=0)

    b2=Button(root,text="VIEW ALL STUDENTS",command=view_student,width=40)
    b2.grid(row=12,column=0)

    b3=Button(root,text="DELETE STUDENT",command=delete_student,width=40)
    b3.grid(row=13,column=0)

    b4=Button(root,text="UPDATE INFO",command=update_student,width=40)
    b4.grid(row=14,column=0)

    b5=Button(root,text="CLOSE",command=close,width=40)
    b5.grid(row=15,column=0)
    
    b6=Button(root,text="RESET",command=reset,width=40)
    b6.grid(row=16,column=0)


    root.mainloop()
