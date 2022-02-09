import cv2
import tkinter as tk 
from tkinter import *
from PIL import Image, ImageTk

def createwidgets():    
    global cameralabel
    cameralabel = Label(root, borderwidth=0, bg="white")
    cameralabel.grid(row=0, column=0)

    captureBtn = Button(root, text = "Capture", command=capture, bg="Lightblue", width= 20, font=("Comic Sans MS", 15))
    captureBtn.place(in_= cameralabel, relx = 0.5, rely = 1.0, anchor = S, y= -20)

    global frame
    frame = Frame(root, bg="white")
    frame.grid(row=0, column=1, sticky=NW)

    recommendationLabelText = Label(frame, borderwidth=0, relief="groove", text="Recommendations", bg="white", fg="black", font=("Arial", 25))
    recommendationLabelText.pack(side=TOP)

    recommendations()
    showfeed()

def recommendations():
    global frame
    optionList = ["Option 1", "Option 2", "Option 3", "Option 4", "Option 5", "Option 6"]

    checkedItem = StringVar()
    for item in range(len(optionList)):
        recommendationListCheck = Checkbutton(frame, text = optionList[item], variable = checkedItem, onvalue = optionList[item],  bg="white", fg="black", font=("Arial", 20))
        recommendationListCheck.pack(side=TOP, padx=20, pady=20)


def rescale_frame(frame, percent=75):
    width = int(frame.shape[1] * percent/ 100)
    # height = int(frame.shape[0] * percent/ 100)
    height = root.winfo_screenheight()
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)

def showfeed():
    ret, frame = root.cap.read()
    frame = rescale_frame(frame, percent = 90)
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

# width, height = root.winfo_screenwidth()*0.5, root.winfo_screenheight()*0.5

root.cap = cv2.VideoCapture(0)

# width, height = 30,30
# root.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
# root.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

root.title("FrameKart")
# root.geometry("1440x900")
root.attributes('-fullscreen', True)
root.config(background = "white")

createwidgets()
root.mainloop()