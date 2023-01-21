from tkinter import *
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk,messagebox
from login_page import login_page
from report import reportclass
import os
class stdntlg:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#86C8BC")
        #==========title=========
        title=Label(self.root,text="Student Result Management System",font=("chalkboard SE",50,"bold"),bg="#CEEDC7", fg="blue").place(x=0,y=10,relwidth=1,height=130)
        #=======================
        btn_course=Button(self.root,text="View student\n Result",font=("Chalkduster",40,"bold"),bg='red',fg="black", cursor="pirate",command=self.add_report).place(x=200,y=250,width=400,height=150)
        btn_course=Button(self.root,text="Admin Login",font=("Chalkduster",40,"bold"),bg='red',fg="red", cursor="pirate",command=self.admin).place(x=700,y=250,width=400,height=150)
        
    def admin(self):
        self.root.destroy()
        os.system("python login_page.py")
        # root = Tk()
        # obj = login_page(root)
        # root.mainloop()
    def add_report(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=reportclass(self.new_win)
if __name__=="__main__":
        root = Tk()
        obj = stdntlg(root)
        root.mainloop()