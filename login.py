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
from tkinter import messagebox
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector 


def main():
    win  = Tk()
    app = login_window(win)
    win.mainloop()
class login_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1600x900+0+0")

        self.bg = ImageTk.PhotoImage(file = r"C:\Users\Dell\Downloads\a1.jpg")#image declaration 
        labe_bg = Label(self.root, image = self.bg)
        labe_bg.place(x=0,y=0,width=1600,height=900)

        frame  = Frame(self.root, bg = "black")
        frame.place(x = 550, y=170, width = 400, height = 500)
         

        img1 = Image.open(r"C:\Users\Dell\Downloads\login.png")
        img1 = img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        labelimg1 = Label(image = self.photoimage1,bg = "black", borderwidth=0)
        labelimg1.place(x = 700, y=175, width=100, height=100) 

        get_str = Label(frame, text = "Login To Get Started",font = ("times new roman", 28, "bold"), fg = "white", bg = "black")
        get_str.place(x = 25, y=115)

        #label

        username_label = Label(frame, text = "User Name",font = ("times new roman", 15, "bold"), fg = "white", bg = "black")
        username_label.place(x=70,y=175)
        self.txtuser = ttk.Entry(frame,font = ("times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=210, width=270)
        

        pss_label = Label(frame, text = "Password",font = ("times new roman", 15, "bold"), fg = "white", bg = "black")
        pss_label.place(x=70,y=255)
        self.txtuser1 = ttk.Entry(frame,font = ("times new roman", 15, "bold"))
        self.txtuser1.place(x=40, y=290, width=270)

        login_button = Button(frame, text="Login", font = ("times new roman",15, "bold"),command =self.login1,bd = 3, relief=RIDGE, bg = "white", fg = "blue",activeforeground="blue", activebackground="white")

        login_button.place(x=110,y=341,width=120,height = 35)

        reg_button = Button(frame, text="New?, Register",command = self.register_window, font = ("times new roman",15, "bold"),bd = 3,borderwidth = 0, relief=RIDGE, bg = "black", fg = "yellow",activeforeground="yellow", activebackground="black")

        reg_button.place(x=75,y=386,width=200)

        fp_button = Button(frame, text="Forgot Password?",command = self.forgot_password, font = ("times new roman",15, "bold"),bd = 3,borderwidth = 0, relief=RIDGE, bg = "black", fg = "yellow",activeforeground="yellow", activebackground="black")

        fp_button.place(x=75,y=435,width=200)


    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)

    def login1(self):
        if self.txtuser.get() == "" or self.txtuser1.get() == "":
            messagebox.showerror("Error", "Enter the required fields")
        elif self.txtuser.get() == "kunal" and self.txtuser1.get() == "lllll":
            messagebox.showinfo("Success", "Welcome to Attendance Management System")
        else:
           conn = mysql.connector.connect(host = "127.0.0.1", username = "root", password ="Kunal123!", database = "facerecognition", auth_plugin='mysql_native_password')
           my_cursor = conn.cursor()
           my_cursor.execute("select * from regiser where Email=%s and Password = %s",(

               self.txtuser.get(),
               self.txtuser1.get()
           ))
           row  = my_cursor.fetchone()
           if row == None:
               messagebox.showerror("Error", "Invalid username/password")
           else:
               open_main = messagebox.askyesno("ask","Only authorized person should access")
               if open_main>0:
                   self.new_window = Toplevel(self.root)
                   self.app = facerecognitionsystem(self.new_window)
               else:
                   if not open_main:
                       return
               conn.commit()
               conn.close()

    def resetpas(self):
        if self.comboseq4.get() == "Select":
            messagebox.showerror("Error", "Select the security question",parent=self.root2)
        elif self.txtuser44.get() == "":
            messagebox.showerror("Error", "Enter the security answer",parent=self.root2)
        elif self.txtuser54.get() == "":
            messagebox.showerror("Error", "Enter the password",parent=self.root2)

        else:
           conn = mysql.connector.connect(host = "127.0.0.1", username = "root", password ="Kunal123!", database = "facerecognition", auth_plugin='mysql_native_password')
           my_cursor = conn.cursor()
           qury = ("select * from regiser where Email=%s and SecurityQuestion=%s and SecurityAnswer=%s")
           vlue = (self.txtuser.get(),self.comboseq4.get(),self.txtuser44.get(),)
           my_cursor.execute(qury,vlue)

           roww = my_cursor.fetchone()

           if roww==None:
               messagebox.showerror("Error", "please enter the correct answer")
           else:
               queryyy = ("update regiser set Password = %s where Email = %s")
               valueee = (self.txtuser54.get(),self.txtuser.get(),)
               my_cursor.execute(queryyy,valueee)

               conn.commit()
               conn.close()
               messagebox.showinfo("Success", "Password has been reset successfully",parent=self.root2)
               self.root2.destroy()









    def forgot_password(self):
        if self.txtuser.get() == "":
            messagebox.showerror("Error", "please enter the email address to reset password")
        else:
           conn = mysql.connector.connect(host = "127.0.0.1", username = "root", password ="Kunal123!", database = "facerecognition", auth_plugin='mysql_native_password')
           my_cursor = conn.cursor()
           query = ("select * from regiser where Email=%s")
           value = (self.txtuser.get(),)
           my_cursor.execute(query,value)
           row = my_cursor.fetchone()
        if row== None:
            messagebox.showerror("Error", "username not found, please enter the valid username!")
        else:
            conn.close()
            self.root2 = Toplevel()
            self.root2.title("Forgot password")
            self.root2.geometry("348x450+610+170")
            l = Label(self.root2,text="Forgot password",font = ("times new roman", 28, "bold"), fg = "red", bg = "green")
            l.place(x = 0, y = 10, relwidth = 1)

            seqq_label4 = Label(self.root2, text = "Select Security Question",font = ("times new roman", 15, "bold"), fg = "green", bg = "white")
            seqq_label4.place(x=50,y=80)

            self.comboseq4 = ttk.Combobox(self.root2,font=("times new roman", 15, "bold"), width=17, state = "readonly")
            self.comboseq4["values"] = ("Select Question ", "Which is your favourite site to surf on?","Which site , you browse the least?","Which is your least favorite color?")
            self.comboseq4.place(x= 50,y=110,width=250)
            self.comboseq4.current(0)
            

            seqa_label4 = Label(self.root2, text = "Security Answer",font = ("times new roman", 15, "bold"), fg = "green", bg = "white")
            seqa_label4.place(x=50,y=150)
            self.txtuser44 = ttk.Entry(self.root2,font = ("times new roman", 15, "bold"))
            self.txtuser44.place(x=50, y=180, width=100)

            password_label4 = Label(self.root2, text = "New Password",font = ("times new roman", 15, "bold"), fg = "green", bg = "white")
            password_label4.place(x=50,y=220)
            self.txtuser54 = ttk.Entry(self.root2,font = ("times new roman", 15, "bold"))
            self.txtuser54.place(x=50, y=250, width=100)

            submit_button = Button(self.root2, text="Submit",command = self.resetpas,font = ("times new roman",15, "bold"),bd = 6, relief=RIDGE, bg = "black", fg = "white")

            submit_button.place(x=50,y=300,width=150,height = 50)
    

    









class Register:
    def __init__(self,root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        ## text variables

        self.var_firstname = StringVar()
        self.var_lastname = StringVar()
        self.var_contaact = StringVar()
        self.var_email = StringVar()
        self.var_seqq = StringVar()
        self.var_seqa = StringVar()
        self.var_password = StringVar()
        self.var_cpassword = StringVar()



        

        img = Image.open(r"C:\Users\Dell\Downloads\PS4.jpg")
        img = img.resize((1600,900),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        first_label = Label(self.root,image = self.photoimg)
        first_label.place(x=0,y=0,width=1600,height=900)


        frame = Frame(self.root,bg = "white")
        frame.place(x=400,y=200,width=800,height = 500)

        get_str = Label(frame, text = "Register Here",font = ("times new roman", 28, "bold"), fg = "white", bg = "green")
        get_str.place(x = 270, y=30)


        firstname_label = Label(frame, text = "First Name",font = ("times new roman", 15, "bold"), fg = "green", bg = "white")
        firstname_label.place(x=50,y=100)
        self.txtuser = ttk.Entry(frame,textvariable=self.var_firstname,font = ("times new roman", 15, "bold"))
        self.txtuser.place(x=50, y=140, width=100)

        lastname_label = Label(frame, text = "Last Name",font = ("times new roman", 15, "bold"), fg = "green", bg = "white")
        lastname_label.place(x=250,y=100)
        self.txtuser1 = ttk.Entry(frame,textvariable=self.var_lastname,font = ("times new roman", 15, "bold"))
        self.txtuser1.place(x=250, y=140, width=100)

        contact_label = Label(frame, text = "Contact Number",font = ("times new roman", 15, "bold"), fg = "green", bg = "white")
        contact_label.place(x=550,y=100)
        self.txtuser2 = ttk.Entry(frame,textvariable=self.var_contaact,font = ("times new roman", 15, "bold"))
        self.txtuser2.place(x=550, y=140, width=100)

        email_label = Label(frame, text = "Email",font = ("times new roman", 15, "bold"), fg = "green", bg = "white")
        email_label.place(x=50,y=200)
        self.txtuser3 = ttk.Entry(frame,textvariable=self.var_email,font = ("times new roman", 15, "bold"))
        self.txtuser3.place(x=50, y=240, width=100)

        seqq_label = Label(frame, text = "Select Security Question",font = ("times new roman", 15, "bold"), fg = "green", bg = "white")
        seqq_label.place(x=250,y=200)

        self.comboseq = ttk.Combobox(frame,textvariable=self.var_seqq,font=("times new roman", 15, "bold"), width=17, state = "readonly")
        self.comboseq["values"] = ("Select Question ", "Which is your favourite site to surf on?","Which site , you browse the least?","Which is your least favorite color?")
        self.comboseq.place(x= 250,y=240,width=250)
        self.comboseq.current(0)
        

        seqa_label = Label(frame, text = "Security Answer",font = ("times new roman", 15, "bold"), fg = "green", bg = "white")
        seqa_label.place(x=550,y=200)
        self.txtuser4 = ttk.Entry(frame,textvariable=self.var_seqa,font = ("times new roman", 15, "bold"))
        self.txtuser4.place(x=550, y=240, width=100)

        password_label = Label(frame, text = "Password",font = ("times new roman", 15, "bold"), fg = "green", bg = "white")
        password_label.place(x=50,y=300)
        self.txtuser5 = ttk.Entry(frame,textvariable=self.var_password,font = ("times new roman", 15, "bold"))
        self.txtuser5.place(x=50, y=340, width=100)

        cpassword_label = Label(frame, text = "Confirm Password",font = ("times new roman", 15, "bold"), fg = "green", bg = "white")
        cpassword_label.place(x=250,y=300)
        self.txtuser6 = ttk.Entry(frame,textvariable=self.var_cpassword,font = ("times new roman", 15, "bold"))
        self.txtuser6.place(x=250, y=340, width=100)

        end_button = Button(frame, text="Register Now", command = self.register_data,font = ("times new roman",15, "bold"),bd = 6, relief=RIDGE, bg = "black", fg = "white")

        end_button.place(x=550,y=400,width=150,height = 50)

        btologin_button = Button(frame, text="Back to login page",command = self.login_return, font = ("times new roman",15, "bold"),bd = 6, relief=RIDGE, bg = "white", fg = "blue")

        btologin_button.place(x=300,y=400,width=170,height = 50)

    # function declaration for register Button
    def login_return(self):
        self.root.destroy()

    def register_data(self):
       if self.var_firstname.get() == "" or self.var_email.get() == "" or  self.var_seqq.get() == "Select" or self.var_seqa.get() == "" or self.var_contaact.get() == "" or self.var_password.get() == "" or self.var_cpassword.get() == "" :

           messagebox.showerror("Error","Enter all fields")
       elif self.var_password.get() != self.var_cpassword.get():

           messagebox.showerror("Error","password and confirm password must be same")
       else:
           conn = mysql.connector.connect(host = "127.0.0.1", username = "root", password ="Kunal123!", database = "facerecognition", auth_plugin='mysql_native_password')
           my_cursor = conn.cursor()
           query = ("select * from regiser where Email = %s")
           
           value  = (self.var_email.get(),)
           
           my_cursor.execute(query,value)
           
           row  = my_cursor.fetchone()
           
           if row!=None:
               messagebox.showerror("Error", "email id already registered")
           else:
               my_cursor.execute("insert into regiser values(%s,%s,%s,%s,%s,%s,%s)",(

                self.var_firstname.get(),
                self.var_lastname.get(),
                self.var_contaact.get(),
                self.var_email.get(),
                self.var_seqq.get(),
                self.var_seqa.get(),
                self.var_password.get()
    
               )
               
               
               
               
               
               )

               conn.commit()
               
               conn.close()
               messagebox.showinfo("Success", "Details has been added successfully")



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
    main()