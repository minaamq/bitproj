from tkinter import *
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk,messagebox
import sqlite3
class resultclass:
    def __init__(self, root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="#F8EDE3")
        self.root.focus_force()
        #====title====
        title=Label(self.root,text="Add Student Result",font=("chalkboard SE",30,"bold"),bg="#13005A", fg="red").place(x=10,y=15,width=1180,height=60)
        #======widgets=======
        #=======variables======
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_course=StringVar()
        self.var_marks=StringVar()
        self.var_full_marks=StringVar()
        self.roll_list=[]
        self.fetch_roll()
        
        lbl_select=Label(self.root,text="Select Student",font=("chalkboard SE",21,"bold"),bg="#F8EDE3",fg="Black").place(x=50,y=100)
        lbl_name=Label(self.root,text="Name",font=("chalkboard SE",21,"bold"),bg="#F8EDE3", fg="Black").place(x=50,y=160)
        lbl_course=Label(self.root,text="Course",font=("chalkboard SE",21,"bold"),bg="#F8EDE3",fg="Black").place(x=50,y=220)
        lbl_marks=Label(self.root,text="Marks Obtained",font=("chalkboard SE",21,"bold"),bg="#F8EDE3", fg="Black").place(x=50,y=280)
        lbl_full_marks=Label(self.root,text="Full Marks",font=("chalkboard SE",21,"bold"),bg="#F8EDE3", fg="Black").place(x=50,y=340)
        
        self.txt_student=ttk.Combobox(self.root,textvariable=self.var_roll,font=("Times New Roman",15,"bold"),values=self.roll_list,state='readonly',justify=CENTER)
        self.txt_student.place(x=280,y=100,width=200)
        self.txt_student.set("Select")
        btn_search=Button(self.root,text="Search",font=("helvetica neue",15,"bold"),fg="black", cursor="pirate",command=self.search).place(x=500,y=100,width=100,height=29)

        txt_name=Entry(self.root,textvariable=self.var_name,font=("Times New Roman",20,"bold"),bg="#FAF8F1", fg="gold",state="readonly").place(x=280,y=160,width=320)
        txt_course=Entry(self.root,textvariable=self.var_course,font=("Times New Roman",20,"bold"),bg="#FAF8F1", fg="gold",state="readonly").place(x=280,y=220,width=320)
        txt_marks=Entry(self.root,textvariable=self.var_marks,font=("Times New Roman",20,"bold"),bg="#FAF8F1", fg="Black").place(x=280,y=280,width=320)
        txt_full_marks=Entry(self.root,textvariable=self.var_full_marks,font=("Times New Roman",20,"bold"),bg="#FAF8F1", fg="Black").place(x=280,y=340,width=320)
        
        #======button======
        btn_add=Button(self.root,text="Submit",font=("helvetica neue",15,"bold"),fg="black",cursor="pirate",command=self.add).place(x=300,y=420,width=120,height=35)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("helvetica neue",15,"bold"),fg="black", cursor="pirate").place(x=440,y=420,width=120,height=35)

        #=====image=======
        self.bg_img=Image.open("//Users/minaam/Desktop/RMS/images/result.jpg")
        self.bg_img=self.bg_img.resize((500,300),Image.ANTIALIAS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)
        self.lbl_img=Label(self.root,image=self.bg_img).place(x=650,y=120)
     #========================================================
    def fetch_roll(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("select roll from student")
            rows=cur.fetchall() 
            if len(rows)>0:
                for row in rows:
                    self.roll_list.append(row[0])
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to {str(ex)}")
    
    def search(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("select name,course from student where roll=?",(self.var_roll.get(),))
            row=cur.fetchone()
            if row!=None:
                self.var_name.set(row[0])
                self.var_course.set(row[1])
            else:
                messagebox.showerror("Error","No record found",parent=self.root)
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to {str(ex)}")               
    def add(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_name.get()=="Select":
                messagebox.showerror("Error","please first search student record",parent=self.root)
            else:
                cur.execute("select * from result where roll=? and course=?",(self.var_roll.get(),self.var_course.get()))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Result already present",parent=self.root)
                else:
                    per=(int(self.var_marks.get())*100/int(self.var_full_marks.get()))
                    cur.execute("insert into result(roll,name,course,marks_ob,full_marks,per) values(?,?,?,?,?,?)",(
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_course.get(),
                        self.var_marks.get(),
                        self.var_full_marks.get(),
                        str(per)
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Result Added Succsessfully",parent=self.root) 
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
            
    def clear(self):
        self.var_roll.set("Select"),
        self.var_name.set(""),
        self.var_course.set(""),
        self.var_marks.set(""),
        self.var_full_marks.set(""),
                 
  
if __name__=="__main__": 
        root = Tk()
        obj = resultclass(root)
        root.mainloop()