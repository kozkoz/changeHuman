import cv2

cap = cv2.VideoCapture(0)

if cap.isOpened() is False:
    print("IO Error")
else:
    ret, frame = cap.read()
    if ( ret == True ):
        cv2.imwrite("image.png", frame)
    else:
        print("Read Error")

cap.release()