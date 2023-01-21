from tkinter import*
from PIL import Image,ImageTk #pip install pillow
from course import Courseclass
from student import studentClass
from result import resultclass
from report import reportclass
import os
from tkinter import messagebox
import os
class RMS:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#F8EDE3")
        #=====icons====
        self.logo_dash=ImageTk.PhotoImage(file="images/rsz_1logo.png")
        #=====title====
        title=Label(self.root,text="Student Result Management System",compound=LEFT, padx=10,image=self.logo_dash,font=("chalkboard SE",30,"bold"),bg="#DFD3C3", fg="Black").place(x=0,y=0,relwidth=1,height=70)
        # ====Menu===
        M_Frame=LabelFrame(self.root, text="Menus", font=("Chalkboard",15,"bold"),bg="#DFD3C3",fg="black")
        M_Frame.place(x=10,y=80,width=1340,height=80)
        btn_course=Button(M_Frame,text="Course",font=("helvetica neue",18,"bold"),bg='red',fg="black", cursor="pirate",command=self.add_course).place(x=20,y=5,width=200,height=40)
        btn_student=Button(M_Frame,text="Student",font=("helvetica neue",18,"bold"),bg='red',fg="black", cursor="pirate",command=self.add_student).place(x=240,y=5,width=200,height=40)
        btn_result=Button(M_Frame,text="Result",font=("helvetica neue",18,"bold"),bg='red',fg="black", cursor="pirate",command=self.add_result).place(x=460,y=5,width=200,height=40)
        btn_view=Button(M_Frame,text="View Student Result",font=("helvetica neue",18,"bold"),bg='red',fg="black", cursor="pirate",command=self.add_report).place(x=680,y=5,width=205,height=40)
        btn_logout=Button(M_Frame,text="Logout",font=("helvetica neue",18,"bold"),bg='red',fg="black", cursor="pirate",command=self.logout).place(x=900,y=5,width=200,height=40)
        btn_exit=Button(M_Frame,text="Exit",font=("helvetica neue",18,"bold"),bg='red',fg="black", cursor="pirate",command=self.exit_).place(x=1120,y=5,width=200,height=40)
        #====content====
        self.bg_img=Image.open("/Users/minaam/Desktop/RMS/images/00E1BA9D-725E-43F9-9EA4-BEE93501335F.jpeg")
        self.bg_img=self.bg_img.resize((500,450),Image.ANTIALIAS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)
        self.lbl_img=Label(self.root,image=self.bg_img).place(x=730,y=180,height=350,width=400)
        #===Update_details====
        self.lbl_course=Label(self.root,text="Total Course\n[0]",font=("Chalkboard SE",20),bd=10,relief=RIDGE,bg="#E5E5CB",fg="Black")
        self.lbl_course.place(x=400,y=530,width=300,height=100)
        self.lbl_student=Label(self.root,text="Total Courses\n[0]",font=("Chalkboard SE",20),bd=10,relief=RIDGE,bg="#D5CEA3",fg="Black")
        self.lbl_student.place(x=710,y=530,width=300,height=100)    
        self.lbl_result=Label(self.root,text="Total result\n[0]",font=("Chalkboard SE",20),bd=10,relief=RIDGE,bg="#B09B71",fg="Black")
        self.lbl_result.place(x=1020,y=530,width=300,height=100)
        #=====footer====
        footer=Label(self.root,text="SRMS\nContact Us for any Technical issue: 962xxxx79",font=("chalkboard SE",15),bg="#85586F", fg="white").pack(side=BOTTOM,fill=X)
    def add_course(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=Courseclass(self.new_win)
    def add_student(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=studentClass(self.new_win)
    def add_result(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=resultclass(self.new_win)
    def add_report(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=reportclass(self.new_win)
    def logout(self):
        op=messagebox.askyesno("Confirm","Do you really want to logout?",parent=self.root)
        if op==True:
            os.system("python login_page.py")
            self.root.destroy()
            root.mainloop()
    def exit_(self):
        op=messagebox.askyesno("Confirm","Do you really want to Exit?",parent=self.root)
        if op==True:
            self.root.destroy()
            os.system("python login_page.py")
if __name__=="__main__":
        root = Tk()
        obj = RMS(root)
        root.mainloop()