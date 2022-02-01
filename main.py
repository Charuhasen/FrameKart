import cv2 

faceCascade = cv2.CascadeClassifier('haarcascade.xml')
cap = cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()

    cv2.imshow('Camera',frame)

    K = cv2.waitKey(1)

    if K == 32:
        fileName = 'FaceImage.jpg'
        cv2.imwrite(fileName,frame)
        print('Image Captured!')
        break

img = cv2.imread('FaceImage.jpg')
faces = faceCascade.detectMultiScale(img, 1.1, 4)

for (x,y,w,h) in faces:
    FaceImg = img[y:y+h, x:x+w]
    #To save image to drive
    filename = 'Face' + '.jpg'
    cv2.imwrite(filename, FaceImg)
