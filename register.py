from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector 

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

        btologin_button = Button(frame, text="Back to login page", font = ("times new roman",15, "bold"),bd = 6, relief=RIDGE, bg = "white", fg = "blue")

        btologin_button.place(x=300,y=400,width=170,height = 50)

    # function declaration for register Button

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












        


if __name__ == "__main__":
    root = Tk()
    app = Register(root)
    root.mainloop()




    
