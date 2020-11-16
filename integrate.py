import tkinter as tk
from tkinter import *
from tkinter import messagebox

import cv2
from PIL import Image,ImageTk
import numpy as np
import os
import time
import threading
import requests
import json
import base64

HEIGHT = 1200
WIDTH = 800

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
        # global leftShoulder,rightShoulder,leftElbow,rightElbow
        # leftShoulder = data["result"]["person1"]["LShoulder"]
        # rightShoulder = data["result"]["person1"]["RShoulder"]
        # leftElbow = data["result"]["person1"]["LElbow"]
        # rightElbow = data["result"]["person1"]["RElbow"]

        time.sleep(3)
    c.release()

def userlocal():
    root=tk.Tk()
    root.title("camera")
    root.geometry("640x480")
    root.resizable(width=False, height=False)
    canvas=tk.Canvas(root, width=640, height=480, bg="white")
    canvas.pack()

    th1 = threading.Thread(target=cameraPng)
    th2 = threading.Thread(target=u)

    capStart()
    th1.start()
    th2.start()

def popup():
    response = messagebox.askyesno("We would like to access your camera")
    Label(root, text = response).pack()
    if response == True:
        Label(root, text ="You clicked Yes!").pack()
        userlocal()
    else :
        Label(root, text ="You clicked No :(").pack()     

root =tk.Tk()

#bg
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

# background_image = tk.PhotoImage(file='bg.png')
# background_label = tk.Label(root, image=background_image)
# background_label.place(relwidth=1, relheight=1)

# them khung
frame = tk.Frame(root, bg='#EC725B', bd=5)
frame.place(relx=0.5, rely=0.6, relwidth=0.15, relheight=0.075, anchor='n')

button = tk.Button(frame, text="JOINT", font=40 , command= popup)
button.place(relx=0.5, relheight=0.75, relwidth=0.3)
button.pack()

root.mainloop()