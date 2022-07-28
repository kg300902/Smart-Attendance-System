from tkinter import* 
from tkinter import ttk 
from tkinter import Tk 
from PIL import Image, ImageTk
from student import student
import os
import tkinter
from train import Train
from facereco import Face_Reco
from attendance import atendance
from developer import developer
from help import help






class facerecognitionsystem:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recogn")
        
        img = Image.open(r"C:\Users\Dell\Desktop\tiet.jfif")
        img = img.resize((500,130),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        first_label = Label(self.root,image = self.photoimg)
        first_label.place(x=0,y=0,width=500,height=160)
       
        img1 = Image.open(r"C:\Users\Dell\Desktop\ss.jpg")
        img1 = img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        first_label = Label(self.root,image = self.photoimg1)
        first_label.place(x=500,y=0,width=500,height=160)


        img2 = Image.open(r"C:\Users\Dell\Desktop\sjd.jfif")
        img2 = img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        first_label = Label(self.root,image = self.photoimg2)
        first_label.place(x=1000,y=0,width=500,height=160)


        img3 = Image.open(r"C:\Users\Dell\Desktop\bg.jpg")
        img3 = img3.resize((1530,630),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_label = Label(self.root,image = self.photoimg3)
        bg_label.place(x=0,y=160,width=1530,height=630)


        title_lbl = Label(bg_label, text ="FACE RECOGNITION SYSYTEM ", font=("times new roman", 35, "bold"), bg = "white", fg = "green")
        title_lbl.place(x=0,y=0,width=1530,height=100)
        


        #student button
        img4 = Image.open(r"C:\Users\Dell\Desktop\student details.jfif")
        img4 = img4.resize((160,160),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        
        
        b1 = Button(bg_label, image = self.photoimg4, command = self.student_details, cursor ="hand2")
        b1.place(x=150,y=80,width=160,height=160)

        b1_1 = Button(bg_label, text = "Student Details",command = self.student_details , cursor ="hand2", font=("times new roman", 15, "bold"), bg = "white", fg = "green")
        b1_1.place(x=150,y=240,width=160,height=40)
 
        #detect faces

        img5 = Image.open(r"C:\Users\Dell\Desktop\fr.jfif")
        img5 = img5.resize((160,160),Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        
        
        b2 = Button(bg_label, image = self.photoimg5, cursor ="hand2",command=self.face_data)
        b2.place(x=400,y=80,width=160,height=160)

        b2_1 = Button(bg_label, text = "Face Detector",command=self.face_data, cursor ="hand2", font=("times new roman", 15, "bold"), bg = "white", fg = "green")
        b2_1.place(x=400,y=240,width=160,height=40)

        img6 = Image.open(r"C:\Users\Dell\Desktop\attendance.jfif")
        img6 = img6.resize((160,160),Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        
        
        b3 = Button(bg_label, image = self.photoimg6, cursor ="hand2",command=self.attendance_data,)
        b3.place(x=700,y=80,width=160,height=160)

        b3_1 = Button(bg_label, text = "Attendance", cursor ="hand2",command=self.attendance_data, font=("times new roman", 15, "bold"), bg = "white", fg = "green")
        b3_1.place(x=700,y=240,width=160,height=40)

        img7 = Image.open(r"C:\Users\Dell\Desktop\help desk.png")
        img7 = img7.resize((160,160),Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        
        
        b4 = Button(bg_label, image = self.photoimg7,command = self.help1, cursor ="hand2")
        b4.place(x=1000,y=80,width=160,height=160)

        b4_1 = Button(bg_label, text = "Help Desk",command = self.help1, cursor ="hand2", font=("times new roman", 15, "bold"), bg = "white", fg = "green")
        b4_1.place(x=1000,y=240,width=160,height=40)


        img8 = Image.open(r"C:\Users\Dell\Pictures\training data.png")
        img8 = img8.resize((160,160),Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        
        
        b5 = Button(bg_label, image = self.photoimg8, cursor ="hand2", command =self.train_data)
        b5.place(x=150,y=350,width=160,height=160)

        b5_1 = Button(bg_label, text = "Train Data", cursor ="hand2", font=("times new roman", 15, "bold"), bg = "white", fg = "green",command=self.train_data)
        b5_1.place(x=150,y=510,width=160,height=40)
 
        #detect faces

        img9 = Image.open(r"C:\Users\Dell\Desktop\photos.jfif")
        img9 = img9.resize((160,160),Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        
        
        b6 = Button(bg_label, image = self.photoimg9, cursor ="hand2",command =self.open_image)
        b6.place(x=400,y=350,width=160,height=160)

        b6_1 = Button(bg_label, text = "Photos", cursor ="hand2",command =self.open_image ,font=("times new roman", 15, "bold"), bg = "white", fg = "green")
        b6_1.place(x=400,y=510,width=160,height=40)



        img10 = Image.open(r"C:\Users\Dell\Pictures\dev.png")
        img10 = img10.resize((160,160),Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        
        
        b7 = Button(bg_label, image = self.photoimg10, command = self.developer,cursor ="hand2")
        b7.place(x=700,y=350,width=160,height=160)

        b7_1 = Button(bg_label, text = "Developer",command = self.developer, cursor ="hand2", font=("times new roman", 15, "bold"), bg = "white", fg = "green")
        b7_1.place(x=700,y=510,width=160,height=40)

        img11 = Image.open(r"C:\Users\Dell\Desktop\exit.jfif")
        img11 = img11.resize((160,160),Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        
        
        b8 = Button(bg_label, image = self.photoimg11,command = self.exitf, cursor ="hand2")
        b8.place(x=1000,y=350,width=160,height=160)

        b8_1 = Button(bg_label, text = "Exit",command = self.exitf, cursor ="hand2", font=("times new roman", 15, "bold"), bg = "white", fg = "green")
        b8_1.place(x=1000,y=510,width=160,height=40)

    def open_image(self):
        os.startfile("data")


        #function buttons
    def student_details(self):

        self.new_window = Toplevel(self.root)
        self.app = student(self.new_window)
    
    def train_data(self):

        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):

        self.new_window = Toplevel(self.root)
        self.app = Face_Reco(self.new_window)
    
    def attendance_data(self):

        self.new_window = Toplevel(self.root)
        self.app = atendance(self.new_window)

    def developer(self):

        self.new_window = Toplevel(self.root)
        self.app = developer(self.new_window)

    def help1(self):

        self.new_window = Toplevel(self.root)
        self.app = help(self.new_window)
    
    def exitf(self):
        self.exitf = tkinter.messagebox.askyesno("Face Recognition", "Are you sure you want to exit?",parent = self.root)

        if self.exitf>0:
            self.root.destroy()
        else:
            return 





        

if __name__ == "__main__":
    root = Tk()
    obj = facerecognitionsystem(root)
    root.mainloop()

