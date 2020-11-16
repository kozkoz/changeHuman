import tkinter as tk
import cv2
from PIL import Image,ImageTk
import numpy as np
import os
import time
import threading
import requests
import json
import base64

root=tk.Tk()
root.title("camera")
root.geometry("640x480")
root.resizable(width=False, height=False)
canvas=tk.Canvas(root, width=640, height=480, bg="white")
canvas.pack()

image_path = "image.png"


def capStart():
    print('camera-ON')
    try:
        global c, w, h, img
        c=cv2.VideoCapture(0)
        w, h= c.get(cv2.CAP_PROP_FRAME_WIDTH), c.get(cv2.CAP_PROP_FRAME_HEIGHT)
        print('w:'+str(w)+'px+h:'+str(h)+'px')
        
    except:
        import sys
        print("error-----")
        print(sys.exec_info()[0])
        print(sys.exec_info()[1])
        '''終了時の処理はここでは省略します。
        c.release()
        cv2.destroyAllWindows()'''

def u():#update
    global img
    ret, frame =c.read()
    if ret:
        img=ImageTk.PhotoImage(Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
        canvas.create_image(w/2,h/2,image=img)
    else:
        print("u-Fail")
    root.after(1,u)

def cameraPng():
    while True:
        if c.isOpened() is False:
            print("IO Error")
        else:
            ret, frame = c.read()
            if ( ret == True ):
                cv2.imwrite("image.png", frame)
            else:
                print("Read Error")
        image =  open(image_path, "rb").read()
        response_type = "json"
        request_body = {"response_type": response_type}
        url = "https://ai-api.userlocal.jp/human_pose"
        res = requests.post(url, data=request_body, files={"image_data": image})
        data = json.loads(res.content)
        image = base64.b64decode(data["image_data"])
        with open("test.png", "wb") as f:
            f.write(image)
        print(data["result"]["person1"])
        global leftShoulder,rightShoulder,leftElbow,rightElbow
        try:
            leftShoulder = data["result"]["person1"]["LShoulder"]
        except NameError:
            print("noData")
        try:
            rightShoulder = data["result"]["person1"]["RShoulder"]
        except NameError:
            print("nodata")
        try:
            leftElbow = data["result"]["person1"]["LElbow"]
        except NameError:
            print("noLeftElbow")
        try:
            rightElbow = data["result"]["person1"]["RElbow"]
        except NameError:
            print("noRightElbow")
        time.sleep(3)
    c.release()

th1 = threading.Thread(target=cameraPng)
th2 = threading.Thread(target=u)


capStart()
th1.start()
th2.start()
root.mainloop()