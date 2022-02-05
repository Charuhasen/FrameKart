from turtle import width
import cv2
import tkinter as tk 
from tkinter import *
from PIL import Image, ImageTk

def createwidgets():
    feedlabel = Label(root, bg = "steelblue", fg = "white", text = "Webcam", font = ("Comic Sans MS", 20))
    feedlabel.grid(row = 1, column=1, padx = 10, pady = 10, columnspan = 2)

    global cameralabel
    cameralabel = Label(root, bg="steelblue", borderwidth=3, relief="groove")
    cameralabel.grid(row = 2, column=1, padx = 10, pady = 10, columnspan = 2)

    captureBtn = Button(root, text = "Capture", command=capture, bg="Lightblue", width= 20, font=("Comic Sans MS", 15))
    captureBtn.grid(row=4, column=1, padx=10, pady=10)

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

root.cap = cv2.VideoCapture(0)

width, height = 640,480
root.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
root.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)


root.title("FrameKart")
root.geometry("1340x700")
root.config(background = "sky blue")

destPath = StringVar()
imagePath = StringVar()

createwidgets()
root.mainloop()