from tkinter import* 
from tkinter import ttk 
from tkinter import Tk 
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2











class student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recogn")


        #### texxt variables


        self.var_department = StringVar()
        self.var_gender = StringVar()
        self.var_contactno = StringVar()
        self.var_dob = StringVar()
        self.var_address = StringVar()
        self.var_mentor = StringVar()
        self.var_course = StringVar()
        self.var_semester = StringVar()
        self.var_batch = StringVar()
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_student_id = StringVar()
        self.var_rno = StringVar()
        self.var_year = StringVar()
        

        img = Image.open(r"C:\Users\Dell\Desktop\student1.jfif")
        img = img.resize((500,130),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        first_label = Label(self.root,image = self.photoimg)
        first_label.place(x=0,y=0,width=500,height=160)
       
        img1 = Image.open(r"C:\Users\Dell\Desktop\student2.jfif")
        img1 = img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        first_label = Label(self.root,image = self.photoimg1)
        first_label.place(x=500,y=0,width=500,height=160)


        img2 = Image.open(r"C:\Users\Dell\Desktop\student3.jfif")
        img2 = img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        first_label = Label(self.root,image = self.photoimg2)
        first_label.place(x=1000,y=0,width=500,height=160)


        

        img3 = Image.open(r"C:\Users\Dell\Desktop\bg.jpg")
        img3 = img3.resize((1530,630),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_label = Label(self.root,image = self.photoimg3)
        bg_label.place(x=0,y=160,width=1530,height=630)


        title_lbl = Label(bg_label, text ="STUDENT MANAGEMENT SYSYTEM ", font=("times new roman", 35, "bold"), bg = "white", fg = "green")
        title_lbl.place(x=0,y=0,width=1530,height=100)


        Mainframe  = Frame(bg_label,bg= "white",bd=2)
        Mainframe.place(x=0,y=100,width=1530,height=530)


        left_label = LabelFrame(Mainframe, bd = 2,bg= "white", relief = RIDGE, text = "Student Details", font = ("times new roman",12, "bold"))
        left_label.place(x=10,y=10,width=760,height=500)
        

        imgl = Image.open(r"C:\Users\Dell\Desktop\tsta.jfif")
        imgl = imgl.resize((1530,630),Image.ANTIALIAS)
        self.photoimgl = ImageTk.PhotoImage(imgl)

        bg_label = Label(left_label,image = self.photoimgl)
        bg_label.place(x=0,y=0,width=760,height=130)

        course_label = LabelFrame(left_label, bd = 2,bg= "white", relief = RIDGE, text = "Current course information", font = ("times new roman",12, "bold"))
        course_label.place(x=5,y=135,width=740,height=120)

        dep_label = Label(course_label,text = "Department",  font=("times new roman", 12, "bold"), bg = "white", fg = "black")
        dep_label.grid(row=0,column = 0,padx = 10,sticky=W)
       
        dep_combo = ttk.Combobox(course_label, textvariable=self.var_department, font=("times new roman", 12, "bold"), width=17, state = "readonly")
        dep_combo["values"] = ("Select department/branch", "CS","ECE","ELE","MEE","Civil","Chemical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        dep_label2 = Label(course_label,text = "Course",  font=("times new roman", 12, "bold"), bg = "white", fg = "black")
        dep_label2.grid(row=0,column = 2,padx = 10,sticky=W)
       
        dep_combo2 = ttk.Combobox(course_label,  textvariable=self.var_course ,font=("times new roman", 12, "bold"), width=17, state = "readonly")
        dep_combo2["values"] = ("Select course", "B.TECH","M.TECH","PG")
        dep_combo2.current(0)
        dep_combo2.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        dep_label3 = Label(course_label,text = "Year of completion",  font=("times new roman", 12, "bold"), bg = "white", fg = "black")
        dep_label3.grid(row=1,column = 0,padx = 10,sticky=W)
       
        dep_combo3 = ttk.Combobox(course_label, textvariable=self.var_year, font=("times new roman", 12, "bold"), width=17, state = "readonly")
        dep_combo3["values"] = ("Select year", "2021","2022","2023","2024")
        dep_combo3.current(0)
        dep_combo3.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        dep_label4 = Label(course_label,text = "Semester",  font=("times new roman", 12, "bold"), bg = "white", fg = "black")
        dep_label4.grid(row=1,column = 2,padx = 10,sticky=W)
       
        dep_combo4 = ttk.Combobox(course_label, textvariable=self.var_semester, font=("times new roman", 12, "bold"), width=17, state = "readonly")
        dep_combo4["values"] = ("Select semester ", "1","2","3","4","5","6","7","8")
        dep_combo4.current(0)
        dep_combo4.grid(row=1,column=3,padx=2,pady=10,sticky=W)


        #class student information
        class_student_frame = LabelFrame(left_label, bd = 2, bg = "white", relief= RIDGE, text = "Class Student Information", font = ("times new roman",12, "bold"))
        class_student_frame.place(x=5,y=255,width=740,height=220)

        student_id = Label(class_student_frame,text = "Student Id",  font=("times new roman", 12, "bold"), bg = "white", fg = "black")
        student_id.grid(row=0,column = 0,padx = 10,sticky=W)

        student_id_entry = ttk.Entry(class_student_frame, textvariable=self.var_student_id, width=20, font = ("times new roman",12, "bold"))
        student_id_entry.grid(row=0,column = 1,padx = 10,sticky = W)

        student_name = Label(class_student_frame,text = "Student Name",  font=("times new roman", 12, "bold"), bg = "white", fg = "black")
        student_name.grid(row=0,column = 2,padx = 10,sticky=W)

        student_name_entry = ttk.Entry(class_student_frame, textvariable=self.var_name, width=20, font = ("times new roman",12, "bold"))
        student_name_entry.grid(row=0,column = 3,padx = 10,sticky = W)

        student_batch = Label(class_student_frame,text = "Student Batch",  font=("times new roman", 12, "bold"), bg = "white", fg = "black")
        student_batch.grid(row=1,column = 0,padx = 10,sticky=W)

        student_batch_entry = ttk.Entry(class_student_frame, textvariable=self.var_batch, width=20, font = ("times new roman",12, "bold"))
        student_batch_entry.grid(row=1,column = 1,padx = 10,sticky = W)

        student_rno = Label(class_student_frame,text = "Roll No.",  font=("times new roman", 12, "bold"), bg = "white", fg = "black")
        student_rno.grid(row=1,column = 2,padx = 10,sticky=W)

        student_rno_entry = ttk.Entry(class_student_frame, textvariable=self.var_rno, width=20, font = ("times new roman",12, "bold"))
        student_rno_entry.grid(row=1,column = 3,padx = 10,sticky = W)

        student_gender = Label(class_student_frame,text = "Gender",  font=("times new roman", 12, "bold"), bg = "white", fg = "black")
        student_gender.grid(row=2,column = 0,padx = 10,sticky=W)

        dep_combo8 = ttk.Combobox(class_student_frame, textvariable=self.var_gender, font=("times new roman", 12, "bold"), width=17, state = "readonly")
        dep_combo8["values"] = ("Select gender", "M", "F","other")
        dep_combo8.current(0)
        dep_combo8.grid(row=2,column=1,padx=10,sticky=W)

        
        student_dob = Label(class_student_frame,text = "D.O.B.",  font=("times new roman", 12, "bold"), bg = "white", fg = "black")
        student_dob.grid(row=2,column = 2,padx = 10,sticky=W)

        student_dob_entry = ttk.Entry(class_student_frame, textvariable=self.var_dob, width=20, font = ("times new roman",12, "bold"))
        student_dob_entry.grid(row=2,column = 3,padx = 10,sticky = W)

        student_email = Label(class_student_frame,text = "Email",  font=("times new roman", 12, "bold"), bg = "white", fg = "black")
        student_email.grid(row=3,column = 0,padx = 10,sticky=W)

        student_email_entry = ttk.Entry(class_student_frame, textvariable=self.var_email, width=20, font = ("times new roman",12, "bold"))
        student_email_entry.grid(row=3,column = 1,padx = 10,sticky = W)

        student_phone = Label(class_student_frame,text = "Contact no.",  font=("times new roman", 12, "bold"), bg = "white", fg = "black")
        student_phone.grid(row=3,column = 2,padx = 10,sticky=W)

        student_phone_entry = ttk.Entry(class_student_frame, textvariable=self.var_contactno, width=20, font = ("times new roman",12, "bold"))
        student_phone_entry.grid(row=3,column = 3,padx = 10,sticky = W)

        student_city = Label(class_student_frame,text = "Adderss(City)",  font=("times new roman", 12, "bold"), bg = "white", fg = "black")
        student_city.grid(row=4,column = 0,padx = 10,sticky=W)

        student_city_entry = ttk.Entry(class_student_frame, textvariable=self.var_address, width=20, font = ("times new roman",12, "bold"))
        student_city_entry.grid(row=4,column = 1,padx = 10,sticky = W)

        student_techer = Label(class_student_frame,text = "Mentor",  font=("times new roman", 12, "bold"), bg = "white", fg = "black")
        student_techer.grid(row=4,column = 2,padx = 10,sticky=W)

        student_techer_entry = ttk.Entry(class_student_frame, textvariable=self.var_mentor, width=20, font = ("times new roman",12, "bold"))
        student_techer_entry.grid(row=4,column = 3,padx = 10,sticky = W)

        #radio_buttons
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text="Photo Sample", value = "Yes" )
        radiobtn1.grid(row=5,column =0)

        self.var_radio2 = StringVar()
        radiobtn2 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text="NO Photo Sample", value = "No" )
        radiobtn2.grid(row=5,column =2)
        
        
        button_student_frame = Frame(class_student_frame, bd = 2, bg = "white", relief= RIDGE)
        button_student_frame.place(x=0,y=145,width=735,height=50)

        save_button = Button(button_student_frame, text="Save",command = self.add_Data, font = ("times new roman",12, "bold"), bg = "black", fg = "yellow")
        save_button.grid(row=0,column=0)

        uppdate_button = Button(button_student_frame, text="Update", command = self.update_fnc,font = ("times new roman",12, "bold"), bg = "black", fg = "yellow")
        uppdate_button.grid(row=0,column=1)

        delete_button = Button(button_student_frame, text="Delete",command = self.delete_data, font = ("times new roman",12, "bold"), bg = "black", fg = "yellow")
        delete_button.grid(row=0,column=2)

        reset_button = Button(button_student_frame, text="Reset",command = self.reset_data, font = ("times new roman",12, "bold"), bg = "black", fg = "yellow")
        reset_button.grid(row=0,column=3)

        takephoto_button = Button(button_student_frame, command = self.generate_dataset,text="Take photo sample",width=15, font = ("times new roman",12, "bold"), bg = "black", fg = "white")
        takephoto_button.grid(row=0,column=6)

        updatephoto_button = Button(button_student_frame, text="Update photo sample",width=15, font = ("times new roman",12, "bold"), bg = "black", fg = "white")
        updatephoto_button.grid(row=0,column=9)

        









        right_label = LabelFrame(Mainframe, bd = 2,bg= "white", relief = RIDGE, text = "Student Details", font = ("times new roman",12, "bold"))
        right_label.place(x=780,y=10,width=720,height=500)


        imgr = Image.open(r"C:\Users\Dell\Desktop\ll.png")
        imgr = imgr.resize((1530,630),Image.ANTIALIAS)
        self.photoimgr = ImageTk.PhotoImage(imgr)

        bg_label = Label(right_label,image = self.photoimgr)
        bg_label.place(x=0,y=0,width=760,height=130)


        #             searching system 

        search_frame = LabelFrame(right_label, bd = 2, bg = "white", relief= RIDGE, text = "Search System", font = ("times new roman",12, "bold"))
        search_frame.place(x=5,y=135,width=710,height=60)

        search_label = Label(search_frame,text = "Search by :",  font=("times new roman", 12, "bold"), bg = "white", fg = "black")
        search_label.grid(row=0,column = 0,padx = 10,sticky=W)

        search_combo = ttk.Combobox(search_frame, font=("times new roman", 12, "bold"), width=17, state = "readonly")
        search_combo["values"] = ("Select ", "Roll No.","Contact no.")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_button = Button(search_frame, text="Search", font = ("times new roman",12, "bold"), bg = "black", fg = "white")
        search_button.grid(row=0,column=3)

        showll_button = Button(search_frame, text="Show All", font = ("times new roman",12, "bold"), bg = "black", fg = "white")
        showll_button.grid(row=0,column=4)

        search_entry = ttk.Entry(search_frame, width=20, font = ("times new roman",12, "bold"))
        search_entry.grid(row=0,column = 2,padx = 10,sticky = W)

        table_frame = Frame(right_label, bd = 2, bg = "white", relief= RIDGE)
        table_frame.place(x=5,y=200,width=710,height=265)


        scroll_bar_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_bar_y = ttk.Scrollbar(table_frame,orient=VERTICAL)


        self.student_table = ttk.Treeview(table_frame, columns=("Department","course","year","sem","id","name","batch","roll no.","gender","dob","email","contact no.","address","mentor","photo"),xscrollcommand=scroll_bar_x.set, yscrollcommand=scroll_bar_y.set)


        scroll_bar_x.pack(side=BOTTOM, fill = X)
        scroll_bar_y.pack(side=RIGHT, fill = Y)
        scroll_bar_x.config(command= self.student_table.xview)
        scroll_bar_y.config(command= self.student_table.yview)

        self.student_table.heading("Department", text="Department")
        self.student_table.heading("id", text="Student Id")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("roll no.", text="Roll no.")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("batch", text="Batch")
        self.student_table.heading("contact no.", text="Contact no.")
        self.student_table.heading("dob", text="D.O.B.")
        self.student_table.heading("mentor", text="Mentor")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("photo", text="PhotoSampleStatus")
        self.student_table.heading("name", text="Name")
        self.student_table["show"] = "headings"

        self.student_table.column("Department", width = 100)
        self.student_table.column("id", width = 100)
        self.student_table.column("gender", width = 100)
        self.student_table.column("course", width = 100)
        self.student_table.column("roll no.", width = 100)
        self.student_table.column("year", width = 100)
        self.student_table.column("sem", width = 100)
        self.student_table.column("batch", width = 100)
        self.student_table.column("contact no.", width = 100)
        self.student_table.column("dob", width = 100)
        self.student_table.column("mentor", width = 100)
        self.student_table.column("email", width = 100)
        self.student_table.column("address", width = 100)
        self.student_table.column("photo", width = 100)
        self.student_table.column("name", width = 100)
        self.fetch_data()
        

        
        
        

        self.student_table.pack(fill=BOTH, expand = True)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()
        
        ### function declarations
    
    def add_Data(self):
        if self.var_department.get() == "Select department/branch" or self.var_name.get() == "" or self.var_student_id == "":
            messagebox.showerror("Error", "All fields are required",parent = self.root)
        else:
            try:
                conn = mysql.connector.connect(host = "127.0.0.1", username = "root", password ="Kunal123!", database = "facerecognition", auth_plugin='mysql_native_password')
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                self.var_department.get(),
                self.var_course.get(),
                self.var_year.get(),
                self.var_semester.get(),
                self.var_student_id.get(),
                self.var_name.get(),
                self.var_batch.get(),
                self.var_rno.get(),
                self.var_gender.get(),
                self.var_dob.get(),
                self.var_email.get(),
                self.var_contactno.get(),
                self.var_address.get(),
                self.var_mentor.get(),
                self.var_radio1.get()

                
                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details has been added successfully", parent=self.root)
        
            except Exception as es:
                messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.root)

