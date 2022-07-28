from tkinter import* 
from tkinter import ttk 
from tkinter import Tk 
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2
import os
import numpy as np



class Train :
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recogn")


        title_lbl = Label(self.root, text ="DATASET TRAINING", font=("times new roman", 35, "bold"), bg = "white", fg = "brown")
        title_lbl.place(x=0,y=0,width=1530,height=100)


        img_top = Image.open(r"C:\Users\Dell\Downloads\55.jpg")
        img_top = img_top.resize((1530,630),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img_top)

        top_label = Label(self.root,image = self.photoimg)
        top_label.place(x=0,y=100,width=1540,height=300)


        img_down = Image.open(r"C:\Users\Dell\Downloads\55.jpg")
        img_down = img_down.resize((1530,630),Image.ANTIALIAS)
        self.photoimgd = ImageTk.PhotoImage(img_down)

        down_label = Label(self.root,image = self.photoimgd)
        down_label.place(x=0,y=500,width=1540,height=300)

        b1_1 = Button(self.root, text = "TRAIN DATA" ,command=self.train_classifier, cursor ="hand2", font=("times new roman", 35, "bold"), bg = "yellow", fg = "black")
        b1_1.place(x=0,y=400,width=1540,height=100)


    def train_classifier(self):
        data_dir = ("data")
        path = [os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        


        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')##################grayscale
            imagenp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imagenp)
            ids.append(id)

            cv2.imshow("training", imagenp)
            cv2.waitKey(1)==13
        
        ids = np.array(ids)

        ##############classifier train

        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()

        messagebox.showinfo("result", "training completed !!!!!!!")























if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()

