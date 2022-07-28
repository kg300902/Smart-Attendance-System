from tkinter import* 
from tkinter import ttk 
from tkinter import Tk 
from PIL import Image, ImageTk
from tkinter import messagebox
from time import time
from datetime import datetime

import mysql.connector 
import cv2
import os
import numpy as np



class Face_Reco :
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recogn")

        title_lbl = Label(self.root, text ="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg = "white", fg = "blue")
        title_lbl.place(x=0,y=0,width=1530,height=100)

        img_top1 = Image.open(r"C:\Users\Dell\Desktop\lo.jfif")
        img_top1 = img_top1.resize((1530,630),Image.ANTIALIAS)
        self.photoimg12 = ImageTk.PhotoImage(img_top1)

        top_label1 = Label(self.root,image = self.photoimg12)
        top_label1.place(x=0,y=100,width=1530,height=600)

        b1_12 = Button(self.root, text = "FACE RECOGNIZATION" ,command = self.face_rec, cursor ="hand2", font=("times new roman", 35, "bold"), bg = "yellow", fg = "black")
        b1_12.place(x=0,y=700,width=1540,height=100)

    def attendance(self,i,r,n,d):
        with open("m.csv","r+", newline = "\n") as f:
            mydatalist = f.readlines()
            name_list = []

            for line in mydatalist:
                entry  = line.split((","))
                name_list.append(entry[0])
            if ((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now  = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtstring = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtstring},{d1},present")


                


    def face_rec(self):

        def draw_boundary(img, classifier, scaleFactor,minNeighbors, color, text, clf):
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            features = classifier.detectMultiScale(gray_img,scaleFactor,minNeighbors)
            coordinates = []


            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
                id, predict = clf.predict(gray_img[y:y+h,x:x+w])
                confidence = int(100*(1-predict/300))

                conn = mysql.connector.connect(host = "127.0.0.1", username = "root", password ="Kunal123!", database = "facerecognition", auth_plugin='mysql_native_password')
                my_cursor = conn.cursor()

                my_cursor.execute("select Name from student where Student_Id="+str(id))

                n = my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select Roll from student where Student_Id="+str(id))

                r = my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select Department from student where Student_Id="+str(id))

                d = my_cursor.fetchone()
                d="+".join(d)

                my_cursor.execute("select Student_Id from student where Student_Id="+str(id))

                i = my_cursor.fetchone()
                i="+".join(i)

                


                if confidence > 80:
                    cv2.putText(img,f"Id  :  {i}",(x,y-70),cv2.FONT_HERSHEY_DUPLEX,0.8,(0,0,255),3)
                    cv2.putText(img,f"RollNo.  :  {r}",(x,y-50),cv2.FONT_HERSHEY_DUPLEX,0.8,(0,0,255),3)
                    cv2.putText(img,f"Name.    :  {n}",(x,y-30),cv2.FONT_HERSHEY_DUPLEX,0.8,(0,0,255),3)
                    cv2.putText(img,f"Department : {d}",(x,y-10),cv2.FONT_HERSHEY_DUPLEX,0.8,(0,0,255),3)
                    self.attendance(i,r,n,d)

                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)

                    cv2.putText(img,"unauthorized person",(x,y-50),cv2.FONT_HERSHEY_DUPLEX ,0.8,(0,0,255),3)

                coordinates = [x,y,w,h]

            return coordinates

        def recognize(img, clf,faceCascade):

            coordinates =draw_boundary(img,faceCascade,1.1,10,(0,0,255),"face",clf)
            return img

        faceCascade =cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")


        video_cap = cv2.VideoCapture(0)
        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf,faceCascade)
            cv2.imshow("Face_Recognition",img)

            if cv2.waitKey(1) == 13:

             break
        video_cap.release()
        cv2.destroyAllWindows()







            





if __name__ == "__main__":
    root = Tk()
    obj = Face_Reco(root)
    root.mainloop()