### fetch database
    def fetch_data(self):
        conn = mysql.connector.connect(host = "127.0.0.1", username = "root", password ="Kunal123!", database = "facerecognition", auth_plugin='mysql_native_password')
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()


        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END,values = i)
            conn.commit()
        conn.commit()
    
    def get_cursor(self,event=""):

        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_department.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_student_id.set(data[4])
        self.var_name.set(data[5])
        self.var_batch.set(data[6])
        self.var_rno.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_contactno.set(data[11])
        self.var_address.set(data[12])
        self.var_mentor.set(data[13])
        self.var_radio1.set(data[14])

    def update_fnc(self):
        if self.var_department.get() == "Select department/branch" or self.var_name.get() == "" or self.var_student_id == "":
            messagebox.showerror("Error", "All fields are required",parent = self.root)
        else:
        
            try:

                Upadate = messagebox.askyesno("Update", "do you want to update details?", parent = self.root)
                if Upadate>0:
                    conn = mysql.connector.connect(host = "127.0.0.1", username = "root", password ="Kunal123!", database = "facerecognition", auth_plugin='mysql_native_password')
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Department = %s,Course = %s,Year = %s,Semester = %s,Name = %s,Batch = %s,Roll = %s,Gender = %s,`D.O.B.` = %s,`Email`= %s,`Contact No.` = %s,Adderss=%s,Mentor=%s,`Photo Sample`=%s where `Student_Id` = %s", (




                                                                                                                                                                                    self.var_department.get(),
                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                    self.var_semester.get(),
                                                                                                                                                                                    self.var_name.get(),
                                                                                                                                                                                    self.var_batch.get(),
                                                                                                                                                                                    self.var_rno.get(),
                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                    self.var_contactno.get(),
                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                    self.var_mentor.get(),
                                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                                                    self.var_student_id.get(),
                ))
                else:
                    if not Upadate:
                        return
                messagebox.showinfo("Success","student details added successfully",parent = self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"due to :{str(es)}", parent = self.root)

    

    def delete_data(self):
        if self.var_student_id.get() == "":
            messagebox.showerror("Error","student id must be required", parent = self.root)
        else:
            try:
                delete = messagebox.askyesno("delete details page", "do you want to delete the student details ", parent = self.root)
                if delete>0:
                    conn = mysql.connector.connect(host = "127.0.0.1", username = "root", password ="Kunal123!", database = "facerecognition", auth_plugin='mysql_native_password')
                    my_cursor = conn.cursor()
                    sql = "delete from student where student_id=%s"
                    val = (self.var_student_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return


                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "details deleted successfully", parent = self.root)
            except Exception as es:
                messagebox.showerror("Error",f"due to :{str(es)}", parent = self.root)
    def reset_data(self):

        self.var_department.set("Select department/branch")
        self.var_course.set("select course")
        self.var_year.set("Select year")
        self.var_semester.set("Select semester")
        self.var_rno.set("")
        self.var_batch.set("")
        self.var_name.set("")
        self.var_gender.set("Select gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_contactno.set("")
        self.var_student_id.set("")
        self.var_address.set("")
        self.var_mentor.set("")
        self.var_radio1.set("")

    #generete dataset photo samople
    def generate_dataset(self):
        if self.var_department.get() == "Select department/branch" or self.var_name.get() == "" or self.var_student_id == "":
            messagebox.showerror("Error", "All fields are required",parent = self.root)
        else:
        
            try:

               
                conn = mysql.connector.connect(host = "127.0.0.1", username = "root", password ="Kunal123!", database = "facerecognition", auth_plugin='mysql_native_password')
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id =0
                for x in myresult:
                    id +=1
                my_cursor.execute("update student set Department = %s,Course = %s,Year = %s,Semester = %s,Name = %s,Batch = %s,Roll = %s,Gender = %s,`D.O.B.` = %s,`Email`= %s,`Contact No.` = %s,Adderss=%s,Mentor=%s,`Photo Sample`=%s where `Student_Id` = %s", (




                                                                                                                                                                                    self.var_department.get(),
                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                    self.var_semester.get(),
                                                                                                                                                                                    self.var_name.get(),
                                                                                                                                                                                    self.var_batch.get(),
                                                                                                                                                                                    self.var_rno.get(),
                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                    self.var_contactno.get(),
                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                    self.var_mentor.get(),
                                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                                                    self.var_student_id.get()==id+1,
                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                #load data on facerecognition



                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_crop(img):

                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                    #1.3 scaling factor 5 min neighbour

                    for (x,y,w,h) in faces:
                        face_crop = img[y:y+h,x:x+w]
                        return face_crop
                
                capture = cv2.VideoCapture(0)
                img_id = 0

                while True:
                    ret, myframe = capture.read()
                    if face_crop(myframe) is not None:
                        img_id+=1
                        face  = cv2.resize(face_crop(myframe),(450,450))
                        face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        filename_path = "data/user."+str(id)+"."+str(img_id)+".jpg"

                        cv2.imwrite(filename_path, face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0), 2)
                        cv2.imshow("cropped face", face)


                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                

                capture.release()
                cv2.destroyAllWindows()

                messagebox.showinfo("result","generating dataset completed")
            except Exception as es:
                messagebox.showerror("Error",f"due to :{str(es)}", parent = self.root)













            








    






        


if __name__ == "__main__":
    root = Tk()
    obj = student(root)
    root.mainloop()

