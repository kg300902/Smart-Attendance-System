from tkinter import* 
from tkinter import ttk 
from tkinter import Tk 
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2
import os

import csv
from tkinter import filedialog 




mydata  = []


class atendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendance")

        #### texxt variables


        self.var_id = StringVar()
        self.var_rol = StringVar()
        self.var_name = StringVar()
        self.var_department = StringVar()
        self.var_time = StringVar()
        self.var_data = StringVar()
        self.var_attend = StringVar()
        


        img = Image.open(r"C:\Users\Dell\Desktop\atn.jpg")
        img = img.resize((800,200),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        first_label = Label(self.root,image = self.photoimg)
        first_label.place(x=0,y=0,width=800,height=200)
       
        img1 = Image.open(r"C:\Users\Dell\Desktop\download.jpg")
        img1 = img1.resize((800,200),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        first_label = Label(self.root,image = self.photoimg1)
        first_label.place(x=800,y=0,width=800,height=200)

        img3 = Image.open(r"C:\Users\Dell\Desktop\bg1.jpeg")
        img3 = img3.resize((1530,630),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_label = Label(self.root,image = self.photoimg3)
        bg_label.place(x=0,y=200,width=1530,height=630)

        title_lbl = Label(bg_label, text ="ATTENDANCE MANAGEMENT SYSYTEM ", font=("times new roman", 35, "bold"), bg = "white", fg = "green")
        title_lbl.place(x=0,y=0,width=1530,height=50)

        Mainframe  = Frame(bg_label,bg= "white",bd=2)
        Mainframe.place(x=0,y=55,width=1530,height=630)

        left_label = LabelFrame(Mainframe, bd = 2,bg= "white", relief = RIDGE, text = "Attendance Details", font = ("times new roman",12, "bold"))
        left_label.place(x=10,y=10,width=760,height=500)

        left_inside_frame  = Frame(left_label,bg= "white",relief = RIDGE,bd=2)
        left_inside_frame.place(x=0,y=0,width=700,height=350)

        #label and entry

        attendance_id = Label(left_inside_frame,text = "Attendance Id",  font=("times new roman", 12, "bold"), bg = "white", fg = "black")
        attendance_id.grid(row=0,column = 0,padx = 10,sticky=W)

        attendance_id_entry = ttk.Entry(left_inside_frame,  width=20,textvariable=self.var_id, font = ("times new roman",12, "bold"))
        attendance_id_entry.grid(row=0,column = 1,padx = 10,sticky = W)

        Rollno_id = Label(left_inside_frame,text = "Roll No.",  font=("times new roman", 12, "bold"), bg = "white", fg = "black")
        Rollno_id.grid(row=0,column = 2,padx = 10,sticky=W)

        Rollno_id_entry = ttk.Entry(left_inside_frame,  width=20,textvariable=self.var_rol ,font = ("times new roman",12, "bold"))
        Rollno_id_entry.grid(row=0,column = 3,padx = 10,sticky = W)

        Name_id = Label(left_inside_frame,text = "Name",  font=("times new roman", 12, "bold"), bg = "white", fg = "black")
        Name_id.grid(row=1,column = 0,padx = 10,sticky=W)

        Name_id_entry = ttk.Entry(left_inside_frame,  width=20,textvariable=self.var_name ,font = ("times new roman",12, "bold"))
        Name_id_entry.grid(row=1,column = 1,padx = 10,sticky = W)

        Department_id = Label(left_inside_frame,text = "Department",  font=("times new roman", 12, "bold"), bg = "white", fg = "black")
        Department_id.grid(row=1,column = 2,padx = 10,sticky=W)

        Department_id_entry = ttk.Entry(left_inside_frame,  width=20,textvariable=self.var_department, font = ("times new roman",12, "bold"))
        Department_id_entry.grid(row=1,column = 3,padx = 10,sticky = W)

        Time_id = Label(left_inside_frame,text = "Time",  font=("times new roman", 12, "bold"), bg = "white", fg = "black")
        Time_id.grid(row=2,column = 0,padx = 10,sticky=W)

        Time_id_entry = ttk.Entry(left_inside_frame,  width=20,textvariable=self.var_time, font = ("times new roman",12, "bold"))
        Time_id_entry.grid(row=2,column = 1,padx = 10,sticky = W)

        Date_id = Label(left_inside_frame,text = "Date",  font=("times new roman", 12, "bold"), bg = "white", fg = "black")
        Date_id.grid(row=2,column = 2,padx = 10,sticky=W)

        Date_id_entry = ttk.Entry(left_inside_frame,  width=20,textvariable=self.var_data, font = ("times new roman",12, "bold"))
        Date_id_entry.grid(row=2,column = 3,padx = 10,sticky = W)

        At_id = Label(left_inside_frame,text = "Attendance status",  font=("times new roman", 12, "bold"), bg = "white", fg = "black")
        At_id.grid(row=4,column = 1,padx = 10,sticky=W)

        dep_combo = ttk.Combobox(left_inside_frame, font=("times new roman", 12, "bold"), width=17,textvariable=self.var_attend, state = "readonly")
        dep_combo["values"] = ("Status","Absent", "Present")
        dep_combo.current(0)
        dep_combo.grid(row=4,column=2,padx=10,sticky=W)

        button_student_frame = Frame(left_inside_frame, bd = 2, bg = "white", relief= RIDGE)
        button_student_frame.place(x=0,y=250,width=400,height=50)

        save_button = Button(button_student_frame, text="Import data",command=self.importCsv, font = ("times new roman",12, "bold"), bg = "black", fg = "yellow")
        save_button.grid(row=0,column=0)

        uppdate_button = Button(button_student_frame, text="Export data",command = self.exportCsv, font = ("times new roman",12, "bold"), bg = "black", fg = "yellow")
        uppdate_button.grid(row=0,column=1)

        

        reset_button = Button(button_student_frame, text="Reset",command = self.resetdata, font = ("times new roman",12, "bold"), bg = "black", fg = "yellow")
        reset_button.grid(row=0,column=3)

        




        right_label = LabelFrame(Mainframe, bd = 2,bg= "white", relief = RIDGE, text = "Student Details", font = ("times new roman",12, "bold"))
        right_label.place(x=780,y=10,width=760,height=500)

        table_frame = Frame(right_label, bd = 2, bg = "white", relief= RIDGE)
        table_frame.place(x=5,y=5,width=700,height=450)

        #scrollbar
        scroll_bar_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_bar_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame, columns=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_bar_x.set, yscrollcommand=scroll_bar_y.set)
        scroll_bar_x.pack(side=BOTTOM, fill = X)
        scroll_bar_y.pack(side=RIGHT, fill = Y)
        scroll_bar_x.config(command= self.AttendanceReportTable.xview)
        scroll_bar_y.config(command= self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id", text="Attendanceid")
        self.AttendanceReportTable.heading("roll", text="Roll")
        self.AttendanceReportTable.heading("name", text="Name")
        self.AttendanceReportTable.heading("department", text="Department")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading("attendance", text="Attendance")
        
        self.AttendanceReportTable["show"] = "headings"
        self.AttendanceReportTable.column("id", width=100)
        self.AttendanceReportTable.column("roll", width=100)
        self.AttendanceReportTable.column("name", width=100)
        self.AttendanceReportTable.column("department", width=100)
        self.AttendanceReportTable.column("time", width=100)
        self.AttendanceReportTable.column("date", width=100)
        self.AttendanceReportTable.column("attendance", width=100)

        self.AttendanceReportTable.pack(fill=BOTH, expand = True)
        self.AttendanceReportTable.bind("<ButtonRelease>", self.getcursor)




        #fetch data 

    def fetchdata(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
        

    def importCsv(self):

        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir= os.getcwd(),title = "Open CSV", filetypes=(("CSV File","*csv"),("ALL File","*.*")),parent = self.root)
        with open(fln) as myflie:
            csvread = csv.reader(myflie, delimiter =",")
            for i in csvread:
                mydata.append(i)
            self.fetchdata(mydata)

    def exportCsv(self):

        try:
            if len(mydata)<1:
                messagebox.showerror("NO Data", "No Data to Export",parent=self.root)
                return False
            fln1 = filedialog.asksaveasfilename(initialdir= os.getcwd(),title = "Open CSV", filetypes=(("CSV File","*csv"),("ALL File","*.*")),parent = self.root)
            with open(fln1,mode = "w",newline = "") as myfile:
                csvwrite = csv.writer(myfile, delimiter =",")
                for i in mydata:
                    csvwrite.writerow(i)
                messagebox.showinfo("Data Exported","Data exported successfully")
        except Exception as es:
                messagebox.showerror("Error",f"due to :{str(es)}", parent = self.root)

    def getcursor(self,event=""):
        cursor_focus = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_focus)
        data = content["values"]

        self.var_id.set(data[0])
        self.var_rol.set(data[1])
        self.var_name.set(data[2])
        self.var_department.set(data[3])
        self.var_time.set(data[4])
        self.var_data.set(data[5])
        self.var_attend.set(data[6])


    def resetdata(self):

        self.var_id.set("")
        self.var_rol.set("")
        self.var_name.set("")
        self.var_department.set("")
        self.var_time.set("")
        self.var_data.set("")
        self.var_attend.set("Status")

        











        







if __name__ == "__main__":
    root = Tk()
    obj = atendance(root)
    root.mainloop()