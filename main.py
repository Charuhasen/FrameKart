from turtle import width
import cv2
import tkinter as tk 
from tkinter import *
from PIL import Image, ImageTk


def createwidgets():
    global cameralabel
    cameralabel = Label(root, borderwidth=3, relief="groove", bg="white")
    cameralabel.grid(row=0, column=0)

    recommendationlabel = Label(root, borderwidth=3, relief="groove", text="Recommendation", bg="white", fg="black", font=("Comic Sans MS", 18))
    recommendationlabel.place(in_= cameralabel, relx = 1.0, rely = 0.0, anchor = NE)

    recommendationList = Listbox(root)
    recommendationList.insert(0, recommendationlabel, "Option 2")
    recommendationList.place(in_= cameralabel, relx = 1.0, rely = 0.04, anchor = NE)

    captureBtn = Button(root, text = "Capture", command=capture, bg="Lightblue", width= 20, font=("Comic Sans MS", 15))
    captureBtn.place(in_= cameralabel, relx = 0.5, rely = 1.0, anchor = S)

    #-------------------------------------------------------------
    # recommendationText = Text(root, height = 5, width = 52)
    # recommendationText.grid(row=0, column=1, rowspan=2)
    # recommendationText.insert(tk.END, "Recommendation")

    # listcanvas = Canvas(root, borderwidth=3, relief="groove")
    # listcanvas.grid(row = 1, column=1)

    showfeed()

def showfeed():
    ret, frame = root.cap.read()
    global cameralabel

    if ret:
        frame = cv2.flip(frame, 1)
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)

        videoimg = Image.fromarray(cv2image)

        imgtk = ImageTk.PhotoImage(image = videoimg)
        cameralabel.configure(image = imgtk)
        cameralabel.imgtk = imgtk
        cameralabel.after(10, showfeed)
    
    else:
        cameralabel.configure(image= "")

def capture():

    fileName = 'FaceImage.jpg'
    ret, frame = root.cap.read()
    cv2.imwrite(fileName, frame)
    print('Image Captured!')

    img = cv2.imread('FaceImage.jpg')
    faceCascade = cv2.CascadeClassifier('haarcascade.xml')
    faces = faceCascade.detectMultiScale(img, 1.1, 4)

    for (x,y,w,h) in faces:
        FaceImg = img[y:y+h, x:x+w]
        #To save image to drive
        filename = 'Face' + '.jpg'
        cv2.imwrite(filename, FaceImg)


root = tk.Tk()

width, height = root.winfo_screenwidth(), root.winfo_screenheight()

root.cap = cv2.VideoCapture(0)

# width, height = 30,30
root.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
root.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

root.title("FrameKart")
root.geometry("1440x900")
# root.attributes('-fullscreen', True)
root.config(background = "white")

createwidgets()
root.mainloop()