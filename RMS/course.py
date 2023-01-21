from tkinter import *
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk,messagebox
import sqlite3
class Courseclass:
    def __init__(self, root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="#F8EDE3")
        self.root.focus_force()
        #====title====
        title=Label(self.root,text="Manage Course Details",font=("chalkboard SE",20,"bold"),bg="#DFD3C3", fg="Black").place(x=10,y=15,width=1180,height=45)
        #====variables====
        self.var_course=StringVar()
        self.var_duration=StringVar()
        self.var_charges=StringVar()
        #====widgets====
        lbl_courseName=Label(self.root,text="Course Name",font=("chalkboard SE",15,"bold"),bg="#F8EDE3", fg="Black").place(x=10,y=70)
        lbl_duration=Label(self.root,text="Duration",font=("chalkboard SE",15,"bold"),bg="#F8EDE3", fg="Black").place(x=10,y=110)
        lbl_charges=Label(self.root,text="Charges",font=("chalkboard SE",15,"bold"),bg="#F8EDE3", fg="Black").place(x=10,y=150)
        lbl_description=Label(self.root,text="Description",font=("chalkboard SE",15,"bold"),bg="#F8EDE3", fg="Black").place(x=10,y=190)
        #====Entry fields====
        self.txt_courseName=Entry(self.root,textvariable=self.var_course,font=("Times New Roman",15,"bold"),bg="#FAF8F1", fg="gold")
        self.txt_courseName.place(x=150,y=70,width=200)
        self.txt_duration=Entry(self.root,textvariable=self.var_duration,font=("Times New Roman",15,"bold"),bg="#FAF8F1", fg="Black")
        self.txt_duration.place(x=150,y=110,width=200)
        self.txt_charges=Entry(self.root,textvariable=self.var_charges,font=("Times New Roman",15,"bold"),bg="#FAF8F1", fg="Black")
        self.txt_charges.place(x=150,y=150,width=200)
        self.txt_description=Text(self.root,font=("chalkboard SE",15,"bold"),bg="#FAF8F1", fg="Black")
        self.txt_description.place(x=150,y=190, width=500,height=180)
        #=====Buttons=====
        self.btn_add=Button(self.root,text="Save",font=("helvetica neue",18,"bold"),fg="black", cursor="pirate",command=self.add)
        self.btn_add.place(x=150,y=400,width=110,height=40)
        self.btn_update=Button(self.root,text="Update",font=("helvetica neue",18,"bold"),fg="black", cursor="pirate",command=self.update)
        self.btn_update.place(x=270,y=400,width=110,height=40)
        self.btn_delete=Button(self.root,text="Delete",font=("helvetica neue",18,"bold"),fg="black", cursor="pirate",command=self.delete)
        self.btn_delete.place(x=390,y=400,width=110,height=40)
        self.btn_clear=Button(self.root,text="Clear",font=("helvetica neue",18,"bold"),fg="black", cursor="pirate",command=self.clear)
        self.btn_clear.place(x=510,y=400,width=110,height=40)
        #====Search Pannel======
        self.var_search=StringVar()
        lbl_search_courseName=Label(self.root,text="Course Name",font=("chalkboard SE",20,"bold"),bg="#F8EDE3", fg="black").place(x=720,y=60)
        txt_search_courseName=Entry(self.root,textvariable=self.var_search,font=("Times New Roman",15,"bold"),bg="#FAF8F1", fg="Black").place(x=870,y=70,width=180)
        btn_search=Button(self.root,text="Search",font=("helvetica neue",15,"bold"),fg="black", cursor="pirate",command=self.search).place(x=1070,y=70,width=100,height=29)
        #===content====
        self.C_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="#EFEFEF",)
        self.C_Frame.place(x=720,y=100,width=470,height=340)
        scrolly = Scrollbar(self.C_Frame,orient=VERTICAL)
        scrollx = Scrollbar(self.C_Frame,orient=HORIZONTAL)
        self.CourseTable=ttk.Treeview(self.C_Frame,columns=("cid","Name","duration","charges","description"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)
        self.CourseTable.heading("cid",text="Course ID")
        self.CourseTable.heading("Name",text="Name")
        self.CourseTable.heading("duration",text="Duration")
        self.CourseTable.heading("charges",text="Charges")
        self.CourseTable.heading("description",text="Description")
        self.CourseTable["show"]='headings'
        self.CourseTable.column("cid",width=70)
        self.CourseTable.column("Name",width=100)
        self.CourseTable.column("duration",width=100)
        self.CourseTable.column("charges",width=100)
        self.CourseTable.column("description",width=150)
        self.CourseTable.pack(fill=BOTH,expand=1) 
        self.CourseTable.bind("<ButtonRelease-1>",self.get_data) 
        self.show()
    #=============================================================================
    def clear(self):
        self.show()
        self.var_course.set("")
        self.var_duration.set("")
        self.var_charges.set("")
        self.var_search.set("")
        self.txt_description.delete("1.0",END)
        self.txt_courseName.config(state=NORMAL)
    def delete(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error","Course Name should be required",parent=self.root)
            else:
                cur.execute("select * from course where name=?",(self.var_course.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","please select course from the list first",parent=self.root)
                else:
                    op=messagebox.askyesno("confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from course where name=?",(self.var_course.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Course deleted successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
                
        
    def get_data(self,ev):
        self.txt_courseName.config(state="readonly")
        r=self.CourseTable.focus()
        content=self.CourseTable.item(r)
        row=content["values"]
        #print(row)
        self.var_course.set(row[1])
        self.var_duration.set(row[2])
        self.var_charges.set(row[3])
        self.txt_description.delete("1.0",END)
        self.txt_description.insert(END,row[4])
    def add(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error","Course Name should be required",parent=self.root)
            else:
                cur.execute("select * from course where name=?",(self.var_course.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Course Name already present",parent=self.root)
                else:
                    cur.execute("insert into course (name,duration,charges,description) values(?,?,?,?)",(
                        self.var_course.get(),
                        self.var_duration.get(),
                        self.var_charges.get(),
                        self.txt_description.get("1.0",END)
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Course Added Succsessfully",parent=self.root)  
                    self.show()
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to {str(ex)}")
                
    def update(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error","Course Name should be required",parent=self.root)
            else:
                cur.execute("select * from course where name=?",(self.var_course.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Select course from list",parent=self.root)
                else:
                    cur.execute("update course set duration=?,charges=?,description=? where name=?",(
                        self.var_duration.get(),
                        self.var_charges.get(),
                        self.txt_description.get("1.0",END),
                        self.var_course.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Course Update Succsessfully",parent=self.root)  
                    self.show()
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to {str(ex)}")
    def show(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("select * from course")
            rows=cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('',END,values=row)
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to {str(ex)}")
    def search(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute(f"select * from course where name LIKE '%{self.var_search.get()}%'")
            rows=cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('',END,values=row)
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to {str(ex)}")               
if __name__=="__main__":
        root = Tk()
        obj = Courseclass(root)
        root.mainloop()