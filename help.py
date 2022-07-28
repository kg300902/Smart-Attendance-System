from tkinter import* 
from tkinter import ttk 
from tkinter import Tk 
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2











class help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("HELP DESK")

        title_lbl = Label(self.root, text ="HELP DESK", font=("times new roman", 35, "bold"), bg = "white", fg = "brown")
        title_lbl.place(x=0,y=0,width=1530,height=100)


        img_top = Image.open(r"C:\Users\Dell\Desktop\download.png")
        img_top = img_top.resize((1530,720),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img_top)

        top_label = Label(self.root,image = self.photoimg)
        top_label.place(x=0,y=100,width=1530,height=720)

        Mainframe  = Frame(top_label,bg= "white",bd=2)
        Mainframe.place(x=0,y=55,width=400,height=150)

        

        dep_label = Label(Mainframe,text = "Email : ",  font=("times new roman", 20, "bold"), bg = "white", fg = "black")
        dep_label.place(x=0,y=5)
        dep_label2 = Label(Mainframe,text = "gkunal770@gmail.com",  font=("times new roman", 30, "bold"), bg = "white", fg = "black")
        dep_label2.place(x=0,y=55)
        







if __name__ == "__main__":
    root = Tk()
    obj = help(root)
    root.mainloop()
