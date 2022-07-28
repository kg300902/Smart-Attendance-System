from tkinter import* 
from tkinter import ttk 
from tkinter import Tk 
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2











class developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Developer")

        title_lbl = Label(self.root, text ="DEVELOPER", font=("times new roman", 35, "bold"), bg = "white", fg = "brown")
        title_lbl.place(x=0,y=0,width=1530,height=100)


        img_top = Image.open(r"C:\Users\Dell\Desktop\pexels-photo-546819.jpeg")
        img_top = img_top.resize((1530,720),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img_top)

        top_label = Label(self.root,image = self.photoimg)
        top_label.place(x=0,y=100,width=1530,height=720)

        Mainframe  = Frame(top_label,bg= "white",bd=2)
        Mainframe.place(x=1000,y=55,width=1480,height=600)

        img_top2 = Image.open(r"C:\Users\Dell\Desktop\download (1).jpg")
        img_top2 = img_top2.resize((200,200),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img_top2)

        top_label2 = Label(Mainframe,image = self.photoimg2)
        top_label2.place(x=300,y=170,width=200,height=200)

        dep_label = Label(Mainframe,text = "KUNAL GUPTA",  font=("times new roman", 45, "bold"), bg = "white", fg = "black")
        dep_label.place(x=0,y=5)
        dep_label2 = Label(Mainframe,text = "BE-ECE",  font=("times new roman", 45, "bold"), bg = "white", fg = "black")
        dep_label2.place(x=0,y=70)
        dep_label3 = Label(Mainframe,text = "TIET",  font=("times new roman",45 , "bold"), bg = "white", fg = "black")
        dep_label3.place(x=0,y=135)







if __name__ == "__main__":
    root = Tk()
    obj = developer(root)
    root.mainloop()
