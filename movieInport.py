import tkinter as tk
from tkinter import *
# from tkinter import messagebox
import tkinter.messagebox as mb

import cv2
from PIL import Image, ImageTk
import numpy as np
import os
import time
import threading
import requests
import json
import base64

import wave  
import pygame.mixer as pyx
import sys

HEIGHT = 800
WIDTH = 800

image_path = "image.png"
sound_file = "evening.mp3"




def popup():
    request = tk.messagebox.askyesno("カメラアクセスについて", "このアプリではカメラを使用します。")
    if request == True:
        # background_label.configure(image='')
        # canvas.pack_forget()
        # userlocal()
        video()
        
    else :
        Label(root, text ="You clicked No :").pack()

def video():
    channel.pause() # 一時停止
    frame1.destroy()
    btn1.destroy()
    label.pack_forget()
    
    c=cv2.VideoCapture('変身前.mp4')
    while(c.isOpened()):
        ret, frame = c.read()
        if ret==True:
            # frame = cv2.flip(frame,0)  #frameを左右反転
            # write the flipped frame　　
            # out.write(frame)           #output.aviにframe毎書込み

        # 以下通常の動画表示
            cv2.imshow('movie',frame)  #反転frameを表示
            cv2.moveWindow('movie',0,0)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
        # ここまで

    c.release()
    cv2.destroyAllWindows()
    userlocal()


root =tk.Tk()
# root.geometry('250x250')
#bg
img = Image.open("bg.png")
tkimg = ImageTk.PhotoImage(img)
label = tk.Label(root, image=tkimg, bg="white")
label.pack()


pyx.init(frequency = 44100, size = -16, channels = 2, buffer = 4096) # 初期設定
sounds = pyx.Sound(sound_file) # 再生ファイルを設定
    
sd_loop = -1 # 再生階数(-1:無限ループ)

channel = sounds.play(loops = sd_loop) # 音楽再生
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

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

def u():#
    global img
    ret, frame =c.read()
    frame = cv2.flip(frame, 1) # 左右反転
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
        global leftShoulder,rightShoulder,leftElbow,rightElbow
        print(data["result"])
        print("person1" in data["result"])
        if "person1" in data["result"]:
            print("person1 is checked")
            if "LShoulder" in data["result"]["person1"]:
                leftShoulder = data["result"]["person1"]["LShoulder"]
                print(leftShoulder)
                if 450 < leftShoulder[0] < 700 and 100 < leftShoulder[1] < 500:
                    print("leftShoulder is true")
                else:
                    print("leftShoulder is false")
                if "LElbow" in data["result"]["person1"]:
                    leftElbow = data["result"]["person1"]["LElbow"]
                    print(leftElbow)
                    if 300 < leftElbow[0] < 700 and 100 < leftElbow[1] < 500:
                        print("leftElbow is true")
                    else:
                        print("leftElbow is false")
                else:
                    print("左手が映っていません")
                    leftElbow = [0,0]
            else:
                print("左腕が映っていません")
                leftShoulder = [0,0]
            if "RShoulder" in data["result"]["person1"]:
                rightShoulder = data["result"]["person1"]["RShoulder"]
                print(rightShoulder)
                if 300 < rightShoulder[0] < 500 and 100 < rightShoulder[1] < 500:
                    print("rightShoulder is true")
                else:
                    print("rightShoulder is false")
                if "RElbow" in data["result"]["person1"]:
                    rightElbow = data["result"]["person1"]["RElbow"]
                    if 100 < rightElbow[0] < 500 and 100 < rightElbow[1] < 500:
                        print("rightElbow is true")
                    else:
                        print("rightElbow is false")
                else:
                    print("右手が映っていません")
                    rightElbow = [0,0]
            else:
                print("右腕が映っていません")
                rightShoulder = [0,0]
        else:
            print("noHuman")
        if 450 < leftShoulder[0] < 700 and 100 < leftShoulder[1] < 500 and 300 < leftElbow[0] < 700 and 100 < leftElbow[1] < 500 and 300 < rightShoulder[0] < 500 and 100 < rightShoulder[1] < 500 and 100 < rightElbow[0] < 500 and 100 < rightElbow[1] < 500: 
            print("Aaa")
            # ここに動画の処理を入れるよ！
        time.sleep(3)
    c.release()

def userlocal():
    th1 = threading.Thread(target=cameraPng)
    th2 = threading.Thread(target=u)
    capStart()
    th1.start()
    th2.start()


frame1 = tk.Frame(root, bg='#EC725B', bd=5)
frame1.place(relx=0.5, rely=0.6, relwidth=0.15, relheight=0.075, anchor='n')
btn1 = tk.Button(frame1, text='わーい', font=40,  command = popup)
btn1.place(relx=0.5, relheight=0.75, relwidth=0.3)
btn1.pack()
# btn1.grid(row=0, column=0)



root.mainloop()