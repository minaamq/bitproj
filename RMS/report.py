from tkinter import *
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk,messagebox
import sqlite3
class reportclass:
    def __init__(self, root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="#F8EDE3")
        self.root.focus_force()
        #========title============
        title=Label(self.root,text="View Student Result",font=("chalkboard SE",30,"bold"),bg="#13005A", fg="red").place(x=10,y=15,width=1180,height=50)
        #========search=========
        self.var_search=StringVar()
        self.var_id=""
        
        lbl_search=Label(self.root,text="Search By Roll No.",font=("chalkboard SE",21,"bold"),bg="#F8EDE3",fg="Black").place(x=280,y=100)
        txt_select=Entry(self.root,textvariable=self.var_search,font=("Times New Roman",21,"bold"),bg="#FAF8F1",fg="Black").place(x=500,y=100,width=180)
        btn_search=Button(self.root,text="Search",font=("helvetica neue",15,"bold"),fg="black", cursor="pirate",command=self.search).place(x=690,y=103,width=100,height=35)
        btn_clear=Button(self.root,text="Clear",font=("helvetica neue",15,"bold"),fg="black", cursor="pirate",command=self.clear).place(x=805,y=103,width=100,height=35)


        #======result_labels=========
        lbl_roll=Label(self.root,text="Roll No.",font=("chalkboard SE",15,"bold"),bg="lightgrey",fg="black",bd=2,relief=RIDGE).place(x=155,y=230,width=150,height=50)
        lbl_name=Label(self.root,text="Name",font=("chalkboard SE",15,"bold"),bg="lightgrey",fg="Black",bd=2,relief=RIDGE).place(x=300,y=230,width=155,height=50)
        lbl_course=Label(self.root,text="Course",font=("chalkboard SE",15,"bold"),bg="lightgrey",fg="Black",bd=2,relief=RIDGE).place(x=450,y=230,width=155,height=50)
        lbl_marks=Label(self.root,text="Marks Obtained",font=("chalkboard SE",15,"bold"),bg="lightgrey",fg="Black",bd=2,relief=RIDGE).place(x=600,y=230,width=155,height=50)
        lbl_full=Label(self.root,text="Total Marks",font=("chalkboard SE",15,"bold"),bg="lightgrey",fg="Black",bd=2,relief=RIDGE).place(x=750,y=230,width=155,height=50)
        lbl_per=Label(self.root,text="percentage",font=("chalkboard SE",15,"bold"),bg="lightgrey",fg="Black",bd=2,relief=RIDGE).place(x=900,y=230,width=155,height=50)
         
        self.roll=Label(self.root,font=("helvetica neue SE",15,"bold"),bg="#F8EDE3",fg="red",bd=2,relief=RIDGE)
        self.roll.place(x=155,y=279,width=150,height=50)
        self.name=Label(self.root,font=("helvetica neue SE",15,"bold"),bg="#F8EDE3",fg="red",bd=2,relief=RIDGE)
        self.name.place(x=300,y=279,width=155,height=50)
        self.course=Label(self.root,font=("helvetica neue SE",15,"bold"),bg="#F8EDE3",fg="red",bd=2,relief=RIDGE)
        self.course.place(x=450,y=279,width=155,height=50)
        self.marks=Label(self.root,font=("helvetica neue SE",15,"bold"),bg="#F8EDE3",fg="red",bd=2,relief=RIDGE)
        self.marks.place(x=600,y=279,width=155,height=50)
        self.full=Label(self.root,font=("helvetica neue SE",15,"bold"),bg="#F8EDE3",fg="red",bd=2,relief=RIDGE)
        self.full.place(x=750,y=279,width=155,height=50)
        self.per=Label(self.root,font=("helvetica neue SE",15,"bold"),bg="#F8EDE3",fg="red",bd=2,relief=RIDGE)
        self.per.place(x=900,y=279,width=155,height=50)
        
        
        
        #=========button delete========
        btn_delete=Button(self.root,text="Delete",font=("helvetica neue",15,"bold"),fg="black", cursor="pirate",command=self.delete).place(x=505,y=353,width=150,height=35)
#===============================================================================
    def search(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_search.get()=="":
                messagebox.showerror("Error","Roll No. should be required",parent=self.root)
            cur.execute("select * from result where roll=?",(self.var_search.get(),))
            row=cur.fetchone()
            if row!=None:
                self.var_id=row[0]
                self.roll.config(text=row[1])
                self.name.config(text=row[2])
                self.course.config(text=row[3])
                self.marks.config(text=row[4])
                self.full.config(text=row[5])
                self.per.config(text=row[6])
            else:
                messagebox.showerror("Error","No record found",parent=self.root)
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to {str(ex)}") 
    def clear(self):
        self.var_id=""
        self.roll.config(text="")
        self.name.config(text="")
        self.course.config(text="")
        self.marks.config(text="")
        self.full.config(text="")
        self.per.config(text="")
        self.var_search.set("")
      
    def delete(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_id=="":
                messagebox.showerror("Error","Search student result first",parent=self.root)
            else:
                cur.execute("select * from result  Where rid=?",(self.var_id,))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid student Result",parent=self.root)
                else:
                    op=messagebox.askyesno("confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from result where rid=?",(self.var_id,))
                        con.commit()
                        messagebox.showinfo("Delete","Result deleted successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
                    messagebox.showerror("Error",f"Error due to {str(ex)}")     
if __name__=="__main__": 
        root = Tk()
        obj = reportclass(root)
        root.mainloop()